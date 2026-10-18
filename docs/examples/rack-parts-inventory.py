# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Reconcile rack members with the 94-object baseline.

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
levels = len(p["LEVEL_ELEVATIONS"])
per_rack = {"uprights": 4, "base_plates": 4, "beams": 4 * levels,
            "visual_decks": levels, "side_braces": 2 * 2 * 2}
totals = {key: count * p["RACK_COUNT"] for key, count in per_rack.items()}
for key in per_rack:
    print(key, "per_rack", per_rack[key], "all_racks", totals[key])
actual = sum(totals.values()) + 1
printed_formula = p["RACK_COUNT"] * (8 + p["LEVEL_COUNT"] * 5 + 8) + 1
assert actual == printed_formula == 94
print("floor_reference", 1)
print("total_objects", actual)
