<!-- (kommiBo) Operator-assisted maintenance; source-reviewed documentation. -->
# FreeCAD model validation: change boundaries and recovery

| Source | Associated review boundary |
| --- | --- |
| `FreeCAD Hull/FullCatamaranHull.py` | Hull solids, dimensions, and port/starboard placement. |
| `FreeCAD Hull/SampleCatHull.py` | Guide geometry and centerline. |
| `FreeCAD_WHRackDesign/WarehouseRack3x3.py` | Rack geometry and floor/aisle reference. |
| Committed `.FCStd` files | Reference artifacts; preserve them for documentation-only changes. |

Quote paths containing spaces in shell commands. Consult the [hull guide](../FreeCAD%20Hull/README.md) and [rack guide](../FreeCAD_WHRackDesign/README.md) for their own usage details. If a source change requires a refreshed model, review source and binary artifact together; a readable code diff alone cannot describe every binary change.

## Recover through a reviewed PR

1. Read the current default branch and preserve the failing PR URL, its head SHA, and the relevant CI log. Distinguish an infrastructure failure from a changed project contract.
2. Create a separate recovery branch from the latest default branch. Inspect the original change and later dependent commits before choosing a corrective edit or `git revert`.
3. For a squash commit, revert that commit on the recovery branch. For a merge commit, inspect its parents and deliberately select the mainline; do not blindly copy a `-m` value. Resolve conflicts explicitly and preserve unrelated later work.
4. Run the [repository validation](validation-guide.md), inspect the diff, and open a recovery PR. Record the reason and the original PR/commit it compensates for.
5. Require the configured CI and separate reviewer approval on the current head. If the head changes, verify its checks and review again. Merge through the normal branch rules without bypass.
6. Verify the merge SHA on GitHub and the resulting default-branch validation. A successful local command or PR creation is not proof of merge completion.

Do not force-push the default branch or delete pre-existing files as a recovery shortcut. If kommiBo reports an uncertain effect, preserve its operation/run identity and reconcile it before submitting duplicate work. Writer and reviewer accounts are separate technical actors under one HOC; this is not an independent audit.
