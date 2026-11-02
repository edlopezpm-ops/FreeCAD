<!-- (kommiBo) Source-reviewed repository notice; no runtime or license grant is implied. -->

# Privacy — FreeCAD

Reviewed 2026-11-01.

## Scope and responsibility

AEKR maintains this project's notices and is the contact for questions at
[aekr@aekr.io](mailto:aekr@aekr.io). This notice covers local hobby generators and reference FreeCAD files for hull and warehouse-rack geometry.
It does not claim a new legal entity or apply the aekr.io website's analytics,
questionnaire, browser-data email service or retention periods to this repository.

## What the reviewed source does

The three generator scripts create geometry in the local FreeCAD process. The
validator executes those scripts and opens the two committed `.FCStd` reference files.
The reviewed generators do not implement an analytics collector, hosted account
service or model API call.

A saved `.FCStd` is a document archive and may contain labels and metadata beyond a
rendered shape. Local exports, screenshots, preferences and logs are separate data
surfaces. Neither a successful geometry check nor this notice establishes that every
model or a user's FreeCAD installation is free of personal or confidential content.

Source evidence: [hull generators](FreeCAD%20Hull/README.md), [rack generator](FreeCAD_WHRackDesign/WarehouseRack3x3.py), [geometry validator](tests/validate_models.py). This is a source review, not a guarantee about every
dependency, host, historical artifact or future deployment.

## Hosting, requests and retention

GitHub processes repository visits and collaboration activity under its
[privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).
If you serve a local copy over HTTP, that server can log requests. Downloading runtimes
or dependencies contacts their providers. Those operations are distinct from collection
implemented by the project itself. No repository-wide anonymous-visitor or zero-log
guarantee is made here.

Public issues, commits and attachments can be retained in history, forks, caches and
clones. Do not submit secrets, personal records or confidential data. For questions,
corrections, access or removal requests about project-held information, contact AEKR;
use [SECURITY.md](SECURITY.md) for a vulnerability report. Requests are considered under
applicable requirements; this notice promises neither a specific legal outcome nor
deletion of copies controlled by other parties. Local files have the retention described
in the [data-handling guide](docs/data-handling.md).
