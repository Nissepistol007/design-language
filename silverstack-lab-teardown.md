# Silverstack Lab UI Teardown & Pattern Brief

**Date:** 2026-11-17  
**Authoritative Reference:** `silverstack-lab-teardown-handoff.md`  
**Target Stack:** SwiftUI (macOS Native)  
**Deliverable Format:** Single Markdown Document  

---

## Executive Summary & Domain Brief

### A. Core Workflow & Operations
- **Ingest:** Run offload workflows copying camera media to multiple volumes, verifying via checksum (XXH64/MD5), registering clip records in the central library `[doc·D6]`.
- **Organise & Verify:** Group into Projects, Bins, Folders, Smart Folders. Assign metadata (Scene, Shot, Take, Flag, Rating, Color Label) `[doc·D3, D4]`.
- **QC, Grade & Transcode:** Frame-accurate scrub with JKL, scopes, audio sync, apply CDL/3D LUT/ACES looks, export proxies in DNxHD/ProRes/H.264 `[doc·D7, D8, D9]`.
- **Deliver & Report:** Generate ASC MHL lists, post-step job reports, Frame.io uploads, shooting-day/contact-print PDF/HTML reports `[doc·D5, D10, D14]`.

### B. Core Vocabulary Table
| Term | Meaning | UI Impact | Src |
|---|---|---|---|
| Offload | Media copy from card to storage | Requires volume selector, path rules, backup slots | D6 |
| Workflow | Chained sequence of automated tasks | Monitored in multi-level progress trees | D5, D6 |
| Checksum | Hash verification (XXH64, MD5) | Pass/fail visual status pills (`# All Resources Verified`) | D6, D13 |
| ASC MHL | Standardized XML media hash list | Export action / completion step affordance | D6, D10 |
| Look | CDL + LUT + ACES color transform | Dedicated Look Library sidebar + thumbnail grid | D3, D8 |
| Smart Folder | Live filtered clip query | Dynamic container in outline tree with criteria count | D4 |

### C. Critical UI Challenges
1. **Metadata Density at Scale:** Over 100 metadata fields per clip `[doc·D11]`. Custom-field take-over in the inspector header `[doc·D3]`. Columns must stay rock-solid while supporting dynamic reordering and middle truncation.
2. **High-Stakes Media Verbs:** Irreversible actions (Eject, Seal, Abort) live alongside live background ingest `[doc·D5]`. Confirmations and explicit task state histories prevent accidental data loss.
3. **Parallel Background Trust:** Jobs fan out into sub-tasks (Backup, Verify, Transcode, Upload) with auto-pausing rules `[doc·D5]`. Progress requires aggregate-level status bar + detailed multi-pane grid view.

---

## Phase 1: Screenshot Teardown & Component Inventory

### 1. Per-Screen Wireframe & Layout Audits

#### Screen 1: Manage Layout (Collection / Grid View)
- **Purpose:** Visual media inspection, thumbnail sorting, metadata panel tagging.
- **Anchor vs Scroll:** Left outline & Right inspector are anchored. Middle thumbnail grid scrolls vertically.
- **Anchor Basis:** `≈11px` body font calibration. Header bar = `≈38px`, Sidebar row = `≈22px`, Thumbnail card = `≈140x110px`.

```
+-----------------------------------------------------------------------------------------+
| Toolbar: [Offload] [Add Clips] [Media] [Export]... | [Files] [Manage*] [QC] [Color]     | ~38px
+----------------------------------------------------+------------------------------------+
| Breadcrumbs: Library > 20240426_Day_1 > Camera_Media| Search [Search in "All Fi...    ]  | ~28px
+-----------------------+----------------------------+------------------------------------+
| Left Sidebar (Outline)| Middle Grid (Collection)   | Right Inspector (General Info)     |
| [Header Card]         | [Sort: Clip Name  v] [^A-Z]| v Video Clip                       |
| 24fps 37 sec  889 fr  | +-------+ +-------+        |   Name     A_0001C005...           |
| 1 file with 4 backups | | [ALE] | | [BIN] |        |   ShotID   3ND-VCP-MB3             |
|                       | +-------+ +-------+        |   Duration 37 sec                  |
| v Library          418| +-------+ +-------+        | v Timecode                         |
|   > Day_1          171| |[IMG 1]| |[IMG 2]| (SEL)  |   TC Format 24 fps                 |
|     Camera_Media    93| +-------+ +-------+        |   TC Start  08:38:02:12             |
|     * A_0001_1DJH   12| +-------+ +-------+        | > Edit/User                        |
|                       | |[IMG 3]| |[IMG 4]|        | > Camera Settings                  |
+-----------------------+----------------------------+------------------------------------+
| Footer: [Library|Jobs]| Bottom Indicators (Eject/LTFS/Cloud...)  [Filter General Info   ] | ~24px
+-----------------------------------------------------------------------------------------+
```

#### Screen 2: Files Layout (List / Table View)
- **Purpose:** Dense tabular metadata verification, storage path inspection, hash verification status.
- **Anchor vs Scroll:** Left outline & Right inspector (Files & Hashes) anchored. Main Table scrolls horizontally & vertically.
- **Anchor Basis:** `≈11px` font basis. Row height = `≈22px` fixed. Header row = `≈24px`.

```
+-----------------------------------------------------------------------------------------+
| Toolbar: Standard Top Bar                                                               | ~38px
+-----------------------------------------------------------------------------------------+
| Table Header: Name | ShotID | Duration | Frames | Camera | EI/ISO | WB | Shutter |...   | ~24px
+-----------------------+------------------------------------+----------------------------+
| Outline Sidebar       | Main Table (Scrollable Columns)    | Right Sidebar: Files&Hashes|
|                       | A_0001C001... X7R-T4U 24sec 581 A  | Size: 4.68 GB              |
|                       | A_0001C002... U2D-2GS 30sec 728 A  | Hash: XXH64: 2e76b3b1ce... |
|                       |*A_0001C005... 3ND-VCP 37sec 889 A  | # All Resources Verified   |
|                       | (Active selected blue row)         | [ SOURCE ] A_0001_1DJH     |
|                       | A_0001C006... 5NJ-RNE 1:03  1519 A | [ BACKUP ] PFN_RAID        |
|                       | A_0001C007... P3N-44R 1:22  1972 A | [ BACKUP ] BACKUP_RAID     |
+-----------------------+------------------------------------+----------------------------+
| Footer Status Bar                                                                       | ~24px
+-----------------------------------------------------------------------------------------+
```

#### Screen 3: QC & Color Layout (Playback View + Color Controls)
- **Purpose:** Quality control visual checks, frame scrubbing, CDL 3-wheel primary color grading.
- **Anchor vs Scroll:** Player canvas & CDL bottom panel anchored. Thumbnail filmstrip scrolls horizontally.

```
+-----------------------------------------------------------------------------------------+
| Top Bar + Timecode Display [08:38:20:12]                                                | ~38px
+-----------------------------------------------------+-----------------------------------+
| Player Canvas (Aspect Ratio Maintained Video Display)| Right Inspector / Look Library   |
|                                                     | v Custom looks                    |
|                                                     |   Cool looks                      |
|                                                     | +--------+ +--------+             |
|                                                     | |[THUMB1]| |[THUMB2]| (Grid)      |
|                                                     | +--------+ +--------+             |
+-----------------------------------------------------+-----------------------------------+
| Horizontal Filmstrip (Clip Timeline Scrubber)       | Look Details Inspector Panel      |
| [A_0001...][A_0002...][*A_0005...*][A_0006...]      | Name: Nightish                    |
+-----------------------------------------------------+ Reel: A015R2EC                    |
| Bottom CDL Panel:                                   | Start TC: 00:03:48.10             |
| (O) Offset  (O) Power  (O) Slope | RGB Numeric Fields| End TC:   00:04:52.01             |
| [ Saturation Slider ----------- ] | [LUT Curve Display]|                                |
+-----------------------------------------------------------------------------------------+
```

#### Screen 4: Jobs View (Background Activity & Queue Manager)
- **Purpose:** Workflow queue inspection, background ingest monitoring, error log diagnoses.
- **Anchor vs Scroll:** Left queue control anchored. Centre execution grid & right job detail inspector scroll.

```
+-----------------------------------------------------------------------------------------+
| Top Bar: [Suspend All] [Resume All] | Filter: Summary [All|Unread|State|Date]           |
+-----------------------------------------------------------------------------------------+
| Queue | Source | Job | Config | Progress | State | Remaining | File Size                |
| (>)   | C300 Footage  | Upload | MOV    | [=== 100% ===] | Complete  | 11 sec  | 1.75 GB  |
| (>)   | C300 Footage  | Transc | Post   | [=== 100% ===] | Complete  | 17 sec  | 0.00 KB  |
| (>)   | C300 Footage  | Transc | Edit   | [=== 100% ===] | Complete  | 13 sec  | 0.00 KB  |
+---------------------------------------------------------------------+-------------------+
| Active Running Queue Section                                        | Job Details       |
| (>)   | C300 Footage  | Upload | Silver | [==== 45% ====] | 18.45EB/s | C300 Footage(Post)|
+---------------------------------------------------------------------+ State: Complete   |
| Bottom Status Bar: [v Jobs]  [ 1 running   |||||||||||| ] [ 8 sec left ]    [ Silverstack 6 ok ] |
+-----------------------------------------------------------------------------------------+
```

---

### 2. Consolidated Design Tokens

#### Color Palette
| Token Name | Hex Value | Observed Usage / Role |
|---|---|---|
| `bg-dark-base` | `#1E1E1E` | Main window background, background canvas |
| `bg-panel-dark` | `#282828` | Sidebar panels, inspector backgrounds, toolbar strip |
| `bg-surface-elevated` | `#323232` | Table header background, card containers |
| `accent-blue-selection` | `#2A609E` | Active list row highlight, selected thumbnail outline |
| `status-green-success` | `#34C759` | Verified checksum tag, job complete status indicator |
| `status-amber-warning` | `#FF9F0A` | Suspended jobs, non-critical metadata flags |
| `status-red-error` | `#FF3B30` | Failed verification hash, aborted workflow error |
| `text-primary` | `#F2F2F7` | Standard label, heading, and table text |
| `text-secondary` | `#8E8E93` | Subtitles, disabled tabs, non-active metadata key labels |
| `border-divider` | `#3A3A3C` | 1px separator lines between inspector sections |

#### Typography Scale
| Role | Size | Weight | Line Height | Application |
|---|---|---|---|---|
| `font-header` | 13px | Semi-Bold | 16px | Section headers (e.g. "General Info", "Look Details") |
| `font-body-regular` | 11px | Regular | 14px | Data table cells, list values, metadata inspector key/values |
| `font-body-bold` | 11px | Bold | 14px | Primary identifiers, clip names, TC values |
| `font-caption` | 9px | Medium | 11px | Badge labels, thumbnail metadata overlay text, status pills |
| `font-mono-code` | 11px | Monospaced | 14px | Timecode, Checksum Hash Strings, File Path Strings |

#### Spacing & Layout Metrics
- **Fixed Table Row Height:** `≈22px`
- **Sidebar Header Height:** `≈28px`
- **Inspector Key-Value Padding:** Vertical `4px`, Horizontal `8px`
- **Control Element Border Radius:** `3px` (subtle macOS dark mode rounding)
- **Gutter Divider Width:** `1px solid #3A3A3C`

---

### 3. Component Inventory & Observed vs Assumed States

| Component | Observed States `[obs]` | Assumed / Undocumented States `[recall]` | Evidence Source |
|---|---|---|---|
| **Outline Tree Item** | Standard, Hover, Selected Blue, Expanded/Collapsed Arrow | Drag-and-drop target, drop insertion indicator | `[obs]` `D_layout-manage.jpg` |
| **Data Table Row** | Normal, Alternate Stripe, Selected Active Blue | Multi-selection focus, context-menu right-click state | `[obs]` `C_layout-files.jpg` |
| **Thumbnail Card** | Standard, Selected Outline Blue, Ingest Audio Badge | Multi-select badge overlay, missing resource warning icon | `[obs]` `D_layout-manage.jpg` |
| **Job Progress Bar** | Active Animated Blue (with velocity EB/s), Complete Green | Aborted Gray, Failed Solid Red | `[obs]` `Z1_frameio-jobstatus.png` |
| **Verification Pill** | Green Verified Tag (`# All Resources Verified`) | Red Unverified / Failed Tag | `[obs]` `C_layout-files.jpg` |
| **3-Wheel CDL Control** | Active Ring Color, Numeric Value Inputs, Reset Curves | Mouse-drag scrub sensitivity states | `[obs]` `E_layout-qc.jpg` |

---

### 4. Density & Ergonomics Audit

#### 3 Key UI Strengths
1. **Persistent Task-Oriented Mode Switching:** Direct 1-click preset switches (Files, Manage, QC, Color, Presets) in the top bar instantaneously reconfigure screen real estate without losing scroll selection `[obs·D_layout-manage.jpg]`.
2. **Strict Monospaced Alignment for Critical Data:** Timecodes, frame counts, and SHA/XXH64 hash values are exclusively set in monospaced type, preventing layout jitter during real-time background updates `[obs·C_layout-files.jpg]`.
3. **Multi-tier Hierarchical Status Aggregation:** Real-time system progress is visible simultaneously at the per-task level, per-workflow level, and summary footer bar level `[obs·Z1_frameio-jobstatus.png]`.

#### 3 Key UI Weaknesses
1. **High Visual Noise in Metadata Inspector:** The right-hand General Info inspector presents key-value fields with uniform spacing, lacking visual hierarchy between high-frequency fields (TC, Duration) and low-frequency tags `[obs·D_layout-manage.jpg]`.
2. **Ambiguous Status Colors in Minimal Controls:** Non-standard icon badges rely on small inline color dots without explicit text labels in thumbnail mode `[obs·D_layout-manage.jpg]`.
3. **Density-Induced Truncation:** Dense table layouts aggressively truncate file paths in the center, requiring inspect-panel focus to read destination directories `[obs·C_layout-files.jpg]`.

---

### 5. Checklist Reconciliation (Documentation vs Observation)

| Named Region / Component | Status Tag | Reference Source |
|---|---|---|
| Main Toolbar & Layout Mode Switcher | `present → [obs]` | `D_layout-manage.jpg`, `D1` |
| Library Outline Sidebar with Item Counts | `present → [obs]` | `D_layout-manage.jpg`, `D4` |
| Collection / Thumbnail Grid View | `present → [obs]` | `D_layout-manage.jpg`, `D1` |
| Files & Hashes Tab Inspector | `present → [obs]` | `C_layout-files.jpg`, `D2`, `D3` |
| General Info Editable Inspector | `present → [obs]` | `D_layout-manage.jpg`, `D3` |
| Jobs View Multi-tier Status Bar | `present → [obs]` | `Z1_frameio-jobstatus.png`, `D5` |
| Offload Dropdown Quick Menu | `present → [obs]` | `M_offload-menu.jpg`, `D6` |
| 3-Color Wheel Primary CDL Panel | `present → [obs]` | `E_layout-qc.jpg`, `D8` |
| Preset Selector & Transcode Details | `present → [obs]` | `G_layout-transcode.jpg`, `D9` |
| Look Library Grid Inspector | `present → [obs]` | `X_looklibrary.png`, `D3`, `D8` |
| Dynamic Metadata Extraction Timeline Chart | `described in docs but not visible → [doc, not shown]` | `D5` |
| LTFS Tape Storage Management Controls | `described in docs but not visible → [doc, not shown]` | `D5` |

---

## Phase 2: Reusable UI Patterns & macOS SwiftUI Implementation Brief

### 1. 7 Reusable Professional Desktop UI Patterns

| Pattern Name | When to Use | Structural Rule (Imperative) | Anti-Pattern Prevented |
|---|---|---|---|
| **1. Dynamic Layout Mode Presets** | Complex multi-step workflows requiring distinct tool arrangements. | Bind top toolbar mode buttons directly to layout panel visibility states while maintaining single active document selection. | Modal dialog overload and window clutter. |
| **2. Monospaced Alignment Anchor** | Rendering numbers, timecodes, hashes, or live dynamic metrics. | Format numeric and hash values using monospaced font features (`monospacedDigit()`) with middle truncation. | Layout jitter and text shift during live updates. |
| **3. Three-Tier Queue Aggregation** | Multi-threaded background tasks with parent-child dependencies. | Surface overall status in a persistent footer, parent status in queue rows, and sub-task status in expandable inspectors. | Silent background failures and progress ambiguity. |
| **4. Accordion Inspector Sectioning** | Displaying >50 metadata properties in a single sidebar. | Group parameters into collapsible sections; preserve state across selection changes. | Endless vertical scrolling and cognitive overload. |
| **5. High-Density Fixed Grid Constraints** | List and table structures displaying thousands of records. | Fix row height at 22–26px with virtualized list rendering and inline truncation. | Variable-height row jumps and performance lag. |
| **6. Non-Destructive Ingest Verification Badging** | Displaying media integrity and verification states. | Display explicit pass/fail badges with checksum format tooltips alongside file paths. | Accidental overwrite or unverified media ingest. |
| **7. Dual-Inspector Header Take-Over** | Editing clip metadata vs global project properties. | Convert inspector headers dynamically into quick-edit entry forms when double-clicked. | Detached modal edit sheets for minor property updates. |

---

### 2. Implementation Brief for SwiftUI (macOS Native)

#### A. Design System Tokens (SwiftUI Code Block)

```swift
import SwiftUI

public enum SilverstackTokens {
    // MARK: - Colors
    public static let bgDarkBase = Color(red: 0.118, green: 0.118, blue: 0.118) // #1E1E1E
    public static let bgPanelDark = Color(red: 0.157, green: 0.157, blue: 0.157) // #282828
    public static let bgSurfaceElevated = Color(red: 0.196, green: 0.196, blue: 0.196) // #323232
    public static let accentSelection = Color(red: 0.165, green: 0.376, blue: 0.620) // #2A609E
    public static let statusSuccess = Color(red: 0.204, green: 0.780, blue: 0.349) // #34C759
    public static let statusError = Color(red: 0.996, green: 0.231, blue: 0.188) // #FF3B30
    public static let textPrimary = Color(red: 0.949, green: 0.949, blue: 0.969) // #F2F2F7
    public static let textSecondary = Color(red: 0.557, green: 0.557, blue: 0.576) // #8E8E93
    public static let borderDivider = Color(red: 0.227, green: 0.227, blue: 0.235) // #3A3A3C

    // MARK: - Layout & Typography
    public static let tableRowHeight: CGFloat = 22.0
    public static let fontHeader = Font.system(size: 13, weight: .semibold, design: .default)
    public static let fontBody = Font.system(size: 11, weight: .regular, design: .default)
    public static let fontMono = Font.system(size: 11, weight: .medium, design: .monospaced)
    public static let fontCaption = Font.system(size: 9, weight: .medium, design: .default)
}
```

#### B. Component Architecture Tree

```
MainAppWindow (HSplitView)
├── NavigationSidebarView (VSplitView)
│   ├── LibraryOutlineTree (List with TreeModifier)
│   └── VolumeStatusList (Section)
├── WorkspaceCenterView (ZStack)
│   ├── LayoutModeBar (Picker / Segmented Control)
│   ├── TableView (Table with Monospaced Columns)
│   ├── CollectionView (LazyVGrid with ThumbnailCards)
│   └── QCPlayerView (AVPlayer + ScopesOverlay)
├── MetadataInspectorView (ScrollView + VStack)
│   ├── GeneralInfoAccordion (DisclosureGroup)
│   └── FilesAndHashesPanel (VStack with StatusPill)
└── MainFooterStatusBar (HStack)
    ├── JobQueueSummaryPill (Button)
    └── GlobalProgressBar (Gauge / ProgressView)
```

#### C. Top 3 Hardest SwiftUI Components & Solutions

1. **Virtualised High-Density Data Table with 100+ Custom Columns**
   - *Challenge:* Standard `Table` performance degrades with complex dynamic columns and frequent selection re-renders.
   - *Solution:* Use SwiftUI `Table` bound to flat model structures, leveraging `.monospacedDigit()` and fixed `frame(height: 22)` specifiers on cell views to bypass auto-layout calculations.

2. **Custom 3-Wheel CDL Color Controls**
   - *Challenge:* SwiftUI lacks native color wheel trackpad controls for Lift/Gamma/Gain or Offset/Power/Slope adjustments.
   - *Solution:* Implement a custom `Gesture`-driven `Canvas` control rendering vector color circles with interactive drag handles bound to RGB float vectors (`Vector3`).

3. **Multi-level Async Job Execution Progress Bar**
   - *Challenge:* Rendering real-time velocity updates (e.g., `18.45 EB/s`) without triggering total view hierarchy re-evaluations.
   - *Solution:* Isolate the bottom status bar view component using `@Observable` state sub-objects, isolating high-frequency telemetry updates from the parent window tree.

#### D. Ordered Build Sequence
1. **Step 1: Core Layout Spine:** Build `HSplitView` shell with top layout mode switcher and bottom status bar.
2. **Step 2: Table & Collection Views:** Implement high-density `Table` and `LazyVGrid` clip rendering.
3. **Step 3: Accordion Inspector:** Build key-value `DisclosureGroup` inspector sidebar.
4. **Step 4: QC & Player Integration:** Construct AVFoundation player wrapper with filmstrip timeline.
5. **Step 5: Job Queue Engine:** Integrate async job execution tracking into the bottom status bar.

---

## Confidence Matrix & Verification Gaps

| Claim / Component | Basis Tag | Uncertainty / Risk Factor | Verification Step |
|---|---|---|---|
| Fixed Table Row Height (≈22px) | `[obs]` | Screen calibration anchored against 11px font; minor rendering scale differences may occur on Retina displays. | Measure pixel dimensions on native 4K display dump. |
| Job Aggregation Algorithm | `[doc]` | Official docs state aggregate progress is unweighted average of running jobs. | Test execution with jobs of varying total byte sizes. |
| Custom Field Header Take-over | `[doc]` | Described in 2013 documentation (`D3`); observed in modern UI screenshot. | Verify double-click edit trigger on active clip header. |
| Card Format Verbs | `[recall]` | No format card verbs appear in documentation or screenshots. | Treat as non-existent; do not build format card workflows. |

### Top 3 Questions for a Silverstack UX Designer
1. *How are column layout presets saved and shared across production teams working on multiple DIT carts?*
2. *What is the fallback visualization strategy when a clip contains missing or offline media resources during playback?*
3. *What visual cues differentiate an auto-paused background verify job from a user-suspended job in dense queue views?*
