import random
import time
import pytest
from check2List import areEqual


def test_areEqual_identical():
    assert areEqual([1, 2, 3], [1, 2, 3]) is True


def test_areEqual_permuted():
    assert areEqual([3, 5, 2, 5, 2], [2, 3, 5, 5, 2]) is True


def test_areEqual_different_lengths():
    assert areEqual([1, 2], [1, 2, 3]) is False


def test_areEqual_different_frequencies():
    assert areEqual([1, 1, 2], [1, 2, 2]) is False


def test_areEqual_disjoint():
    assert areEqual([1, 2, 3], [4, 5, 6]) is False


def test_areEqual_empty():
    assert areEqual([], []) is True


def test_areEqual_performance():
    # Construct large arrays of size N = 1,000,000
    arr1 = list(range(500000)) * 2
    arr2 = list(arr1)
    random.seed(42)
    random.shuffle(arr2)

    start_time = time.perf_counter()
    result = areEqual(arr1, arr2)
    elapsed = time.perf_counter() - start_time

    assert result is True
    # Pure Python loop implementation takes > 0.6 seconds.
    # C-optimized Counter implementation takes < 0.2 seconds.
    assert (
        elapsed < 0.40
    ), f"areEqual took {elapsed:.4f} seconds, expected < 0.40s (optimized Counter implementation required)"