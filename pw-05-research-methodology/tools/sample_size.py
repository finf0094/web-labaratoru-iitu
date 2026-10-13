"""Sample-size calculations used in Practical Work 5 (Section 3).

Topic: tools for LLM agents - MCP vs native LangChain tools.
Standard library only:  python3 tools/sample_size.py

1) Developer experiment (RQ1, H1): paired t-test, normal approximation
   (within-subjects: every developer works in both conditions).
2) Benchmark task suite (RQ2, H2b): McNemar test for paired binary outcomes
   (the same task solved with 5 tools and with 20 tools), Connor (1987).
3) Benchmark task suite (RQ2, H2a): precision of the paired difference in
   tool-call accuracy between MCP and native tools (equivalence margin 5 p.p.).
4) Benchmark task suite (RQ2): precision of a single accuracy estimate.
5) Latency micro-benchmark (RQ3): how many calls are above the 95th percentile.
"""
import math
from statistics import NormalDist

Z = NormalDist().inv_cdf
ALPHA, POWER = 0.05, 0.80


def paired_t(d, alpha=ALPHA, power=POWER):
    """Number of pairs for a two-sided paired t-test with effect size d (Cohen's d_z)."""
    za, zb = Z(1 - alpha / 2), Z(power)
    return math.ceil(((za + zb) / d) ** 2 + za ** 2 / 2)


def mcnemar(p10, p01, alpha=ALPHA, power=POWER):
    """Number of paired units for McNemar's test (Connor, 1987).

    p10 - share of tasks solved with 5 tools but failed with 20 tools,
    p01 - share of tasks failed with 5 tools but solved with 20 tools.
    """
    za, zb = Z(1 - alpha / 2), Z(power)
    psi, delta = p10 + p01, p10 - p01
    return math.ceil((za * math.sqrt(psi) + zb * math.sqrt(psi - delta ** 2)) ** 2 / delta ** 2)


def paired_diff_halfwidth(n, discordant, confidence=0.95):
    """Half-width of the CI for a paired difference of proportions (worst case delta = 0)."""
    z = Z(1 - (1 - confidence) / 2)
    return z * math.sqrt(discordant / n)


def proportion_precision(p, margin, confidence=0.95):
    z = Z(1 - (1 - confidence) / 2)
    return math.ceil(z ** 2 * p * (1 - p) / margin ** 2)


def main():
    print("1) Developer experiment, MCP vs native @tool (H1), paired t-test, alpha = .05, power = .80")
    for d in (0.5, 0.6, 0.8):
        print(f"   effect size d = {d}: n = {paired_t(d)} developers")
    print("   -> plan 24 (d = 0.6, multiple of 4 for the Latin square), recruit 28 for ~15% dropout;")
    print("      36 if resources allow (d = 0.5 needs 34, rounded up to a multiple of 4)")

    print("2) Tool-call accuracy with 5 vs 20 tools (H2b), McNemar, alpha = .05, power = .80")
    for p10, p01 in ((0.12, 0.02), (0.14, 0.04)):
        print(f"   discordant p10 = {p10:.2f}, p01 = {p01:.2f} (drop {p10 - p01:.0%}): "
              f"n = {mcnemar(p10, p01)} tasks")
    print("   -> plan 120 tasks (108 needed in the main scenario + ~10% reserve for tasks dropped after the pilot)")

    print("3) MCP vs native accuracy (H2a), 95% CI half-width of the paired difference")
    for n_tasks, runs in ((60, 3), (120, 3)):
        n = n_tasks * runs
        for disc in (0.06, 0.10):
            print(f"   {n_tasks} tasks x {runs} runs = {n} trials, discordant {disc:.0%}: "
                  f"+/-{paired_diff_halfwidth(n, disc):.1%}")
    print("   (task-level clustering is handled by bootstrap over tasks; target half-width < 5 p.p.)")

    print("4) Precision of one accuracy estimate, 95% confidence")
    for p, m in ((0.85, 0.07), (0.85, 0.05)):
        print(f"   expected accuracy {p:.0%}, margin +/-{m:.0%}: n = {proportion_precision(p, m)} tasks")

    print("5) Latency micro-benchmark (RQ3): calls above the 95th percentile")
    for n in (200, 1000):
        print(f"   {n} measured calls -> {int(n * 0.05)} observations above p95")


if __name__ == "__main__":
    main()
