"""Boundary: input validation and orchestration hooks (no PyQt here)."""

from __future__ import annotations

from magicsquare.constants import MATRIX_SIZE


def validate(grid: list[list[int]]) -> None:
    """Reject grids whose shape is not ``MATRIX_SIZE``×``MATRIX_SIZE``.

    Raises:
        ValueError: If the matrix is not square of the required size.

    """
    if len(grid) != MATRIX_SIZE:
        raise ValueError(
            f"grid must have {MATRIX_SIZE} rows, got {len(grid)}",
        )
    for i, row in enumerate(grid):
        if len(row) != MATRIX_SIZE:
            raise ValueError(
                f"row {i} must have {MATRIX_SIZE} columns, got {len(row)}",
            )
