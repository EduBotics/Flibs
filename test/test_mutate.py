from flib import Flib
import pytest


@pytest.fixture
def setup():
    return Flib("111202011000")


def test_mutate(setup):
    flib = setup
    for _ in range(100):
        c = flib.chromosome_string
        flib.mutate()
        new_c = flib.chromosome_string
        assert sum([old_val != new_val for old_val, new_val in zip(c, new_c)]) == 1


def test_mutate_output_locus(setup):
    flib = setup
    for _ in range(100):
        c = flib.chromosome_string
        flib.mutate()
        new_c = flib.chromosome_string
        output_loci = list(zip(c, new_c))[::2]
        selector = [old_val != new_val for old_val, new_val in output_loci]
        if any(selector):
            (o, n) = [locus for locus, t in zip(output_loci, selector) if t][0]
            assert o in ["0", "1"] and n in ["0", "1"] and o != n
