import re


id = "([a-zA-Z_][a-zA-Z_0-9]*)"
op = r'((==)|(!=)|(>)|(<)|(>=)|(<=))'
number = '[0-9]+'
conif = r'((\&\&)|(\|\|))'


fa = rf'(({id}|{number})\s*{op}\s*({id}|{number}))'

pattern = rf'if\s*\(\s*{fa}\s*({conif}\s*{fa}\s*)*\)'

pattern = re.compile(pattern)

print(pattern.match("if( i == 6 )"))
# print(pattern.match(input("enter con: ")))
