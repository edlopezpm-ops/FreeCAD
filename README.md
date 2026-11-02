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

No project license has been selected. GitHub’s platform terms permit viewing and forking; broader project reuse requires appropriate permission. The separate AEKR provenance notice does not license the project material.

## Governance

Changes follow the AEKR engineering workflow: bounded scope, deterministic geometry validation, pull-request review, and revert-PR recovery. The PR author and reviewer are distinct technical actors under one HOC authority; the reviewer approves and merges the exact validated head. This separation is an operational control, not an independent audit.

<!-- (kommiBo) Source-backed documentation navigation. -->
## Engineering recipes

See the [engineering notes](docs/engineering-notes/README.md) for reproducible examples, source references and validation limits.

<!-- (kommiBo) Project-specific behavior, privacy and permission boundaries. -->
## Privacy, use and permissions

The generators run inside a FreeCAD installation, not a normal standalone Python
interpreter. Valid geometry is not evidence of rack load capacity or vessel safety.
Reference CAD files and new exports need a metadata and provenance review before sharing.

- [Privacy notice](PRIVACY.md): project processing, hosting and requests.
- [Use and service boundaries](TERMS.md): intended use and license precedence.
- [Licensing inventory](docs/licensing.md): project, dependency and AEKR provenance scopes.
- [Data handling](docs/data-handling.md): local artifacts and publication checks.
- [Security reporting](SECURITY.md): private reports and support limits.

---

Built with the **[AI Engineering Knowledge Racking (AEKR)](https://aekr.io)** workflow.
