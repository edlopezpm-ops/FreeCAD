# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Verify the direction and volume of a synthetic brace.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]

import math

ns = runpy.run_path(str(ROOT / "FreeCAD_WHRackDesign/WarehouseRack3x3.py"))
doc = App.newDocument("Engineering_Example_Brace")
start = App.Vector(0, 0, 200)
end = App.Vector(0, 1100, 2100)
radius = ns["SIDE_BRACE_SIZE"] / 2
brace = ns["add_cylinder_between_points"](doc, "Synthetic_Brace", start, end, radius, (0.2, 0.2, 0.2))
doc.recompute()
axis_length = end.sub(start).Length
expected_center = App.Vector(0, 550, 1150)
expected_volume = math.pi * radius ** 2 * axis_length
assert brace.Shape.isValid() and len(brace.Shape.Solids) == 1
assert brace.Shape.CenterOfMass.sub(expected_center).Length < 1e-6
assert abs(brace.Shape.Volume - expected_volume) / expected_volume < 1e-9
print("axis_length_mm", axis_length, "volume_mm3", brace.Shape.Volume)
print("brace_geometry", True)
before = len(doc.Objects)
try:
    ns["add_cylinder_between_points"](doc, "Rejected", start, start, radius, (0, 0, 0))
except RuntimeError as error:
    assert "greater than zero" in str(error)
else:
    raise AssertionError("coincident endpoints were accepted")
assert len(doc.Objects) == before
print("zero_length_rejected", True)
