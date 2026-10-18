# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Separate rack-center dimensions from component envelopes.

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
origins = [i * (p["RACK_WIDTH"] + p["RACK_GAP"]) for i in range(p["RACK_COUNT"])]
nominal_width = p["RACK_COUNT"] * p["RACK_WIDTH"] + (p["RACK_COUNT"] - 1) * p["RACK_GAP"]
half_plate = p["BASE_PLATE_SIZE"] / 2
plate_x = (-half_plate, nominal_width + half_plate)
plate_y = (-half_plate, p["RACK_DEPTH"] + half_plate)
floor_margin = 600.0  # Local constant in create_floor_reference, not a source global.
floor_x = (-floor_margin, nominal_width + floor_margin)
floor_y = (-floor_margin, p["RACK_DEPTH"] + floor_margin)
assert floor_x[0] < plate_x[0] < plate_x[1] < floor_x[1]
assert floor_y[0] < plate_y[0] < plate_y[1] < floor_y[1]
print("rack_origins_x_mm", origins)
print("plate_x_mm", plate_x, "plate_y_mm", plate_y)
print("floor_x_mm", floor_x, "floor_y_mm", floor_y)
print("adjacent_plate_gap_mm", p["RACK_GAP"] - p["BASE_PLATE_SIZE"])
print("adjacent_upright_gap_mm", p["RACK_GAP"] - p["UPRIGHT_SIZE"])
