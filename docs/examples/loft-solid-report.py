# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Report closed hull topology and measured dimensions.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


ns = runpy.run_path(str(ROOT / "FreeCAD Hull/FullCatamaranHull.py"))
doc = App.getDocument(ns["DOC_NAME"])
volumes = []
for name in ("Port_Hull", "Starboard_Hull"):
    obj = doc.getObject(name)
    assert obj is not None
    shape = obj.Shape
    assert not shape.isNull() and shape.isValid()
    assert len(shape.Solids) == 1 and shape.Volume > 0
    box = shape.BoundBox
    assert abs(box.XLength - ns["LENGTH"]) < 1.0
    assert box.YMax < 0 if name == "Port_Hull" else box.YMin > 0
    print(name, "solids", len(shape.Solids), "shells", len(shape.Shells),
          "faces", len(shape.Faces), "edges", len(shape.Edges), "volume_mm3", shape.Volume)
    print("bounds_mm", (box.XMin, box.XMax, box.YMin, box.YMax, box.ZMin, box.ZMax))
    volumes.append(shape.Volume)
print("relative_volume_difference", abs(volumes[0] - volumes[1]) / max(volumes))
print("FreeCAD_version", App.Version())
