# Sequential Calculator

A simple interactive calculator written in Python. It lets you enter a full arithmetic expression, evaluate it, and continue calculating from the result.

---

## Overview

The calculator prompts the user to enter a full arithmetic expression (e.g. `9+8*10/4`). The expression is stored as a string. When the user types `=`, the expression is evaluated and the result becomes the new starting value for the next calculation.

- Enter a full expression in one line, then evaluate with `=`
- Each result continues into the next calculation
- Uses Python's built-in `eval()` — no external parsing library
- Handles errors like division by zero and invalid input

---

## Features

- Enter a full arithmetic expression in one line
- Evaluate on demand by typing `=`
- Sequential chaining — each result feeds the next calculation
- Supports full arithmetic: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Special commands:
  - `=` — evaluate the current expression
  - `c` — clear and start over
  - `q` — quit the program
- Friendly error messages for division by zero and invalid input

---

## Requirements

- Python 3.6+
- No third-party libraries
