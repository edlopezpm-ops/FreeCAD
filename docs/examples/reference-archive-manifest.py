# (kommiBo) Optional documentation example; source-backed, bounded evidence.
"""Fingerprint source and inspect reference archives without opening CAD.

Uses standard-library Python; does not validate FreeCAD geometry.
See the paired engineering note for expected output and limitations.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

root = Path(__file__).resolve().parents[2]
references = ("FreeCAD Hull/Catamaran_Hull_Only.FCStd",
              "FreeCAD_WHRackDesign/FreeCAD_WHRackDesign_3_Racks_3_Levels.FCStd")
paths = ("FreeCAD Hull/FullCatamaranHull.py", "FreeCAD Hull/SampleCatHull.py",
         "FreeCAD_WHRackDesign/WarehouseRack3x3.py", "tests/validate_models.py", *references)
files = {}
for relative in paths:
    raw = (root / relative).read_bytes()
    files[relative] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}
archives = {}
for relative in references:
    with zipfile.ZipFile(root / relative) as archive:
        assert archive.testzip() is None, relative
        entries = sorted(archive.namelist())
        assert "Document.xml" in entries
        archives[relative] = entries
head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True, check=False)
print(json.dumps({"head": head.stdout.strip() if head.returncode == 0 else None,
                  "files": files, "archive_entries": archives,
                  "geometry_validation": "not_run_by_this_example"}, indent=2, sort_keys=True))
