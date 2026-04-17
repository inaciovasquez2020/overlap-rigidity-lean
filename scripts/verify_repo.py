#!/usr/bin/env python3
from pathlib import Path
import sys

required = [
    "README.md",
    "CITATION.cff",
    "lakefile.lean",
    "lean-toolchain",
    "Main.lean",
    "OverlapRigidityLean.lean",
    "OverlapRigidityLean",
    "docs",
    "infra",
    "tests",
]

missing = [p for p in required if not Path(p).exists()]
if missing:
    print({"valid": False, "missing": missing})
    sys.exit(1)

readme = Path("README.md").read_text(errors="ignore").lower()

checks = {
    "mentions_overlap": "overlap" in readme,
    "mentions_rigidity": "rigidity" in readme,
    "mentions_lean": "lean" in readme,
    "mentions_formalization_or_theorem": (
        "formalization" in readme or "theorem" in readme or "proof" in readme
    ),
    "mentions_build_or_verify": (
        "build" in readme or "verify" in readme or "lake build" in readme
    ),
}

failed = [k for k, v in checks.items() if not v]
if failed:
    print({"valid": False, "failed_checks": failed, "checks": checks})
    sys.exit(1)

print({"valid": True, "checked": required, "checks": checks})
