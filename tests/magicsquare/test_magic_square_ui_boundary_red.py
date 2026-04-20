"""UI / boundary RED skeleton — Magic Square 4×4 (dual-track, pytest)."""

from __future__ import annotations

import pytest

from magicsquare.boundary import validate
from magicsquare.constants import MATRIX_SIZE


class TestMagicSquareUiBoundaryRed:
    """Track A — UI RED (§6.2). Methods intentionally fail until GREEN."""

    def test_ui_red_01_non_four_by_four_raises(self) -> None:
        too_few_rows = [[0] * MATRIX_SIZE for _ in range(MATRIX_SIZE - 1)]
        with pytest.raises(ValueError):
            validate(too_few_rows)

        wrong_row_width = [[0] * (MATRIX_SIZE - 1) for _ in range(MATRIX_SIZE)]
        with pytest.raises(ValueError):
            validate(wrong_row_width)

    def test_ui_red_02_blank_count_not_two_raises(self) -> None:
        pytest.fail("RED")

    def test_ui_red_03_value_out_of_range_raises(self) -> None:
        pytest.fail("RED")

    def test_ui_red_04_duplicate_non_zero_raises(self) -> None:
        pytest.fail("RED")

    def test_ui_red_05_solution_returns_length_six(self) -> None:
        pytest.fail("RED")

    def test_ui_red_06_solution_coords_are_one_indexed(self) -> None:
        pytest.fail("RED")
