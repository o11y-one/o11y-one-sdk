// A seeded PRNG for a TypeScript code scorer. Copy this file into your bundle and import it as "./o11y_prng.ts": a
// scorer imports only its own bundle's .ts files and Node's built-ins.
//
// The sandbox gives V8 no seed, so Math.random() differs on every run. Draw from `context.seed` instead, and every
// retry and repeatability trial of a job sees the same numbers. Two splitmix64 outputs carry all 64 bits of the seed
// into sfc32's 128-bit state, so seeds that differ in any bit start from different states.

const GOLDEN_GAMMA = 0x9e3779b97f4a7c15n;

/** Answers a function that returns the next float in [0, 1) on each call; the same seed, the same sequence. */
export function seededRandom(seed: bigint): () => number {
  let state = BigInt.asUintN(64, seed);
  const splitmix64 = (): bigint => {
    state = BigInt.asUintN(64, state + GOLDEN_GAMMA);
    let z = state;
    z = BigInt.asUintN(64, (z ^ (z >> 30n)) * 0xbf58476d1ce4e5b9n);
    z = BigInt.asUintN(64, (z ^ (z >> 27n)) * 0x94d049bb133111ebn);
    return z ^ (z >> 31n);
  };
  const first = splitmix64();
  const second = splitmix64();
  let a = Number(first >> 32n) | 0;
  let b = Number(first & 0xffffffffn) | 0;
  let c = Number(second >> 32n) | 0;
  let d = Number(second & 0xffffffffn) | 0;
  // sfc32: 32-bit integer arithmetic, so each draw costs no BigInt work.
  const next = (): number => {
    const t = (((a + b) | 0) + d) | 0;
    d = (d + 1) | 0;
    a = b ^ (b >>> 9);
    b = (c + (c << 3)) | 0;
    c = (c << 21) | (c >>> 11);
    c = (c + t) | 0;
    return (t >>> 0) / 4294967296;
  };
  // As sfc32's own seeding does: its first outputs still show the state they started from.
  for (let i = 0; i < 12; i++) next();
  return next;
}
