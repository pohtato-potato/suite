#!/usr/bin/env python3
"""Timed mental-maths drills that go with PLAN.md.

Examples:
    python3 drills.py baseline              # 6 x 2-minute benchmark
    python3 drills.py add --minutes 3
    python3 drills.py tables --max 20
    python3 drills.py mul --a 2 --b 2
    python3 drills.py mixed

Type the answer and press Enter (a blank answer counts as a miss); type q to stop early.
Each session is appended to progress.csv next to this script.
"""

import argparse
import csv
import datetime as dt
import math
import random
import time
from pathlib import Path

PROGRESS = Path(__file__).with_name("progress.csv")


def rnd(digits):
    return random.randint(10 ** (digits - 1), 10**digits - 1)


# Each generator returns (prompt, answer, tolerance). Tolerance is relative for
# estimate (fraction of answer) and absolute otherwise.
def g_add(o):
    a, b = rnd(o.a), rnd(o.b)
    return f"{a} + {b}", a + b, 0


def g_sub(o):
    a, b = sorted((rnd(o.a), rnd(o.b)), reverse=True)
    return f"{a} - {b}", a - b, 0


def g_complement(o):
    base = random.choice([100, 1000])
    n = random.randint(1, base - 1)
    return f"{base} - {n}", base - n, 0


def g_tables(o):
    a, b = random.randint(2, o.max), random.randint(2, o.max)
    return f"{a} x {b}", a * b, 0


def g_squares(o):
    n = random.randint(2, o.max)
    return f"{n}^2", n * n, 0


def g_cubes(o):
    n = random.randint(2, 15)
    return f"{n}^3", n**3, 0


def g_mul(o):
    a, b = rnd(o.a), rnd(o.b)
    return f"{a} x {b}", a * b, 0


def g_div(o):
    q, d = rnd(o.a), random.randint(2, 19)
    return f"{q * d} / {d}", q, 0


FRACTIONS = [(n, d) for d in range(2, 17) for n in range(1, d) if math.gcd(n, d) == 1] + [(1, 20)]


def g_fractions(o):
    n, d = random.choice(FRACTIONS)
    if random.random() < 0.5:
        return f"{n}/{d} as % (2 dp)", round(100 * n / d, 2), 0.011
    # Reverse direction only for the memorised unit fractions.
    d = random.choice([2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 16, 20])
    return f"{round(100 / d, 2)}% = 1/?", d, 0


def g_percent(o):
    p = random.choice([5, 10, 12.5, 15, 20, 25, 30, 35, 40, 45, 60, 75] + list(range(2, 99)))
    y = random.choice([rnd(2), rnd(3)])
    return f"{p}% of {y}", round(p * y / 100, 2), 0.011


def g_pchange(o):
    if random.random() < 0.5:
        a = random.choice([5, 10, 15, 20, 25, 30, 40, 50])
        b = random.choice([5, 10, 15, 20, 25, 30, 40, 50]) * random.choice([1, -1])
        sb = f"+{b}" if b > 0 else str(b)
        return f"+{a}% then {sb}%: net %", round(a + b + a * b / 100, 2), 0.011
    old = random.choice([20, 25, 40, 50, 60, 75, 80, 120, 125, 150, 200, 250])
    new = old + old * random.choice([-50, -40, -25, -20, -10, 10, 20, 25, 50, 60, 100]) // 100
    return f"{old} -> {new}: % change", round(100 * (new - old) / old, 2), 0.011


def g_estimate(o):
    a, b = rnd(3), rnd(2)
    if random.random() < 0.5:
        return f"~ {a} x {b} (within 5%)", a * b, 0.05
    return f"~ {a * b + random.randint(0, b - 1)} / {b} (within 5%)", a, 0.05


def g_roots(o):
    n = random.randint(2, 999)
    return f"sqrt({n}) to 1 dp", round(math.sqrt(n), 1), 0.11


GENERATORS = {
    "add": g_add, "sub": g_sub, "complement": g_complement, "tables": g_tables,
    "squares": g_squares, "cubes": g_cubes, "mul": g_mul, "div": g_div,
    "fractions": g_fractions, "percent": g_percent, "pchange": g_pchange,
    "estimate": g_estimate, "roots": g_roots,
}
MIXED = ["add", "sub", "tables", "squares", "mul", "div", "fractions", "percent", "pchange"]
BASELINE = [
    ("add", dict(a=2, b=2)), ("sub", dict(a=3, b=2)), ("tables", dict(max=12)),
    ("mul", dict(a=2, b=1)), ("percent", {}), ("fractions", {}),
]


def correct(given, answer, tol, relative):
    try:
        x = float(given.replace(",", "").rstrip("%"))
    except ValueError:
        return False
    limit = abs(answer) * tol if relative else tol
    return abs(x - answer) <= limit + 1e-9


def run(skill, opts, minutes):
    gen = GENERATORS[skill]
    relative = skill == "estimate"
    print(f"\n== {skill}: {minutes:g} min. Press Enter to start ==")
    input()
    end = time.monotonic() + minutes * 60
    right = attempted = 0
    misses = []
    while time.monotonic() < end:
        prompt, answer, tol = gen(opts)
        given = input(f"{prompt} = ").strip()
        if given.lower() == "q":
            break
        if time.monotonic() > end:
            print("(time up: last answer not counted)")
            break
        attempted += 1
        if correct(given, answer, tol, relative):
            right += 1
        else:
            misses.append((prompt, answer, given))
            print(f"   x  {answer}")
    elapsed = max(minutes * 60 - max(end - time.monotonic(), 0), 1) / 60
    acc = right / attempted if attempted else 0
    print(f"-- {skill}: {right}/{attempted} correct, {acc:.0%} accuracy, {right / elapsed:.1f} correct/min")
    if misses:
        print("   Review these:", "; ".join(f"{p} = {a}" for p, a, _ in misses[:10]))
    log(skill, opts, right, attempted, elapsed)
    return right, attempted


def log(skill, opts, right, attempted, elapsed):
    new = not PROGRESS.exists()
    with PROGRESS.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["date", "skill", "settings", "correct", "attempted", "minutes", "per_min"])
        settings = " ".join(f"{k}={v}" for k, v in sorted(vars(opts).items()))
        w.writerow([dt.date.today().isoformat(), skill, settings, right, attempted,
                    round(elapsed, 2), round(right / elapsed, 2)])


class MixedGen:
    """Pick a random skill for each question, with that skill's sensible defaults."""

    def __init__(self, opts):
        self.opts = opts

    def __call__(self, _):
        skill = random.choice(MIXED)
        o = argparse.Namespace(**{**vars(self.opts), **defaults(skill)})
        return GENERATORS[skill](o)


def defaults(skill):
    return {
        "add": dict(a=2, b=2), "sub": dict(a=3, b=2), "tables": dict(max=20),
        "squares": dict(max=30), "mul": dict(a=2, b=1), "div": dict(a=2),
    }.get(skill, {})


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("skill", choices=sorted(GENERATORS) + ["mixed", "baseline"])
    p.add_argument("--minutes", type=float, default=None, help="round length (default 4, baseline 2)")
    p.add_argument("--a", type=int, default=2, help="digits in first number (add/sub/mul/div)")
    p.add_argument("--b", type=int, default=2, help="digits in second number (add/sub/mul)")
    p.add_argument("--max", type=int, default=None, help="largest number for tables/squares")
    p.add_argument("--seed", type=int, default=None)
    o = p.parse_args()
    random.seed(o.seed)

    if o.skill == "baseline":
        total = [0, 0]
        for skill, extra in BASELINE:
            opts = argparse.Namespace(**{**vars(o), "max": None, **extra})
            r, a = run(skill, opts, o.minutes or 2)
            total[0] += r
            total[1] += a
        print(f"\nBaseline total: {total[0]}/{total[1]} correct. Saved to {PROGRESS.name}")
        return

    if o.max is None:
        o.max = 30 if o.skill == "squares" else 12
    if o.skill == "mixed":
        GENERATORS["mixed"] = MixedGen(o)
    run(o.skill, o, o.minutes or 4)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nStopped.")
