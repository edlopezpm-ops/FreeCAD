# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Inspect a closed station profile before interpreting the loft.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


ns = runpy.run_path(str(ROOT / "FreeCAD Hull/FullCatamaranHull.py"))
points = ns["station_profile_points"](ns["PORT_CENTER_Y"], .5)
assert len(points) == 12
assert all(abs(point.x - 6000) < 1e-7 for point in points)
for point in points:
    print(tuple(round(value, 6) for value in (point.x, point.y, point.z)))
wire = ns["make_closed_profile"](points)
assert wire.isClosed() and wire.isValid()
assert len(wire.Edges) == 1
print("input_points", len(points), "wire_edges", len(wire.Edges),
      "closed", wire.isClosed(), "valid", wire.isValid())
box = wire.BoundBox
print("profile_bounds_mm", (box.XMin, box.XMax, box.YMin, box.YMax, box.ZMin, box.ZMax))
