#!/usr/bin/env bash
# Reproduces every number and figure of the PW6 report.
set -euo pipefail
cd "$(dirname "$0")"
python3 prepare_data.py
python3 run_retrieval.py
python3 make_figures.py
python3 test_metrics.py
