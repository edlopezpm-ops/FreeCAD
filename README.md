# FreeCAD Hobby Projects

Python scripts for generating simple FreeCAD models as hobby/learning projects.

## Status

These are executable learning models, not certified naval, structural, storage-system, or safety designs. The committed `.FCStd` files are reference artifacts; the Python generators are the reviewable source for validation.

## Projects

- `FreeCAD Hull`: catamaran hull-only model generated with FreeCAD Python APIs.
- `FreeCAD_WHRackDesign`: three warehouse pallet racks with three storage levels each.

## Usage

Open a script, copy it into the FreeCAD Python console, or run it with `freecadcmd` for a quick geometry check.

These are visual learning models, not certified naval, structural, or engineering designs.

## Validate

Requirements: FreeCAD 1.1.3. From the repository root, run:

```bash
freecadcmd --safe-mode --console "import runpy; runpy.run_path('tests/validate_models.py', run_name='__main__')"
```

The validator executes all three generators headlessly, checks the expected geometry, and opens both committed `.FCStd` files. CI downloads the official Linux x86-64 FreeCAD 1.1.3 AppImage and verifies its SHA-256 before running the same validator.

## License

No license file is present, so this repository grants no general permission to copy, modify, distribute, or reuse the work. Professionalization did not add or change licensing terms.

## Governance

Changes follow the AEKR engineering workflow: bounded scope, deterministic geometry validation, pull-request review, and revert-PR recovery. The PR author and reviewer are distinct technical actors under one HOC authority; the reviewer approves and merges the exact validated head. This separation is an operational control, not an independent audit.

---

Built with the **[AI Engineering Knowledge Racking (AEKR)](https://aekr.io)** workflow.
