import re


id = "([a-zA-Z_][a-zA-Z_[0-9]*)"
op = r'((==)|(!=)|(>)|(<)|(>=)|(<=))'
number = '([0-9]+)'
# 'operation'
pa = r"((\+\+)|(\-\-))"
pa2 = r"((\+\=)|(\-\=)|(\*\=)|(\/\=))"
pa3 = r"((\+)|(\-)|(\*)|(\/))"

firstin = rf"({id}\s*\=\s*({id}\s*|{number}\s*))"

second = rf"(\s*({id}|{number})\s*{op}\s*({id}|{number})\s*)"

third = rf"(\s*{id}\s*{pa2}\s*{number}\s*)|(\s*{id}\s*{pa2}\s*{id}\s*)|(\s*{id}\s*\=\s*{id}\s*{pa3}\s*{id}\s*)|\
            (\s*{id}\s*\=\s*{id}\s*{pa3}\s*{number}\s*)|(\s*{id}{pa}\s*)|(\s*{pa}{id}\s*)"

barc = '(\s*{\s*.*\s*\}\s*)'

finalform = rf'(for\s*\(\s*({firstin})\s*\;\s*({second})\s*\;\s*({third})\s*\){barc})'

# print(re.match(finalform,"for(i=0;i<10;i++){}"))
idop = rf"({id}|{number})"

colla = rf"(\s*{idop}\s*{op}\s*{idop}\s*)"


whiles = r"(while\s*\("+colla+"\s*\)"+barc+")"

while2 = rf"while\s*\({colla}\s*\)"
do1 = rf"(do\s*{barc}\s*{while2}\s*\;)"


looping = rf"({finalform})|({whiles})|({do1})"

pattern = re.compile(looping)

print(pattern.match("do{nasnd}while(i<10);"))
