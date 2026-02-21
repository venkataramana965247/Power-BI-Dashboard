# Copilot & AI Agent Instructions for Data teach.ai (Python examples)

Summary
- This repository is a small collection of teaching Python scripts under the top-level `python/` folder. Files are self-contained examples (loops, functions, pattern printing, I/O) and usually contain commented-out variants and explanation blocks.

What an AI assistant should know (big picture)
- Project layout is flat: all example programs live in `python/` and are independent script files (no package, no tests, no CI).
- Files are typically named with a date and a short topic (examples: `functions 16-12-25.py`, `data teach 15-12-25.py`, `slicing concept 19-12-25.py`). Filenames may include spaces—use quotes when running them from a shell.
- Most scripts rely only on the Python standard library; do not introduce external dependencies without asking the repo owner.

Editing & change guidelines (be conservative)
- Preserve commented examples and docstrings: these are teaching material and valuable context. Avoid deleting or reformatting large commented blocks without confirmation.
- Prefer adding new files for experimental changes (e.g., `python/21-12-25 <topic>-refactor.py`) rather than editing many examples in place.
- Keep changes minimal and focused: small refactors (name fixes, small bug fixes, add helper functions) are OK; major refactors or adding packages require explicit confirmation.

How to run & test locally (Windows notes)
- Run individual scripts from PowerShell or another terminal: python "python/slicing concept 19-12-25.py"
- Because filenames include spaces, always quote filenames when invoking from the shell.
- There are no automated tests; to verify changes, run the relevant script and check stdout manually.

Workspace additions (autocomplete helper)
- I added a workspace `.vscode/settings.json` with recommended autocomplete settings and `.vscode/extensions.json` recommending `ms-python.python`, `ms-python.vscode-pylance`, and `GitHub.copilot`.
- A small example file `python/test_autocomplete_example.py` is included to exercise type hints, docstrings, and typical patterns used in the repo.

Patterns & coding conventions observed
- Examples use `print()` and `f-strings` heavily (e.g., `print(f"{n} * {i}= {n*i}")`). Match this style when adding examples.
- Teaching pattern: code often contains multiple variations in commented sections; new variations should follow the same commenting style and include short explanation comments.
- Input usage: some scripts use `input()` for interactive runs. When adding non-interactive examples, prefer parameterized functions that can be called from a simple test harness.

Examples for the agent to reference
- `python/functions 16-12-25.py`: multiple function examples covering required/default/keyword/varargs patterns — use these as canonical examples of function-style teaching.
- `python/data teach 15-12-25.py`: pattern printing and loop examples — good for loop-based test cases and simple output verification.
- `python/slicing concept 19-12-25.py`: slice and list methods examples — demonstrates typical list operations and idioms used across the repo.

When to ask the user
- Before renaming files (especially those with date suffixes) or converting many examples into a module/package.
- Before adding new dependencies, CI, or test frameworks.
- If any change could remove or obscure teaching content (comment blocks, example outputs).

Reporting and PR style
- Keep PRs small and focused; include: (1) summary of change, (2) list of edited files, (3) minimal manual verification instructions (what script to run and expected output).
- If adding a test or example, include a short README line in the `python/` folder explaining how to run it.

Contact & follow-up
- If anything is unclear (naming conventions, whether to convert examples into tests), ask the repo owner before large-scale edits.

---

If you'd like, I can: (1) convert one example into a small testable function and add a minimal test harness, or (2) expand the `python/README.md` with run instructions. Which would you prefer next?