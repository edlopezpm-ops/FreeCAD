# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Report placeholder volumes with explicit component categories.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]

from collections import defaultdict

ns = runpy.run_path(str(ROOT / "FreeCAD_WHRackDesign/WarehouseRack3x3.py"))
doc = App.getDocument(ns["DOC_NAME"])
groups = defaultdict(list)
for obj in doc.Objects:
    if obj.Name == "Floor_Aisle_Reference":
        continue
    if "_Upright" in obj.Name:
        category = "uprights"
    elif "_BasePlate" in obj.Name:
        category = "plates"
    elif "_WireDeck_Visual" in obj.Name:
        category = "decks"
    elif "_SideBrace_" in obj.Name:
        category = "braces"
    elif "_Beam" in obj.Name:
        category = "beams"
    else:
        raise AssertionError((obj.Name, "unclassified rack object"))
    assert obj.Shape.isValid() and len(obj.Shape.Solids) == 1
    groups[category].append(obj.Shape.Volume)
expected = {"uprights": 12, "plates": 12, "beams": 36, "decks": 9, "braces": 24}
assert {key: len(values) for key, values in groups.items()} == expected
for key in sorted(groups):
    volume = sum(groups[key])
    assert volume > 0
    print(key, "count", len(groups[key]), "volume_mm3", volume, "volume_m3", volume / 1e9)
print("floor_reference_volume_mm3", doc.getObject("Floor_Aisle_Reference").Shape.Volume)
