import re
txt = input("enter string:")
id = '([a-zA-Z_])([a-zA-Z0-9_])*'
num = '(([-|+]?\d+)|([-|+]?\d+\.)|([-|+]?\.\d+)|([-|+]?\d+\.\d+))'
num1 = '(\d+)'
op = '((<)|(>)|(==)|(!=)|(<=)|(>=))'
inc_pat = '^(('+num+'|'+id+')'+op+'('+num+'|'+id+'))$'
if_pat = rf'(if\s*\(\s*{id+op+id}\s*\))|(if\s*\(\s*{id+op+num}\s*\))|(if\s*\(\s*{num+op+num}\s*\))|(if\s*\(\s*{num+op+id}\s*\))'
if re.match(if_pat, txt):
    print('True')
else:
    print('False')
