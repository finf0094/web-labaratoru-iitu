"""Pattern-based detector of injected instructions in retrieved passages.

Patterns were written from generic descriptions of prompt-injection attacks
(OWASP LLM01; Greshake et al., 2023) in English, Russian and Kazakh *before*
the evaluation and were not tuned on the test passages.
"""
import re

PATTERNS = {
    "override": [
        r"\b(ignore|disregard|forget)\b.{0,20}\b(previous|prior|above|earlier)\b.{0,15}\b(instructions?|directions?|rules)\b",
        r"игнорир\w*.{0,30}(инструкц|указани|правил)",
        r"забудь\w*.{0,30}(инструкц|указани|правил)",
        r"(нұсқау|нұсқаулар)\w*.{0,30}(елеме|ескерме)",
    ],
    "role": [
        r"\bsystem\s+(message|prompt|instruction)",
        r"системн\w*\s+(сообщени|промпт|инструкц)",
        r"жүйелік\s+(хабарлама|нұсқау)",
        r"\b(attention|note to)\s*,?\s*(the\s+)?(assistant|ai|model)\b",
        r"внимание\s*,?\s*ассистент",
    ],
    "tool_call": [
        r"\b(call|invoke|run|use)\s+(the\s+)?[a-z]+_[a-z_]+\s*(tool|function)?",
        r"(вызови|вызовите|используй)\w*\s+инструмент",
        r"\b[a-z]+_[a-z]+\b\s+(tool|құралы|инструмент)",
    ],
    "exfiltration": [
        r"[\w.+-]+@[\w-]+\.[\w.]+",
    ],
}
COMPILED = {k: [re.compile(p, re.IGNORECASE | re.UNICODE) for p in v] for k, v in PATTERNS.items()}


def detect(text):
    """Return the list of matched pattern groups (empty list = passage looks clean)."""
    return [group for group, pats in COMPILED.items() if any(p.search(text) for p in pats)]
