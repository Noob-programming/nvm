import re

id = "[a-zA-Z_][a-zA-Z_0-9]*"
op = r'((==)|(!=)|(>)|(<)|(>=)|(<=))'
number = '[0-9]+'
conif = r'((\&\&)|(\|\|))'
barc = '(\s*{\s*.*\s*\}\s*)'
pattern = rf'(if\s*\(\s*(({id}|{number})\s*{op}\s*({id}|{number})\s*({conif}\s*({id}|{number})\s*{op}\s*({id}|{number}))*\s*)\){barc})'

pattern = re.compile(pattern)

print(pattern.match("if( i == 6 && j == 8 ) { }"))
