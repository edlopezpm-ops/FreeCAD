# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Read the rack inputs and their actual construction dependencies.

Uses standard-library Python; does not validate FreeCAD geometry.
See the paired engineering note for expected output and limitations.
"""

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def literals(relative_path):
    tree = ast.parse((ROOT / relative_path).read_text(encoding="utf-8"))
    values = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                try:
                    values[target.id] = ast.literal_eval(node.value)
                except (ValueError, TypeError):
                    pass
    return values


p = literals("FreeCAD_WHRackDesign/WarehouseRack3x3.py")
keys = ("RACK_COUNT", "LEVEL_COUNT", "LEVEL_ELEVATIONS", "RACK_WIDTH", "RACK_DEPTH",
        "RACK_HEIGHT", "UPRIGHT_SIZE", "BEAM_HEIGHT", "DECK_THICKNESS")
for key in keys:
    print(key, p[key])
assert p["LEVEL_COUNT"] == len(p["LEVEL_ELEVATIONS"])
assert p["RACK_COUNT"] > 0
assert all(p[key] > 0 for key in keys if key not in ("LEVEL_ELEVATIONS",))
assert all(a < b for a, b in zip(p["LEVEL_ELEVATIONS"], p["LEVEL_ELEVATIONS"][1:]))
assert p["LEVEL_ELEVATIONS"][-1] + p["BEAM_HEIGHT"] + p["DECK_THICKNESS"] < p["RACK_HEIGHT"]
print("level_count_matches", True)
