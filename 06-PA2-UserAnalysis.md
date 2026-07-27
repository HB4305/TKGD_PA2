# PA2 Report - Requirement 2: User Analysis

**Group:** 06  
**Course:** CSC13112 - UI/UX Design  
**Assignment:** Project Assignment 2  
**Product Scope:** Freestyle Chess mobile website on smartphone browser  
**Document Purpose:** User problem identification, idea generation, affinity diagramming, and problem prioritization  

---

## 1. Overview & Brainstorming Setup

### 1.1 Objectives
The goal of this phase is to analyze the empirical evidence collected from Requirement 1 (72 survey responses and 13 direct interview sessions), brainstorm to identify core user problems, generate potential solution ideas, organize them using an **Affinity Diagram**, and prioritize the most severe problems to solve in the subsequent design proposal.

### 1.2 Brainstorming Session Record

| Field | Details |
|---|---|
| **Date & Time** | July 23, 2026 |
| **Participants** | Group 06 Members (Lê Mai Hoài Bảo, Trương Công Thiên Phú, Lâm Hữu Khánh, Phạm Chí Bảo Ninh, Phùng Ngọc Tuấn) |
| **Tool Used** | Digital Sticky Notes via Figma / FigJam |
| **Input Evidence** | `06-PA2-UserResearch.md`, `Khảo sát trải nghiệm người dùng trên Freestyle Chess mobile web (Responses) - Form Responses 1.csv`, Interview clip recordings |
| **Deliverable Output** | Affinity Diagram & Prioritized Problem Matrix |

---

## 2. Affinity Diagram

### 2.1 Visual Affinity Board (Digital Sticky Notes)

Below is the structured Affinity Board generated during the group brainstorming session, grouping user observations, pain points, and potential solution ideas into logical clusters.

> *Note: Embed or link your Miro/Figma/FigJam canvas export image below.*

![Affinity Diagram Board](./docs/artifacts/affinity_diagram.png)  
*(Link to interactive FigJam/Figma board: [FigJam Affinity Diagram Canvas](#))*

---

### 2.2 Raw Sticky Notes Inventory

| Note ID | Category | Source / Evidence | Sticky Note Content |
|---|---|---|---|
| **N01** | Problem | Survey Q12, Interview P01/P02/P03 | Mobile Hamburger menu is placed at top-left, making one-handed thumb interaction painful. |
| **N02** | Problem | Survey Q13 (43.1%), P01 clip | Users must stretch fingers, shift phone grip, or use two hands to tap navigation items. |
| **N03** | Idea | Brainstorm | Move primary navigation to a persistent Bottom Navigation Bar. |
| **N04** | Idea | Brainstorm | Provide a floating action button (FAB) or bottom-right drawer for one-handed reachability. |
| **N05** | Problem | Survey Q09 (3.68/5), P03 clip | Homepage Hero section is cluttered with banners and lacks onboarding explaining Freestyle Chess format to new users. |
| **N06** | Problem | Survey Q10 (52.8% first-timers) | New users feel disoriented and do not understand website purpose upon landing. |
| **N07** | Idea | Brainstorm | Redesign Hero section with a minimalist intro banner, clear onboarding text, and prominent CTA. |
| **N08** | Idea | Brainstorm | Add an interactive "What is Freestyle Chess?" quick modal guide for newcomers. |
| **N09** | Problem | Survey Q16 (3.60/5), P01/P02 clip | Rating leaderboard is an infinite scroll list with no sticky search bar, causing repetitive scrolling. |
| **N10** | Problem | Survey Q19 (61.1%), P04 clip | Users cannot search news/events by keywords and must browse long chronological lists. |
| **N11** | Idea | Brainstorm | Add a Sticky Search Bar fixed at top of long listing pages (Rating, News, Videos). |
| **N12** | Idea | Brainstorm | Provide filter chips (by major event, date, rating range) and auto-suggest search queries. |
| **N13** | Problem | Survey Q21 (52.8%), P03/P09 clip | Video player lacks immediate visual feedback (loading spinner) when tapped, leading to rage clicks. |
| **N14** | Problem | Interview P02/P09 clip | Playing a new video does not pause the previous video, resulting in overlapping audio channels. |
| **N15** | Idea | Brainstorm | Enforce a Single-Player audio/video model (playing new video automatically stops old video). |
| **N16** | Idea | Brainstorm | Add skeleton loaders and loading spinners instantly upon tapping video play controls. |

---

### 2.3 Affinity Cluster Descriptions

#### Cluster A: Ergonomic Navigation & One-Handed Reachability
* **Core Problem:** The current hamburger menu icon is positioned at the top-left corner. On modern smartphone screens, this forces right-handed users (44.4% one-handed users) to stretch their thumb unnaturally or change their grip, increasing device drop risk.
* **Generated Ideas:**
  * Implement a mobile **Bottom Navigation Bar** with key tabs (Home, News, Schedule, Rating, Videos).
  * Place a floating drawer or menu button at the bottom-right corner.

#### Cluster B: Homepage Onboarding & Value Proposition Clarity
* **Core Problem:** 52.8% of surveyed users had never heard of Freestyle Chess. The current homepage Hero section is overloaded with event banners without explaining the unique rules/format of Freestyle Chess, causing cognitive fatigue.
* **Generated Ideas:**
  * Simplify the Hero section hierarchy.
  * Add a prominent onboarding banner with a concise explanation ("Fischer Random / Chess 960 format") and a primary CTA ("Explore Events").

#### Cluster C: Search, Filtering & Information Retrieval
* **Core Problem:** 61.1% of users reported difficulty finding specific info when they don't remember exact names. Long rating lists require 20+ seconds of vertical scrolling without a sticky search bar or pagination.
* **Generated Ideas:**
  * Add a **Sticky Search Bar** that remains visible while scrolling.
  * Implement **Quick Filter Chips** (e.g., "Geller Cup", "Grandmaster Rating") and Auto-suggest queries.

#### Cluster D: Video Player Interactions & Feedback
* **Core Problem:** Tapping video thumbnails provides no loading indicator, causing users to think the site is frozen. Multiple videos can play simultaneously, causing overlapping audio streams.
* **Generated Ideas:**
  * Enforce **Single-Active-Player logic** (auto-pause active video when another starts).
  * Integrate skeleton loaders and instant visual press states.

---

## 3. Problem Prioritization Matrix

To select the most critical problems for the design proposal phase, each identified problem was evaluated on a scale from 1 (Low) to 5 (High) across four criteria:
* **Frequency:** How many users experience this issue?
* **Severity:** How severely does it block task completion or degrade user experience?
* **Evidence Strength:** Quality of quantitative (survey) and qualitative (interview clip) evidence.
* **Feasibility:** Technical ease of solving the problem in a mobile web redesign.

$$ \text{Priority Score} = \text{Frequency} + \text{Severity} + \text{Evidence Strength} + \text{Feasibility} $$

| Problem ID | Problem Description | Frequency (1-5) | Severity (1-5) | Evidence Strength (1-5) | Feasibility (1-5) | Priority Score (4-20) | Decision |
|---|---|---:|---:|---:|---:|---:|---|
| **P-01** | One-handed reachability issues with top-left hamburger menu | 4 | 5 | 5 | 5 | **19** | **Selected (High)** |
| **P-02** | Lack of sticky search & filtering on long listing pages (Rating & News) | 5 | 4 | 5 | 4 | **18** | **Selected (High)** |
| **P-03** | Overlapping video audio streams & lack of loading feedback | 4 | 4 | 5 | 5 | **18** | **Selected (High)** |
| **P-04** | Overloaded Hero section & lack of onboarding for first-time users | 4 | 3 | 4 | 5 | **16** | **Selected (Medium)** |

---

## 4. Final Problem Statements

Based on the synthesis and prioritization matrix above, Group 06 selected the top severe problems to solve in the project proposal:

### Problem Statement 1 (Navigation & Reachability)
> **Mobile users need** an ergonomically reachable navigation system **because** placing critical navigation controls at the top-left corner causes thumb stretching, grip instability, and accidental taps, **especially when** operating the smartphone with one hand on the move.

### Problem Statement 2 (Information Retrieval & Search)
> **Mobile users need** a flexible search and filtering mechanism (sticky search bar and filter chips) **because** browsing long rating leaderboards and chronological news feeds requires excessive vertical scrolling and exact keyword memory, **especially during** quick 2-3 minute mobile browsing sessions.

### Problem Statement 3 (Media Interaction & Feedback)
> **Mobile users need** clear visual feedback during loading and controlled single-video playback **because** unresponsive tap states lead to rage clicks and simultaneous video playback produces confusing overlapping audio, **especially when** viewing match highlights or livestreams.

---

## 5. Conclusion & Transition to Project Proposal

The user analysis phase successfully consolidated the raw empirical data from Requirement 1 into four clear affinity clusters, prioritized the key problems using a structured score matrix, and formulated three final Problem Statements. 

These problem statements will serve as the direct foundation for generating conceptual design solutions in **Requirement 3 (Project Proposal)**.
