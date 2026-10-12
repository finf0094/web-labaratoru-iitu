"""Sample-size calculations used in Practical Work 5 (Section 3).

Standard library only:  python3 tools/sample_size.py [--population 5000]

* Cochran's formula with finite population correction (student survey).
* Paired t-test, normal approximation (within-subject dashboard comparison, H3).
* Two-proportion z-test (pilot vs control FX/F rate, H4).
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


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--population", type=int, default=5000,
                    help="number of students in the sampling frame (default: 5000, illustrative)")
    ap.add_argument("--response-rate", type=float, default=0.60)
    args = ap.parse_args()

    n0, n = cochran(args.population)
    invite = math.ceil(n / args.response_rate)
    print("1) Student survey (95% confidence, +/-5% margin, p = 0.5)")
    print(f"   infinite population n0 = {n0:.1f}")
    print(f"   N = {args.population}: n = {n}; invitations at {args.response_rate:.0%} response = {invite}")

    print("2) Within-subject comparison of dashboards (H3), paired t-test, alpha = .05, power = .80")
    for d in (0.5, 0.6, 0.8):
        print(f"   effect size d = {d}: n = {paired_t(d)} participants")

    print("3) Pilot vs control share of FX/F grades (H4), two-sided, alpha = .05, power = .80")
    for p1, p2 in ((0.20, 0.12), (0.20, 0.10), (0.15, 0.08)):
        print(f"   {p1:.0%} -> {p2:.0%}: n = {two_proportions(p1, p2)} student-course enrolments per arm")


if __name__ == "__main__":
    main()
