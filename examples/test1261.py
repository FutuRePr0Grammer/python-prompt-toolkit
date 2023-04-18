from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

parenthesis_test_completer = WordCompleter(
    [
        # This can be a list of functions for an IDE, but for simplicity just these two are used for demos
        "dir",
        "print",
    ],
    ignore_case=True,
    # Removing move_back_one_space=True allows for a preview of the word you are autofilling but puts cursor at end not
    # between parenthesis
    move_back_one_space=True,
    isFunction=True,
)


def main():
    text = prompt(
        "Type part of function print or dir name then autocomplete: ", completer=parenthesis_test_completer, complete_while_typing=False
    )


if __name__ == "__main__":
    main()