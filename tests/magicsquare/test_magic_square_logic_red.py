"""Logic RED skeleton — Magic Square 4×4 (dual-track, pytest)."""

from __future__ import annotations

import pytest

from magicsquare.domain import find_blank_coords

# PRD §9.3 — TQ-01 (정상 복원)
_TQ_01: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]


class TestMagicSquareLogicRed:
    """Track B — Logic RED (§6.3). Methods intentionally fail until GREEN."""

    def test_log_red_01_find_blank_coords_row_major_two_cells(self) -> None:
        # TQ-01: row-major에서 첫 0은 (3,3), 둘째는 (4,4) — §9.3 행렬 리터럴 기준
        first, second = find_blank_coords(_TQ_01)
        assert first == (3, 3)
        assert second == (4, 4)
        assert first != second

    def test_log_red_02_find_not_exist_nums_two_sorted_ascending(self) -> None:
        pytest.fail("RED")

    def test_log_red_03a_is_magic_square_false_when_only_rows_match(self) -> None:
        pytest.fail("RED")

    def test_log_red_03b_is_magic_square_false_when_only_cols_match(self) -> None:
        pytest.fail("RED")

    def test_log_red_03c_is_magic_square_false_when_diagonal_wrong(self) -> None:
        pytest.fail("RED")

    def test_log_red_03d_is_magic_square_true_for_known_complete(self) -> None:
        pytest.fail("RED")

    def test_log_red_04a_solution_returns_six_elements_ordered(self) -> None:
        pytest.fail("RED")

    def test_log_red_04b_solution_coords_one_indexed_in_range(self) -> None:
        pytest.fail("RED")

    def test_log_red_04c_solution_reverse_policy_after_small_first_fails(self) -> None:
        pytest.fail("RED")

    def test_log_red_04d_solution_numbers_match_find_not_exist_nums(self) -> None:
        pytest.fail("RED")
