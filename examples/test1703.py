from __future__ import annotations

import pytest
from keyboard import press_and_release

from prompt_toolkit.buffer import Buffer


@pytest.fixture
def _buffer():
    buff = Buffer()
    return buff

def _(event):
    event.current_buffer.undo()

def test_single_redo(_buffer):
    _buffer.save_to_undo_stack("T")
    _buffer.save_to_undo_stack("T")


    assert _buffer._undo_stack == "T"

    # Because of the issue of the problem (Keystrokes resetting redo stack in key_processor), A manual test is required
    # to test if the issue is fixed. Simply inserting into the stack would have passed a test before my fix