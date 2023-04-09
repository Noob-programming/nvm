import re


id = "[a-zA-Z_][a-zA-Z_0-9]*"
op = r'((==)|(!=)|(>)|(<)|(>=)|(<=))'
number = '[0-9]+'

pattern = rf'({id+op+id})|({id+op+number})|({number+op+number})|({number+op+id})'
# print(pattern)
pattern = re.compile(pattern)
x = '8>=8'
print(pattern.match(x))
