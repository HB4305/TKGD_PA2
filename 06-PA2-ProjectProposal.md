# PA2 Report - Requirement 3: Project Proposal

**Group:** 06  
**Course:** CSC13112 - UI/UX Design  
**Assignment:** Project Assignment 2  
**Product Scope:** Freestyle Chess mobile website on smartphone browser  
**Document Purpose:** Propose initial design concepts to solve the most severe user problems identified in Requirement 2.

---

## 1. Selected Problems

Following the assignment's guidance to focus on a few "tough problems" rather than attempting to solve everything, our group selected the two highest-priority problems from the Priority Matrix in `06-PA2-UserAnalysis.md`:

| Problem ID | Problem Description | Priority Score |
|---|---|---:|
| **P-01** | One-handed reachability issues with top-left hamburger menu | 19/20 |
| **P-02** | Lack of sticky search & filtering on long listing pages (Rating & News) | 18/20 |

These two problems were chosen because they scored highest across Frequency, Severity, Evidence Strength, and Feasibility, and because existing market solutions (competing chess/sports sites) do not sufficiently address either issue on mobile. P-03 (video feedback/audio overlap) was considered but set aside for this proposal, as its underlying issues read more as implementation bugs (state-desynced controls, missing loading feedback) to be fixed rather than a genuine UX redesign opportunity.

---

## 2. Overall Concept

The team's solution keeps the same product form as the original scope defined in PA1: a **responsive mobile website** (not a native app), accessed through a smartphone browser. We are not proposing a platform change; we are proposing an interaction-model change.

The core conceptual shift is moving from a **top-down, desktop-inherited layout** (hamburger menu at top-left, long unfiltered scrolling lists) to a **thumb-zone-first design philosophy**, where:

- Primary navigation and search controls are relocated or made reachable within the lower half of the screen, where one-handed users (44.4% per Q4) and situational grip-switchers (41.7% per Q4) can operate them without shifting grip.
- Information retrieval (search/filter) is treated as a first-class, always-accessible action rather than a per-page afterthought.

Users will conceptually interact with the redesigned site the same way they browse any modern mobile-first website — but with critical actions (navigate, search) always within a comfortable one-handed reach, instead of requiring two-handed operation or grip changes.

---

## 3. Problem 1 — P-01: One-Handed Reachability of the Hamburger Menu

### 3.1 Problem Restated

The hamburger menu is anchored top-left. This forces users (particularly the 43.1% who reported stretching, changing grip, or using their other hand — Q13) to perform awkward hand movements just to open navigation, especially during one-handed mobile use while commuting, waiting, or resting.

### 3.2 Evidence Base

N01, N02, N03, N04; Q11 (3.94/5), Q12 (3.50/5), Q13 (43.1%); interview observations from P01, P02, P03, P05, P07, P08 all describing thumb-stretching, grip-shifting, or phone-repositioning behavior when reaching for the menu button.

### 3.3 Proposed Conceptual Solutions

#### Solution 1 — Persistent Bottom Navigation Bar
- **Concept:** A fixed navigation bar with 4-5 tabs (Home, News, Schedule, Rating, Videos) permanently visible at the bottom of the screen. No open/close interaction is required.
- **Rationale:** Directly implements N03; repeatedly requested by P01, P02, P03 during interviews.
- **Strengths:** Familiar mobile pattern; reduces navigation from two steps (open menu, then tap item) to one; no discoverability risk.
- **Weaknesses:** Permanently occupies vertical screen space on an already small viewport; does not scale well if more top-level sections are added later.

#### Solution 2 — Draggable Floating Action Button (FAB)
- **Concept:** A floating circular button, not fixed in the page layout, defaulting to the bottom-right corner but **draggable** by the user to match their dominant hand. Tapping expands it into a short radial or list-style menu.
- **Rationale:** Implements N04; directly addresses P05's own suggestion ("a bar to drag instead of a fixed button") and the 41.7% of users whose grip depends on the situation (Q4).
- **Strengths:** Personalizes to actual handedness/grip rather than assuming one "correct" position for all users; does not consume layout space when idle.
- **Weaknesses:** Can visually overlap page content when expanded; requires additional engineering to persist the user's chosen position across sessions.

### 3.4 Comparison

| Criteria | Sol.1: Bottom Nav Bar | Sol.2: Draggable FAB |
|---|---|---|
| Familiarity to users | High | Medium |
| Adapts to handedness | No | Yes |
| Screen space used (idle) | Fixed, always-on | Minimal |
| Implementation complexity | Low | Medium-High |
| Discoverability risk | Low | Medium |

---

## 4. Problem 2 — P-02: Lack of Sticky Search & Filtering on Long Lists

### 4.1 Problem Restated

Long content lists (Rating leaderboard, News feed) rely on unassisted infinite scrolling with no persistent search. 61.1% of users (Q19) reported difficulty when they could not recall an exact name, event, or detail, and the existing Rating search requires exact-format name matching, causing failed searches even when the user typed a real player's name.

### 4.2 Evidence Base

N09, N10, N11, N12, N22, N23, N27; Q16 (3.60/5), Q17 (81.9%), Q19 (61.1%); interview observations from P02 (no search bar on News), P04/P07/P08 (want search beyond Rating), P06 (search fails on natural first-name/last-name order), P09 (needed three attempts — "Le Quang" → "Liem Le" → "Liem" — before a search succeeded), P10 (searching "FM" or a numeric rating returns nothing because the field only matches player names).

### 4.3 Proposed Conceptual Solutions

#### Solution 1 — Sticky Search Bar with Flexible Name Matching
- **Concept:** A text search bar that stays fixed (sticky) at the top of the Rating and News pages while scrolling. The underlying matching logic is upgraded to accept names in any word order, with diacritic-insensitive input and auto-suggestions as the user types.
- **Rationale:** Directly fixes the root cause behind P06 and P09's failed searches (stored-name-order dependency).
- **Strengths:** Preserves a familiar interaction model (a search bar); low structural change to existing pages.
- **Weaknesses:** Still requires the user to recall and type at least part of a name; does not address searching by attribute (title, rating) as raised by P10 and P08.

#### Solution 2 — Faceted Filter Chips (tap-to-filter, no typing required)
- **Concept:** Replace or supplement the search box with tappable filter chips: by chess title (GM, FM, IM...), by rating range, and by event/date for News. Results update in real time as chips are selected, with no text entry needed.
- **Rationale:** Directly resolves N27 and P10's failed attempts to search by "FM" or a numeric rating; also matches the most-selected support option in Q17 ("filters by event/date/player," chosen by 31 users).
- **Strengths:** Removes dependency on remembering exact names — well suited to newcomers like P10 who don't know any player names yet; tapping is faster than typing on mobile.
- **Weaknesses:** Less efficient for users who already know the exact name they want (still requires scrolling/selecting through chips); needs careful compact UI design to avoid cluttering a small screen.

### 4.4 Comparison

| Criteria | Sol.1: Sticky Search + Flexible Matching | Sol.2: Faceted Filter Chips |
|---|---|---|
| Fixes name-order failures (P06/P09) | Yes (directly) | Yes (indirectly, no typing) |
| Search by title/rating (P10) | No | Yes (directly) |
| Extends to News | Requires separate dev effort | Yes, via event/date chips |
| Implementation complexity | Low-Medium | Medium |
| Suited to users who don't know exact names | Low | High |

---

## 5. Summary

Both problems are addressed within the same overall concept — a responsive mobile website redesigned around thumb-zone accessibility and always-available information retrieval — while each is given two meaningfully distinct conceptual solutions rather than superficial variations of one idea. This gives the team a genuine basis for comparison before committing to a single direction for prototyping.