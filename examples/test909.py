from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

mycompleter = WordCompleter(['reeeeeeeeeallyreallyreallyreallylong.word.test.completion_test_trying_to_add_ellipsis123456763322323243asdfasdsdf323232',
                             'reallytestshortstring', 'testunrelatedstring'])

text = prompt('prompt: ', completer=mycompleter)
print('You said: %s' % text)