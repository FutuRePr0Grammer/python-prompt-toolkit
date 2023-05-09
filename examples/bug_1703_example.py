#!/usr/bin/env python
# Part of this was provided by the github page for issue #1703 as the demo for it
# I added the clear keybind and fixed the escape keybind

from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings


def dyn_prompt(buf):
    def inner():
        return f"undo: {len(buf._undo_stack)} | redo: {len(buf._redo_stack)}"
    return inner


def main():
    kb = KeyBindings()

    @kb.add("escape", "u")
    def _(event):
        # Prevents undo being used when there is nothing to undo
        if (len(event.current_buffer._undo_stack) > 0):
            event.current_buffer.undo()

    @kb.add("escape", "r")
    def _(event):
        event.current_buffer.redo()

    @kb.add("escape", "c")
    def _(event):
        event.current_buffer.clear()

    print("Try to type some text, then try: Alt-u to undo | Alt-r to redo | Alt-c to clear redo queue")
    s = PromptSession(">", key_bindings=kb)
    s.rprompt = dyn_prompt(s.app.current_buffer)
    try:
        s.prompt()
    except (EOFError, KeyboardInterrupt):
        pass


if __name__ == "__main__":
    main()
