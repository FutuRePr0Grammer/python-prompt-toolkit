#!/usr/bin/env python
"""
Autocompletion example.

Press [Tab] to complete the current word.
- The first Tab press fills in the common part of all completions
    and shows all the completions. (In the menu)
- Any following tab press cycles through all the possible completions.
"""
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

test_completer = WordCompleter(
    [
        "author:",
        "title()"
    ],
    ignore_case=True,
    move_back_one_space=True,
)


def main():
    text = prompt(
        "Begin typing author or title to autocomplete: ", completer=test_completer, complete_while_typing=False
    )
    print("You said: %s" % text)


if __name__ == "__main__":
    main()
