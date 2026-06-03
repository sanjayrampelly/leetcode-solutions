# LeetCode Solutions

A personal collection of LeetCode problem solutions, organised one problem per
folder and written primarily in Python, with a few SQL and JavaScript answers
mixed in.

## Structure

Each problem lives in its own folder named `<problem-id>-<slug>/`. Inside, you
will find:

- `README.md` — the official LeetCode problem statement (HTML).
- `<slug>.py` (or `.sql` / `.js`) — the solution.
- `Notes.md` — optional notes when a problem deserved them.

For example:

```text
1-two-sum/
├── README.md
└── two-sum.py
```

## Languages

| Language   | Used for                                        |
| ---------- | ----------------------------------------------- |
| Python 3   | Most problems (default)                         |
| SQL        | Database problems (`176`, `1301`, `1948`, etc.) |
| JavaScript | "30 Days of JavaScript" track problems          |

## Topics covered

- Arrays and hashing
- Two pointers and sliding window
- Binary search
- Stacks and queues
- Linked lists
- Trees and BSTs (DFS / BFS, traversal variants)
- Bit manipulation
- Basic dynamic programming

## Running a solution

The solutions are written to match the LeetCode runner: each file defines a
`Solution` class with the required method. To run one locally, paste the
class into a small driver:

```python
from importlib import import_module

mod = import_module("1-two-sum.two-sum")
print(mod.Solution().twoSum([2, 7, 11, 15], 9))  # -> [0, 1]
```

(The hyphenated folder names mean direct `import` does not work; use the
LeetCode site, or copy the class into a fresh file.)
