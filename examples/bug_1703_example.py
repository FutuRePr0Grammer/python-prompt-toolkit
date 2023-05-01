#!/usr/bin/env python

from prompt_toolkit import PromptSession
from prompt_toolkit.key_binding import KeyBindings


def dyn_prompt(buf):
    def inner():
        #print("This is the undo")
        #print(buf._undo_stack)
        #print("This is the redo")
        #print(buf._redo_stack)
        return f"undo: {len(buf._undo_stack)} | redo: {len(buf._redo_stack)}"
    return inner


def main():
    kb = KeyBindings()

    @kb.add("escape", "u")
    def _(event):
        event.current_buffer.undo()
        #print(event.current_buffer)

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
