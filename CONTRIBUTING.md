<!-- (kommiBo) Project-specific contribution and reproduction guidance. -->

# Contributing to FreeCAD

Start with the [README](README.md), [use boundaries](TERMS.md) and
[licensing inventory](docs/licensing.md). The root [license scope](LICENSE) identifies
the files available under the standard [MIT License](LICENSES/MIT.txt). This guide
does not expand that scope, add conditions to MIT, or create a contributor agreement
or promise of support. Submit only material you are entitled to share. For restricted
material or an unclear permission, contact [aekr@aekr.io](mailto:aekr@aekr.io) before
sharing it. Use [SECURITY.md](SECURITY.md) for a private vulnerability report.

## Reproduce a geometry change

Use FreeCAD 1.1.3. From the repository root in a disposable session, run:

```sh
freecadcmd --safe-mode --console "import runpy; runpy.run_path('tests/validate_models.py', run_name='__main__')"
```

The [validator](tests/validate_models.py) runs the three Python generators, checks
their expected geometry and opens both committed `.FCStd` reference files. The
[CI workflow](.github/workflows/validation.yml) verifies a pinned Linux AppImage
before running that validator. A syntax check under standard Python does not execute
the FreeCAD APIs and cannot replace geometry validation.

Include the exact generator or reference file, changed parameters, FreeCAD version,
OS, fresh-session steps, failing assertion or traceback, and expected versus actual
geometry. State dimensions with units and include a screenshot when it clarifies the
failure. Avoid personal paths or customer drawings in attachments.

## Keep source and reference artifacts reviewable

Explain whether a change affects a generator, a committed CAD reference, or both.
When updating a binary model, describe how it was produced and what changed; preserve
the source needed to reproduce the intended result. Inspect labels and metadata before
sharing exports using the [data-handling guide](docs/data-handling.md).

A valid solid or positive volume does not establish hull safety, rack load capacity,
installation suitability or code compliance. Keep such claims outside the software
validation result and seek the appropriate engineering review for real-world use.

## Submit a bounded pull request

Describe the concrete problem, affected files, resulting behavior and validation
actually performed, including failures or missing runtime checks. Separate unrelated
changes. For documentation-only edits, check relative links, commands and claims
against the repository; do not claim runtime evidence from prose checks.

Do not include credentials, personal records or generated temporary artifacts.
Preserve copyright and dependency notices, and explain any proposed permission change
explicitly. Keep review and acceptance separate from implementation. A reviewed merge
is not proof of deployment or real-world suitability. Recover a bad merged change
through a reviewed revert rather than rewriting shared history.
