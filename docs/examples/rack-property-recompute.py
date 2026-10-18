# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Demonstrate a document-property edit with restoration.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


ns = runpy.run_path(str(ROOT / "FreeCAD_WHRackDesign/WarehouseRack3x3.py"))
doc = App.getDocument(ns["DOC_NAME"])
deck = doc.getObject("Rack_01_Level_1_WireDeck_Visual")
assert deck is not None and deck.TypeId == "Part::Box"
original_height = deck.Height.Value
original_volume = deck.Shape.Volume
expected_delta = deck.Length.Value * deck.Width.Value * 10.0
try:
    deck.Height = original_height + 10.0
    doc.recompute()
    observed_delta = deck.Shape.Volume - original_volume
    assert abs(observed_delta - expected_delta) < 1e-5
    print("volume_delta_mm3", observed_delta)
finally:
    deck.Height = original_height
    doc.recompute()
assert abs(deck.Shape.Volume - original_volume) < 1e-5
print("original_volume_restored", True)
