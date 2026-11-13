<!-- (kommiBo) Source-reviewed repository notice; no runtime or license grant is implied. -->

# Licensing and provenance inventory

Reviewed 2026-11-12.

No root project license has been selected. The scripts and committed CAD reference files have no general reuse grant from this maintenance change.

| Component | Evidence and licensing boundary |
|---|---|
| Hull/rack scripts and committed `.FCStd` files | No root project license; review ownership and permission before reuse. |
| `FreeCAD`, `Part`, `Draft`, optional `FreeCADGui` | External runtime modules with their own distribution and dependency notices. |
| Exported BREP or other geometry | Export does not itself grant rights or demonstrate engineering certification. |

## AEKR provenance has a bounded scope

The [AEKR banner notice](../assets/AEKR-BANNER-LICENSE.txt) is copied unchanged from
the AEKR project-branding scaffold. It records the MIT provenance of that upstream
scaffold and any AEKR banner copied from it. Upstream references inside that verbatim
notice describe the toolkit, not a requirement to add its handbook here. It is not a
license for unrelated project code, data, personal material or third-party marks.

The AEKR footer names the workflow used. It neither transfers copyright to AEKR nor
imports the toolkit's CC BY handbook license into this repository. Where no banner
image is present, retaining its provenance notice does not claim that an image is bundled.

## Recorded license and permission changes

This history distinguishes a changed permission from an update to its documentation.
The linked commits identify the material being described; this inventory is not a new grant.

| Date | Source change | Effect on permissions |
|---|---|---|
| 2026-11-01 | [Licensing inventory added](https://github.com/edlopezpm-ops/FreeCAD/commit/2566cdb8e307f44b1865e95b937b7e99330d795d) | Documented the absent root license and the distinction between project models and the FreeCAD runtime; no general license was added. |
| 2026-11-12 | This inventory update | Adds reuse guidance and traceable history; preserves the existing permissions. |

## Which permission applies to a proposed reuse?

| Proposed action | Applicable boundary |
|---|---|
| View or fork this public repository on GitHub | GitHub's platform terms permit these platform actions; this is not a general project license. |
| Redistribute or adapt scripts, committed CAD files or exported project geometry beyond applicable rights | Request the missing permission and identify the source files and revision, including the generator behind an export. |
| Package FreeCAD or an add-on alongside these models | Review that distribution's own notices and requirements separately; the runtime license does not license these models. |
| Publish a screenshot or export | Review project permissions, third-party material and embedded metadata; a successful geometry test supplies none of those permissions. |

For a permission request, send [aekr@aekr.io](mailto:aekr@aekr.io) the repository,
commit or release, relevant paths, and intended use or distribution. Omit confidential
source data. A request is not approval; retain any actual written permission with the
revision and files it covers. A future license change needs an explicit scope and must
preserve third-party notices and permissions already granted.

## Before redistributing

Check the actual files and installed dependency versions, preserve their applicable
notices, and obtain any missing permissions. A package name, a public repository,
a passing test or a software bill of materials is not itself a grant. This is a bounded
source inventory, not an exhaustive dependency-license or ownership certification.
The [use notes](../TERMS.md) cannot override a license grant.

Reference: [GitHub's repository licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository).
