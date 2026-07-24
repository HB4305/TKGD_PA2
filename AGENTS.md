# Repository Guidelines

## Project Structure & Module Organization

This repository contains PA2 UI/UX research deliverables for the Freestyle Chess mobile web study. Root-level Markdown files are primary submissions, such as `06-PA2-UserResearch.md` and `06-PA2-UserResearch-Questionnaire.md`. Supporting research materials live in `docs/`, including the moderator script, observation sheet, pilot checklist, and task-analysis PDF. Source evidence and handoff artifacts include the Google Forms CSV export and `PA2-LKDuy-2026-Public.pdf`.

## Build, Test, and Development Commands

There is no application build system or package manager configuration in this repo. Use lightweight document checks instead:

- `rg --files` lists tracked project files quickly.
- `rg "term" docs 06-PA2-UserResearch.md` searches research notes and supporting materials.
- Open Markdown files in a previewer before submission to verify headings, tables, and links render correctly.

If adding code or scripts later, include the required commands in this section and commit the relevant config file, such as `package.json`, `Makefile`, or test runner settings.

## Coding Style & Naming Conventions

Use Markdown for written deliverables. Keep headings sentence-style and descriptive, use pipe tables for structured observation data, and keep participant IDs anonymous with patterns such as `P01`, `P02`, and `P03`. Prefer concise file names that describe the artifact and use kebab-case for new files under `docs/`, for example `freestyle-chess-mobile-summary.md`.

For Vietnamese content, keep terminology consistent across the questionnaire, moderator script, observation sheet, and final report. Do not rename existing deliverables unless every internal reference is updated.

## Testing Guidelines

No automated tests are currently defined. Before submitting changes, manually verify that Markdown tables align, images or linked files exist, CSV data remains intact, and PDFs are not corrupted. For research updates, cross-check claims against the questionnaire, observation notes, and response CSV.

## Commit & Pull Request Guidelines

Recent commits use short, lowercase conventional-style messages such as `docs: add user research`. Continue using `docs: ...` for document changes and choose a precise summary, for example `docs: revise pilot checklist`.

Pull requests should describe the changed research artifact, explain why the update was made, and mention any affected source evidence or PDFs. Include screenshots only when visual formatting, exported slides, or rendered Markdown tables need review.

## Agent-Specific Instructions

Keep edits focused on the requested deliverable. Preserve existing Vietnamese text, participant anonymity, file names, and raw survey exports unless the user explicitly asks for cleanup or translation.
