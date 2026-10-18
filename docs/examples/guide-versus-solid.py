# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Compare the sample guide model with the closed hull model.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


sample = runpy.run_path(str(ROOT / "FreeCAD Hull/SampleCatHull.py"))
sample_doc = sample["doc"]
full = runpy.run_path(str(ROOT / "FreeCAD Hull/FullCatamaranHull.py"))
full_doc = App.getDocument(full["DOC_NAME"])
assert sample["L"] == full["LENGTH"] == 12000
for label, doc, count, solid_count in (("sample", sample_doc, 44, 0), ("full", full_doc, 7, 2)):
    solids = sum(len(obj.Shape.Solids) for obj in doc.Objects if hasattr(obj, "Shape"))
    assert len(doc.Objects) == count and solids == solid_count
    assert all(not obj.Shape.isNull() and obj.Shape.isValid() for obj in doc.Objects)
    print(label, "document", doc.Name, "objects", len(doc.Objects), "solids", solids)
