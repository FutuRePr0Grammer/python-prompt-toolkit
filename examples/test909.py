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
from prompt_toolkit.layout import CompletionsMenu

test_completer = WordCompleter(
    [
        "author:",
        "title()",
        "AUTO_COMPLETE_A_VERY_LONG_STRING_BECAUSE_SOMETIMES_THIS_HAPPENS",
        "12345678910",
        "1234567",
        "12345678"
    ],
    ignore_case=True,
    move_back_one_space=False,
)


# trim_text = CompletionsMenu(
#    max_width=8
# )


def main():
    text = prompt(
        "Begin typing author or title to autocomplete: ", completer=test_completer, complete_while_typing=True)
    print("You said: %s" % text)


if __name__ == "__main__":
    main()

