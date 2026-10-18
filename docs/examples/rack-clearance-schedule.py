# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Calculate deck elevations and nominal vertical gaps.

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
levels = p["LEVEL_ELEVATIONS"]
assert all(a < b for a, b in zip(levels, levels[1:]))
for index, bottom in enumerate(levels):
    beam_top = bottom + p["BEAM_HEIGHT"]
    deck_top = beam_top + p["DECK_THICKNESS"]
    upper = levels[index + 1] if index + 1 < len(levels) else p["RACK_HEIGHT"]
    gap = upper - deck_top
    assert gap > 0
    print("level", index + 1, "beam_bottom_mm", bottom, "beam_top_mm", beam_top,
          "deck_top_mm", deck_top, "gap_above_mm", gap)
