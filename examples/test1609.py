from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt

mycompleter = WordCompleter(['-a', '-app', '--apple', '--apricot' ,'build', 'builder', 'buildx'])

text = prompt('prompt: ', completer=mycompleter)
print('You said: %s' % text)
