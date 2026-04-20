"""UI / boundary RED skeleton — Magic Square 4×4 (dual-track, pytest)."""

from __future__ import annotations

import pytest


class TestMagicSquareUiBoundaryRed:
    """Track A — UI RED (§6.2). Methods intentionally fail until GREEN."""

    def test_ui_red_01_non_four_by_four_raises(self) -> None:
        pytest.fail("RED")

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
