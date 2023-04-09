import re


id = "[a-zA-Z_][a-zA-Z_0-9]*"
op = r'((==)|(!=)|(>)|(<)|(>=)|(<=))'
number = '[0-9]+'
# ifc = rf'if\({}'

pattern = rf'(if\s*\(\s*{id+op+id}\s*\))|(if\s*\(\s*{id+op+number}\s*\))|(if\s*\(\s*{number+op+number}\s*\))|(if\s*\(\s*{number+op+id}\s*\))'

pattern = re.compile(pattern)

print(pattern.match("if (  4==4)"))
