from flib import Flib
import pytest


@pytest.fixture
def setup():
    return Flib("111111111111"), Flib("000000000000")


def test_crossover(setup):
    parent_flib, mate_flib = setup

    for _ in range(100):
        child_flib = parent_flib.crossover(mate_flib)
        assert (
            0
            < sum(v == "1" for v in child_flib.chromosome_string)
            < child_flib.chromosome_length
        )
        assert (
            0
            < sum(v == "0" for v in child_flib.chromosome_string)
            < child_flib.chromosome_length
        )
        # There should be a run of 1s, followed by a run of 0s, followed by another run of 1s
        assert -1 == child_flib.chromosome_string.find(
            "0",
            child_flib.chromosome_string.find(
                "1", child_flib.chromosome_string.find("0")
            ),
        )
