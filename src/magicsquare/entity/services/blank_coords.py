"""Row-major blank cell discovery for 4×4 Magic Square grids."""

from __future__ import annotations


def find_blank_coords(grid: list[list[int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the two ``0`` cells in 1-based row-major order.

    Preconditions (caller-validated): ``grid`` is 4×4 and contains exactly
    two cells with value ``0``.

    Returns:
        ``((r1, c1), (r2, c2))`` where ``(r1, c1)`` is the first zero in
        row-major scan (rows 1→4, cols 1→4), and ``(r2, c2)`` is the second.

    """
    found: list[tuple[int, int]] = []
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 0:
                found.append((r + 1, c + 1))
    return (found[0], found[1])
