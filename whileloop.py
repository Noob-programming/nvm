import re


id = "[a-zA-Z_][a-zA-Z_0-9]*"
op = r'((==)|(!=)|(>)|(<)|(>=)|(<=))'
number = '[0-9]+'
conif = r'((\&\&)|(\|\|))'
barc = r'(\s*{\s*.+\s*\}\s*)'

idop = rf"({id}|{number})"

colla = rf"(\s*{idop}\s*{op}\s*{idop}\s*)"

# print(colla)
a = input("enter while: ")
pattern = r"(while\s*\("+colla+"\s*\)"+barc+")"
pattern = re.compile(pattern)

print(pattern.match(a))

while2 = rf"while\s*\({colla}\s*\)"
do1 = rf"(do\s*{barc}\s*{while2}\s*\;)"
do1 = re.compile(do1)
b = input("enter do while : ")
print(do1.match(b))
