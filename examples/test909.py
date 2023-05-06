from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

mycompleter = WordCompleter(['reeeeeeeeeallyreallyreallyreallylong.word.test.completion_test_trying_to_add_ellipsis123456763322323243asdfasdsdf323232',
                             'AUTO_COMPLETE_A_VERY_LONG_STRING_BECAUSE_SOMETIMES_THIS_HAPPENSAUTO_COMPLETE_A_VERY_LONG_STRING_BECAUSE_SOMETIMES_THIS_HAPPENSAUTO_COMPLETE_A_VERY_LONG_STRING_BECAUSE_SOMETIMES_THIS_HAPPENS2'
                             'reallytestshortstring', 'testunrelatedstring',
                             'welcome to the test!', 'wow this is fun', 'wonderful ways to win'])

text = prompt('prompt: ', completer=mycompleter)
print('You said: %s' % text)