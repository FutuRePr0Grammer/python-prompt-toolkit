from prompt_toolkit import prompt
from prompt_toolkit.widgets import MenuItem

test_menu = MenuItem


def main():
    text = prompt(
        "Begin typing author or title to autocomplete: "
    )
    print("You said: %s" % text)


if __name__ == "__main__":
    main()
