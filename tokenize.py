import re

the_input='( 3.5 + (2*5))'
tokens = []
tokenizer = re.compile(r'\s*([()+*/-]|\d+)')
current_pos = 0
while current_pos < len(the_input):
  match = tokenizer.match(the_input, current_pos)
  if match is None:
     raise Error('Syntax error')
  tokens.append(match.group(1))
  current_pos = match.end()
print(tokens)