import pytest
from chromosome import Chromosome
from collections import namedtuple

TableEntry = namedtuple("TableEntry", ["state", "input", "entry"])


@pytest.fixture
def setup():
    c = Chromosome("111202011000")

    expected_table_entries = [
        TableEntry("0", "0", "11"),
        TableEntry("0", "1", "12"),
        TableEntry("1", "0", "02"),
        TableEntry("1", "1", "01"),
        TableEntry("2", "0", "10"),
        TableEntry("2", "1", "00"),
    ]
    return (c, expected_table_entries)


def test_table_entry(setup):
    c, expected_table_entries = setup
    for expected_table_entry in expected_table_entries:
        c.current_state = expected_table_entry.state
        assert c.get_table_entry(expected_table_entry.input) == expected_table_entry.entry


def test_output_entry(setup):
    c, expected_table_entries = setup
    for expected_table_entry in expected_table_entries:
        c.current_state = expected_table_entry.state
        assert c.get_output(expected_table_entry.input) == expected_table_entry.entry[0]


def test_next_state(setup):
    c, expected_table_entries = setup
    for expected_table_entry in expected_table_entries:
        c.current_state = expected_table_entry.state
        assert c.get_nextstate(expected_table_entry.input) == expected_table_entry.entry[1]


def test_state_transition(setup):
    c, expected_table_entries = setup
    assert c.current_state == "0"
    sequence = [["0", 0], ["0", 2], ["1", 5], ["1", 1]]
    for input_val, table_idx in sequence:
        output = c.transition(input_val)
        expected_table_entry = expected_table_entries[table_idx]
        print(f"{expected_table_entry = }")
        assert c.current_state == expected_table_entry.entry[1]
        assert output == expected_table_entry.entry[0]
