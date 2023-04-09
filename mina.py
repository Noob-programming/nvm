import re


a = input("enter id: ")

pt = r"([a-zA_Z_])([a-zA_Z_0-9])*"

pa = rf"({pt}\+\+)|(\+\+{pt})|(\-\-{pt})|({pt}\-\-)|({pt}\+\=)|({pt}\-\=)"

pattern = re.compile(pa)

if pattern.match(a):
    print("true")
else:
    print("error")
