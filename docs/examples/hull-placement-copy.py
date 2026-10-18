# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Translate a copied hull without editing the source object.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


ns = runpy.run_path(str(ROOT / "FreeCAD Hull/FullCatamaranHull.py"))
source_doc = App.getDocument(ns["DOC_NAME"])
source = source_doc.getObject("Port_Hull")
before = source.Shape.BoundBox
original_placement = source.Placement.copy()
doc = App.newDocument("Engineering_Example_Placement")
copy = doc.addObject("Part::Feature", "Translated_Port_Hull")
copy.Shape = source.Shape.copy()
copy.Placement.Base = App.Vector(15000, 0, 2500)
doc.recompute()
after = copy.Shape.BoundBox
for actual, expected in ((after.XMin, before.XMin + 15000), (after.XMax, before.XMax + 15000),
                         (after.ZMin, before.ZMin + 2500), (after.ZMax, before.ZMax + 2500),
                         (after.YMin, before.YMin), (after.YMax, before.YMax)):
    assert abs(actual - expected) < 1e-5
assert abs(copy.Shape.Volume - source.Shape.Volume) / source.Shape.Volume < 1e-9
assert source.Placement.Base.sub(original_placement.Base).Length < 1e-9
assert abs(source.Shape.BoundBox.XMin - before.XMin) < 1e-9
print("translated_copy", True)
print("original_unchanged", True)
