# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Open committed reference models without overwriting them.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


paths = ("FreeCAD Hull/Catamaran_Hull_Only.FCStd",
         "FreeCAD_WHRackDesign/FreeCAD_WHRackDesign_3_Racks_3_Levels.FCStd")
for relative in paths:
    doc = App.openDocument(str(ROOT / relative))
    try:
        doc.recompute()
        objects = [obj for obj in doc.Objects if hasattr(obj, "Shape")]
        assert objects
        failures = [obj.Name for obj in objects if obj.Shape.isNull() or not obj.Shape.isValid()]
        assert not failures, failures
        print(relative, "document", doc.Name, "objects", len(doc.Objects),
              "shaped_objects", len(objects), "reference_valid", True)
    finally:
        App.closeDocument(doc.Name)
