from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT_WORKBOOK = REPO_ROOT / "data" / "SUPP_TABLES_BRCA12_APR_2026.xlsx"
DEFAULT_EVE_WORKBOOK = REPO_ROOT / "data" / "eve" / "EVE_BRCA12_scores.xlsx"
DEFAULT_OTHER_POINTS_WORKBOOK = REPO_ROOT / "data" / "ACMG_other_points.xlsx"
DEFAULT_RESULTS_DIR = REPO_ROOT / "results"
DEFAULT_FIGURES_DIR = REPO_ROOT / "figures"
