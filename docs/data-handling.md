<!-- (kommiBo) Source-reviewed repository notice; no runtime or license grant is implied. -->

# Safe data handling and publication

Reviewed 2026-11-01.

This is an operator checklist for local hobby generators and reference FreeCAD files for hull and warehouse-rack geometry, not a claim that these controls
are automatically enforced by the code.

1. Work in a disposable FreeCAD session and preserve unrelated open documents before
   running a generator. Document replacement and saving are separate from validation.
2. Inspect reference-file properties and object labels before sharing CAD archives;
   reviewing only a screenshot does not inspect the embedded document.
3. Use invented customer names, warehouse layouts and dimensions in demonstrations.
   Exclude real facility plans and operational constraints from public examples.
4. Review screenshots and exports for file paths and application metadata. Keep local
   preferences, add-ons and unrelated models outside a publication bundle.
5. Preserve the committed reference models when checking generator changes. A deliberate
   new export requires its own geometry, provenance and disclosure review.

The project provides no automatic cleanup policy for files you save locally. Remove
unwanted exports and backups explicitly; prior public copies can remain available.

## Review before publishing

Check the complete staged diff and all attachments, not just source extensions. Reject
secrets, real customer records, personal documents and unexplained binary exports.
Use synthetic reproductions in public discussions. If information is already public,
contact AEKR through [the privacy notice](../PRIVACY.md); changing the current file
does not erase Git history or third-party copies. Rotate an exposed credential through
its provider rather than relying on a later Git deletion.
