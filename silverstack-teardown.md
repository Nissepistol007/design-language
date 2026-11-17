# Silverstack Lab — Forensic UI Teardown

**Worked example for an AI coding assistant**
Target for Phase 2: **SwiftUI / macOS-native**
Author: product-design + front-end architecture pass
Date: 2026-11-16
Phases: 0 (research) → 1 (teardown) → 2 (distillation)

---

## 0. Method & provenance

### 0.1 Sources read (Phase 0)

All 14 sources in the brief were fetched successfully. **No fetch failed.**

| Key | URL | What it gave |
|---|---|---|
| D1 | `https://kb.pomfort.com/silverstack/reference/library/user-interface-overview/` | The 24-point region map of the main window; collection-view badge legend |
| D2 | `https://kb.pomfort.com/silverstack/reference/library/user-interface-window-layouts/` | The 5 named UI layouts and what each one enables/disables |
| D3 | `https://kb.pomfort.com/silverstack/reference/library/the-information-panel/` | The 6 information-panel tabs and the read-only/edit split |
| D4 | `https://kb.pomfort.com/silverstack/reference/library/library-outline/` | Project/Folder/Bin/Smart Folder tree model and sort options |
| D5 | `https://kb.pomfort.com/silverstack/reference/library/jobs-view/` | workflows→activities→jobs→tasks, job states, jobs-view anatomy |
| D6 | `https://kb.pomfort.com/silverstack/getting-started/data-management/` | Offload→backup→jobs→post-steps model; XXH64; ASC MHL |
| D7 | `https://kb.pomfort.com/silverstack/getting-started/playback-quality-check/` | JKL, scopes, overlays, playback priority, grid & wipe |
| D8 | `https://kb.pomfort.com/silverstack/getting-started/dailies-grading/` | Look source, CDL/3D-LUT/ACES modes, look library, ScopeBox |
| D9 | `https://kb.pomfort.com/silverstack/getting-started/transcoding/` | Preset panel → workflow config → jobs view; sidecar metadata export |
| D10 | `https://kb.pomfort.com/silverstack/getting-started/reports/` | 5 report types, classic/updated style, light+dark, PDF/HTML |
| D11 | `https://pomfort.com/silverstacklab/` | Product positioning; "over 100 metadata fields per clip" |
| D12 | `https://pomfort.com/workflow/` | Workflow taxonomy around the Pomfort ecosystem (looks-on-set, ACES, Frame.io) |
| D13 | `https://www.cined.com/pomforts-silverstack-lab-simplifies-set-data-handling/` | 2017 review: set-to-post narrative, GPU transcode, feature list |
| D14 | `https://blog.frame.io/2021/04/05/frameio-pomfort-silverstack-lab-integration/` | Frame.io integration; job-status screen; PDF job report on completion |

> D13's page returns ~4,100 lines of site navigation before the article body. The article body was read from the saved full output; content confirmed present (title *"Pomfort's Silverstack Lab Simplifies On-Set Data Handling"*, Olaf von Voss, 10 Apr 2017). No content was invented.

### 0.2 Captures obtained (Phase 1)

No user screenshots were supplied, so the analysis uses **first-party Pomfort imagery**: the knowledge-base reference captures, the product-page screenshot, and two partner-blog captures. All were downloaded to `silverstack_refs/`.

| ID | File | Source | Native px | Scale | Used for |
|---|---|---|---|---|---|
| **C-FILES** | `C_layout-files.jpg` | kb.pomfort.com/…/user-interface-window-layouts/images/2025-…-UI-Window-Layouts-Files.jpg | 3456×2160 | 2× → 1728×1080 pt | Primary: table, outline, Files & Hashes |
| **C-MANAGE** | `D_layout-manage.jpg` | …/UI-Window-Layouts-Manage.jpg | 3456×2160 | 2× | Collection grid, General Info panel |
| **C-QC** | `E_layout-qc.jpg` | …/UI-Window-Layouts-Quality-Control.jpg | 3456×2160 | 2× | Playback, User Info, Audio & Color |
| **C-TRANS** | `G_layout-transcode.jpg` | …/UI-Window-Layouts-Transcoding-Presets.jpg | 3456×2160 | 2× | Preset panel, preview |
| **C-OVW** | `A_ui-overview.jpg` | …/user-interface-overview/images/2025-…-User-Interface-Overview.jpg | 4832×3020 | annotated | Canonical region map, 24 callouts |
| **C-OVW-COLL** | `B_collection-thumb.jpg` | …/User-Interface-Overview-Collection-View-Thumbnail.jpg | 1269×793 | downscaled | Collection-view badge legend (cropped) |
| **C-INFP** | `H_info-panel.png` | …/the-information-panel/images/RightBarTabs-1.png | 666×1670 | unknown, 2017 build | Info-panel tabs, field rows |
| **C-VERIF** | `N_verification.png` | …/verification-states/images/Screen-Shot-2018-06-07-at-09.51.44.png | 2032×1289 | windowed, 6.4 build | Verification states, volume cards |
| **C-OFFLOAD** | `M_offload-menu.jpg` | …/offload-menu/images/2026-03_UI-Screenshots-Highlighting-Elements_OffloadMenu.jpg | 3456×2160 | 2× | Downloaded; **not visually inspected** |
| **C-PROJ** | `R_project-chooser.jpg` | …/project-chooser/images/2025-…-Project-Chooser.jpg | 3456×2160 | 2× | Downloaded; **not visually inspected** |
| **C-SMART** | `Q_smartfolders.png` | …/smart-folders/images/9a-Smart-Folders.png | 2033×795 | — | Downloaded; **not visually inspected** |
| **C-LOOK** | `X_looklibrary.png` | …/the-silverstack-look-library/images/LookLibrary2.png | 347×788 | — | Downloaded; **not visually inspected** |
| **C-QUICK** | `Y_quickentry.png` | …/quick-metadata-entry-tricks/images/quick-entry-tricks-1.png | 533×287 | — | Downloaded; **not visually inspected** |
| **C-PTBAR** | `O_player-toolbar.png` | …/playback/images/Silverstack_Player_Toolbar.png | 818×392 | — | Downloaded; **not visually inspected** |
| **C-PLAY** | `P_playback.png` | …/playback/images/Screenshot-2020-03-03-at-12.37.59.png | 1202×216 | — | Downloaded; **not visually inspected** |
| **C-JOBS** | `Z1_frameio-jobstatus.png` | blog.frame.io/…/fixed-upload-job-status.png | 1600×1000 | 1×, v7.3 (2021) | Jobs view, **historical** (pre-9.x table layout) |
| **C-JOBS9** | *(user-supplied screenshot, not on disk)* | conversation input, 2026-11-16 | rendered ≈2000×1250, **DPR unverified** | Jobs view, **current (9.x)** — the card-grid layout |
| **C-FIO-AUDIO** | `Z2_frameio-audio.png` | blog.frame.io/…/silverstack-lab-audio-media.png | 1600×969 | 1× | Downloaded; **not visually inspected** |
| **C-FIO-UP** | `Z3_frameio-upload.png` | blog.frame.io/…/upload-clips-pt2.png | 1600×979 | 1× | Downloaded; **not visually inspected** |
| **C-CINE** | `V_cined-screen.jpg` | cined.com/…/Silverstack-Lab-_-screen.jpg | 1920×1200 | — | Downloaded; **not visually inspected** |

### 0.3 Measurement protocol

- Primary captures are **2× Retina** (3456×2160 native). All native-pixel measurements below are converted to points by ÷2. **Basis for the conversion: the capture is exactly 3456×2160, i.e. 1728×1080 pt at DPR 2** — a stock macOS scaled resolution.
- Structural numbers (row pitch, control heights, icon boxes, panel boundaries) were extracted programmatically with `silverstack_refs/probe.py` + `rows.py` (row-ink-band detection + connected-component bounding boxes), not by eye.
- **Every numeric value is an estimate** and is prefixed **≈**. Where a value is literally legible in a capture (e.g. a hash string, a byte count, a resolution) it is quoted verbatim and tagged as such.

> **C-JOBS9 measurement caveat (important).** The 2026 Jobs view was supplied as a chat attachment and **is not on disk**, so `probe.py` / `rows.py` could not be run against it and its colours could not be sampled. Every C-JOBS9 number below is a **visual estimate read off the rendered view** (≈2000 px wide), and every colour is a **visual judgement, not a sampled value**. Treat C-JOBS9 point values as **±30%** and its hex values as **±15%**. All structural claims (what exists, where, in what order) are high-confidence; all numeric claims from this capture are low-confidence. Every C-JOBS9 measurement is additionally tagged **[est]** to distinguish it from the sampled values elsewhere in this document.

### 0.4 Citation key

| Tag | Meaning |
|---|---|
| `[doc]` | Stated on a page fetched this session. URL given. |
| `[obs]` | Visible in a capture named in-line. |
| `[recall]` | From training data, **not verified** above. Flagged every time. |

**Capture-generation caveat:** C-FILES / C-MANAGE / C-QC / C-TRANS are one 2025 release family (Silverstack 9.x, per D11's "Version 9.4"). C-VERIF is a 2018 6.4 build. C-JOBS is a 2021 7.3 build. C-INFP is a 2017 build. Where they disagree, the document says so rather than merging.

---

# PHASE 1 — SCREENSHOT TEARDOWN

## 1.0 Shared chrome (applies to C-FILES, C-MANAGE, C-QC, C-TRANS)

Silverstack is one window, one top-level menu bar, and three stacked horizontal bands plus a bottom bar. Almost every screen is a **re-configuration of the same four bands**; that is the single most important structural fact about this product.

```
┌──────────────────────────────────────────────────────────────────────┐
│ BAND 0  OS menu bar                                                 │
├──────────────────────────────────────────────────────────────────────┤
│ BAND 1  TOOLBAR   [7 action icons+labels]   [project ⌄] [9 modes]   │  ≈48pt
├──────────────────────────────────────────────────────────────────────┤
│ BAND 2  CONTEXT   [sidebar tools][view tabs][breadcrumb][search][⚡] │  ≈30pt
├───────────────┬──────────────────────────────────────┬───────────────┤
│               │  BAND 3  CONTENT                     │               │
│  LEFT SIDEBAR │  table | grid | player | presets     │  RIGHT SIDEBAR │
│  ≈371pt      │  ≈924pt                               │  ≈432pt       │
│               │                                      │               │
├───────────────┴──────────────────────────────────────┴───────────────┤
│ BAND 4  STATUS BAR  [Library|Jobs]      [5 job-type glyphs]  [pill] │  ≈40pt
└──────────────────────────────────────────────────────────────────────┘
```

**Band 1 — toolbar.** Left cluster is seven icon+label actions: `Offload · Add Clips · Media · Export · Import · Report · Transcode` `[obs C-FILES]`. Centre holds the project chooser (`Silverstack ⌄`) and a ShotHub cloud button `[doc D1][obs C-FILES]`. Right cluster is nine items: five *named* mode buttons with labels (`Files · Manage · QC · Color · Presets`) followed by four icon+label toggles (`Miniplayer · Scopes · Audio & Color · Sidebars`) `[obs C-FILES]`. The five mode buttons are the "UI layouts" of D2; they are not decorative — clicking `QC` re-writes which sidebars are enabled and what the centre pane shows.

| Measured (C-FILES, 2×) | Value | Basis |
|---|---|---|
| Band 1 height | ≈96 native px = **48 pt** | row-ink boundary at native y≈96 |
| Action icon glyph box | 29–36 native px = **≈15–18 pt** | connected-component bbox; Offload 35×35, Media 31×31, Export 29×27, Transcode 30×30 |
| `Add Clips` glyph | 14×24 native px = **≈7×12 pt** | dashed-frame glyph, intrinsically narrower |
| Toolbar label ink band | 14 native px = **7 pt** ≈ **10 pt font** | row-ink band y 76–89 |
| Right-mode icon box | 22–40 native px = **≈11–20 pt** | bbox sweep x 2256–3410 |

**Band 2 — context bar.** Background `#3D3D3D`, ≈30 pt tall (native y 105–165). Left end: three small tool buttons (info, group, person/running) plus a gear at the right edge of the left sidebar. Then a **4-way view-mode segmented toggle** (list / table / grid / preview) `[doc D1 calls these "view tabs"]`. Centre: a **breadcrumb** — `Library › 20240426_Day_1 › Camera_Media › ▪A_0001_1DJH 1` — where the last node carries a coloured square glyph that matches the outline tree's node colour `[obs C-FILES]`. Right end: a contextual popup (`Digital Imaging Tec…`), a scoped search field (`Search in 'All Fi…`), four small icon toggles, an `A|B` toggle, and two more icon buttons.

**Band 4 — status bar.** Background `#3D3D3D`, **40 pt** (native y 2080–2160). Left: a macOS `NSSegmentedControl` reading `Library | Jobs` — the global Library↔Jobs switch `[doc D5 calls this the "Library/Jobs switch"]`. Centre: five dimmed job-type glyphs (backup, verify, transcode, upload, dynamic-metadata) that light up when their job type runs `[doc D5 lists exactly these five]`. Right: a status-count pill. In the 2018/2021 builds this is a green `7 ok` / `6 ok` pill `[obs C-VERIF][obs C-JOBS]`; in the 2025 Files capture no pill is rendered because no job is running `[obs C-FILES]`.

---

## S1 — Library View · "Files" layout (clip table + Files & Hashes)

**Screen name:** Library View / Files layout
**Capture:** C-FILES
**Purpose:** Compare every file resource belonging to every clip against its source volume and its backups, by checksum.

**Dominant layout pattern:** Three columns — persistent tree / dense data table / stacked resource cards. The centre column is the only scrolling body; the right column is a scrolling *stack of cards*, not a list.

```
┌─371pt────────┬─────────────────────924pt─────────────┬────432pt────┐
│ INFO DISPLAY │▸PREVIEW│NAME│SHOTID│DUR│FR│CAM│EI│…  │ FILES&HASHES │
│  name/dur    │ ▤     │A_0001…│3ND-…│37s│889│A_ │…  │ ┌─ file ───┐ │
│  4 backups   │ ▤     │A_0002…│U2D-…│30s│728│A_ │…  │ │size/hash │ │
│  4.68 GB     │ ▤     │A_0003…│CV6-…│35s│843│A_ │…  │ └──────────┘ │
│── tree ──────│ ▤     │A_0004…│EDP-…│37s│892│A_ │…  │ 3 backups  │
│ ▾ Library 418│ ▤ ★   │A_0005…│3ND-…│37s│889│A_ │…  │ # All OK   │
│  ▾ Day_1  171│ ▤     │A_0006…│5N3-…│1:03│1519│A_│…  │ ┌SOURCE───┐ │
│   ▾ Cam  93 │ ▤     │A_0007…│P3N-…│1:22│1972│A_│…  │ │folder/…  │ │
│    ★ A_0001 12│ ▤     │A_0008…│J8Q-…│1:28│2131│A_│…  │ └─────────┘ │
│    ★ B001R  12│        ← selected row = blue fill       │ ┌BACKUP────┐ │
│  ▾ Sound  78 │                                       │ └─────────┘ │
│ Sort Bins ▾  │ ← h-scroll thumb ≈30% of track        │ 🔍Filter   │
├──────────────┴───────────────────────────────────────┴─────────────┤
│ [Library|Jobs]            ▣ ⚡ ☁ ☺              ✓ pill (when busy) │
└─────────────────────────────────────────────────────────────────────┘
```

**Anchored vs scrolling**
- *Anchored:* Band 1 toolbar, Band 2 context bar, Band 4 status bar, the left tree's own scroll, the table's **column header row**, and the right panel's **filter field** (pinned to the bottom of the panel, not to the bottom of the document).
- *Scrolling:* table body (vertical), table body (horizontal — the header scrolls with it), right-panel card stack, left tree body.
- *The "General Info filter" is pinned at the bottom of the right sidebar* `[doc D1 #16][obs C-FILES]`, which is a different anchoring behaviour from the table header. Two different "search" idioms coexist in one window.

**Measurements (C-FILES, 2×)**

| Element | Value | Basis |
|---|---|---|
| Left sidebar width | 742 native px = **371 pt** (21.5% of 1728 pt) | bg boundary `#424242`→`#383838` at x=743 |
| Right sidebar width | 864 native px = **432 pt** (25%) | bg boundary at x=2592/2610 |
| Centre content | 1849 native px = **924 pt** (53.5%) | remainder |
| Table header row | ≈30 native px = **≈15 pt** | ink band at native y 175–195 |
| **Table data row pitch** | **58 native px = 29 pt** | 13 consecutive ink bands, pitch 58, median 58 |
| Table cell text ink band | 24 native px = **12 pt** | ink band height |
| Preview column width | ≈146 native px = **73 pt** | thumbnail gutter x 744–890 |
| Tree row pitch | **50 native px = 25 pt** | 15 ink bands, median 50 |
| Tree indent per level | ≈27 native px = **≈13.5 pt** | icon x-offsets 40/68/95/120 |
| Folder icon | 36 native px = **18 pt** | bbox |
| Purple "custom look" badge | 28×28 native px = **14×14 pt**, radius ≈6 native px = 3 pt | bbox + radius |
| Green verification glyph | 13–14 × 22 native px = **≈7×11 pt** | connected-component bbox, 4 instances |
| General Info row pitch | **40 native px = 20 pt** | 12 ink bands, median 40 |
| General Info key column | 2627→2920 native = **146 pt** | label/value x positions |
| General Info value column | 2920→3456 native = **268 pt** | remainder |
| Edit (pencil) button | ≈22 native px = **≈11 pt** diameter, circular | bbox on C-INFP |
| Status bar height | 80 native px = **40 pt** | `#3D3D3D` band y 2080–2160 |
| `Library｜Jobs` control | 235×44 native px = **117×22 pt**, radius ≈14 native px = 7 pt | bbox + corner sample |
| Horizontal scroll thumb | ≈546 native px in a 1848 native track → **≈30% of columns visible** | visual + ratio |

**Checklist D (from Phase 0) — region by region**

| Region named in docs | Status in C-FILES |
|---|---|
| Playback view / playback controls / timecode | not shown (this layout replaces them with a table) |
| Toolbar (offload, add, media, export, import, report, transcode) | **[obs]** — all 7 present |
| View tabs (summary/table/collection/playback) | **[obs]** — 4-way toggle present in Band 2 |
| Navigation (breadcrumbs) | **[obs]** — present, Band 2 centre |
| Project chooser | **[obs]** — Band 1 centre |
| ShotHub sync | **[obs]** — cloud button beside project chooser |
| Library/Jobs switch | **[obs]** — status bar left |
| Library outline + sorting | **[obs]** — tree + `Sort Bins by Custom Order ⌄` |
| General info / general-info filter | **[obs]** — but the right sidebar is showing **Files & Hashes**, not General Info |
| Info display (read-only) + dynamic metadata panel | **[obs]** — the read-only clip header strip at the top of the left sidebar |
| Jobs summary / running-jobs progress | **[doc, not shown]** — no jobs in flight in this capture |
| Miniplayer, scopes, Audio & Color panel | **[doc, not shown]** in this layout; **[obs]** in C-QC |
| Presets (transcoding presets) | **[doc, not shown]** in this layout; **[obs]** in C-TRANS |
| Layout switcher: Files / Manage / QC / Color / Presets | **[obs]** — Band 1 right cluster, all 5 |
| Clip thumbnail, name+duration, ingest date, audio indicator, flag, resource indicator | **[obs]** — the 6 collection-view badges |
| Files & Hashes sidebar | **[obs, undocumented]** — D2 names the right sidebar's role per layout ("Files and Hashes") but D1's 24-point list never names it as a region |
| Verification-state glyph per clip | **[obs]** — green `#` in the tree; **[doc D-list]** names "Verification states" only as a separate article |
| Volume-level detail cards (Folder / Filename / Created / Registered / Last Verified) | **[obs, undocumented]** in D1's region list; **[doc D5]** describes equivalent content in the Jobs view |

---

## S2 — Library View · "Manage" layout (collection grid + General Info)

**Screen name:** Library View / Manage layout
**Capture:** C-MANAGE
**Purpose:** Browse clips visually and edit their metadata in place.

**Dominant layout pattern:** Same chrome, but the centre becomes a **3-column thumbnail grid** and the right sidebar switches to the **General Info** tab.

```
┌─371pt────────┬─────────────────────924pt─────────────┬────432pt────┐
│ INFO DISPLAY │ Sort Clips by:[Clip Name ⌄][A-Z ⌄][◴] │ GENERAL INFO│
│  37 sec      │ ┌────────┐  ┌────────┐  ┌────────┐     │ ▾Video Clip │
│  889 frames  │ │  ▤     │  │  ▤     │  │  ▤     │     │  Name  A_00…│
│  4 backups   │ │        │  │        │  │        │     │  ShotID3ND-…│
│── tree ──────│ │  ▤     │  │  ▤     │  │  ▤     │     │  Duration37s│
│  (as S1)     │ └────────┘  └────────┘  └────────┘     │ ▾Slate Info │
│              │ name 37s   name 1:03   name 1:22      │ ▾Timecode   │
│              │ 26.04 26.04 26.04   ◁i  3 ▶          │ ▸Edit/User  │
│              │ ┌────────┐  ┌────────┐  ┌────────┐     │ ▸Camera Set │
│              │ │  ▤     │  │  ▤     │  │  ▤     │     │ ▸Lens       │
│              │ └────────┘  └────────┘  └────────┘     │ ▸Look       │
│              │  ← selected cell = 1px blue outline    │ 🔍Filter Gen│
├──────────────┴───────────────────────────────────────┴─────────────┤
│ [Library|Jobs]            ▣ ⚡ ☁ ☺                                   │
└─────────────────────────────────────────────────────────────────────┘
```

**Anchored vs scrolling**
- *Anchored:* all four chrome bands; the `Sort Clips by:` control row (Band 3 header, native y ≈160–210) — this row exists in the Manage layout and does **not** exist in the Files layout.
- *Scrolling:* the grid scrolls vertically as a whole; the right panel scrolls independently; the tree scrolls.

**Measurements (C-MANAGE, 2×)**

| Element | Value | Basis |
|---|---|---|
| Grid columns | 3 | visible |
| Thumbnail size | ≈440×250 native px = **≈220×125 pt** (16:9) | visual on the 2× capture |
| Grid gutter | ≈48 native px = **24 pt** | visual |
| Caption line 1 (filename + duration) | ink band 20 native px = **10 pt** | ink band y 885–904 |
| Caption line 2 (date/time + badges) | ink band ≈16 native px = **8 pt** | ink band y 915+ |
| Filename truncation | **tail ellipsis** (`A_0001C005_240426_083229…`) | rendered |
| Duration placement | **same line, right of the filename**, not a separate column | rendered |
| Audio indicator | glyph `◁i` = speaker + `i` for internal audio | rendered |
| Resource indicator | numeric badge `3` + a play triangle, in a pill | rendered |
| Selected cell | **1 px blue outline around the thumbnail**, no fill | rendered |
| General Info rows | 20 pt pitch, identical to S1 | measured |
| General Info group header | bold, ink band 22 native px = **11 pt**, `▾` disclosure | measured |
| General Info value truncation | **tail ellipsis** | rendered |

**Checklist D — region by region**

| Region | Status in C-MANAGE |
|---|---|
| Toolbar (all 7 + 9 modes) | **[obs]** |
| View tabs | **[obs]** — 4-way toggle, collection active |
| Breadcrumb navigation | **[obs]** |
| Project chooser | **[obs]** |
| Library outline + sorting | **[obs]** |
| Library/Jobs switch | **[obs]** |
| **General info panel** | **[obs]** — 12 groups visible: Video Clip, Slate Info, Timecode, Edit/User, Custom, Camera Settings, Camera/Recorder, Lens, Look, Processing, Production, Format |
| **General info filter** | **[obs]** — pinned `🔍 Filter General Info` at panel foot |
| Dynamic metadata panel | **[doc, not shown]** — D1 names it as living inside the *info display* (left strip), which is collapsed to a 4-line summary here |
| Info display | **[obs]** — left sidebar top strip: clip name, duration, frames, backup count, total size, a flag glyph |
| Jobs summary / running-jobs progress | **[doc, not shown]** |
| Collection-view badges (thumbnail, name+duration+label, ingest date/time, audio indicator, flag, resource count) | **[obs]** — all 6 present in the grid caption; label chip absent because no clip is labelled |

---

## S3 — Library View · "QC" layout (player + User Info + Audio & Color)

**Screen name:** Library View / QC layout
**Capture:** C-QC
**Purpose:** Judge one clip's image and technical integrity, and record the verdict.

**Dominant layout pattern:** Video dominates; the left sidebar is **removed entirely** (D2: "Left sidebar is disabled"); the right sidebar swaps to the **User Info** tab; a new **bottom-docked Audio & Color panel** appears, taking ≈30% of the centre column's height.

```
┌──────────────────────────────────────────────┬────432pt───────────┐
│ BAR 1 + BAR 2 (context)      08:38:20:12    │ USER INFO          │
├──────────────────────────────────────────────┤ ┌──┐┌──┐┌──┐┌──┐│
│ ░░░░░░░ letterboxed video ░░░░░░░░░░░░░░░░ │ │Ca││Sc││Sh││Ta││
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ └──┘└──┘└──┘└──┘│
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ ⚑Flagged  ★★★★★ │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ Comment▁▁▁▁▁▁▁▁▁ │
│ ├──── scrub bar, red playhead ──────────────┤ Caption▁▁▁▁▁▁▁▁▁ │
│ ├──── clip strip (horizontal scroll) ────────┤ ShotDesc▁▁▁▁▁▁▁▁ │
├──────────────────────────────────────────────┤ Label ●●●● [None] │
│ 🔊↻  Look [CDL Advanced ▾]        Edit ☺ ≡  │ Tags▁▁▁▁▁▁▁▁▁▁▁▁ │
│ ☑|CDL│ ⬤Offset ⬤Power ⬤Slope  R .0000 G..    │ Custom 1..6       │
│  |LOG│  (3 colour wheels)       R 1.0000      │ Cue Points ▭▭▭▭   │
│  |SPL│  (O|H toggles, reset ↺)  B 1.0000      │  + − →|  🔍Search │
│  |PRT│ Saturation ──────●──── 1.0            │                  │
│ ☑| Load… Default.ALF4 (From File) Size:65   │                  │
│ ☑| Preset ▾ ↺   ╱‾╲ ╱‾╲ ╱‾╲  (RGB curves)   │                  │
├──────────────────────────────────────────────┴──────────────────┤
│ [Library|Jobs]            ▣ ⚡ ☁ ☺                               │
└────────────────────────────────────────────────────────────────────┘
```

**Anchored vs scrolling**
- *Anchored:* all chrome bands; the Audio & Color panel header (Look dropdown, Edit, ☺, ≡); the colour-wheel row; the clip strip (horizontally scrolling).
- *Scrolling:* the video frame letterboxes to fit; the User Info form scrolls; the Audio & Color panel scrolls internally between grading rows.

**Measurements (C-QC, 2×)**

| Element | Value | Basis |
|---|---|---|
| Player pillarbox | video area centred; black bars ≈271 native px each side of a 1849 px column | visual |
| Scrub bar | full width of centre column, ≈20 native px = **10 pt** | visual |
| Red playhead marker | ≈4 native px = **2 pt** wide | visual |
| Clip strip | ≈40 native px = **20 pt** tall chips; selected chip = solid blue `#4D7ABE` with white text; unselected = `#3A3A3A` fill + 1 px border + **middle-ellipsis** filename (`A_0001C006_240426_0…`) | rendered |
| Colour wheel outer diameter | ≈130 native px = **≈65 pt** | visual on 2× capture |
| Colour-wheel numeric fields | ≈95 native px = **≈48 pt** wide, 4-decimal format | visual |
| Grading rail tabs (CDL/LOG/SPL/PRT) | ≈20 native px = **10 pt** wide, vertical 2-letter labels | visual |
| User Info big fields (Camera/Scene/Shot/Take) | ≈173×78 native px = **≈86×39 pt** | visual |
| User Info single-line field height | ≈24 native px = **12 pt** | visual |
| User Info form row pitch | **44 native px = 22 pt** | 13 ink bands, median 44 |
| Rating control | 5 discrete star glyphs, unselected = hollow | rendered |
| Label control | 9 colour dots + a `No Label` popup menu | rendered |
| Cue Points | a 4-column mini-table (Position/Duration/Name/Type) with empty rows + `+ − →|` toolbar + search field | rendered |

**Checklist D — region by region**

| Region | Status in C-QC |
|---|---|
| Playback view | **[obs]** |
| Playback controls | **[obs]** — not the floating JKL cluster here; in this capture the transport is off the visible bottom of the player. See C-OVW for the transport cluster (JBK/L, ⏮ ⏯ ⏭, loop, in/out) |
| Visual controls & full-screen playback buttons | **[obs]** in C-OVW (callout #10) |
| Timecode | **[obs]** — `08:38:20:12` in Band 2 centre, monospaced, large |
| Playback view options (single/grid/split) | **[obs]** in C-OVW (callout #9) |
| Miniplayer & scopes | **[obs]** in C-OVW (callout #12) — not visible in C-QC |
| Audio & Color panel + its audio/color tabs | **[obs]** — bottom-docked, with a vertical grading-mode rail |
| General info tabs → **User Info** | **[obs]** — right sidebar is the User Info tab |
| Info display | **[doc, not shown]** — left sidebar disabled in this layout |
| Library outline | **[doc, not shown]** — D2 explicitly disables it in QC layout |
| Jobs summary | **[doc, not shown]** |

---

## S4 — Library View · "Transcoding Presets" layout

**Screen name:** Library View / Transcoding Presets layout
**Capture:** C-TRANS
**Purpose:** Define and preview an output format, then hand it to a workflow.

**Dominant layout pattern:** The right sidebar becomes a **two-section panel (presets list over settings form)** while the centre stays a player — so the right sidebar is itself split vertically.

```
┌──────────────────────────────────────────────┬────432pt───────────┐
│ BAR 1 + BAR 2            08:38:20:12        │ PRESETS [Activate] │
├──────────────────────────────────────────────┤ [Video][Still] + ⋯ │
│ ░░░░░░░ letterboxed video ░░░░░░░░░░░░░░░░ │ ┌16:9┐ 720p         │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ │H264│ H.264,1280×7… │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ └────┘ 🔊 ◴         │
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ ┌16:9┐ Editorial-DNx│
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ │DNxHD│ DNxHD LB 1080…│
│ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │ └────┘  ╔═ selected │
│ ├──── scrub bar ─────────────────────────────┤ ┌16:9┐ blue fill  │
│ ├──── clip strip ────────────────────────────┤ └────┘             │
├──────────────────────────────────────────────┤ SETTINGS        🔓 │
│ [Library|Jobs]            ▣ ⚡ ☁ ☺            │ ▾Video           │
└──────────────────────────────────────────────┴──────────────────┘
```

**Anchored vs scrolling**
- *Anchored:* the `Presets` header and its green `Activate Preview` button; the `Video|Still` segmented toggle.
- *Scrolling:* presets list (its own scroll, ≈310 native px tall) above a hairline; settings form (its own scroll) below the hairline.

**Measurements (C-TRANS, 2×)**

| Element | Value | Basis |
|---|---|---|
| `Activate Preview` button | ≈100×26 native px = **≈50×13 pt**, mint-green fill, radius ≈13 native px = 6.5 pt | visual |
| Preset aspect chip | ≈60×42 native px = **≈30×21 pt**, mint fill `#7CE95C`-family, radius ≈6 native px = 3 pt | visual |
| Selected preset row | full-width blue `#4D7ABE` fill, white title, **desaturated blue** spec text | rendered |
| Settings group card | 1 px border `#3A3A3A`, radius ≈8 native px = 4 pt, disclosure `▸` at left, checkbox inside the header for Audio/Source | rendered |
| Settings label/value split | labels right-aligned, controls left-aligned in the right ≈55% of the card | rendered |
| Lock toggle | single icon button in the `Settings` header, right-aligned | rendered |
| Collapsed groups | `Framelines`, `Resizing`, `Grading` render as a single 1-line header each | rendered |

**Checklist D — region by region**

| Region | Status in C-TRANS |
|---|---|
| Toolbar | **[obs]** — `Presets` mode button active |
| Playback view / scrub bar / clip strip | **[obs]** — persists from the QC layout |
| Transcoding presets panel | **[obs]** — D2 names "Right sidebar shows the presets" |
| **"Transcoding Preview" centre view** | **[doc, not shown]** — D2 states the centre is set to "Transcoding Preview"; the capture shows a normal player with the clip strip. Either the preview is the letterboxed player itself, or the capture predates that centre mode. **Unresolved — flagged, not merged.** |
| Transcoding tab in the info panel | **[doc, not shown]** — D3 names it; D9 says a transcoding preview "is automatically shown in the player view when the transcoding tab is opened". The visible right sidebar here is the **Presets** panel, not the info panel's Transcoding tab. Two different things share the word "transcoding preset". |

---

## S5 — Jobs View (current, Silverstack 9.x)

**Screen name:** Jobs & Volumes view
**Capture:** C-JOBS9 (user-supplied, 2026-11-16; project "7 Dagar med familjen")
**Purpose:** Watch, control and explain long-running background work across a whole shoot.

**Dominant layout pattern:** A **filter strip + card grid + details rail**. Not a table. Each workflow is a row of **cards**: card 1 = the workflow, card 2..n = the jobs that belong to it.

```
┌──────────────────────────────────────────────────────────────────────┐
│ ⏸ Suspend All  ▶ Resume All   [7 Dagar med familjen ⌄]  ⊞⊟≡  [🔍…] ⊞⊟│
├──────────────────────────────────────────────────────────────────────┤
│ Stage:[Sched][Run][Hist] │ Finish:[All][OK][Fail][Abr] │ Read:[All][Unread│
│ Date:[All][Today][Yest][Week][LastWk]              ⊖⊕⤢⊕  │            │
├────────────────────────────────────────────────────┬─────────────────┤
│ Workflow History                                   │                 │
│ ●┌──────────────┐ ┌──────────────┐                 │   Select a      │
│  │▪★ DJI_C009   │ │Backup (copy& │                 │   workflow, job,│
│  │  Backup Wkfl │ │   verify)    │                 │   or volume to  │
│  │ 2026-11-13   │ │     ✓        │                 │   show details. │
│  │ 16 min 36 sec│ │ 126TB_7Dagar_02│               │                 │
│  └──────────────┘ └──────────────┘                 │                 │
│ ●┌──────────────┐ ┌──────────────┐                 │                 │
│  │▮★ A_0058…hde │ │Backup (copy& │                 │                 │
│  │  ARRI_001 Wf │ │   verify)    │                 │                 │
│  │ 2026-11-13   │ │     ✓        │                 │                 │
│  │ 65 min 12 sec│ │ 126TB_7Dagar_01│               │                 │
│  └──────────────┘ └──────────────┘                 │                 │
│ … 9 visible rows, then a vast empty field to the right …             │
├────────────────────────────────────────────────────┴─────────────────┤
│ [Library|Jobs]         ▣ # ⚡ ☁ ☺                        [17 aborted][358 ok]│
└──────────────────────────────────────────────────────────────────────┘
```

**Anchored vs scrolling**
- *Anchored:* the whole top toolbar (Suspend/Resume, project chooser, Workflows/Tasks/Chart, search, Volumes/Details); the **filter strip**; the details rail (including its empty state); the status bar.
- *Scrolling:* the card grid only. A thin vertical scrollbar sits at the **right edge of the grid field, immediately left of the details rail divider** (≈x 1507 of 2000) — so the grid's scroll context is unambiguous, and the rail never scrolls.
- *The filter strip does **not** scroll.* It stays pinned above a long, unbounded history. This is the fix for the weakness I logged against the 2021 build.

**Measurements (C-JOBS9 — all [est], visual, ±30%)**

| Element | Value | Basis |
|---|---|---|
| Top toolbar height | ≈64 px | first row, y 0–64 |
| Filter strip height | ≈30 px | chip row centred at y ≈ 81 |
| Grid field top | y ≈ 92 | below the filter strip |
| Section label `Workflow History` | y ≈ 140, ≈12 px, secondary grey | rendered |
| **Card height** | ≈100 px | card 1 spans y 152–252 |
| **Card width** | ≈284 px | workflow card x 48–332; job card x 348–632 |
| Card gap (horizontal) | ≈16 px | 332→348 |
| **Card pitch (vertical)** | ≈116 px | 9 cards, name baselines 181→1112, median ≈116 |
| Workflow-card green state bar | ≈5 px wide, full card height | x 48–53 |
| Unread dot gutter | ≈14 px, at x ≈ 38 | outside the card, in the grid's left padding |
| Media-type icon | ≈22×22 px, ≈5 px radius | rounded square, purple or amber |
| Card title | ≈15 px, white, semibold | rendered |
| Card subtitle | ≈12 px, grey | rendered |
| Card meta row (date · duration) | ≈11 px, grey | rendered |
| Job-card green check | ≈26 px tall, centred | rendered |
| Job-card source string | ≈11 px, grey, centred | rendered |
| Details rail | x 1512–2000 = 488 px ≈ **24.4%** | divider position |
| Empty-state text | ≈14 px, centred both axes | rendered |
| Bottom bar | ≈45 px | y 1205–1250 |
| `Library｜Jobs` control | ≈136×26 px | rendered |
| Count pills | ≈70–75 × 22 px, ≈6 px radius | rendered |
| Filter chips | ≈68×20 px, ≈10 px radius, ≈8 px gap | rendered |
| Zoom glyph cluster | 3–4 magnifier buttons, ≈14 px, at the filter strip's right end | rendered |

**Doc ↔ capture conformance — this capture is unusually strong validation of D5**

| D5 claim | Status in C-JOBS9 |
|---|---|
| Top bar: Suspend All, Resume All | **[obs]** — both present, left |
| Top bar: Search Bar "to search for workflows and tasks" | **[obs]** — the field's placeholder is literally *Search for workflows and tasks* |
| Top bar: Tasks button (view individual tasks) | **[obs]** — `Tasks` with a list glyph, next to `Workflows` and `Chart` |
| Top bar: Chart button (timeline of job execution) | **[obs]** — `Chart` with a bar glyph |
| Top bar: Volumes toggle | **[obs]** — `Volumes` split-panel glyph, far right |
| Top bar: Details toggle | **[obs]** — `Details` split-panel glyph, far right |
| Grid filter criteria: **Stage / Finish / Read / Date** | **[obs]** — *exactly* those four groups, in that order, with those option sets (Stage: Scheduled/Running/History; Finish: All/Successful/Failed/Aborted; Read: All/Unread; Date: All/Today/Yesterday/This Week/Last Week) |
| Zoom in / out, Zoom 1:1, Zoom to fit | **[obs]** — magnifier cluster at the filter strip's right end |
| 1st column = workflow name and input; 2nd column and beyond = its jobs | **[obs]** — rendered as **cards** rather than table columns, but the same left-to-right job fan-out |
| Scheduled / Running / Workflow History | **[obs]** — three section headings; only *Workflow History* is expanded in this capture |
| Read/Unread = "a small blue dot next to the workflow on the left side" | **[obs]** — exact match: a blue dot in the grid's left gutter, outside the card |
| Complete = "a green checkmark icon indicates this state" | **[obs]** — green check centred in each job card |
| Status bar: Library/Jobs switch | **[obs]** — segmented control, Jobs selected |
| Status bar: job-type indicator icons (backup, verify, transcode, upload, dynamic metadata) | **[obs]** — five dimmed glyphs, centre |
| Status bar: Failed / Aborted / Ok summary | **[obs]** — `17 aborted` and `358 ok` pills. **No "failed" pill**, consistent with zero failed jobs |
| Right details bar depends on whether a workflow, job **or volume** is selected | **[obs]** — the empty state names all three: *"Select a workflow, job, or volume to show details."* |
| Status bar: Scheduled count, Running progress, Workflows/Summary switch | **[doc, not shown]** — no scheduled/running workflows in this capture, so those affordances are absent |
| **Left volumes sidebar** (+ per-volume `+` offload button, count indicators, progress view, context menu) | **[doc, not shown]** — the `Volumes` top-bar toggle exists, so the sidebar is collapsible, but it is **collapsed here**. Still unverified. |
| Details sections: Workflow Summary, Show State History…, Log File…, Status, Errors, Configuration, Completion Steps, Parent Workflow | **[doc, not shown]** — no selection made, so only the empty state is visible |
| Volume details: Eject, Volume Summary, Performance Settings (Playback Prio, LTFS, Read/Write, Max R/W) | **[doc, not shown]** — **the single largest remaining gap** |
| "Project Chooser is disabled in the Jobs & Volumes view" | **[obs, contradicts]** — the project chooser is present and appears enabled (chevron visible) |

---

## S5b — Jobs View (historical, Silverstack 7.3, 2021) — for contrast only

**Screen name:** Jobs & Volumes view, legacy table layout
**Capture:** C-JOBS (1600×1000, 1×, 2021 build)

**Dominant layout pattern:** A **two-pane stack** (running/queued grid above, history grid below) with a **right details rail**, a filter strip between them, and a persistent status bar.

```
┌────────────────────────────────────────────────────────┬────────────┐
│ MENU BAR   Silverstack Lab File Edit View Clip …       │            │
├────────────────────────────────────────────────────────┤ JOB        │
│ ⏸Suspend All  ▶Resume All      [Frame.io Test ⇅][☁] [✕]│ C300 (Post)│
│ Queue│Source│Job│Config│Progress│State│Rem│Start│…    │ 1.75GB/8   │
│ ▶ ▷ C300 Footage (Editorial) ☁ Upload Clips  ▓▓░░ 18EB/s│ State:Done │
│                                       11s  Today 697MB │ Log… ▣    │
│────────────────────────────────────────────────────────│ Clips Upload│
│ Summary:[All][Unread] State:[All][Succeeded][Failed]    │ Source Fold│
│ Date:[Anytime][2H][Today][Week][Month]      🔍Search   │ Config:MOV │
│ Source│Job│Config│Progress│State│Start│Size│Fin│Dur  │            │
│ ▶ ▷C300(Editorial) ☁Upload  Frame.io:MOV  ☑Complete    │            │
│ ▶ ▷C300(Editorial) ☁Upload  Frame.io:SST  ☑Complete    │            │
│ ▶ ✦C300 Footage      ⚡Transcode  Post      ☑Complete    │            │
├────────────────────────────────────────────────────────┴────────────┤
│ ▾Jobs              1 running ▓▓▓▓▓░░░ 8 sec left   Silverstack [6 ok]│
└──────────────────────────────────────────────────────────────────────┘
```

**Measurements (C-JOBS, 1×)**

| Element | Value | Basis |
|---|---|---|
| Bottom status bar height | 38 px = **38 pt** (1× capture) | `#3C3C3C` band y 962–1000 |
| Bottom progress bar | 268×18 px = **268×18 pt** | blue bbox x 666–933, y 973–990 |
| `6 ok` status pill | 88×24 px, radius ≈6 px, fill ≈**#448932**, white text | bbox x 1501–1588, y 970–993 |
| Lower table header height | ≈26 px | separator rows at y 433–435 and 451–453 |
| Lower table row pitch | **45–46 px** | 6 rows, y 475→702 |
| Filter strip | ≈22 px, segmented pills with selected = lighter fill | visual |
| Right details rail | 357 px = **22% of window width** | boundary at x=1243 |
| Grid header height | ≈16 px | visual |

**Checklist D — region by region (jobs view, 2021 build)**

| Region named in D5 | Status in C-JOBS |
|---|---|
| Left volumes bar | **[doc, not shown]** — the 2021 build has no volumes sidebar; D5's volume bar, `+` offload button, count indicators and per-volume progress view are **absent from this capture**. Strong evidence the Jobs view was re-architected between 7.3 and 9.x. |
| Centre grid: workflows and jobs | **[obs]** — Queue/Source/Job/Configuration/Progress/State columns |
| Scheduled / Running / Workflow History sections | **[doc, not shown]** — the capture shows one continuous grid, not three labelled sections |
| 1st column = workflow, 2nd+ = jobs | **[obs]** — partially: the source column plays the workflow role |
| Right details bar | **[obs]** — but it shows only *job* detail (State/Start/End/Duration, Clips Upload, Source Folder, Configuration). D5's **Workflow Summary**, **Show State History…**, **Log File…**, **Parent Workflow**, **Errors** and **Completion Steps** sections are **[doc, not shown]** |
| Top bar: Suspend All / Resume All / Search / Tasks / Chart / Volumes / Details | **[obs]** for Suspend All, Resume All and Search. **Tasks / Chart / Volumes / Details toggles: [doc, not shown]** |
| Bottom bar: Library/Jobs, Workflows/Summary, Scheduled, Running, job-type icons, Failed/Aborted/Ok | **[obs]** for the job-type strip, the running count + progress, and the Ok pill. **Scheduled count, Workflows/Summary switch and Failed/Aborted counters: [doc, not shown]** |
| Volume details (Eject, Playback Prio, LTFS flag, Read/Write, Max Reading/Writing) | **[doc, not shown]** |


---

## S6 — Files layout, Silverstack 6.4 (2018): verification states & volume cards

**Screen name:** Library View / Files layout, older build
**Capture:** C-VERIF (2032×1289, windowed)
**Purpose:** Show the *state* of every copy of every file, per volume.

**Dominant layout pattern:** Same three columns, but the centre table is reduced to 3 columns (Preview, Name, Verification…) and the right rail becomes a **document** — a file hash block, then a "Source & Backups" summary, then one card per volume.

```
┌──────────────────────────────────────────────────────────────────────┐
│ ●●● [7 action icons]   [Migration Test 6.3.5-6.4 ⌄] [10 mode btns]  │
├───────────────┬──────────────────────────────────────┬───────────────┤
│ INFO DISPLAY  │▸Preview│Name│Verification…            │ FILES & HASHES│
│ No dynamic    │ ▤      │A007C002…  │ #                 │ A007C002_…   │
│ metadata      │ ▤      │A007C003…  │ #                 │ Size 5.56GB   │
│ support       │ ▤      │A007C001…  │ #                 │ MD5…          │
│ Lens N/A      │                                      │ SHA1:c41d85…  │
│ Filter N/A    │                                      │ xxHash64:…    │
│ ND Filter N/A │                                      │───────────────│
│── tree ───────│                                      │1 src, 2 bkups │
│ ▾Library   19 │                                      │⚠Verif incompl│
│  ★X001[MD5] 5#│                                      │ ┌SOURCE──────┐│
│  ★A007R1KL 3#│                                      │ │A007R1KL    ││
│ ▾Smart Folders│                                      │ │folder/…    ││
│  Versions w/o │                                      │ │✓ verified  ││
│  Backup    3#│                                      │ └────────────┘│
│  ▸Volumes     │                                      │ ┌BACKUP─────┐│
│               │                                      │ │G-SPEED TB3││
│               │                                      │ │✓ verified  ││
│               │                                      │ └───────────┘│
│               │                                      │ ┌BACKUP─────┐│
│               │                                      │ │WD HDD Copy││
│               │                                      │ │✗ not verif││
│               │                                      │ └───────────┘│
├───────────────┴──────────────────────────────────────┴───────────────┤
│ ▲Jobs                                          Silverstack   [7 ok]  │
└──────────────────────────────────────────────────────────────────────┘
```

**Checklist D — region by region**

| Region | Status in C-VERIF |
|---|---|
| Toolbar | **[obs]** — 7 left actions (incl. `Seal`), 10 right modes incl. `Config` and `Second Display` |
| Info display | **[obs]** — full read-only strip: "No dynamic metadata support for this format" + explanatory sentence + a 3-column `Lens N/A / Filter N/A / ND Filter N/A` mini-grid |
| Library outline | **[obs]** — tree now includes a `Volumes` node |
| Verification-state column | **[obs]** — one glyph per row in a dedicated column |
| Per-volume resource cards with role badges `SOURCE` / `BACKUP` | **[obs]** |
| `Verification incomplete: 1 unverified file resource(s)` | **[obs]** — a global banner above the cards |
| Volume summary (capacity) | **[doc, not shown]** |
| Volume performance settings (Playback Prio, LTFS, Read/Write, Max R/W) | **[doc, not shown]** |
| Eject button | **[doc, not shown]** |
| Jobs view | **[doc, not shown]** — the capture is the Library view |

**Version drift note (contradiction, not merged):** C-VERIF has a **window title bar with traffic lights** and a centred project chooser; C-FILES is **full-screen with no traffic lights** and a project chooser inside the app's own toolbar. Both are "Silverstack" but the chrome changed.

---

## S7 — Information panel (2017 build)

**Screen name:** The Information Panel, General Info tab
**Capture:** C-INFP (666×1670 PNG, scale unknown, 2017 build)

```
┌──────────────────────────────────────────────────┐
│ [i][⚑][▤][<>]                      [🙂][⚡]     │  ← 6 tab icons
├──────────────────────────────────────────────────┤
│ General Info                                     │
│ ▾ Video Clip                                     │
│   Name              A003C012_160205…        ✎   │  ← pencil only on
│   Duration          41 sec                         │    editable rows
│   Frames            977                            │
│   Source File Date  16/03/17 10:12:29…            │
│   Registration Date 01/04/17 15:52:54…            │
│ ▾ Slate Info                                     │
│   Episode 4 ✎ | Scene 3A-3 ✎ | Shot - ✎ | …     │
│ ▾ Timecode                                       │
│ ▾ Edit                                            │
│ ▾ Settings                                        │
└──────────────────────────────────────────────────┘
```

**Measurements (C-INFP)** — crop scale unknown; row pitch measured 40 px in the crop.

| Element | Value | Basis |
|---|---|---|
| Field row pitch | 40 px in-crop | ink bands y 302/343/382/421 |
| Label ink band | ≈16 px | ink band height |
| Group header ink band | ≈22 px, bold | ink band height |
| Pencil button | circular, ≈22 px in-crop | visual |
| Value truncation | **tail ellipsis** | rendered |
| Row banding | alternating full-width bands, ΔL ≈ 2–3 levels | visual |

**Checklist D — region by region**

| Region named in D3 | Status in C-INFP |
|---|---|
| Six tabs: General Info, User, File, Header, Look Library, Transcoding | **[obs]** — 4 icons left + 2 icons right = 6. Consistent with D3. |
| Editable fields marked with a «pencil» icon | **[obs]** |
| Flags, ratings, labels, cue points | **[obs]** on other tabs (C-QC User Info), **[doc, not shown]** here |
| Read-only technical metadata "in a raw format" (Header tab) | **[doc, not shown]** |
| Take-over of header fields into custom fields | **[doc, not shown]** |
| Look Library tab / Transcoding tab | **[doc, not shown]** |

---

## S8 — Annotated UI overview (C-OVW)

**Screen name:** Canonical region map, 24 callouts
**Capture:** C-OVW (4832×3020, annotated with pink markers)

This capture is the 24-point legend from D1 rendered as an image. Its value is not new pixels but **the authoritative map**: callouts 1–24 are positioned over a single window showing the player, the Audio & Color panel, the General Info panel and the tree simultaneously.

**What it adds that no other capture shows:** the **transport control cluster** (callout 2) — a floating pill containing `Zoom: Fit ⌄`, `Full Resolution ⌄`, `Loop ☐`, `In/Out ☐`, a `T` button, ⏮ ⏪ ⏩ ⏭ ⏭, a fullscreen toggle and a snapshot button — and the **breadcrumbs-are-for-hiding-the-sidebars** note in D1 #5 ("This feature is specifically useful when hiding the library and clip information view").

**Callout → observed region mapping (condensed):**

| # | Region | Found in |
|---|---|---|
| 1 | Playback view | C-QC, C-TRANS, C-OVW |
| 2 | Playback controls (transport pill) | **C-OVW only** |
| 3 | Toolbar | C-FILES, C-MANAGE, C-QC, C-TRANS |
| 4 | View tabs | C-FILES, C-MANAGE, C-QC, C-TRANS |
| 5 | Navigation / breadcrumbs | C-FILES, C-MANAGE, C-QC, C-TRANS |
| 6 | Project chooser | C-FILES, C-MANAGE, C-QC, C-TRANS |
| 7 | ShotHub sync | C-FILES, C-MANAGE, C-QC, C-TRANS |
| 8 | Timecode | C-QC, C-TRANS, C-OVW |
| 9 | Playback view options (single/grid/split) | **C-OVW only** |
| 10 | Visual controls + full-screen | **C-OVW only** |
| 11 | Toolbar (layout switcher) | C-FILES, C-MANAGE, C-QC, C-TRANS |
| 12 | Miniplayer + scopes | **C-OVW only** |
| 13 | Toolbar (Audio & Color + sidebars toggles) | C-FILES, C-MANAGE, C-QC, C-TRANS |
| 14 | General info tabs / look library / transcoding presets | C-MANAGE, C-TRANS, C-OVW |
| 15 | General info | C-MANAGE, C-OVW |
| 16 | General info filter | C-MANAGE, C-OVW |
| 17 | Jobs summary | **[doc, not shown]** in any capture |
| 18 | Running jobs summary + progress | C-JOBS (equivalent), **[doc, not shown]** in 2025 captures |
| 19 | Audio & Color panel | C-QC, C-OVW |
| 20 | Audio & color tabs | C-QC, C-OVW |
| 21 | Library/Jobs switch | C-FILES, C-MANAGE, C-QC, C-TRANS, C-JOBS |
| 22 | Library outline sorting | C-FILES, C-MANAGE, C-VERIF |
| 23 | Library outline | C-FILES, C-MANAGE, C-VERIF |
| 24 | Info display (+ dynamic metadata panel) | C-FILES, C-MANAGE, C-VERIF |

---

## 1.9 Contradictions across captures (called out, not merged)

| # | Contradiction | Evidence | Reading |
|---|---|---|---|
| **X1** | **Jobs view anatomy.** D5 (updated 2025-03-04) describes: volumes sidebar left, centre grid with Scheduled/Running/History sections, right details bar with 9 named sections, top bar with Tasks/Chart/Volumes/Details toggles, bottom bar with Scheduled/Running/Failed/Aborted/Ok counters. C-JOBS (2021, 7.3) shows **none** of the volumes bar, none of the three sections, none of the Tasks/Chart/Volumes/Details toggles, none of the Failed/Aborted counters, and a details rail with only job-level content. | [doc D5] vs [obs C-JOBS] | **RESOLVED by C-JOBS9.** The 2021 build was the outlier; D5 describes the current UI accurately. C-JOBS9 confirms: the Volumes/Tasks/Chart/Details toggles, the Stage/Finish/Read/Date filter groups, the three stages, the read/unread blue dot, the Failed/Aborted/Ok counters, and the details rail that accepts a workflow, job *or volume*. **What changed is the centre: the 2021 table became a card grid.** So the sequence is 7.3 table → 9.x card grid, and D5 was updated to describe the 9.x card grid while its wording ("1st column", "2nd column and beyond") still describes the *table* metaphor. The doc is right about the parts; its vocabulary is one generation stale. |
| **X1b** | **"1st column / 2nd column and beyond"** (D5 §2.1) vs. the card layout | [doc D5] vs [obs C-JOBS9] | The *ordering* is preserved (workflow first, then its jobs left-to-right) but they are **cards**, not table columns. A Phase 2 implementation that builds a table would miss the point: the unit of the grid is the **workflow**, and its jobs fan out horizontally from it. |
| **X2** | **"Transcoding Preview" centre view.** D2 says the Transcoding Presets layout sets the centre view to "Transcoding Preview". C-TRANS shows a plain letterboxed player with the clip strip. | [doc D2] vs [obs C-TRANS] | Either the preview *is* the player, or the capture predates the centre mode. Unresolved. Flagged. |
| **X3** | **Green.** Two distinct greens for the same semantic: text/status green `#7CE95C` in the 2025 Files build vs a dark-green pill fill `#448932` with white text in the 2018/2021 builds. | [obs C-FILES] vs [obs C-JOBS, C-VERIF] | Two different components (inline status text vs. a count badge) rather than one token. A build-conditional palette. |
| **X4** | **Window chrome.** C-VERIF (2018) is a window with traffic lights and a centred project chooser in the title bar. C-FILES (2025) is full-screen with the project chooser inside the app's own Band 1. | [obs C-VERIF] vs [obs C-FILES] | Full-screen became the primary presentation; windowed is legacy. |
| **X5** | **Toolbar composition.** C-VERIF's right cluster is 10 items including `Config` and `Second Display`; C-FILES' right cluster is 9 items with `Miniplayer`/`Scopes` and no `Config`/`Second Display`. | [obs C-VERIF] vs [obs C-FILES] | Toolbar contents are **editable, not fixed**. The product page says "Tailor the toolbar to show only the tools you need" [doc D11]. A toolbar is a user-composed surface, not a hard-coded one. |
| **X6** | **Status bar counts.** D5 promises `Failed / Aborted / Ok` counters on the status bar. C-FILES shows no counters (no jobs in flight) but does show the 5 job-type glyphs; C-JOBS shows a single `6 ok` pill. | [doc D5] vs [obs C-FILES, C-JOBS] | The counters are **conditional on activity**, not always-present. A static recreation would get this wrong. |
| **X7** | **"Format a card".** The brief's example destructive action does not appear anywhere in the docs. D5 lists volume context-menu actions as Offload / Seal / Eject / Open in Finder / Manage Resources / Show in Offload Menu. | [doc D5] | "Format" is **[recall] only** and probably not a Silverstack operation — sealing is the destructive one (it marks a volume write-protected). The docs win. |
| **X8** | **Right sidebar role.** D2 says the right sidebar's content is chosen by layout (Files and Hashes / General Info / User Info / Look Library / presets). D1's 24-point legend never names the right sidebar as a region at all — it names its *contents* (general info, filter, tabs). | [doc D1] vs [doc D2] | The sidebar is a **slot with pluggable panels**, and D1's list is content-oriented, not chrome-oriented. |
| **X9** | **"Project Chooser is disabled in the Jobs & Volumes view."** D5 §2.4.1 says this explicitly. C-JOBS9 shows the project chooser (`7 Dagar med familjen ⌄`) **present, in the top bar, with a visible chevron** — i.e. apparently enabled. | [doc D5] vs [obs C-JOBS9] | Either the doc is stale, or "disabled" means *not clickable in this pane* while still displayed. The capture cannot distinguish a disabled control from an enabled one at this scale with confidence. **Flagged, not merged.** The safe implementation rule is: show the chooser, disable it while the Jobs view is active. |
| **X10** | **Status-count pills.** D5 §2.4.2 promises `Failed / Aborted / Ok`. C-JOBS9 shows only **`17 aborted`** and **`358 ok`** — no "failed" pill. | [doc D5] vs [obs C-JOBS9] | The counters are **conditional on the count being non-zero**, not merely on activity. This is a refinement of X6 and changes the implementation: a count pill must not reserve space when its count is zero. |
| **X11** | **Green token drift across builds (refined).** `#448932` (dark green, 2021 badge fill) → `#7CE95C` (bright green, 2025 inline text) → a mid-saturated green pill in C-JOBS9 `[est]`. | [obs C-JOBS][obs C-FILES][obs C-JOBS9] | Three different greens across three builds and three component roles. **Do not** treat "the app's green" as one token: status text, status bar pills and iconography have drifted apart over eight years. Any faithful re-implementation must pick *one* green per role and accept that it will not match the original byte-for-byte. |

---

## 1.10 Design tokens

> All values from C-FILES / C-MANAGE / C-QC / C-TRANS (3456×2160 @2×). Point values = native ÷ 2. Every value is **≈** because the capture is a scaled screenshot, not a design file.

### Colour

| Role | Value | Where measured |
|---|---|---|
| OS / app chrome base | `#313131`–`#323232` | Band 1 toolbar bg |
| Context bar bg | `#3D3D3D` | Band 2 |
| Left sidebar bg (tree) | `#424242` | x 0–741, y 1200 |
| Content / table bg | `#383838` (rows alternate imperceptibly `#383838`/`#373737`) | x 744–2592 |
| Right sidebar bg | `#4D4D4D` | x 2620–2700, y 1300 |
| Right sidebar header bar | `#333333` | x 2801–3455, y 190 |
| Right sidebar cards | `#4F4E4C` vs panel `#494949` | h-profile y 1200 |
| Status bar bg | `#3D3D3D` | y 2080–2160 |
| Segmented control — selected segment | `#767676` | y 2102–2140 |
| Segmented control — track | `#3D3D3D` + 1 px `#4D4D4D` border | |
| Table column-header text | `#7A7B7F` | h-profile y 190 |
| **Selection fill (table row)** | `#4B78BC` → `#4D7ABE` (a vertical gradient across the row) | y 547–610 |
| **Selection fill (clip chip, presets row)** | `#4D7ABE` | rendered |
| Selection outline (collection cell) | 1 px `#4D7ABE`, **no fill** | rendered |
| **Success / verified green (text)** | `#7CE95C` | right panel, 4 glyph instances |
| **Success / verified green (outline tree glyph)** | same `#7CE95C` family | bbox 13×22 |
| Success green (2018/2021 build, badge fill) | `#448932` | C-JOBS pill |
| **"Has custom look" purple** | `#A572F3` (badge fill), white star glyph | bbox 28×28 |
| Folder / node blue | `#6DA8E2` | tree icon |
| Breadcrumb node swatch | saturated blue-violet, matched to tree node | rendered |
| Red — failure / stop sign | `#FF3B30`-family | **[recall]** — not legible in a capture at this resolution; D5 names the red stop-sign icon but not its colour |
| Amber — warning / partial | `#E9CF61` / `#D5BD4F` | present in the same-pixel scan (F8_SD1 audio-bin glyph in the tree) |
| Player letterbox | `#000000` | C-QC, C-TRANS |

**Jobs view palette (C-JOBS9 — all [est], visual, ±15%)**

| Role | Value | Notes |
|---|---|---|
| Grid field bg (behind the cards) | ≈`#1E1E1E`–`#222222` | markedly darker than the cards; this is what makes the cards read as cards |
| Card fill | ≈`#383838` | both workflow cards and job cards |
| Workflow-card green state bar | ≈`#2FBF4C` | ≈5 px, full card height |
| Green check in job card | ≈`#2FBF4C` | |
| `358 ok` pill | ≈`#2E9E3E` fill, white text | ≈70×22 px, ≈6 px radius |
| `17 aborted` pill | ≈`#4A4A4A` fill, ≈`#CCCCCC` text | same geometry as the ok pill |
| Unread dot | ≈`#3B7DD8` | ≈7 px, in the grid's left gutter |
| Purple media badge (camera) | ≈`#A572F3` | **consistent with the measured `#A572F3` in C-FILES** — the only cross-capture colour match I can assert |
| Amber media badge (audio) | ≈`#E0A93B` | consistent with the amber tree glyph in C-FILES |
| Details rail bg / divider | ≈`#2E2E2E` / 1 px ≈`#1A1A1A` | |
| Filter chip — selected | ≈`#55555A` fill | |
| Filter chip — unselected | transparent + ≈1 px ≈`#4A4A4A` border | |
| Card title / meta text | ≈`#FFFFFF` / ≈`#9A9A9A` | |

### Type

| Level | Measured ink band | ≈ point size | Font |
|---|---|---|---|
| Toolbar action label | 14 native px | **≈10 pt** | SF Pro / system |
| Toolbar large timecode | — | **≈18 pt, monospaced** | tabular figures |
| Table column header | ≈15 native px | **≈11 pt** | system, `#7A7B7F` |
| Table cell | 24 native px | **≈12 pt** | system |
| Tree label | ≈32 native px band (asc+desc) | **≈12–13 pt** | system |
| General Info group header | 22 native px, bold | **≈11 pt bold** | system |
| General Info label | 16–17 native px | **≈11 pt** | system |
| General Info value | 16–17 native px | **≈11 pt** | system |
| Numeric spinner (colour wheels) | ≈12 pt, **4 decimal places**, tabular | **≈11 pt tabular** | |
| Status bar (`1 running`, `8 sec left`) | — | **≈11 pt** | |
| Wordmark (`Silverstack`) | — | **≈14 pt italic** | product wordmark |

> **Density claim:** 12 pt body in a 29 pt row is a 0.41 ratio — normal for macOS. The density comes from *row pitch*, not from small type. Type size is ordinary; the tables are just many.

### Spacing scale

| Step | Native px | Points | Where |
|---|---|---|---|
| 1 | 2 | **1 pt** | hairline dividers |
| 2 | 8 | **4 pt** | icon-to-label gap, tree icon-to-text |
| 3 | 20 | **10 pt** | toolbar label baseline padding |
| 4 | 27 | **≈13.5 pt** | tree indent per level |
| 5 | 48 | **24 pt** | collection grid gutter |
| 6 | 80 | **40 pt** | status bar height |
| 7 | 96 | **48 pt** | toolbar height |

Spacing is **not** on a single scale — it is dominated by two component-driven values (29 pt table row, 25 pt tree row) and a 4 pt sub-grid.

### Radii, borders, elevation

| Element | Value | Basis |
|---|---|---|
| Segmented control | **≈7 pt** radius | corner sample |
| Preset aspect chip | **≈3 pt** | visual |
| Purple look badge | **≈3 pt** | visual |
| Tree folder icon | **≈3 pt** | visual |
| `Activate Preview` button | **≈6.5 pt** | visual |
| Selected-preset blue row | **0 pt** (square) | rendered |
| Group card (Settings) | **≈4 pt** | visual |
| Media-type badge (Jobs) | **≈5 px** radius | [est] C-JOBS9 |
| Filter chip | **≈10 px** radius | [est] C-JOBS9 |
| Count pill | **≈6 px** radius | [est] C-JOBS9 |
| Workflow/job card | **≈6–8 px** radius | [est] C-JOBS9 |
| Dividers | **1 pt** `#3A3A3C` / `#4D4D4D` | h-profile |
| Elevation | **none.** No drop shadows anywhere. Separation is achieved by a **4-step background ramp** (`#333333` → `#3D3D3D` → `#424242`/`#383838` → `#4D4D4D`) plus 1 pt borders | verified across all 2025 captures |
| Player frame | black letterbox, no border | rendered |

**The single most transferable token fact: there is no elevation system. There is a background-value ramp and 1 px hairlines.** On macOS this is idiomatic and free; on any other stack it must be re-implemented deliberately.

**But note the Jobs view breaks the rule it inherits.** The 2025 Library view has *no* elevation and no cards at all; the 2026 Jobs view introduces cards on a near-black field with no shadow `[obs C-JOBS9]`. So the "no elevation" rule is a **Library-view** property, not an app-wide one. The Jobs view achieves separation by **inverting the ramp** (cards lighter than the field) rather than by adding shadows. Both are shadow-free; they differ in which direction the value ramp runs. An implementation brief that hard-codes "no elevation, ramp up" will produce a Jobs view that looks wrong.

### Non-token rules worth naming

| Rule | Evidence | Why it matters |
|---|---|---|
| **Duration format is adaptive-granularity** | [obs C-JOBS9] — `16 min 36 sec`, `3 min 44 sec`, `23 sec`, `8 min 8 sec` | Under 60 s it prints seconds only; above, it prints `m s`. Two units, one format function, no "0 min". |
| **Media type is encoded by badge colour, app-wide** | [obs C-FILES] tree: purple ✦ for camera bins, amber ≡ for audio bins (`F8_SD1`); [obs C-JOBS9] cards: purple ✦ for `DJI_C009`/`A_0058_1E2W_hde`, amber ≡ for `788T_059` | The same purple and the same amber mean the same thing in the tree and in the jobs grid. Purple = camera media, amber = sound media. Consistent across two radically different screens and three build generations. |
| **Counts use free-form unitless numerals** | [obs C-JOBS9] `358 ok`, `17 aborted` | Counts are integers with no thousands separator; the unit is in the label, not the number. |
| **Timestamps are `YYYY-MM-DD, HH:MM`** | [obs C-JOBS9] `2026-11-13, 23:37` | ISO-like date, 24-hour time, comma separator, no seconds. |

---

## 1.11 Component inventory

| # | Component | Observed states | Assumed states (inferred, not observed) |
|---|---|---|---|
| 1 | Clip table row | default; **selected** (blue gradient fill, white text); **hover** (implied by the grey selected-row variants seen in C-JOBS) | unverified, in-progress, failed, read-only |
| 2 | Table column header | plain text `#7A7B7F`; **sorted** (C-MANAGE shows an ascending chevron on `Clip Name`); **resizable** (D1/D5 imply it, not observable) | grouped, pinned, filter-badge |
| 3 | Tree node | folder (blue), bin (purple star badge), audio bin (amber glyph), smart folder (gear-in-square), volume, trash; expanded `▾` / collapsed `▸`; selected (full-width blue fill) | drag-in-progress, rename-editing, drop-target |
| 4 | Verification glyph | green `#` (verified); grey `#` (unverified) [obs C-VERIF]; red variant [doc D5, not observed] | in-progress (spinner), partially verified |
| 5 | General Info row | read-only value; **editable value with a pencil button** | focused/editing, committing, validation error |
| 6 | General Info group | expanded `▾` with rows; collapsed `▸` (C-MANAGE: Edit/User, Custom, Camera Settings, Lens, Look, Processing, Production, Format) | all-collapsed, all-expanded |
| 7 | Colour wheel | neutral (black ring with hue ring); the "O/H" toggle per wheel; a reset knob + a curved-arrow reset button | active drag, offset linked, clamped |
| 8 | Colour-wheel numeric field | static readout; **stepper** (up/down chevrons on the right) | focused, invalid, scrub-drag |
| 9 | Preset row | default; **selected** (blue fill, white title, desaturated blue spec text) | hovered, "modified" (dirty) |
| 10 | Settings group card | expanded with controls; **collapsed to a 1-line header** (`Framelines`, `Resizing`, `Grading`) | disabled (locked), mixed-state checkbox |
| 11 | Clip chip (filmstrip) | default (dark fill + 1 px border + middle-ellipsis label); **selected** (solid blue fill, white text) | hover, flagged, failed-transcode |
| 12 | Job-type glyph (status bar) | dimmed/idle; **lit** (the job type is running) | warning (job stalled) |
| 13 | Status-count pill | absent (no activity); green `6 ok` / `7 ok` pill | red failure count, amber aborted count [doc D5] |
| 14 | Transport button (⌨ in C-OVW) | default | pressed |
| 15 | Grid/wipe toggle | single / grid / split, 3 states [doc D7; C-OVW callout #9] | — |
| 16 | Segmented `Library｜Jobs` | Library selected; Jobs selected | — |
| 17 | Segmented `Video｜Still` (presets) | Video selected | Still selected [not observed] |
| 18 | `Offload` action | enabled | disabled when no volume mounted [not observed] |
| 19 | `Seal` action | visible in C-VERIF | — |
| 20 | Filter pill row (jobs) | unselected / selected | disabled, count badge |
| 21 | **Workflow card** (Jobs) | default; **green state bar** on the left edge; unread **blue dot** in the gutter outside the card; media badge purple (camera) or amber (audio) | running (amber/blue bar), failed (red bar), suspended (grey bar), selected |
| 22 | **Job card** (Jobs) | default with title + source string; **green check** state glyph | running (blue bar), failed (red stop sign), suspended (grey clock), cancelled (grey cross) — all named in D5 §1.2 but **none observed in C-JOBS9** |
| 23 | **Filter chip group** (Jobs) | unselected (outline) / selected (filled) | multi-select, disabled, count badge |
| 24 | **Zoom cluster** (Jobs) | 3–4 magnifier glyphs: zoom out / zoom in / 1:1 / zoom to fit | disabled at min/max zoom |
| 25 | **Details-rail empty state** | "Select a workflow, job, or volume to show details." | populated states: workflow / job / volume — **none observed** |
| 26 | **Status count pill** (Jobs) | green `ok`; neutral `aborted` | red `failed` (predicted by D5, **not observed**) |
| 27 | **Section heading** (Jobs grid) | plain secondary text ("Workflow History") | collapsed/expanded state |
| 28 | **Read/unread dot** (Jobs) | blue dot present | absent = read; hover = "mark as read" affordance (not observed) |

---

## 1.12 Density & ergonomics audit

### Strengths

**S1. The tree carries count + status + identity without a second panel.**
Every tree row holds a container glyph, a right-aligned version count, and a status glyph — three data types in a 25 pt row with no extra chrome `[obs C-FILES]`. A DIT can answer "how much is in this bin and is it backed up" from a 25 pt band. `[obs C-FILES]` / `[doc D4]` confirms the count is a *version* count with duplicates excluded, which is a non-obvious semantic surfaced by a single number.

**S2. Verification state is legible at three scales simultaneously.**
The same fact (this copy is checksum-verified) appears as a green glyph in the tree at 25 pt rows `[obs C-FILES]`, as a dedicated table column with its own header `[obs C-VERIF]`, and as a sentence in the right rail (`All Resources Verified`, `Verification incomplete: 1 unverified file resource(s)`) `[obs C-FILES][obs C-VERIF]`. The operator never has to leave the current view to learn whether data is safe. `[doc D6]` establishes that checksum verification is the product's primary promise.

**S3. The right rail is a document, not a form.**
The General Info panel renders as a 2-column key/value document with collapsible groups and alternating row bands at a 20 pt pitch `[obs C-MANAGE][obs C-INFP]`. It scales to "over 100 metadata fields per clip" `[doc D11]` because the *structure* (group → row → value) is uniform and only the fields change. The pencil affordance on editable rows only `[obs C-INFP]` is the whole editability model in one glyph.

**S4. Two-level job progress is visible simultaneously.**
The status bar gives an aggregate ("1 running … 8 sec left") while the grid gives per-job FPS/ETA/state `[obs C-JOBS][doc D5]`. A single progress bar would have failed: the docs are explicit that one workflow can fan into one backup plus three verify jobs `[doc D5]`, and that "Has Failed Tasks (but running)" is a state distinct from Failed `[doc D5]`.

**S5. The workflow/job hierarchy is preserved as a spatial relationship, not a nesting.**
In the current Jobs view the unit of the grid is the **workflow**, and its jobs fan out to the right as sibling cards `[obs C-JOBS9]`. A workflow with three verify jobs shows four cards in a row: one workflow card, three job cards. This keeps "which job belongs to which offload" answerable by looking along a row, while still letting each job carry its own state glyph, source volume and duration. The alternative — a table with a `Parent Workflow` column `[doc D5 §2.2.2]` — would make the same fact require a column scan.

**S6. The filter vocabulary is the domain's own vocabulary.**
`Stage: Scheduled / Running / History` · `Finish: All / Successful / Failed / Aborted` · `Read: All / Unread` · `Date: All / Today / Yesterday / This Week / Last Week` `[obs C-JOBS9]`. Each chip is a state the operator already thinks in, and each of the four groups is labelled — so the strip is self-documenting with no help text. This matches D5's filter list exactly `[doc D5 §2.1.1]`, which is unusually good doc-to-UI fidelity and the clearest evidence that the 2025 documentation describes the current build.

**S7. Timecode is the largest text in the app.**
`08:38:20:12` occupies a monospaced readout in Band 2 centre, bigger than the toolbar labels `[obs C-QC]`. The value that must not be misread during a jittery on-set QC session is given the most typographic weight on screen.

**S8. State is encoded redundantly, at three distances.**
A completed job carries a green vertical bar on the workflow card's left edge, a large green check centred in the job card, a green `358 ok` pill in the status bar, and a green check next to the card `[obs C-JOBS9]`. One operator can read state from 3 m away (the bar), at arm's length (the check) or from a chair (the pill). Redundant encoding is cheap here and it is what makes a dense operational grid trustworthy.

### Weaknesses

**W1. Two incompatible truncation idioms for the same kind of value.**
Filenames in the table and collection view truncate with a **tail** ellipsis (`A_0001C005_240426_083229…`) `[obs C-FILES][obs C-MANAGE]`, but filenames in the filmstrip clip chips truncate with a **middle** ellipsis (`A_0001C006_240426_0…`) `[obs C-QC]`. The tail ellipsis is worse: it hides the part of the filename that distinguishes one take from another. A DIT comparing `A_0001C006_240426_0…` and `A_0001C007_240426_0…` cannot tell them apart. This is a bug-level inconsistency, not a style choice.

**W2. The destructive and the ordinary are 6 px apart.**
`Offload`, `Seal`, `Export`, `Import`, `Report`, `Transcode` are peers in one flat row of identical icon+label chips `[obs C-FILES][obs C-VERIF]`. `Seal` makes a volume write-protected and `Eject`/`Seal` are the operations with real consequences `[doc D5][doc D6]`. Nothing in the toolbar expresses "this one is different". There is no grouping, no separator, no icon-weight difference — the visual cost of a wrong click is zero.

**W3. The right rail truncates the values that matter most.**
In General Info, `Name` renders as `A_0001C005_240426_083229_p1D…` `[obs C-MANAGE]` and in the older panel `A003C012_160205…` `[obs C-INFP]`. The unique clip identifier — the thing that must be quoted into a report, an EDL, an NLE metadata export `[doc D9][doc D10]` — is the thing that gets cut. The value column is 268 pt while the key column consumes 146 pt; for a panel whose most-used fields are long identifiers, the split is backwards.

**W4. The clip table is ~3.4× wider than its viewport with no column manager.**
The horizontal scroll thumb is ≈30% of the track `[obs C-FILES]`, so ~70% of columns are off-screen. Columns run Preview · Name · ShotID · Duration · Frames · Camera · EI/ISO · WB · Shutter · Shutter Angle · Sensor… and then more `[obs C-FILES]`. There is no visible column-visibility control, no pinned column, no frozen name column — the Name column scrolls out of view horizontally. D1 calls out "General info filter" as the only filtering surface `[doc D1 #16]`; a *column* filter is not mentioned anywhere.

**W5. The count and the ratio are unreadable at 12 pt.**
Tree counts sit at 12 pt and are right-aligned in a 25 pt row with no unit, no thousands separator, and no column header `[obs C-FILES]`. `Library 418` and a bin's `12` are different kinds of number (all versions vs. deduped versions) `[doc D4]` with nothing on screen to say so.

**W6. The Jobs grid reserves a horizontal slot it never uses.**
Each workflow occupies a row of cards that extends left-to-right, but with one job per workflow only two cards are drawn — so the region from ≈x 632 to ≈x 1500 (≈43% of the window width) is **permanently empty field** `[obs C-JOBS9]`. The layout is correct for a workflow with five jobs and wasteful for one with one. A masonry/column layout, or a card group that is left-anchored *and* wraps, would recover that space. As built, the density of the screen is set by the **worst case** job count rather than the current one.

**W7. The empty state is the only thing that says what the rail can contain.**
"Select a workflow, job, or volume to show details." `[obs C-JOBS9]` is the entire guidance, and it is doing three jobs at once — naming the rail's purpose, its three input types, and the action required. It works, but it is a single sentence carrying all of it, and it names "volume" — an entity with **no other affordance visible in this capture** (the Volumes sidebar is collapsed). A user who has never expanded the Volumes panel meets the word "volume" for the first time inside an empty-state sentence.

**W8. The two green pills sit next to each other with different semantics.**
`17 aborted` and `358 ok` are adjacent pills of similar size, one neutral grey and one green `[obs C-JOBS9]`. `aborted` is a *user-initiated* event and `ok` is a *success*; they are not the same severity class, yet the layout presents them as peers. If a third pill for `failed` appears (which D5 says it does `[doc D5]`), the bar will contain two different severity scales with no visual separation between the serious and the benign.

---

# PHASE 2 — DISTIL INTO A REUSABLE EXAMPLE

## 2.1 Reusable patterns

Each rule is written so an AI coding assistant can apply it to an unrelated app.

> The brief asked for 6–8 rules. The teardown yielded **10** from the Library view alone; the current Jobs view capture (C-JOBS9) added three more (**P11**, **P12**, **P14**) and **corrected P8**, which had been written against the obsolete 2021 table layout. The count is 14 rather than 8 because each rule is independently actionable, and trimming to 8 would have required merging rules that apply to different situations.

| # | Name | When to use | Rule | Anti-pattern prevented |
|---|---|---|---|---|
| **P1** | **Dense data tables: fixed row height, one truncation rule** | Any list of 100+ records in a table | Fix the row height at 24–30 pt and derive nothing from content. Truncate **every** long string with the *same* middle-ellipsis strategy so identifiers stay distinguishable (`…240426_083229…`), and reserve tail-ellipsis for values where the end is meaningful. Never let row height vary with content or with an embedded thumbnail column. | Variable-height rows driven by thumbnails; three different ellipsis strategies in one app; a column that silently reflows when a long value appears. |
| **P2** | **Status glyph at three scales, one colour token** | Any system where "is this safe / done / broken" matters more than the values | Define a single semantic colour set (`verified`, `pending`, `failed`, `unknown`) and render the *same* glyph in the dense list, in a dedicated column, and in the detail panel. Add a sentence form for the aggregate ("all 12 resources verified") next to the glyph form. | Colour-only status (colour-blind failure); status that exists in the list but not in the detail view; a separate palette per screen. |
| **P3** | **Background ramp instead of elevation** | Dense pro-app UI, especially macOS | Separate regions with a **4-step value ramp** (chrome → context bar → panel → content) plus 1 px hairlines, and use **no drop shadows at all**. Reserve elevation for true overlays (menus, popovers, sheets) only. | Shadow soup; region boundaries that disappear in dark mode; the "everything is a card" failure mode. |
| **P4** | **Slot-based sidebars, content-based layouts** | Apps with more than one task mode (browse / inspect / grade / monitor) | Build the window as fixed **slots** (left rail, centre, right rail, bottom dock) and let a *mode* decide what each slot contains. Expose the modes as named buttons in the top-right of the toolbar so the operator can see all modes at once. | A separate screen per task, each with its own chrome; a right panel whose content changes with no visual cue about why. |
| **P5** | **Read-only document rail with per-row edit affordance** | Any metadata inspector | Render metadata as a 2-column key/value **document**: label left, value right, collapsible groups, alternating 1–2 pt row bands, ~20 pt pitch. Put a single small affordance (pencil / chevron) **only on rows that are actually editable**. Make the value column the wider one, and give it room to show the full identifier. | A modal edit form; a uniform "Edit" button that opens one generic dialog; a value column too narrow for the identifier the workflow requires. |
| **P6** | **Two-level progress for parallel work** | Any long-running, resumable, multi-part background job | Always show **two** progress surfaces at once: an aggregate bar for the whole session (with a count of running items and a time remaining) *and* a per-item row with its own state, throughput and error list. Give partial failure its own state ("running, some tasks failed") that is visually distinct from "failed" and from "complete". Never hide the aggregate behind a click. | A single indeterminate spinner; a failure that only reveals itself at 100%; a red bar that conflates "one file of 900 failed" with "the job died". |
| **P7** | **Destructive verbs get a different shape** | Any toolbar containing both ordinary and irreversible actions | Separate irreversible actions from ordinary ones: a hairline separator, a distinct fill (never the same ghost button), and a confirmation that names the specific object ("Seal volume G-SPEED Shuttle TB3?"). Make the irreversible set a visible group, not a flat row. | Six identical icon buttons where one of them can make a physical drive write-protected; a confirm dialog that says "Are you sure?". |
| **P8** | **Filter strip pinned above the work list, details rail beside it** | Any log/history/work-queue screen | Put a **pinned filter strip directly above** the scrolling list (never inside it, never at the bottom), and a **details rail to the right that never scrolls**. Label every filter group (`Stage:`, `Finish:`, `Read:`, `Date:`) and use only states the operator already uses in conversation. Give the rail an empty state that names both its purpose and every input type it accepts. | Filters that scroll out of reach in a long history; an unlabelled row of chips the user has to guess; a details panel that scrolls its own content out of view. |
| **P9** | **Context bar over the content, not in it** | Apps with a deep hierarchy | Put a context bar *above* the content region carrying: (a) the breadcrumb path, (b) a scope selector, (c) a scoped search field, (d) the mode toggle. Keep it visually distinct from the toolbar (one value step apart) so the operator always knows whether a control is global or contextual. | Breadcrumbs buried above a table's column header; one global search box used for two different scopes; a mode switch disguised as a dropdown. |
| **P10** | **Bucketed row summary on collection tiles** | Any grid of media/records with mixed flags | On a tile, put identity + the one distinguishing value (duration) on line 1, and bucket the metadata into discrete chips on line 2 (date, audio-source, resource-count) instead of a prose list. | Prose captions that wrap to two lines and break the grid; badges with no legend; a tile that is 3 lines tall in one state and 5 in another. |
| **P11** | **Parent card + child cards in one row** | Any system where one operation spawns several sub-operations | Make the grid unit the **parent**, not the child. Render the parent as a card, then render its children as **sibling cards to its right in the same row**, so "which sub-operation belongs to which parent" is answered by looking along a row. Give the parent card a full-height coloured edge bar carrying the aggregate state; give each child card its own centred state glyph. | A flat table where the parent-child link is a column you must scan; nesting cards inside cards; a child list that collapses to a "+3" affordance and hides the failures inside it. |
| **P12** | **Type colour is a global vocabulary, not a local decoration** | Any app with more than one *kind* of thing (camera vs. audio, invoice vs. credit note, prod vs. staging) | Assign one colour + one glyph to each entity *type* and reuse that pair **everywhere the type appears** — tree rows, list rows, detail headers, cards. Never let a type's colour differ between two screens, and never introduce a second colour for a type that already has one. | Purple meaning "camera" in the tree and blue meaning "camera" in the list; a colour legend that must be re-learned on every screen. |
| **P13** | **Adaptive duration formatting** | Any screen showing elapsed or media durations | One formatter with **adaptive granularity**: below 60 s print `23 sec`; above print `16 min 36 sec`. Never print `0 min 23 sec`, never print `1 h 0 min`. Same function everywhere a duration appears, so a duration in a card and a duration in a detail panel are always the same shape. | `00:23` in one place and `0 min 23 sec` in another; a duration that wraps to two lines in a fixed-height card; showing hours for a 4-minute transcode. |
| **P14** | **Redundant state encoding at three viewing distances** | Any operational grid that must be readable at a glance *and* precisely | Encode the same state **three times** at three scales: a full-height coloured edge bar on the card (readable across a room), a centred state glyph (readable at arm's length), and a colour-coded count pill in a persistent status bar (readable from a chair). All three must come from one state enum, never from independent booleans. | A grid where success is a green tick that a colour-blind operator cannot see; status that exists only in a panel they have not opened; three places that can disagree about whether a job succeeded. |

---

## 2.2 Implementation brief — SwiftUI / macOS-native

### Token block (paste-ready)

```swift
// MARK: - Design tokens
// Source: Silverstack Lab teardown, 2025 build (Silverstack 9.x).
// Measured on a 3456x2160 @2x capture == 1728x1080 pt. All point values are estimates.

enum SST {
    // MARK: Colour — dark scheme only (observed). Light scheme is [doc, not shown].
    enum Palette {
        static let chrome        = Color(hex: 0x313131)  // Band 1 toolbar
        static let contextBar    = Color(hex: 0x3D3D3D)  // Band 2
        static let panel         = Color(hex: 0x424242)  // left rail
        static let content       = Color(hex: 0x383838)  // centre
        static let rail          = Color(hex: 0x4D4D4D)  // right rail
        static let railHeader    = Color(hex: 0x333333)
        static let statusBar     = Color(hex: 0x3D3D3D)
        static let hairline      = Color(hex: 0x3A3A3C)
        static let hairlineStrong= Color(hex: 0x4D4D4D)

        static let selectionTop  = Color(hex: 0x4B78BC)
        static let selectionBot  = Color(hex: 0x4D7ABE)
        static let labelSecondary= Color(hex: 0x7A7B7F)

        // Semantic status — ONE token set used at every scale (P2)
        static let verified      = Color(hex: 0x7CE95C)  // green
        static let pending       = Color(hex: 0xE9CF61)  // amber
        static let failed        = Color(hex: 0xFF3B30)  // [recall] — not legible in capture
        static let unknown       = Color(hex: 0x8A8A8E)
        static let hasCustomLook = Color(hex: 0xA572F3)  // purple
        static let nodeFolder    = Color(hex: 0x6DA8E2)
    }

    // MARK: Metrics — points
    enum Metric {
        static let toolbarHeight: CGFloat   = 48
        static let contextBarHeight: CGFloat = 30
        static let statusBarHeight: CGFloat = 40

        static let tableRowHeight: CGFloat  = 29   // MEASURED, pitch 58 @2x
        static let treeRowHeight: CGFloat   = 25   // MEASURED, pitch 50 @2x
        static let metaRowHeight: CGFloat   = 20   // MEASURED, pitch 40 @2x
        static let formRowHeight: CGFloat   = 22   // MEASURED, pitch 44 @2x
        static let clipStripHeight: CGFloat = 20   // MEASURED

        static let iconSmall: CGFloat  = 10
        static let iconMedium: CGFloat = 14
        static let iconLarge: CGFloat  = 18   // toolbar action glyphs
        static let iconHuge: CGFloat   = 65   // colour wheel outer diameter

        static let indentStep: CGFloat  = 13.5
        static let gridGutter: CGFloat = 24
        static let tileWidth: CGFloat  = 220

        static let cornerSmall: CGFloat  = 3
        static let cornerMedium: CGFloat = 4
        static let cornerControl: CGFloat = 7
    }

    // MARK: Jobs view (C-JOBS9, current 9.x build)
    // NOTE: every value here is a VISUAL ESTIMATE (that capture was not on disk),
    // so treat them as +/-30% and re-derive from a live build before shipping.
    enum Jobs {
        enum Palette {
            static let field        = Color(hex: 0x1E1E1E)  // behind the cards
            static let card         = Color(hex: 0x383838)
            static let rail         = Color(hex: 0x2E2E2E)
            static let railDivider  = Color(hex: 0x1A1A1A)
            static let stateGreen   = Color(hex: 0x2FBF4C)  // edge bar + check
            static let okPill       = Color(hex: 0x2E9E3E)
            static let neutralPill  = Color(hex: 0x4A4A4A)
            static let unreadDot    = Color(hex: 0x3B7DD8)
            static let mediaCamera  = Color(hex: 0xA572F3)  // == measured in the tree
            static let mediaAudio   = Color(hex: 0xE0A93B)
        }
        enum Metric {
            static let cardWidth: CGFloat     = 284
            static let cardHeight: CGFloat    = 100
            static let cardGap: CGFloat       = 16
            static let cardPitch: CGFloat     = 116   // height + gap
            static let stateBarWidth: CGFloat = 5
            static let badgeSize: CGFloat     = 22
            static let railWidth: CGFloat     = 488
            static let filterChipHeight: CGFloat = 20
            static let pillHeight: CGFloat     = 22
        }
    }

    // MARK: Type
    enum Type_ {
        static let toolbarLabel = Font.system(size: 10)
        static let tableHeader  = Font.system(size: 11)
        static let tableCell    = Font.system(size: 12)
        static let treeLabel    = Font.system(size: 12)
        static let metaLabel    = Font.system(size: 11)
        static let metaValue    = Font.system(size: 11)
        static let groupHeader  = Font.system(size: 11, weight: .semibold)
        static let timecode     = Font.system(size: 18, design: .monospaced)
        static let numeric      = Font.system(size: 11).monospacedDigit()
    }
}

// MARK: - Spacing scale (observed: 1 / 4 / 10 / 13.5 / 24 / 40 / 48 pt)
enum Space { static let hair = 1; static let xs = 4; static let s = 10
             static let indent = 13.5; static let l = 24; static let xl = 40; static let xxl = 48 }
```

### Component tree

```
SilverstackWindow  (HSplitView-free; manual HSplitView for left/centre/right)
├── TopBand
│   ├── ActionToolbar                                // 7 action chips, left
│   │   ├── ToolbarActionButton  (icon 18pt + 10pt label)
│   │   └── DestructiveToolbarActionButton           // "Seal" — distinct fill  (P7)
│   ├── ProjectChooserButton  (centre)
│   └── ModeSwitcher  (right: Files / Manage / QC / Color / Presets)   (P4)
├── ContextBar
│   ├── SidebarToolStrip
│   ├── ViewModeSegmentedControl  (list/table/grid/preview)
│   ├── BreadcrumbTrail             (colour-swatch nodes)
│   └── ScopedSearchField           ("Search in 'All Fi…'")
├── HSplitView
│   ├── LeftRail
│   │   ├── InfoDisplayStrip        (read-only, 4 lines)
│   │   └── OutlineTree             (25pt rows, indent 13.5pt)
│   │       └── OutlineRow
│   │           ├── NodeGlyph  (folder / purple-star / amber-audio / gear)
│   │           ├── VersionCountLabel  (right-aligned)
│   │           └── VerificationGlyph (13x22pt, #7CE95C)         (P2)
│   ├── CentreContent   (swaps by mode)                            (P4)
│   │   ├── ClipTableView            (29pt rows, virtualised List)
│   │   │   ├── TableHeaderRow       (11pt #7A7B7F, sortable)
│   │   │   └── ClipRow
│   │   │       ├── ThumbnailCell
│   │   │       ├── TruncatingTextField (.truncationMode(.middle))  (P1)
│   │   │       └── RowActionsGutter  (hover-revealed, fixed width)  (P1)
│   │   ├── CollectionGrid           (220x125pt tiles, 24pt gutter)   (P10)
│   │   │   └── CollectionTile
│   │   │       ├── ThumbnailImage  (1pt blue outline when selected)
│   │   │       └── TileCaption      (line1: name + duration)
│   │   │                            (line2: date | audio chip | resource pill)
│   │   └── PlayerView
│   │       ├── VideoSurface (pillarboxed, .black)
│   │       ├── ScrubBar (10pt, 2pt red playhead)
│   │       ├── TransportPill  (floating overlay)
│   │       └── ClipStrip (20pt chips, middle-ellipsis)             (P1)
│   ├── BottomDock  (Audio & Color)
│   │   ├── GradingRail (CDL / LOG / SPL / PRT vertical tabs)
│   │   ├── ColorWheelPair  (65pt wheels, O/H toggle, reset)          (P6 in the UI sense)
│   │   ├── NumericStepper (4dp, monospacedDigit)
│   │   └── CurveEditor
│   └── RightRail
│       ├── GeneralInfoPanel
│       │   ├── GroupHeader (disclosure)
│       │   ├── MetadataRow (label left / value right / pencil if editable)  (P5)
│       │   └── PinnedFilterField  (bottom-pinned, NOT scrolling with content)
│       ├── UserInfoPanel  (Camera/Scene/Shot/Take, rating, label, cue points)
│       ├── FilesAndHashesPanel (file block + per-volume cards)
│       ├── LookLibraryPanel
│       └── TranscodePresetPanel
│           ├── PresetList  (selected = blue fill)
│           └── SettingsForm (collapsible group cards, 4pt radius)
└── StatusBar
    ├── LibraryJobsSegmentedControl  (117x22pt, 7pt radius)
    ├── JobTypeGlyphStrip  (5 glyphs, dimmed when idle)              (P6)
    └── StatusCountPill  (conditional on a NON-ZERO count)          (P6, X10)
```

### Jobs view (C-JOBS9) — its own top-level layout

```
JobsView
├── JobsToolbar
│   ├── SuspendAllButton / ResumeAllButton
│   ├── ProjectChooserButton          (present; D5 says disabled — see X9)
│   ├── ModeButtons  [Workflows][Tasks][Chart]
│   ├── ScopedSearchField  (placeholder: "Search for workflows and tasks")
│   └── PanelToggles  [Volumes][Details]
├── FilterStrip  (PINNED — never scrolls)                            (P8)
│   ├── FilterChipGroup "Stage:"  [Scheduled][Running][History]
│   ├── FilterChipGroup "Finish:" [All][Successful][Failed][Aborted]
│   ├── FilterChipGroup "Read:"   [All][Unread]
│   ├── FilterChipGroup "Date:"   [All][Today][Yesterday][This Week][Last Week]
│   └── ZoomCluster  [zoomOut][zoomIn][1:1][zoomToFit]
├── HSplitView
│   ├── JobCardGrid  (left-anchored; scrolls)                       (P11)
│   │   └── WorkflowRow
│   │       ├── WorkflowCard
│   │       │   ├── StateEdgeBar          (5pt, full height)        (P14)
│   │       │   ├── MediaTypeBadge        (purple=cam / amber=audio) (P12)
│   │       │   ├── WorkflowName / WorkflowKindLabel
│   │       │   └── TimestampAndDuration  (adaptive format)         (P13)
│   │       ├── JobCard x N               (siblings to the right)   (P11)
│   │       │   ├── JobTitle
│   │       │   ├── StateGlyph            (green check / red stop / grey clock)
│   │       │   └── SourceVolumeLabel
│   │       └── UnreadDot  (in the grid's left gutter, outside the card)
│   └── DetailsRail  (right, never scrolls)                         (P8)
│       └── EmptyState  ("Select a workflow, job, or volume to show details.")
```

### The three hardest components, and why

**1. `ClipTableView` — virtualised, horizontally-scrollable, 30+ columns, 29 pt rows.**
This is the hardest because SwiftUI's `Table` fights three of Silverstack's requirements at once: (a) the table is ~3.4× wider than the viewport and must scroll horizontally with the header locked to it; (b) the Name column must stay readable while the table scrolls sideways, which means a **pinned leading column**; (c) row actions must not change column widths. **Solution:** do *not* use `Table`. Use a `ScrollView([.horizontal, .vertical])` wrapping a `LazyVStack` of `HStack`s with fixed-width columns and a synchronised header `HStack` that shares the same horizontal offset. Pin Name by rendering it in a separate overlay column translated by `-scrollOffset`. Truncate with `.truncationMode(.middle)` and a fixed `.frame(width:)` per column. Row actions live in a fixed-width right gutter that is always present but only opaque on hover — **the gutter's width is constant, so no column ever shifts** (this is P1's anti-pattern prevention, made concrete).
*Why hardest:* it is the only component where a wrong decision is visible at 10,000 rows, and the only one where the failure mode (janky virtualisation with pinned columns) is a platform problem, not a design problem.

**2. `JobMonitor` — a card grid with a parent/child row model, a pinned filter strip, and a state machine with a "partial failure" state.**
Hard because it encodes the product's most important promise. One workflow fans out into a backup plus several verify jobs `[doc D5]`, each job into per-file tasks, and the overall progress is an **unweighted average** of workflow progresses `[doc D5]`. So you need: (a) a grid whose unit is the **workflow**, with its jobs rendered as **sibling cards to the right in the same row** — not a table with a `Parent Workflow` column, and not nested cards; (b) a **filter strip pinned above** the scrolling grid, never inside it, with the four labelled groups Stage / Finish / Read / Date; (c) a details rail on the right that never scrolls and whose content is a function of the selection type (workflow / job / volume) with an empty state that names all three; (d) an explicit enum that separates `.runningWithFailedTasks` from `.failed` from `.cancelled` `[doc D5 §1.2]`; and (e) status counters that are **omitted entirely when their count is zero** `[obs C-JOBS9]` — `17 aborted` and `358 ok` are shown, `failed` is not, because there were no failures.
*Why hardest:* the state machine has a state that most designs collapse — "running but some files failed" — and collapsing it destroys the operator's trust in the whole job list. The card model is the second trap: it is easy to build the hierarchy as nesting, which destroys the row-wise readability that makes the current layout work.

**3. `MetadataDocumentPanel` — a document, not a form, that must scale to 100+ fields per clip.**
Hard because D3 requires a read-only "raw format" Header tab alongside editable fields, a "take over into custom fields" mechanism `[doc D3]`, and D11 claims over 100 fields per clip. The panel must therefore be **generic over a field schema** (key, value, editable?, raw?), not a set of hard-coded SwiftUI views, and it must render groups, collapsible sections, alternating bands, per-row pencil affordances, and a pinned filter field — all while scrolling 100 rows at a 20 pt pitch without dropping frames.
*Why hardest:* it is the component most likely to be implemented as a generic `List` with `ForEach`, which is exactly how you lose the pencil-per-row model and the pinned filter.

### Ordered build sequence

| Step | Build | Why here | Done when |
|---|---|---|---|
| 1 | Token file (`SST`) + colour ramp + a `HexColor` helper | Everything downstream is a token reference; retrofitting tokens after 20 components is expensive | A SwiftUI preview renders a 4-step background ramp with no shadows |
| 2 | `TopBand` + `ContextBar` + `StatusBar` (chrome only, fake content) | The chrome is identical in every screen; it is also the part with the most measured numbers | Band heights are 48 / 30 / 40 pt and the segmented control is 117×22 pt with a 7 pt radius |
| 3 | `LeftRail`: `InfoDisplayStrip` + `OutlineTree` | The tree is the only hierarchical component and teaches the 25 pt row rhythm and indent step | A tree with 400 nodes scrolls smoothly; counts right-align; the purple-star and green-hash glyphs render at 14 pt and 13×22 pt |
| 4 | `ClipTableView` (the 29 pt row, pinned Name column, middle-ellipsis, hover gutter) | Highest risk in the build; doing it early surfaces the virtualisation problem before other components depend on it | 10,000 rows scroll at 60 fps; the header tracks horizontal scroll; no column width changes on hover or on long values |
| 5 | `RightRail` skeleton + `GeneralInfoPanel` + the pinned filter field | Right rail is present in every mode; the pinned filter is the detail most likely to be got wrong | 100 fields render in groups; only editable rows show a pencil; the filter field stays pinned while the content scrolls |
| 6 | `VerificationGlyph` + the status colour set (P2) applied to tree, table column and detail panel | This is the product's core promise; it must be one token set used in three places | The same green renders identically in the tree, in a table column and in the detail sentence |
| 7 | `CollectionGrid` + `TileCaption` (P10) | Independent of the table; shares only the theme | Tiles are 220×125 pt, 3 across at 1728 pt, captions are always 2 lines, names middle-truncate |
| 8 | `PlayerView`: surface, scrub bar, transport pill, clip strip | The transport pill is the one component only seen in C-OVW; build it from the capture, not from memory | Scrub bar is 10 pt with a 2 pt red playhead; clip chips are 20 pt; selected chip is solid blue |
| 9 | `BottomDock` (Audio & Color): rail, wheels, steppers, curves | Biggest single widget surface; isolated so it can't destabilise the window layout | A wheel drag updates the matching numeric field to 4 dp and the curve preview |
| 10 | `JobMonitor` (card grid, parent→child rows, pinned filter strip, details rail, state enum) | Second-highest risk; needs the chrome from step 2 and the status glyphs from step 6. **Note: this is a card grid, not the two-pane table layout that a 2021 build of the same product used** | A "running with failed tasks" job is visually distinct from "failed" and from "complete"; the filter strip never scrolls; a workflow's jobs appear as sibling cards to its right, not nested under it; a zero count renders no pill at all |
| 11 | `ModeSwitcher` wiring (P4) | Last, because it only reconfigures slots that already exist | Clicking `QC` disables the left rail and docks the Audio & Color panel; clicking `Presets` swaps the right rail to the preset panel — with no other component changing |
| 12 | Destructive-action treatment (P7) + confirmations that name the object | Small, but it is the highest-consequence change | `Seal` is visually separated from `Export`/`Report`; the confirmation names the volume |

---

## 2.3 Confidence & gaps

| Claim | Basis | Why uncertain | How to verify |
|---|---|---|---|
| Table row height is 29 pt | [obs C-FILES] | Measured from ink bands, which give *text* extents; the true row box could be 28 or 30 pt if padding is asymmetric | Inspect a live build's `NSTableView.rowHeight`; or measure a screenshot where a full row border is visible |
| Tree row height is 25 pt | [obs C-FILES] | Same method; 50 native px pitch is solid across 15 bands | Same |
| General Info row height is 20 pt | [obs C-MANAGE] | 12 bands, median 40 native px — high confidence | Same |
| Point values assume DPR 2 | [obs C-FILES] | 3456×2160 could be a 1× capture of a 3456×2160 display, or 2× of 1728×1080. If DPR were 1, every point value halves | Open the capture's EXIF / check a native-resolution UI element with a known size (the macOS traffic lights in C-VERIF are 12 pt → would be 24 px at 2×) |
| Selection fill is a vertical gradient `#4B78BC`→`#4D7ABE` | [obs C-FILES] | 5 near-identical sampled values across a 30 px band could also be JPEG banding on a flat fill | Inspect a raw PNG capture, or read the AppKit `NSColor` in the app |
| Failure red is `#FF3B30` | **[recall]** | Not legible at the resolutions available; D5 names a red stop sign but not its colour | Sample the icon in the Jobs view of a live build |
| The Jobs view today has a volumes sidebar and three workflow sections | [doc D5] + **[obs C-JOBS9]** | **Now largely closed.** C-JOBS9 confirms the top-bar toggles, the Stage/Finish/Read/Date filter groups, the three stages, the read/unread dot, the Failed/Aborted/Ok counters and the details rail's three input types. The **left volumes sidebar and the volume details sections are still [doc, not shown]** — the `Volumes` toggle exists but is collapsed | Capture the Jobs view with the Volumes panel expanded and a volume selected |
| C-JOBS9 geometry (card 284×100 pt, pitch 116 pt, rail 488 pt, badge 22 pt) | [obs C-JOBS9] **[est]** | The file was **not on disk**, so no pixel sampling was possible. Values are read off a ≈2000 px render. DPR unverified | Save the capture as a file and re-run `probe.py` / `rows.py`; or read `NSTableView`/`NSStackView` frame values from a live build |
| C-JOBS9 colours (field `#1E1E1E`, card `#383838`, state green `#2FBF4C`) | [obs C-JOBS9] **[est]** | Visual judgement from a rendered image; ±15% | Sample the pixels. The one colour I *can* assert across captures is the media badge purple `#A572F3`, which was measured in C-FILES and matches by eye here |
| The project chooser is *disabled* in the Jobs view | [doc D5] vs [obs C-JOBS9] | The capture shows the chooser with a chevron; a disabled control and an enabled one look similar at this scale | Interact with it, or read `isEnabled` |
| "Failed / Aborted / Ok" counters are all always present | [doc D5] vs [obs C-JOBS9] | Only `aborted` and `ok` render. Either failed=0 so the pill is omitted, or the doc over-lists | Capture a session containing a failed job |
| Job card state glyphs beyond "complete" | [doc D5 §1.2] | Only the green check was observable. Red stop sign, grey clock, grey cross are documented but unseen | Capture a running, a suspended and a failed job |
| "Transcoding Preview" is a distinct centre view mode | [doc D2] | C-TRANS shows a plain player | Capture the Transcoding Presets layout in a live 9.4 build with a preset selected |
| The 6 info-panel tabs map to the 4-left + 2-right icons | [obs C-INFP] + [doc D3] | The two right-hand icons (a face and a lightning bolt) are inferred to be Look Library and Transcoding from their shape and position; no caption is legible | Open the Transcoding tab of the info panel and confirm the icon order |
| `Seal` makes a volume write-protected | [doc D6] + [doc D5] | Neither page states the *effect* of sealing explicitly; D5 lists Seal as a context-menu action | Read the Sealing wizard article / hands-on "Sealing" page |
| There is no "format card" operation | [doc D5] | Only the Jobs-view context menu was enumerated; the Offload Menu article (`C-OFFLOAD`) was downloaded but not inspected | Inspect C-OFFLOAD and the "Sealing wizard" article |
| Light mode exists and matches the dark ramp | [doc D10] (reports have light + dark) | The app itself was only ever captured in dark mode | Launch the app in light mode |
| The audio-panel half of the "Audio & Color" panel | [doc D1 #19, D1 #20] | Every capture shows only the **Color** half. The Audio tab of that panel was never visible | Capture the Audio tab |
| Miniplayer and scopes | [doc D1 #12] | Visible only in the annotated C-OVW at small scale; no clean capture | Capture the QC layout with scopes open |
| Toolbar is user-configurable | [doc D11] ("Tailor the toolbar to show only the tools you need") | Corroborated by X5 (different toolbars across versions) but the configuration UI was never shown | Open the toolbar customisation dialog |
| `A_0001C005_240426_083229…` truncates with a tail ellipsis | [obs C-MANAGE] | Tail vs. middle is visually ambiguous at this size for a *value* that could be either | Zoom the original capture; the middle ellipsis in the clip strip is unambiguous by contrast |

### Three questions I'd ask a Pomfort designer

1. **"In the clip table, is the filename supposed to truncate at the *end* or in the *middle*? The table and the filmstrip currently disagree, and in a table of `A_0001C00X_240426_…` names the middle is the only part that distinguishes one take from another."** — This is the highest-value question because it is a real, observable inconsistency between two components of the same app, and the fix is a one-line policy change.

2. **"How does a DIT discover which of the 30+ clip-table columns matter for *today's* job — is there a column-visibility manager, or is the expectation that you scroll the table sideways and read the header?"** — D1 lists a filter for the *info panel* but nothing for the *table's columns*. If there is no column manager, that is the largest missing affordance in the densest screen; if there is, it is worth adding to the teardown's component inventory.

3. **"What is the intended reading of the number in the library outline — total versions, or unique clips? D4 says versions with duplicates excluded, but the same glyph is used at every level of the tree, so a DIT cannot tell '171 clips' from '171 versions' without the docs."** — A one-line label or a tooltip would resolve it, and it is the kind of detail that separates a domain-correct tool from a generic dashboard.

---

### Two more, now that the Jobs view has been observed

4. **"In the Jobs grid, a workflow's jobs fan out to the right as sibling cards, which leaves ~43% of the window permanently empty when a workflow has only one job. Is that reserved space deliberate — so the eye expects more jobs — or is it a layout that has not been revisited since the grid moved from a table to cards?"** — This is a question only someone who has seen the current build can answer, and it is the single clearest layout inefficiency in the teardown (W6).

5. **"The jobs grid introduces cards on a near-black field, while the library view has no cards and no shadows at all. Was the ramp deliberately inverted for the Jobs view, or did it happen because cards were introduced without a shadow spec?"** — It affects the implementation brief directly: a designer who assumes "no elevation, ramp up" everywhere will build a Jobs view that does not match (see §1.10).

---

### Appendix A — Phase 0 checklist D, carried forward for screenshot judging

*(Named regions from D1–D5 only. Used as the pass/fail list in §S1–§S8.)*

- **D1 (UI overview, 24 callouts):** playback view; playback controls; toolbar; view tabs; navigation/breadcrumbs; project chooser; ShotHub sync; timecode; playback view options; visual controls + full-screen; toolbar (layout switcher); miniplayer + scopes; toolbar (Audio & Color + sidebar toggles); general-info tabs / look library / transcoding presets; general info; general info filter; jobs summary; running-jobs summary + progress; Audio & Color panel; audio & color tabs; Library/Jobs switch; library outline sorting; library outline; info display (+ dynamic metadata panel). Collection-view badges: thumbnail, name+duration+label, ingest date/time, audio indicator, flag icon, resource indicator.
- **D2 (window layouts):** Files, Manage, Quality control, Color, Transcoding presets; left sidebar = library outline; centre = list / collection / playback / transcoding preview; right sidebar = Files and Hashes / General Info / User Info / Look Library / presets; Audio & Color panel enabled or disabled.
- **D3 (information panel):** six tabs — General Info, User, File, Header, Look Library, Transcoding; pencil-marked editable fields; flags, ratings, labels, cue points, comments.
- **D4 (library outline):** Project, Bin (video/audio), Folder, Smart Folders, Volumes; version count per node; sort options Custom Order / Name A–Z / Name Z–A / Date oldest→newest / Date newest→oldest; drag-and-drop reorder; Duplicate Folder Structure.
- **D5 (jobs view):** volumes sidebar (left); workflow/job grid (centre); details bar (right); top bar; status bar (bottom); Scheduled / Running / Workflow History; job metrics FPS / ETA / Time Remaining / Task progress; details sections Workflow Summary, Show State History, Log File, Workflow's Jobs, Status, Errors, Configuration, Completion Steps, Parent Workflow; volume details Eject, Volume Summary, Performance Settings.

### Appendix B — Files produced

| Path | Contents |
|---|---|
| `silverstack-teardown.md` | This document |
| `silverstack_refs/` | 28 downloaded reference captures |
| `silverstack_refs/crop.py` | Region cropper (used for all zoomed reads) |
| `silverstack_refs/probe.py` | Structural measurement: h/v colour profiles, divider detection, colour histograms, connected-component icon bounding boxes |
| `silverstack_refs/rows.py` | Row-ink-band detector — the source of every row-pitch number in §1.10 |
