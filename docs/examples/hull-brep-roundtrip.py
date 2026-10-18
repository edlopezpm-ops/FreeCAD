# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Export only the two hull solids to temporary BREP custody.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]

from tempfile import TemporaryDirectory
import Part

ns = runpy.run_path(str(ROOT / "FreeCAD Hull/FullCatamaranHull.py"))
doc = App.getDocument(ns["DOC_NAME"])
shapes = [doc.getObject(name).Shape for name in ("Port_Hull", "Starboard_Hull")]
assert all(shape.isValid() and len(shape.Solids) == 1 for shape in shapes)
compound = Part.Compound(shapes)
expected_volume = sum(shape.Volume for shape in shapes)
with TemporaryDirectory(prefix="freecad-hulls-") as directory:
    path = Path(directory) / "two-hulls.brep"
    compound.exportBrep(str(path))
    restored = Part.Shape()
    restored.read(str(path))
    assert not restored.isNull() and restored.isValid()
    assert len(restored.Solids) == 2
    assert abs(restored.Volume - expected_volume) / expected_volume < 1e-9
    print("temporary_brep_bytes", path.stat().st_size, "restored_solids", len(restored.Solids))
print("hull_brep_roundtrip", True)
