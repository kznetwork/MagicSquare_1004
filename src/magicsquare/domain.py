"""Pure domain rules for Magic Square (no UI / IO / framework imports)."""

from __future__ import annotations

from magicsquare.constants import MATRIX_SIZE


def find_blank_coords(grid: list[list[int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the two ``0`` cells in 1-based row-major order.

    Preconditions (caller-validated): ``grid`` is ``MATRIX_SIZE``×``MATRIX_SIZE``
    and contains exactly two cells with value ``0``.

    Returns:
        ``((r1, c1), (r2, c2))`` where ``(r1, c1)`` is the first zero in
        row-major scan, and ``(r2, c2)`` is the second.

    """
    found: list[tuple[int, int]] = []
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            if grid[r][c] == 0:
                found.append((r + 1, c + 1))
    return (found[0], found[1])
