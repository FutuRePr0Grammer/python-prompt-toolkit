from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

mycompleter = WordCompleter(['-a', '-app', '--apple', '--apricot' ,'build', 'builder', 'buildx'], move_back_one_space=False)

text = prompt('prompt: ', completer=mycompleter)
print('You said: %s' % text)
