# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Check guide visibility options against the construction inventory.

Requires the FreeCAD runtime; use a fresh session.
See the paired engineering note for expected output and limitations.
"""

import runpy
from pathlib import Path

import FreeCAD as App

ROOT = Path(__file__).resolve().parents[2]


ns = runpy.run_path(str(ROOT / "FreeCAD Hull/FullCatamaranHull.py"))
rebuild = ns["rebuild_document"]
live = rebuild.__globals__
keys = ("SHOW_STATION_FRAMES", "SHOW_LONGITUDINAL_GUIDES")
original = tuple(live[key] for key in keys)
try:
    for frames, guides in ((False, False), (True, False), (False, True), (True, True)):
        live[keys[0]], live[keys[1]] = frames, guides
        doc = rebuild()
        expected = 2 * (1 + int(frames) + int(guides)) + 1
        assert len(doc.Objects) == expected
        for name in ("Port_Hull", "Starboard_Hull"):
            assert len(doc.getObject(name).Shape.Solids) == 1
        print("frames", frames, "guides", guides, "objects", len(doc.Objects))
finally:
    for key, value in zip(keys, original):
        live[key] = value
    restored = rebuild()
assert len(restored.Objects) == 2 * (1 + int(original[0]) + int(original[1])) + 1
print("default_restored", True)
