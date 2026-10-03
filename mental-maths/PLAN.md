# Arithmetic & Mental Maths: An 8-Week Guided Plan

**Time needed:** 25–35 minutes a day, 6 days a week, plus one rest or review day.
**Goal:** fast, accurate mental arithmetic you can rely on in aptitude tests, interviews and everyday estimates.

The plan has four parts:

1. **Facts.** Memorise the facts you would otherwise work out. Recalling 17×13 is quicker than calculating it.
2. **Techniques.** Learn a small set of methods that turn hard sums into easy ones.
3. **Fluency.** Practise against the clock until the methods come without thinking.
4. **Application.** Use the skills in mixed, word-problem and estimation settings.

Drills are in [`drills.py`](./drills.py). Run `python3 drills.py --help` to see them.

---

## Week 0: Baseline (one sitting, about 20 min)

Before you start, measure where you are. Do not practise first.

```bash
python3 drills.py baseline
```

This runs 2 minutes of each of: addition, subtraction, times tables, 2-digit × 1-digit,
percentages and fractions. It saves your score and accuracy to `progress.csv`.
You will run it again in Weeks 4 and 8 to measure progress.

Rough benchmarks for correct answers per minute:

| Skill            | Starting | Solid | Strong |
|------------------|----------|-------|--------|
| 2-digit addition | < 10     | 15–20 | 25+    |
| Times tables ≤12 | < 20     | 30    | 40+    |
| 2-digit × 1-digit| < 5      | 8–10  | 15+    |
| Percent of number| < 4      | 6–8   | 12+    |

**Rule for the whole plan:** accuracy comes first. If you get fewer than 90% right, slow down.

---

## Daily session template (about 30 min)

| Block       | Time   | What you do                                                       |
|-------------|--------|-------------------------------------------------------------------|
| Warm-up     | 5 min  | Facts drill from your current or previous week (`drills.py tables`, `squares`…) |
| Learn       | 8 min  | Read the day's technique and work 10 examples slowly on paper, then in your head |
| Drill       | 12 min | Timed drill for the week's skill, in 2–3 rounds of 3–4 minutes    |
| Mixed recall| 5 min  | `drills.py mixed` to keep earlier weeks fresh                     |

Write down every mistake. Before each session, spend 1 minute redoing yesterday's mistakes.

---

## Phase 1: Foundations (Weeks 1–2)

### Week 1: Addition and subtraction

**Techniques**
- **Complements:** know the pairs that make 10, 100 and 1000 without thinking (63 → 37, 0.28 → 0.72, 418 → 582).
  For 1000, take each digit from 9 and the last non-zero digit from 10.
- **Work left to right:** 47 + 38 → 47 + 30 = 77, then 77 + 8 = 85. Speak the running total in your head.
- **Round and adjust:** 263 + 98 = 263 + 100 − 2. 512 − 197 = 512 − 200 + 3.
- **Subtract by counting up:** 1000 − 647: count 647 → 650 (3) → 700 (50) → 1000 (300), giving 353.
- **Same-difference trick:** 83 − 47 = 86 − 50 = 36. Shift both numbers by the same amount.

**Drills:** `add`, `sub`, `complement`
**Target by end of week:** 2-digit ± 2-digit at about 20/min with 95% accuracy.

### Week 2: Multiplication facts

**Memorise**
- Times tables up to **20×20**. Spend the most time on rows 13–19.
- Squares from **1² to 30²**, and cubes from **1³ to 15³**.
- Powers of 2 up to 2¹² (4096).

**Techniques**
- **Doubling and halving:** 16 × 25 = 8 × 50 = 4 × 100 = 400.
- **×5** = ×10 ÷ 2. **×25** = ×100 ÷ 4. **×125** = ×1000 ÷ 8.
- **×9** = ×10 − itself. **×11** (2-digit): 63 × 11 = 6 | 6+3 | 3 = 693, carrying when the middle sum is 10 or more.

**Drills:** `tables --max 20`, `squares`, `cubes`
**Target:** tables up to 12 at 40/min, and 13–20 at 25/min.

---

## Phase 2: Multiplication techniques (Weeks 3–4)

### Week 3: Splitting numbers apart

- **Distribute:** 47 × 6 = 40×6 + 7×6 = 240 + 42 = 282.
- **Factor:** 36 × 15 = 36 × 30 ÷ 2 = 540, or 18 × 30.
- **2-digit × 2-digit by splitting:** 34 × 27 = 34×20 + 34×7 = 680 + 238 = 918.
- **Round and compensate:** 49 × 18 = 50×18 − 18 = 882.
- **Squares ending in 5:** 65² → 6×7 = 42, then write 25 to get 4225.

**Drills:** `mul --a 2 --b 1`, then `mul --a 2 --b 2`
**Target:** 2-digit × 1-digit at 12/min, and 2-digit × 2-digit in under 15 s each.

### Week 4: Algebra shortcuts

- **Difference of squares:** 48 × 52 = 50² − 2² = 2496. Use it whenever two numbers are equally spaced around a round number.
- **Squaring near a known square:** 43² = 40² + 2·40·3 + 3² = 1849. Or use (a−b)²: 58² = 3600 − 240 + 4 = 3364.
- **Near-base multiplication** (numbers close to 100): 97 × 94 → shortfalls are 3 and 6.
  97 − 6 = 91, and 3 × 6 = 18, so the answer is 9118.
  Above the base: 104 × 108 → 112 | 32, so the answer is 11232.
- **Same tens, units adding to 10:** 73 × 77 → 7×8 = 56, then 3×7 = 21, giving 5621.

**Drills:** `squares --max 100`, `mul --a 2 --b 2`
**Checkpoint:** run `python3 drills.py baseline` again and compare with Week 0.

---

## Phase 3: Division, fractions and percentages (Week 5–6)

### Week 5: Division and fractions

**Memorise the fraction ↔ percent table**

| Fraction | %     | Fraction | %     | Fraction | %     |
|----------|-------|----------|-------|----------|-------|
| 1/2      | 50    | 1/7      | 14.29 | 1/12     | 8.33  |
| 1/3      | 33.33 | 1/8      | 12.5  | 1/13     | 7.69  |
| 1/4      | 25    | 1/9      | 11.11 | 1/15     | 6.67  |
| 1/5      | 20    | 1/10     | 10    | 1/16     | 6.25  |
| 1/6      | 16.67 | 1/11     | 9.09  | 1/20     | 5     |

Multiples follow from these: 3/8 = 37.5%, 5/6 = 83.33%, 2/7 = 28.57%.

**Techniques**
- **Divisibility rules** for 2, 3, 4, 5, 6, 8, 9 and 11. For 11, take the alternating sum of the digits.
- **Simplify first:** 840 ÷ 35 = 168 ÷ 7 = 24. Divide both numbers by 5.
- **Divide in chunks:** 756 ÷ 7 = 700/7 + 56/7 = 108.
- **÷5** = ×2 ÷ 10. **÷25** = ×4 ÷ 100.

**Drills:** `div`, `fractions`

### Week 6: Percentages and ratios

- **Build from 10% and 1%:** 17% of 340 = 34 + 3×3.4 + 0.7×3.4. An easier route is 10% + 5% + 2% = 34 + 17 + 6.8 = 57.8.
- **Swap the numbers:** x% of y = y% of x. 8% of 25 = 25% of 8 = 2.
- **Successive changes:** a% then b% gives a + b + ab/100.
  For +20% then −10%: 20 − 10 − 2 = +8%.
- **Percentage change** = change ÷ original. Rising from 80 to 100 is +25%. Falling from 100 to 80 is −20%.
- **Ratios:** split 360 in the ratio 4:5 → 360/9 = 40 per part, giving 160 : 200.

**Drills:** `percent`, `pchange`
**Target:** "x% of y" with 2-digit x and 3-digit y in under 8 s.

---

## Phase 4: Estimation, checking and speed (Weeks 7–8)

### Week 7: Estimation and approximation

- Round to 1–2 significant figures, calculate, then adjust in the opposite direction to your rounding.
  398 × 51 ≈ 400 × 50 = 20,000, and the true answer is 20,298.
- **Square roots:** find the nearest perfect squares, then interpolate.
  √70 ≈ 8 + (70−64)/(2·8) = 8.375. The true value is 8.367.
- **Orders of magnitude:** track powers of ten separately. 0.03 × 4,000 = 3 × 40 = 120.
- **Check answers:**
  - Last digit: does 47 × 23 end in 1? 7×3 = 21, so yes.
  - Casting out nines: digit-sum(a) × digit-sum(b) must equal digit-sum(answer), all mod 9.
  - Size: is the answer in the right range?

**Drills:** `estimate` (scored correct within ±5%), `roots`

### Week 8: Speed, mixed sets and review

- Each day, do 3 rounds of `mixed` at 4 minutes each. Then spend 10 minutes on whichever of your skills scores lowest in `progress.csv`.
- Practise multi-step word problems: work, speed and distance, profit and loss, simple and compound interest. Do the arithmetic in your head and write down only the setup.
- **Final test:** `python3 drills.py baseline`. Compare it with Weeks 0 and 4.

---

## After the 8 weeks: maintenance

- 10–15 minutes, 4 days a week: one `mixed` round plus one round of your weakest skill.
- Once a month, run `baseline`.
- Use it in daily life: shop totals, tips, unit prices, and percentage changes in the news.

## Habits that matter more than tricks

1. **Say the running total out loud** (quietly). It keeps your working memory from dropping digits.
2. **Learn one technique at a time.** Practise it until it is automatic before starting the next.
3. **Fix every mistake.** Find out *why* it happened: a fact gap, a carry, or losing your place.
4. **Do short daily sessions.** Thirty minutes every day beats three hours on Sunday.
5. **Practise speed under pressure.** Set the timer slightly faster than is comfortable.
