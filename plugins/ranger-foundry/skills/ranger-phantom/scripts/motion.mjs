/** Pure motion geometry. No browser or network dependencies or side effects. */
function finite(value, label) {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    throw new TypeError(`${label} must be a finite number`);
  }
  return value;
}

function positive(value, label) {
  finite(value, label);
  if (value <= 0) throw new RangeError(`${label} must be positive`);
  return value;
}

function previousPositiveFloat(value) {
  const bits = new DataView(new ArrayBuffer(8));
  bits.setFloat64(0, value);
  bits.setBigUint64(0, bits.getBigUint64(0) - 1n);
  return bits.getFloat64(0);
}

function viewportBounds(viewport) {
  const width = positive(viewport?.width, 'viewport.width');
  const height = positive(viewport?.height, 'viewport.height');
  // CSS coordinates are [0,width) and [0,height), including fractional pixels.
  return { width, height, maxX: previousPositiveFloat(width), maxY: previousPositiveFloat(height) };
}

function checkedPoint(point, bounds, label) {
  const x = finite(point?.x, `${label}.x`);
  const y = finite(point?.y, `${label}.y`);
  if (x < 0 || y < 0 || x > bounds.maxX || y > bounds.maxY) {
    throw new RangeError(`${label} is outside the viewport`);
  }
  return { x, y };
}

function sample(rng) {
  if (typeof rng !== 'function') throw new TypeError('rng must be a function');
  const value = finite(rng(), 'rng result');
  if (value < 0 || value >= 1) throw new RangeError('rng result must be in [0,1)');
  return value;
}

const clamp = (value, low, high) => Math.max(low, Math.min(high, value));

/** Select inside the visible intersection, even for fractional/tiny targets. */
export function interiorPoint(box, viewport, { rng = Math.random, inset = 0.15 } = {}) {
  const bounds = viewportBounds(viewport);
  const x = finite(box?.x, 'box.x');
  const y = finite(box?.y, 'box.y');
  const width = positive(box?.width, 'box.width');
  const height = positive(box?.height, 'box.height');
  finite(inset, 'inset');
  if (inset <= 0 || inset >= 0.5) throw new RangeError('inset must be between 0 and 0.5');
  const left = Math.max(0, x), top = Math.max(0, y);
  const right = Math.min(bounds.width, finite(x + width, 'box.right'));
  const bottom = Math.min(bounds.height, finite(y + height, 'box.bottom'));
  if (left >= right || top >= bottom) throw new RangeError('target has no visible area');
  const px = left + (right - left) * (inset + sample(rng) * (1 - 2 * inset));
  const py = top + (bottom - top) * (inset + sample(rng) * (1 - 2 * inset));
  if (!(px > left && px < right && py > top && py < bottom)) {
    throw new RangeError('target is too small for a representable interior point');
  }
  return checkedPoint({ x: px, y: py }, bounds, 'target');
}

/** Cubic curve with exact endpoints and elapsed timestamps, at most 241 points.
 * A supplied RNG makes fixtures reproducible. The seed/randomness is not a
 * human-likeness or anti-detection guarantee. Consumers own scheduling/actions.
 */
export function bezierPath(start, end, viewport, {
  rng = Math.random, steps = 32, durationMs = 500, curvature = 0.25,
} = {}) {
  const bounds = viewportBounds(viewport);
  const from = checkedPoint(start, bounds, 'start');
  const to = checkedPoint(end, bounds, 'end');
  if (!Number.isInteger(steps) || steps < 2 || steps > 240) {
    throw new RangeError('steps must be an integer from 2 to 240');
  }
  positive(durationMs, 'durationMs');
  if (durationMs < 1 || durationMs > 10000) throw new RangeError('durationMs must be from 1 to 10000');
  finite(curvature, 'curvature');
  if (curvature < 0 || curvature > 0.5) throw new RangeError('curvature must be in [0,0.5]');
  if (from.x === to.x && from.y === to.y) return [{ ...from, atMs: 0 }];
  const dx = to.x - from.x, dy = to.y - from.y;
  const length = Math.hypot(dx, dy);
  finite(length, 'path length');
  const bend = Math.min(length * curvature, 200);
  const control = (fraction) => {
    const offset = (sample(rng) * 2 - 1) * bend;
    return {
      x: clamp(from.x + dx * fraction - dy / length * offset, 0, bounds.maxX),
      y: clamp(from.y + dy * fraction + dx / length * offset, 0, bounds.maxY),
    };
  };
  const c1 = control(1 / 3), c2 = control(2 / 3);
  const points = [{ ...from, atMs: 0 }];
  for (let index = 1; index < steps; index++) {
    const progress = index / steps;
    const t = progress < 0.5 ? 2 * progress ** 2 : 1 - (-2 * progress + 2) ** 2 / 2;
    const u = 1 - t;
    const coordinate = (key, maximum) => clamp(
      u ** 3 * from[key] + 3 * u ** 2 * t * c1[key] +
      3 * u * t ** 2 * c2[key] + t ** 3 * to[key], 0, maximum);
    points.push({ x: coordinate('x', bounds.maxX), y: coordinate('y', bounds.maxY), atMs: durationMs * progress });
  }
  points.push({ ...to, atMs: durationMs });
  return points;
}
