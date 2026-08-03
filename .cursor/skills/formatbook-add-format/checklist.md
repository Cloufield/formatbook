# Format spec checklist

Copy for each `formats/<key>.json`:

```
Format: ___________
File: formats/___________.json

Phase 1 — Intake
- [ ] Software / resource identified
- [ ] Analysis or file role described
- [ ] Example output filename noted

Phase 2 — Identity
- [ ] JSON stem matches formatbook key
- [ ] format_name set
- [ ] Distinct from sibling layouts (or intentional union spec)

Phase 3 — Provenance
- [ ] format_source (docs URL)
- [ ] format_source_2 if needed
- [ ] github_url if repo exists (repo root only)
- [ ] format_version
- [ ] last_check_date (YYYYMMDD)

Phase 4 — Citation
- [ ] format_cite_name
- [ ] format_citation (from software_citations.json or lookup)

Phase 5 — File layout
- [ ] format_separator / format_na / format_comment / format_header
- [ ] format_col_order when column order is fixed

Phase 6 — Analysis context
- [ ] format_description

Phase 7 — Headers
- [ ] format_dict complete
- [ ] format_dict_2 if dual mappings
- [ ] header_description for non-obvious columns

Phase 8 — Validate
- [ ] check_format_jsons.py passes
- [ ] check_format_jsons.py --strict passes
- [ ] format_pages.py regenerated
- [ ] format_summary.py regenerated
- [ ] create_formatbook.py run
```
