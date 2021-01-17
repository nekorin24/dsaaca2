import re
test =  "(-1--10)"

test = test.replace(" ",'')
# a1 = test.split()
# number_or_symbol = re.compile('(\w+|[()\-+*/^])')
# re1 = "\w"
# decimal
# re2 = "[-+]?\d*\.\d+|\d"
# re3 = "[()\-+*/^]"
# number_or_symbol = re.compile("^([-+/*]\d+(\.\d+)?)*")
number_or_symbol = re.compile('([-+]?\d+\.\d+|[-]?[0-9]+|[**]+|[()\-+*/^])')
# number_or_symbol = re.compile('[-+]?\d*\.\d+|[0-9]')
a1 = re.findall(number_or_symbol, test)
# a1 = test.split("(?<=[-+*/])|(?=[-+*/])")
# a1 = [x for x in a1 if x!=' ']
print(a1)