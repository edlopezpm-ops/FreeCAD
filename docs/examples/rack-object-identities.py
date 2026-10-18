# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Audit rack object names without relying on allocation suffixes.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


ns = runpy.run_path(str(ROOT / "FreeCAD_WHRackDesign/WarehouseRack3x3.py"))
doc = App.getDocument(ns["DOC_NAME"])
names = [obj.Name for obj in doc.Objects]
assert len(names) == len(set(names)) == 94
for index in range(1, ns["RACK_COUNT"] + 1):
    prefix = f"Rack_{index:02d}_"
    group = [obj for obj in doc.Objects if obj.Name.startswith(prefix)]
    assert len(group) == 31
    assert sum(obj.Name.startswith(prefix + "Upright") for obj in group) == 4
    assert sum(obj.Name.startswith(prefix + "BasePlate") for obj in group) == 4
    assert sum("_Level_" in obj.Name for obj in group) == 15
    assert sum("_SideBrace_" in obj.Name for obj in group) == 8
    print(prefix, "objects", len(group))
    for obj in group:
        assert doc.getObject(obj.Name) is obj
        print(obj.Name, obj.Label, obj.TypeId)
assert doc.getObject("Floor_Aisle_Reference") is not None
