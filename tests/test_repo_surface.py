from pathlib import Path

def test_required_files():
    req = [
        "CITATION.cff",
        "Main.lean",
        "OverlapRigidityLean.lean",
        "tests",
    ]
    for x in req:
        assert Path(x).exists()
