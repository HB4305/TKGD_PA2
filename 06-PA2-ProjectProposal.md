# PA2 Report - Requirement 3: Project Proposal

**Group:** 06  
**Course:** CSC13112 - UI/UX Design  
**Assignment:** Project Assignment 2  
**Product Scope:** Freestyle Chess mobile website on smartphone browser  
**Document Purpose:** Propose initial design concepts to solve the most severe user problems identified in Requirement 2.

---

## 1. Selected Problems

Following the assignment's guidance to focus on a few "tough problems" rather than attempting to solve everything, our group selected the two highest-priority problems from the Priority Matrix in `06-PA2-UserAnalysis.md`, plus one supplementary problem carried forward despite scoring below the matrix's selection threshold:

| Problem ID | Problem Description | Priority Score |
|---|---|---:|
| **P-01** | One-handed reachability issues with top-left hamburger menu | 19/20 |
| **P-02** | Lack of sticky search & filtering on long listing pages (Rating & News) | 18/20 |
| **P-05** | Schedule does not provide enough information, forcing users to look elsewhere for this information. | 10/20 |

P-01 and P-02 were chosen because they scored highest across Frequency, Severity, Evidence Strength, and Feasibility, and because existing market solutions (competing chess/sports sites) do not sufficiently address either issue on mobile. P-03 (video feedback/audio overlap) was considered but set aside for this proposal, as its underlying issues read more as implementation bugs (state-desynced controls, missing loading feedback) to be fixed rather than a genuine UX redesign opportunity.

P-05 is included despite its low quantitative score (10/20, below the ~16+ threshold used for P-01/P-02/P-04). It was reported by only one interview participant (P09) with no supporting survey data, which the rubric scores as weak evidence. However, the group weighted this qualitatively: P09 is a self-identified active chess follower who deliberately searched for match brackets and player pairings across multiple parts of the site — the exact information-seeking behavior of a dedicated, retention-relevant user — whereas most other respondents in the research are first-time or casual users still forming a basic impression of the site. A gap that blocks this kind of core user was judged worth addressing even though it does not clear the matrix's numeric bar. This trade-off is documented explicitly here, and in the corresponding rationale in `06-PA2-UserAnalysis.md`, rather than left implicit.

---

## 2. Overall Concept

The team's solution keeps the same product form as the original scope defined in PA1: a **responsive mobile website** (not a native app), accessed through a smartphone browser. We are not proposing a platform change; we are proposing an interaction-model change, governed by three concrete design principles:

1. **Thumb-zone-first placement.** Any control a user must tap frequently or urgently (navigation, search) must be reachable within the lower ~60% of the viewport without requiring a grip change. This directly targets the 44.4% of users who hold the phone one-handed and the 41.7% whose grip depends on context (Q4).
2. **Zero-step or one-step access to core actions.** Navigating to a section or searching a list should not require opening a hidden menu first; the control itself should be either always visible or always one gesture away.
3. **Flexible input over exact recall.** Wherever a user is expected to type or remember something exactly (a name, a spelling, a word order), the interface should tolerate approximation or replace typing with tap-based selection, directly addressing the 61.1% of users who struggled when they could not recall an exact name or term (Q19).

Each conceptual solution for P-01 and P-02 below is a distinct way of implementing these principles, not a cosmetic variant of the same idea. **P-05 (Section 5)** is a supplementary problem addressing information completeness rather than thumb-zone reachability or search flexibility, so its two solutions are evaluated against their own rationale rather than these three principles.

---

## 3. Problem 1 — P-01: One-Handed Reachability of the Hamburger Menu

### 3.1 Problem Restated

The hamburger menu is anchored top-left. This forces users (particularly the 43.1% who reported stretching, changing grip, or using their other hand — Q13) to perform awkward hand movements just to open navigation, especially during one-handed mobile use while commuting, waiting, or resting.

### 3.2 Evidence Base

N01, N02, N03, N04; Q11 (3.94/5 — menu is findable), Q12 (3.50/5 — but not reachable one-handed), Q13 (43.1% reported physical adjustment); interview observations from P01, P02, P03, P05, P07, P08, all independently describing thumb-stretching, grip-shifting, or phone-repositioning behavior when reaching for the current top-left menu button.

### 3.3 Solution CS1.1 — Persistent Bottom Navigation Bar

**Concept summary:** Replace the hidden hamburger menu with a navigation bar that is permanently visible and permanently in place at the bottom edge of the viewport. Navigation becomes a single tap on a visible icon rather than a two-step "open menu, then choose item" sequence.

**Layout specification:**
- A horizontal bar fixed at the bottom of the screen (`y = bottom`, `position: fixed`), spanning the full viewport width.
- The full site menu (confirmed against the current production menu, which is larger than N03's simplified 5-item description) is: Home, Schedule, Videos & Streams, News, Press & Media (with children: Press Inquiries, Galleries), Rating, Rules & FC Players Club, Merch, Masterclass (which itself contains a Login link). To keep the bar usable, only **5 core destinations** get a permanent slot, matching the original N03 set: **Home, News, Schedule, Rating, Videos & Streams**. A 6th slot, **"More,"** holds everything else.
- Each of the 6 slots shows an icon with a short text label stacked vertically, consistent with the labels already found understandable without icons (Q14: 3.83/5).
- The currently active section is visually distinguished (e.g., filled icon + accent color) so the user always has a sense of location within the site.

**"More" destination structure:**
- Tapping "More" opens a bottom-sheet listing the remaining items: **Press & Media, Rules & FC Players Club, Merch, Masterclass**.
- **Press & Media** expands inline (accordion) within this sheet to reveal its two children, **Press Inquiries** and **Galleries** — the only item in the entire menu that keeps the original inline-expand behavior, since it is the only branch with exactly two simple children and no further page-level content of its own.
- **Schedule** and **Masterclass** do **not** expand inline. Both navigate to their own dedicated page instead: Schedule opens its existing overlay/submenu (unchanged from current behavior), and Masterclass opens its own full page, inside which the **Login** link lives as part of that page's own content — it is not shown as an accordion child in the main menu, since the current site already treats Masterclass as a standalone page rather than a togglable menu section.

**Interaction rules:**
- Tapping any of the 5 core tabs navigates directly to that section and updates the active-state highlight immediately.
- Tapping the tab for the section the user is *already* on scrolls the current page back to the top, rather than doing nothing (preventing a "dead tap" experience).
- Tapping "More" opens the bottom-sheet described above; tapping outside the sheet or an explicit close control dismisses it without navigating.
- The bar remains visible during scrolling on all pages; it does not hide on scroll-down, since hiding it would reintroduce a reachability problem for a returning tap.

**Rationale:** Directly implements N03 and was independently and repeatedly requested by P01, P02, and P03 during interviews as the preferred fix.

**Strengths:** Uses an interaction pattern nearly every smartphone user already knows from other apps; reduces the task to exactly one tap; carries no discoverability risk since the bar is always visible.

**Weaknesses:** Permanently consumes vertical space on an already small viewport, competing with content height; does not scale gracefully if the site later needs to add a sixth or seventh top-level section, since a bottom bar has a practical limit of about 5 items before labels must shrink or icons must replace text.

### 3.4 Solution CS1.2 — Draggable Floating Action Button (FAB)

**Concept summary:** Instead of a fixed bar, provide a single floating circular button that is not bound to any fixed screen position. The user can drag it to wherever their thumb naturally rests, and the button then expands into a compact navigation menu when tapped.

**Layout specification:**
- A circular button (~48-56px diameter, per standard mobile touch-target sizing) floating above page content, with a default resting position at the bottom-right corner.
- The button casts a subtle shadow to indicate it floats above content rather than being part of the page layout.
- On tap, the button expands into a short list containing the same 5 core destinations as CS1.1 (Home, News, Schedule, Rating, Videos & Streams), plus a 6th "More" entry at the bottom of the list.
- Tapping "More" expands the same list in place to also show: Press & Media, Rules & FC Players Club, Merch, Masterclass — with Press & Media further expanding inline to reveal Press Inquiries and Galleries, identical to the "More" behavior specified in CS1.1. Schedule and Masterclass still navigate to their own dedicated pages rather than expanding, for the same reason given in CS1.1.

**Interaction rules:**
- **Drag:** Press-and-hold, then drag to reposition the button anywhere along the screen edges; on release, the button snaps to the nearest edge (left or right) and the position is remembered for the user's next visit.
- **Tap threshold:** Any touch movement under ~5px is treated as a tap (opens the menu), not a drag — preventing accidental drags from a slightly imprecise tap.
- Selecting a core destination or a "More" sub-item that is a real page navigates there and collapses the button back to its resting state; tapping "Press & Media" or "More" itself only expands the list further and does not collapse the button.

**Rationale:** Implements N04 and directly answers P05's own suggestion during interview ("a bar to drag instead of a fixed button"), while serving the 41.7% of users whose grip depends on the situation rather than being fixed to one hand (Q4).

**Strengths:** Personalizes to the user's actual handedness and grip instead of assuming one "correct" position for everyone; consumes almost no screen space when collapsed, unlike a bar that is always fully expanded.

**Weaknesses:** The expanded menu can visually overlap page content beneath it; requires additional engineering effort to persist a per-user custom position across sessions (e.g., local storage), which CS1.1 does not need at all.

### 3.5 Comparison

| Criteria | CS1.1: Persistent Bottom Nav Bar | CS1.2: Draggable FAB |
|---|---|---|
| Familiarity to users | High (standard mobile pattern) | Medium (drag-to-reposition is less common) |
| Adapts to individual handedness | No — fixed layout for all users | Yes — repositionable per user |
| Screen space used when idle | Fixed strip, always present | Minimal (single small button) |
| Steps to navigate | 1 tap | 2 taps (open, then select) |
| Implementation complexity | Low | Medium-High (drag physics + position persistence) |
| Discoverability risk | Low | Medium (drag affordance must be visually hinted) |

---

## 4. Problem 2 — P-02: Lack of Sticky Search & Filtering on Long Lists

### 4.1 Problem Restated

Long content lists (Rating leaderboard, News feed) rely on unassisted infinite scrolling with no persistent search. 61.1% of users (Q19) reported difficulty when they could not recall an exact name, event, or detail, and the existing Rating search requires exact-format name matching, causing failed searches even when the user typed a real player's name.

### 4.2 Evidence Base

N09, N10, N11, N12, N22, N23, N27; Q16 (3.60/5 — finding info is only moderately easy), Q17 (81.9% want some form of list-browsing support), Q19 (61.1% struggled with imprecise recall); interview observations from P02 (no search bar exists on News at all), P04/P07/P08 (all wanted search extended beyond Rating), P06 (search fails when a name is entered in natural first-name/last-name order instead of the stored "Last, First" format), P09 (needed three separate attempts — "Le Quang" → "Liem Le" → "Liem" — before a search finally succeeded), P10 (typing "FM" or a numeric rating value returns nothing at all, because the field only ever matches against player names).

### 4.3 Solution CS2.1 — Sticky Search Bar with Flexible Name Matching

**Design note — accepted trade-off with Principle #1:** A prior draft moved the search entry point into the thumb zone via a small icon that opened a dedicated overlay, to strictly satisfy the "Thumb-zone-first placement" principle. The group decided against this: the reachability problem with the *original* hamburger menu was specifically about a **small, precisely-positioned icon confined to one corner** (top-left), which forces the thumb to stretch toward one exact point. A **full-width sticky bar** does not have that failure mode — the tap target spans the entire top edge, so the user can tap wherever is horizontally comfortable rather than reaching for one fixed corner. The remaining reach (vertical, to the top of the screen) is judged an acceptable trade-off in exchange for keeping the search bar always visible while scrolling, without adding an extra tap or a second control (an icon plus an overlay) just to open it.

**Concept summary:** Keep the familiar text-search interaction, but fix the two things actually broken about it: it disappears when scrolling, and it fails on any input that isn't in the exact stored name order.

**Layout specification:**
- A search input field fixed at the top of the viewport (`y = 0`, `position: sticky`), spanning the full width of the screen, on both the Rating and News pages, remaining visible regardless of scroll position.
- Includes a clear ("×") button to reset the search instantly, and a dropdown area beneath the field for live auto-suggest results.

**Interaction & matching rules:**
- The matching engine tokenizes the query into individual words and matches them against all name fields (first name, last name, full name) **regardless of the order typed** — so "Liem Le," "Le Liem," and "Liem" all correctly resolve to the same player, directly fixing the failure mode observed with P06 and P09.
- Matching is diacritic-insensitive (accepts input with or without Vietnamese tone marks).
- As the user types, a live auto-suggest list appears beneath the field showing candidate matches (e.g., "GM Le Quang Liem — Rating 2736").
- If no match is found, the system shows a "No player found" state with a suggested closest match ("Did you mean: Liem Le?") rather than a silent empty result.

**Rationale:** Directly fixes the confirmed root cause behind P06 and P09's failed searches — the search engine's dependency on stored name order — rather than only cosmetically adding "stickiness." The full-width bar shape also keeps the control materially easier to reach than the original top-left hamburger icon, even though it remains at the top of the viewport.

**Strengths:** Preserves an interaction model every user already understands (typing into a search box); requires comparatively low structural change to the existing Rating and News pages; no extra tap needed to reveal the field, unlike an icon-triggered overlay.

**Weaknesses:** Still fundamentally a name-based search — it does not help a user who wants to filter by an attribute they know (a title like "FM," or a rating threshold) but not a name, which is exactly the gap P10 and P08 encountered. Also still requires an upward reach to the top of the screen to actually tap into the field, even if the wide target reduces the precision required.

### 4.4 Solution CS2.2 — Faceted Filter Chips (Tap-to-Filter)

**Concept summary:** Replace typed recall with tap-based selection. Instead of asking the user to remember and spell a name, present the dimensions people actually search by — title, rating range, event/date — as selectable chips.

**Layout specification:**
- A horizontally scrollable row of chip-shaped toggle buttons positioned directly beneath the page title on the Rating page (e.g., `All`, `GM`, `IM`, `FM`, `Rating > 2700`) and on the News page (e.g., event names, date ranges).
- Selected chips show a filled/active visual state; unselected chips remain outlined.

**Interaction rules:**
- Tapping a chip immediately filters the visible list — no confirmation step, no keyboard.
- Multiple chips can be active simultaneously, combined with AND logic (e.g., `Title = GM` AND `Rating > 2700` narrows to only players matching both).
- Tapping an already-active chip deselects it, restoring the broader result set.
- If a combination of active chips returns zero results, the system shows a clear empty state ("No players match these filters") with a one-tap "Reset Filters" action, rather than leaving the user staring at a blank list.

**Rationale:** Directly resolves N27 and the failed searches P10 experienced when typing "FM" or a numeric rating into a name-only field; also matches the single most-selected support option from the survey (Q17 — "filters by event/date/player," chosen by 31 of 72 respondents, the highest count of any listed option).

**Strengths:** Removes any dependency on remembering or spelling a name correctly — well suited to newcomers like P10, who does not know any specific player's name yet but does know what she's looking for (a title, a rating range); tapping is faster than typing on a mobile keyboard.

**Weaknesses:** Less efficient for a user who already knows the *exact* name they want — a returning core chess follower may still find scanning/selecting chips slower than a direct name search would be; requires careful, compact chip-row design to avoid consuming excessive horizontal space on a small screen.

### 4.5 Comparison

| Criteria | CS2.1: Sticky Search + Flexible Matching | CS2.2: Faceted Filter Chips |
|---|---|---|
| Fixes name-order failures (P06, P09) | Yes — directly, via flexible tokenized matching | Yes — indirectly, by removing the need to type a name at all |
| Supports searching by title/rating (P10) | No | Yes — directly, via dedicated chips |
| Entry point reachability | Full-width bar at top; wide target reduces the precision-reach problem of the old corner icon, though vertical reach remains | Chip row sits near page top, below the title; single visible tap, no typing |
| Extends naturally to the News page | Requires separate keyword-search logic for articles | Yes — via event/date chips, same mechanism as Rating |
| Best suited for | Users who know the exact or approximate name | Users who know an attribute but not a name (e.g., newcomers) |
| Implementation complexity | Low-Medium (matching-logic upgrade) | Medium (multi-select filter state + combination logic) |

---

## 5. Problem 3 — P-05: Schedule does not provide enough information, forcing users to look elsewhere for this information.

### 5.1 Problem Restated

The Schedule Tab shows only the date and location of where the next event will occur. This lacks a lot of information that an actual interested person would probably want. For example: Time of the matches, how many matches, who is playing, potential big name players, format, style. It also lacks a calendar option to have a big view of the time line of all the events in a period of time. It also doesn't show any item in the past, only now/soon/future.

### 5.2 Evidence Base

N20, N21, N24, N28, N29; interview observations from P02 (misleading expand icon, two ambiguous exit controls on the current Schedule overlay) and P10 (non-tappable banners, broken scroll boundary hiding content). The core information-depth complaint — insufficient match/tournament detail — comes from P09 alone, with no supporting survey question or other participant reporting it directly. By the group's own Priority Matrix rubric (`06-PA2-UserAnalysis.md`, P-05), this yields a low score (10/20). The group nonetheless carries the problem into this proposal because P09, unlike most other participants, is a self-identified active chess follower who deliberately searched the Schedule page, the tournament's own info page, and even an external link looking for match brackets and pairings before giving up — behavior indicative of a dedicated, retention-relevant user rather than a casual first-time visitor. This qualitative weight is judged to outweigh the low frequency score for the purposes of this proposal, though the group is explicit that this is a smaller, less-validated problem than P-01 and P-02.

### 5.3 Solution CS3.1 — Additional important information popup

**Concept summary:** Right now there are 2 rows, events that will soon happen and past events. Keep them the same, but should add additional information on a popup. 

**Layout specification:** A new box will cover the item, holding imporant information. For past events, it will be the top 3. For upcoming events it should be who are (some of) the big names that will be playing.

**Interaction rules:** Clicking on "Read more" will lead the user to the normal page dedicated to that section as usual. If they click inside the box but not the "Read more", the new box appears, click anywhere on it again to close it, or click "Read more" directly to move on.

**Rationale:** Usually for most decided chess players, they have someone they follow, usually a national top player, or the top of the world. And showing who is playing or who won draws more interests. Keeping the row layout the same also keep the user who is already familiar to the site feel like the site added an additional tool instead of needing to relearn.

**Strengths:** Familiar layout for those who are dedicated users. The box is easy to make appear. Users also tend to not click directly on texts but rather the region around it, expecting the same action to happen, this clarify the difference between the box and the button.

**Weaknesses:** The page remains rows of items, most people expect a schedule to look like a timeline or a calendar looking place. This can slow learning for new users.

### 5.4 Solution CS3.2 — Interactive Chess Schedule Calendar

**Concept Summary:**

The proposed solution redesigns the Schedule feature as a dedicated calendar page for viewing and exploring chess matches. The chevron-down icon beside the Schedule tab will be removed because it incorrectly suggests that a dropdown menu will appear. Selecting the Schedule tab will instead navigate users to a full page, matching their expectation of how a primary navigation tab behaves.

The new page will use a familiar calendar metaphor similar to the real-world calendar. It will organize previous and upcoming chess matches by date and allow users to browse schedules, inspect event summaries, open expanded schedule cards, and navigate to detailed match pages.

The calendar highlights the current date, for example, August 2, 2026. When the current date is outside the visible area, a directional indicator helps users locate it: a downward arrow appears at the bottom when the current date is below the visible calendar position, while an upward arrow appears at the top when it is above. Users can touch over the arrow to go back to the current date area.

**Layout Specification:**

* **Schedule navigation tab:** Remove the chevron-down icon. Selecting the tab navigates directly to the Schedule page.

* **Calendar header:** Display the currently selected date range, such as the current week, month, or year. Controls may be provided for changing the calendar view.

* **Date selection input:** Allow users to select a specific date and immediately move the calendar to that period.

* **Search bar:** Allow users to search by location, match, tournament, or chess player. Search results should indicate when the corresponding match will be played or when it was played.

* **Calendar area:** Present matches according to their dates and times. Users can swipe vertically to view previous or future weeks, months, and years.

* **Schedule items:** Display a concise summary for each event, including its start time, match name, and location. Visual styling should make each item clearly distinguishable from ordinary calendar text.

* **Expanded schedule card:** When a schedule item is selected, expand it into a card containing additional information, such as:

  * Date and time
  * Location
  * Chess players
  * Tournament
  * Match status
  * Short description
  * Detail button

* **Match detail page:** The Detail button navigates users to a separate page containing complete information about the match, players, tournament, and other related content.

**Interaction Rules:**

1. When users select the Schedule tab, the application navigates to the dedicated Schedule page.

2. Users can swipe upward to view previous time periods and downward to view upcoming time periods.

3. Users can use the date input to jump directly to a specific date instead of swiping through the calendar.

4. Users can enter a location, match, tournament, or player name in the search bar. The calendar then displays or highlights matching events.

5. When users touch a schedule item, it provides visual feedback and expands into a summary card without leaving the Schedule page.

7. Selecting the expanded item again, touching outside it, or opening another item collapses the current card.

8. When users select another schedule item, the previously expanded card closes and the newly selected item expands. This limits visual clutter.

9. When users select the Detail button, the application navigates to the corresponding match detail page.

10. After users return from the detail page, the calendar should preserve their selected date, scroll position, search query, and expanded event whenever possible.

**Rationale:**

The current interface creates an inaccurate mental model. A chevron-down icon conventionally communicates that selecting the associated element will reveal a dropdown menu or expand content beneath it. However, the existing Schedule tab opens a large overlapping layer that resembles a separate page. This conflict between the visual cue and the resulting behavior can make users uncertain about their current location and how to return to the previous interface.

The overlapping layer also weakens the information hierarchy because it visually covers the current page without clearly behaving as either a dropdown, modal dialog, or full page. Replacing it with explicit page navigation gives the Schedule feature a clear position within the application.

The current schedule presentation relies heavily on text and images. Users must carefully read individual entries to determine when matches occur and how events relate to one another. A calendar organizes the same information spatially and chronologically. Users can therefore recognize match dates and nearby events without processing every line of text.

**Strengths:**

* **Interaction metaphor:** The interface uses a calendar metaphor that users are likely to understand from physical and digital calendars. For example, a user looking for next week’s chess matches can swipe downward and inspect events positioned under the relevant dates.

* **Recognition rather than recall:** Important information is presented within the calendar, so users do not have to remember match dates, player names, or locations while navigating between screens. For example, a user can search for a player and recognize the correct match from its visible date, opponent, and location.

* **Reduced information load:** Schedule items initially display only essential information. Additional details appear only when requested. For example, users can scan several match names and start times without being distracted by full player and tournament descriptions.

* **Visibility of interaction:** Hover, focus, and pressed states make schedule items visibly interactive. For example, when the pointer moves over a match, its background or border changes, indicating that it can be selected.

* **Natural mapping:** Vertical movement corresponds to chronological movement. Scrolling upward shows previous periods, while scrolling downward shows future periods. This resembles browsing through a chronological calendar.

* **Progressive disclosure:** Information is revealed in stages: calendar summary, expanded card, and complete detail page. For example, a user can first identify an interesting match, open its card to check the location, and visit the detail page only when more information is required.

* **Consistency and predictability:** The Schedule tab behaves like other primary navigation tabs by opening a dedicated page. Meanwhile, the Detail button consistently indicates navigation to a more comprehensive view.

* **User control and efficiency:** Users can browse naturally, jump to an exact date, or search directly. For example, a user who knows the tournament date can use the date input, while another user who only knows a player’s name can use search.

* **Clear temporal orientation:** Highlighting the current date and displaying directional indicators when it is outside the visible area helps users maintain awareness of their position in the calendar and quickly return to today.


**Weaknesses:**

If many chess events occur on the same day, the calendar may not have enough space to display every schedule item clearly. This can create visual crowding, increase the height of the date section, or make individual events difficult to distinguish. A possible future improvement would be to show a limited number of events followed by a “View more” indicator, but this introduces an additional interaction and may hide information from immediate view.

### 5.5 Comparison

| Criteria                     | CS3.1 — Additional Information Popup                                                                                           | CS3.2 — Interactive Chess Schedule Calendar                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **Core approach**            | Preserves the existing two-row layout and adds expandable information boxes.                                                   | Replaces the existing schedule interface with a dedicated calendar page.                                                   |
| **Navigation behavior**      | Keeps the current navigation behavior and uses the existing **Read more** link to open a section page.                         | Removes the misleading chevron-down icon and makes the Schedule tab navigate to a dedicated page.                          |
| **Information organization** | Separates upcoming and past events into two rows.                                                                              | Organizes previous and upcoming matches chronologically by date and time.                                                  |
| **Additional information**   | Shows notable players for upcoming events and the top three players or results for past events.                                | Shows time, location, players, tournament, status, and description in an expanded event card.                              |
| **Primary interaction**      | Users touch an event region to open or close its information box.                                                              | Users touch a schedule item to expand it into a detailed summary card.                                                     |
| **Detail navigation**        | Users touch **Read more** to navigate to the existing section page.                                                            | Users touch **Detail** to navigate to the corresponding match detail page.                                                 |
| **Time navigation**          | Users browse events through the existing upcoming and past rows.                                                               | Users swipe vertically to explore previous or future weeks, months, and years.                                             |
| **Date selection**           | Does not provide direct date selection.                                                                                        | Provides a date input for jumping directly to a specific date.                                                             |
| **Search support**           | Does not introduce a new search function.                                                                                      | Allows users to search by match, tournament, location, or chess player.                                                    |
| **Current-date awareness**   | Does not indicate the current date.                                                                                            | Highlights the current date and displays a directional arrow when it is outside the visible area.                          |
| **Interaction metaphor**     | Uses an expandable information box while retaining the existing event-list metaphor.                                           | Uses the familiar metaphor of a real-world calendar.                                                                       |
| **Mental model**             | Requires minimal adjustment for existing users because the original layout remains unchanged.                                  | Creates a clearer mental model by making the Schedule tab and calendar behave as users expect.                             |
| **Recognition support**      | Highlights notable players and winners to attract attention and help users recognize important events.                         | Displays events within their chronological context, reducing the need to remember dates and related information.           |
| **Information load**         | Adds useful information but may make existing rows visually denser.                                                            | Uses progressive disclosure by showing a summary first, an expanded card second, and a detail page last.                   |
| **Visibility and feedback**  | The event region responds to touch by revealing an information box.                                                            | Schedule items provide visual feedback when touched and visibly expand into cards.                                         |
| **Natural mapping**          | Has limited mapping between user movement and chronological navigation.                                                        | Maps vertical swiping to chronological movement through previous and future periods.                                       |
| **Learnability**             | Easy for existing users because it preserves the familiar interface. New users may not immediately recognize it as a schedule. | Easier for new users because the calendar structure communicates its purpose more clearly.                                 |
| **Implementation effort**    | Lower because it extends the current interface without substantially changing its structure.                                   | Higher because it requires a calendar interface, search, date selection, expanded cards, and state preservation.           |
| **Main strength**            | Maintains familiarity while making important players and results easier to discover.                                           | Provides clearer navigation, stronger HCI metaphors, better temporal orientation, and more efficient schedule exploration. |
| **Main weakness**            | The row-based interface does not strongly resemble a schedule, timeline, or calendar.                                          | Many events on the same day may cause visual crowding and limited display space.                                           |


## 6. Summary

First 2 problems are addressed within the same overall concept — a responsive mobile website redesigned around thumb-zone accessibility and always-available information retrieval — while each is given two meaningfully distinct conceptual solutions rather than superficial variations of one idea. This gives the team a genuine basis for comparison before committing to a single direction for prototyping. Final problem address the main information issue present with the Schedule tab, most user that actually uses this tab are dedicated to chess content enough to follow past and upcoming events, the change proposed will give more information that still matters without overloading the users.