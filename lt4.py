import re


id = "([a-zA-Z_][a-zA-Z_0-9]*)"
op = r'((==)|(!=)|(>)|(<)|(>=)|(<=))'
cond = rf"((&&)|(||))"
number = '[0-9]+'

barc = '(\s*{\s*.*\s*\}\s*)'
# ifc = rf'if\({}'

pattern = r"(if\s*\(\s*"+id+op+id+r"\s*\)"+barc+")|(if\s*\(\s*"+id+op+number + \
    r"\s*\)"+barc+")|(if\s*\(\s*"+number+op+number + \
    r"\s*\)"+barc+")|(if\s*\(\s*"+number+op+id+r"\s*\)"+barc+")"
elsepa = r"(else\s*\{\s*.*\s*\}\s*)"
else_if = rf"(else\s* {pattern})"

# print(else_if)
pt = pattern + else_if + elsepa

final = re.compile(pt)

# print(final)
# a = input()
print(final.match("if(i<10) {das} else if (i<10) {ada} else {gjadsf}"))
