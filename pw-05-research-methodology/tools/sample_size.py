"""Sample-size calculations used in Practical Work 5 (Section 3).

Standard library only:  python3 tools/sample_size.py [--population 5000]

* Cochran's formula with finite population correction (user survey, H5).
* Paired t-test, normal approximation (developer study MCP vs bespoke, H1).
* Two proportions (task success of two configurations, H3) — conservative,
  unpaired approximation; the paired McNemar design needs fewer tasks.
* Precision of a single proportion (attack success rate, H4).
"""
import argparse
import math
from statistics import NormalDist

Z = NormalDist().inv_cdf


def cochran(population, margin=0.05, p=0.5, confidence=0.95):
    z = Z(1 - (1 - confidence) / 2)
    n0 = z ** 2 * p * (1 - p) / margin ** 2
    n = n0 / (1 + (n0 - 1) / population) if population else n0
    return n0, math.ceil(n)


def paired_t(d, alpha=0.05, power=0.80):
    za, zb = Z(1 - alpha / 2), Z(power)
    return math.ceil(((za + zb) / d) ** 2 + za ** 2 / 2)


def two_proportions(p1, p2, alpha=0.05, power=0.80):
    za, zb = Z(1 - alpha / 2), Z(power)
    p_bar = (p1 + p2) / 2
    num = za * math.sqrt(2 * p_bar * (1 - p_bar)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(num ** 2 / (p1 - p2) ** 2)


def proportion_precision(p, margin, confidence=0.95):
    z = Z(1 - (1 - confidence) / 2)
    return math.ceil(z ** 2 * p * (1 - p) / margin ** 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--population", type=int, default=5000,
                    help="number of potential users in the sampling frame (default: 5000, illustrative)")
    ap.add_argument("--response-rate", type=float, default=0.60)
    args = ap.parse_args()

    n0, n = cochran(args.population)
    print("1) User survey (95% confidence, +/-5% margin, p = 0.5)")
    print(f"   infinite population n0 = {n0:.1f}")
    print(f"   N = {args.population}: n = {n}; invitations at {args.response_rate:.0%} response = "
          f"{math.ceil(n / args.response_rate)}")

    print("2) Developer study, MCP vs bespoke integration (H1), paired t-test, alpha = .05, power = .80")
    for d in (0.5, 0.6, 0.8):
        print(f"   effect size d = {d}: n = {paired_t(d)} developers")

    print("3) Task success of two configurations (H3), two-sided, alpha = .05, power = .80")
    for p1, p2 in ((0.60, 0.75), (0.50, 0.65), (0.70, 0.85)):
        print(f"   {p1:.0%} -> {p2:.0%}: n = {two_proportions(p1, p2)} tasks/questions per configuration")

    print("4) Attack success rate (H4), 95% confidence")
    for p, m in ((0.10, 0.05), (0.05, 0.03)):
        print(f"   expected ASR {p:.0%}, margin +/-{m:.0%}: n = {proportion_precision(p, m)} attack cases")


if __name__ == "__main__":
    main()
