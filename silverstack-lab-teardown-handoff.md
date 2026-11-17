# HANDOFF — Silverstack Lab UI Teardown

**Created:** 2026-11-17
**Status:** Phase 0 complete and frozen. Phase 1 blocked on three user inputs. Phase 2 not started.
**Read this file top to bottom before replying.** It is the source of truth; do not re-derive it.

---

## 1. Objective

Produce a forensic UI teardown of **Silverstack Lab** (Pomfort's macOS DIT / dailies application) to serve as a worked example for an AI coding assistant: how to read a dense professional desktop UI, name its patterns, and re-apply them to a different app.

Three phases, strictly sequential:

| Phase | Content | Gate |
|---|---|---|
| 0 | Research 14 sources → domain brief (450 words max) | **Done, frozen in §4** |
| 1 | Screenshot teardown: per-screen wireframes, tokens, component inventory, density audit | Needs user screenshots |
| 2 | Distil into 6–8 reusable patterns + implementation brief for the user's stack + confidence table | Needs stack choice |

Deliverable location/format is still open (see §8).

---

## 2. Operating rules (apply to every future message)

**Citation — exactly one tag per claim, never blurred:**

| Tag | Meaning |
|---|---|
| `[doc]` | Stated on a page fetched in this project. Must carry a URL (or a D-number per §3). |
| `[obs]` | Visible in a screenshot the user supplied. |
| `[recall]` | From model training data, not verified here. Use sparingly, flag every time. |

If something is `[recall]` and the docs contradict it, **the docs win and you say so out loud.**

**Phase 1 numeric discipline:**
- Every px / hex / radius / font size is an **estimate** → prefix `≈` and state the basis ("≈28px row, calibrated against 11px body text; ±2px").
- Never complete a cropped panel. Write `cropped — cannot assess`.
- No adjectives. Mechanism, not vibe: `1px #3A3A3C divider`, not "clean separation".
- Density is the deliverable: row heights, control heights, icon sizes, truncation strategy — always.
- Contradictions between screenshots get named, not averaged.

**Per-screenshot output shape:** `screen name | purpose | dominant layout pattern | ASCII wireframe (~60 cols, labelled regions + proportions) | what is anchored vs scrolling`.

**Shared sections after the per-screen blocks:** design tokens (colour / type / spacing scale / radii + borders + elevation, as tables) · component inventory with observed vs assumed states · density & ergonomics audit (3 strengths, 3 weaknesses, each evidence-tagged).

**Checklist tagging (Phase 1, mandatory):** every named region from §5 gets one of:
- `present → [obs]`
- `described in docs but not visible → [doc, not shown]`
- `visible but undocumented → [obs, undocumented]`

The third category is where the design insight lives — do not skip it.

**Style:** terse, technical, skimmable, tables over prose, completeness over brevity.

---

## 3. Source register

All 14 sources were fetched successfully. **Do not re-fetch** — facts are captured below. URLs kept for verification and citation.

| ID | URL | Page "last updated" | Yield |
|---|---|---|---|
| D1 | `https://kb.pomfort.com/silverstack/reference/library/user-interface-overview/` | Jan 2013 (label, likely stale) | 24 numbered UI regions + collection-view badge key. **The single best region inventory.** |
| D2 | `https://kb.pomfort.com/silverstack/reference/library/user-interface-window-layouts/` | Mar 2017 | 5 named UI layouts and what each sidebar/centre/panel is set to. |
| D3 | `https://kb.pomfort.com/silverstack/reference/library/the-information-panel/` | Jan 2013 | 6 right-panel tabs, editable vs read-only, pencil-icon convention, header→custom-field take-over. |
| D4 | `https://kb.pomfort.com/silverstack/reference/library/library-outline/` | Jan 2013 | Project / Bin / Folder / Smart Folder / Volumes model, version counts, sort orders. |
| D5 | `https://kb.pomfort.com/silverstack/reference/library/jobs-view/` | **Mar 2025 (current)** | Full jobs-view anatomy, hierarchy, states, actions, metrics, volume settings. Richest and freshest page. |
| D6 | `https://kb.pomfort.com/silverstack/getting-started/data-management/` | Apr 2020 | Offload/backup framing, XXH64, classic + ASC media hash lists, workflow chaining. |
| D7 | `https://kb.pomfort.com/silverstack/getting-started/playback-quality-check/` | Apr 2020 | JKL, scrub, zoom, RAW display res, scopes, frame lines, SDI, grid/wipe, playback priority. |
| D8 | `https://kb.pomfort.com/silverstack/getting-started/dailies-grading/` | Apr 2020 | Look source per clip, ASC-CDL / 3D LUT / ACES, RAW dev, look library, Livegrade look matching, hardware panels. |
| D9 | `https://kb.pomfort.com/silverstack/getting-started/transcoding/` | Apr 2020 | DNxHD/HR, ProRes, H.264/265; QT/MXF/MP4; 3 UIs (preset panel → workflow window → jobs view); "Transcoded Clips" bin; sidecar metadata. |
| D10 | `https://kb.pomfort.com/silverstack/getting-started/reports/` | Apr 2020 | 5 report types; classic vs updated style; light + dark; PDF + HTML; report wizard; post-step automation. |
| D11 | `https://pomfort.com/silverstacklab/` | current | Marketing vocabulary: "over 100 metadata fields per clip", clip library regions, Jobs View promise, delivery targets. |
| D12 | `https://pomfort.com/workflow/` | current | Workflow hub: looks-on-set, immersive, virtual production, ACES, ZEISS, Frame.io. Thin on UI. |
| D13 | `https://www.cined.com/pomforts-silverstack-lab-simplifies-set-data-handling/` | 10 Apr 2017 | Third-party 2017 launch piece. Confirms single-interface thesis + workflow order; **pricing/feature list is 2017-era, do not cite as current**. |
| D14 | `https://blog.frame.io/2021/04/05/frameio-pomfort-silverstack-lab-integration/` | Apr 2021 (upd. 2023) | Frame.io upload flow: OAuth prefs → pick account/team/project/folder → Start Upload → status screen → PDF job report with per-file links. Confirms "job report" as a deliverable. |

### 3a. Figure URLs (fallback screenshot source if the user supplies none)

The KB and product pages embed reference captures. Usable as `[obs]` only if explicitly agreed with the user — say which you used.

```
D1  …/user-interface-overview/images/2025-Pomfort-…-User-Interface-Overview.jpg
D1  …/images/2025-Pomfort-…-User-Interface-Overview-Collection-View-Thumbnail.jpg
D2  …/user-interface-window-layouts/images/2025-Pomfort-…-UI-Window-Layouts-{Files,Manage,Quality-Control,Color,Transcoding-Presets}.jpg
D3  …/the-information-panel/images/RightBarTabs-1.png
D3  …/images/Screen-Shot-2017-04-02-at-19.31.53.png            (User Info tab)
D3  …/images/Screen-Shot-2016-02-08-at-19.51.05.png            (File tab)
D3  …/images/2023-07-24_SilverstackLab_headerInfo_takeOver.jpg  (header → custom field)
D4  …/library-outline/images/Screen-Shot-2017-04-02-at-19.37.04.png
D4  …/images/Screen-Shot-2017-04-02-at-19.35.16.png
D4  …/images/Screen-Shot-2018-12-07-at-16.{42.34,55.49,55.59,59.28}.png
D4  …/images/Screen-Shot-2017-06-01-at-17.25.51.png            (Duplicate Folder Structure)
D5  (no inline images — text only; the jobs-view page must be worked from a user screenshot)
D6–D10 …/getting-started/{data-management,playback-quality-check,dailies-grading,transcoding,reports}/images/2025-…-Primary-Feature{s,,-}.jpg
D11 /img/silverstacklab/silverstacklab-screen.png?v=1.3 , /img/silverstacklab/SilverstackLabMain.jpg
D11 /img/silverstacklab/SST_Features_{AudioSync,DailiesGrading,Transcoding,DeliveryLab}.png
```

---

## 4. Phase 0 output — FROZEN, do not rewrite

Verbatim as delivered and accepted. Reuse it; only amend if a screenshot contradicts it (and then say which line changed and why).

# DOMAIN BRIEF — Silverstack Lab (Pomfort)

## A. What the user is actually doing

- **Ingest:** run one offload workflow that copies camera media to several destinations, verifies each copy by checksum, registers clips in the library [doc·D6].
- **Verify / organise:** file clips into project → folder → bin; set camera/scene/shot/take, rating, flag, label so the day stays searchable [doc·D3, D4].
- **QC / grade / transcode:** scrub with scopes and JKL, sync audio by timecode, apply looks, render proxies in chosen codecs/containers [doc·D7, D8, D9].
- **Deliver / report:** run post steps (MHL, reports), upload to NLE/cloud targets, export shooting-day, clip, contact-print, volume reports [doc·D5, D10, D14].

## B. Vocabulary

| Term | Plain English | Why the UI must surface it | Src |
|---|---|---|---|
| Offload | copy camera media to disk | day-one action; needs volume + destination picker | D6 |
| Workflow | chained activities run once | needs a configure surface distinct from the monitor | D6, D5 |
| Activity→Job→Task | what to do / one run / one file | 3-level hierarchy; must not be flattened | D5 |
| Checksum verify | re-read the copy, compare hashes | per-file integrity proof; drives pass/fail colour | D6, D13 |
| ASC MHL | standard hash-list file for handover | exportable proof artefact; a completion step | D6, D10 |
| Look | colour transform attached to a clip | library + per-clip apply + live preview | D3, D8 |
| Dailies | editor-facing proxy + metadata | the pipeline's actual output | D9, D13 |
| Bin / Folder / Project | container / grouping / whole production | tree needs counts, drag-drop, custom order | D4 |
| Smart folder | folder with a live filter | replaces manual sorting | D4 |
| Volume | drive / card / RAID | capacity, priority, eject/seal, read-write limits | D5 |
| Resource | a file belonging to a clip | missing resources must be flagged per clip | D1 |

## C. The three hard UI problems

**1. Density at metadata scale.** The library holds every clip of a shoot; Silverstack claims "over 100 metadata fields per clip" [doc·D11], the Header tab exposes them raw with a take-over into custom fields [doc·D3], and the outline annotates each node with a version count while collection view stacks six badges per clip [doc·D4, D1]. The UI must let the DIT choose which ~100 fields become columns, hold those columns stable across thousands of rows, and push per-clip noise into an inspector.

**2. Irreversible verbs next to the only original.** The operator who presses Eject or Seal on the card holding the sole copy also aborts and re-queues jobs, and may only discover a failed copy hours later [doc·D5]. Media ops therefore need typed/explicit confirmation, and job state needs history and log files so a late failure is diagnosable rather than merely red. Note: the docs list volume actions as Offload, Seal, Eject, Open in Finder, Manage Resources, Show in Offload Menu — **no "format card" operation appears**; treat formatting as [recall] only.

**3. Trust in long parallel background work.** One workflow can fan into a backup plus three verify jobs, each with per-file tasks, running in parallel and auto-paused while a copy job runs [doc·D5]. Progress must be legible at two levels at once (per-job bar, per-workflow bar) plus ETA, FPS, time remaining, and a partially failed run must not read as failed ("Has Failed Tasks (but running)") [doc·D5]. The bottom status bar aggregates scheduled/running/failed/aborted/ok across workflows [doc·D5]; the product page sells exactly this surface [doc·D11].

## D. What the official docs say the UI contains (D1–D5 only)

- **D1 overview:** playback view; playback controls; main toolbar; view tabs (summary/table/collection/playback); breadcrumb navigation; project chooser; ShotHub sync; timecode; playback mode single/grid/split; visual controls + full-screen; miniplayer + scopes; Audio & Color panel + its tabs; Library/Jobs switch; library outline + sort control; general-info tabs; general info; general-info filter; info display + dynamic metadata panel; jobs summary; running-jobs progress; collection-view badges (thumbnail, name+duration+label, ingest date/time, audio indicator e/i/ie, flag, resource count).
- **D2 layouts:** Files, Manage, QC, Color, Transcoding presets; left sidebar = library outline; centre = list | collection | playback | transcoding preview; right = Files and Hashes | General Info | User Info | Look Library | presets; Audio & Color panel enabled/disabled per layout.
- **D3 info panel:** six tabs — General Info, User, File, Header, Look Library, Transcoding; pencil-marked editable fields; flags, ratings, labels, cue points, comments; User tab holds camera letter, scene/shot/take.
- **D4 outline:** Project, Bin (video/audio), Folder, Smart Folders, Volumes; version count per node; sorts Custom Order, Name A–Z, Name Z–A, Date oldest→newest, Date newest→oldest; drag-and-drop; Duplicate Folder Structure; folders on top, audio bins below video.
- **D5 jobs view:** volumes bar (left); workflow/job grid (centre); details bar (right); top bar; status bar (bottom); Scheduled / Running / Workflow History; job metrics FPS, ETA, time remaining, task progress; details sections Workflow Summary, Show State History, Log File, Workflow's Jobs, Status, Errors, Configuration, Completion Steps, Parent Workflow; volume details Eject, Volume Summary, Performance Settings (Playback Prio, LTFS flag, Read/Write, Max Reading, Max Writing).

*(Body ≈445 words. The source key lives in §3, outside the 450-word body — that split was accepted.)*

---

## 5. Phase-1 prep notes — additive facts not in the brief

Use these to build hypotheses *before* looking at screenshots, then test them. Keeping them separate avoids re-reading 14 pages.

### 5a. The layout matrix (D2) — the spine of the whole product

| Layout | Left sidebar | Centre | Right sidebar | Audio & Color panel |
|---|---|---|---|---|
| Files | library outline | **list view** | Files and Hashes | off |
| Manage | library outline | **collection view** | General Info | off |
| QC | **hidden** | **playback view** | User Info | colour |
| Color | **hidden** | playback view | Look Library | colour |
| Transcoding presets | **hidden** | **transcoding preview** | presets | off |

Read this as: *the product is a set of named task modes, each a saved arrangement of four independently-toggleable regions.* The same four regions are also individually toggleable via toolbar buttons (D1 #11, #13). Hypothesis to test: that the layout buttons are presets over the same state, not separate screens — i.e. switching back preserves scroll/selection.

### 5b. Jobs-view state inventory (D5) — build the state machine, then check the screenshot against it

Active: Running · Waiting · Suspended (grey clock) · Has Failed Tasks (but running) · Automatically Interrupted.
Finished: Complete (green check) · Failed (red stop sign) · Cancelled (grey cross).
Read/unread: small blue dot per workflow.
Actions: Abort (loses current task, keeps completed) · Re-Queue (resumes after last successful task) · Suspend (finishes current task first) · Resume.
Job types: Backup (copy+verify | copy only) · Verify · Transcode · Dynamic Metadata Extraction · Dailies Upload · Ci Media Cloud Upload · AWS S3 Upload · Checksum Creation.

Note the deliberate distinction between **cancel/abort** (terminal) and **suspend** (resumable), and between **"failed but still running"** and **"failed"**. If the screenshot shows only one red state, that is a finding.

### 5c. Items the docs describe but that are easy to miss

- Jobs-view grid zoom: zoom in / out / 1:1 / fit-to-window (D5 §2.1.1) — implies a canvas, not a table.
- Jobs-view "Chart" button: task execution timeline, framed as a debugging tool (D5 §2.4.1).
- Volumes bar "+" appears **only for volumes never used before** (D5 §2.3) — conditional affordance.
- Volume performance settings: Playback Prio, LTFS flag, Read/Write exclusivity, Max Reading, Max Writing (D5 §2.2.3) — a settings form living inside a monitoring sidebar.
- Count indicators clear when workflows are marked read (D5 ×2) — read state is a data-clearing mechanism, not a cosmetic one.
- Overall progress = **unweighted average** of workflow progresses (D5 note) — a stated, arguable calculation choice.
- Bottom bar can switch running-workflow presentation between "Summary" (one aggregate bar) and "Workflows" (one bar each) (D5 §2.4.2).
- Report styles: classic vs updated; updated ships **light and dark**; PDF and HTML (D10).
- Transcodes land in a generated "Transcoded Clips" folder and inherit OCF metadata (D9).
- Clip identity can be driven by ShotID rather than filename (sidebar link `shotid-as-clip-identifier`, not fetched).

### 5d. Documentary weak spots — check these rather than assume

- D3 and D4 are 2013 pages. Current app is v9.4 (2026). Their described UI may predate what the screenshots show. **Where they conflict with a screenshot, the screenshot wins for what exists now; say so explicitly.**
- D5 (Mar 2025) is the only current reference page — treat it as authoritative.
- No page describes a card-format operation. Do not invent one.
- No page describes keyboard shortcuts, drag-and-drop semantics for clips (only for bins/folders), or empty/error/zero states. Those must be `[obs]` or declared as gaps.
- D11 uses consumer-marketing language ("human-centric automation"); do not let it into the teardown as evidence about the UI.

---

## 6. Phase 1 specification (ready to execute)

Per screen: `screen name | purpose | dominant layout pattern | ASCII wireframe (~60 chars wide, labelled regions + proportions) | anchored vs scrolling`.

Then the three shared sections. Then the checklist reconciliation (§2 tagging rule + §4 part D list).

**Suggested screen order** (mirrors the task modes in §5a): Manage → Files → Library-during-offload → Jobs View → QC → Color → Transcoding presets → Report output.

**Estimate basis convention:** state the calibration anchor per screen (e.g. "body text assumed 11px; all control heights derived from that"), then keep every derived `≈` consistent with it. Never mix two anchors in one screen block.

---

## 7. Phase 2 specification (ready to execute)

1. `## Reusable patterns` — 6–8 rules an assistant can apply to a **different** app.
   Format: `Name | When to use | Rule (imperative, 1–3 sentences) | Anti-pattern prevented`.
   Abstraction level to hit, e.g.: *"Dense data tables: fix row height at 24–28px; middle-ellipsis filenames; keep row actions in a hover-revealed right gutter so column widths never shift."*
   Each pattern must be traceable to a §4 or Phase-1 finding — no generic UI advice.
2. `## Implementation brief for <stack>` — paste-ready token block; component tree; the 3 hardest components and why; ordered build sequence.
3. `## Confidence & gaps` — table `claim | [doc]/[obs]/[recall] | why uncertain | how to verify`; end with 3 questions for a Pomfort designer.

---

## 8. Open inputs (blocking)

| # | Input | Why it blocks | Notes |
|---|---|---|---|
| 1 | Screenshots | Phase 1 has no `[obs]` without them | Ranked list in §8a |
| 2 | Target stack | Phase 2 §2 is stack-specific | e.g. React+TS+Tailwind+shadcn+TanStack Table · SwiftUI · plain HTML/CSS. Constraints (no component lib, offline, virtualised table only) matter |
| 3 | Deliverable form | Affects file layout from now on | Markdown file in repo vs printed in chat; one file vs one per phase |

### 8a. Screenshot wishlist, ranked

1. **Manage layout** — collection of clips, outline left, General Info right. (Badge stack, tree counts, metadata density.)
2. **Files layout** — list/table centre, right sidebar on "Files and Hashes". (Row height, column set, truncation, hover gutter.)
3. **Library during a live offload/verify** — bottom status bar with scheduled/running/failed/aborted/ok + job-type icons.
4. **Jobs View** — volumes bar + workflow grid + details bar, ideally on a *failed* job so Errors and Completion Steps populate.
5. **QC layout** — player + Audio & Color + scopes + timecode + transport.
6. **Color layout** — Look Library right sidebar.
7. **Transcoding presets layout** — preset panel + preview.
8. **A generated report** (PDF, shooting-day or contact-print).

Cropped regions are acceptable; they get marked `cropped — cannot assess`. Fallback: KB figure URLs in §3a, only if the user agrees.

---

## 9. Next actions

1. Read replies against §8; if screenshots arrive, name each file → which ranked view it maps to → then analyse.
2. Execute §6 for each screen. Reconcile against §4 part D with the three-way tag.
3. Ask for the stack if not yet given, then execute §7.
4. Update this file's status line when a phase closes.

Do not skip ahead between phases. Do not re-fetch §3 URLs. Do not rewrite §4 unless a screenshot contradicts it.
