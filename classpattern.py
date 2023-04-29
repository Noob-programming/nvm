import re

# access modifiers in class
access_modifiers = r'\s*(public|private|protected|internal|protected internal)\s*'
instance = r'\s*(static|const)\s*'
const = r'\s*(const)\s*'
static = r'\s*(static)\s*'
# define varib
ID = r"([a-zA-Z_][a-zA-Z_[0-9]*)"
barcket = r'(\[([0-9]?|[0-9]+)\])'
# data type of varbile
datatype = r'(int|bool|char|byte|sbyte|short|ushort|uint|long|ulong|float|double|decimal)\s*'

varible = datatype + ID
varstatic = access_modifiers + static + varible
fullvar = access_modifiers + varible
varconsti = access_modifiers + instance + varible
brakvar = varconsti + barcket + '?'
fullvarible = rf'({fullvar}|{varconsti}|{brakvar})\;'

print(re.match(fullvarible, "protected int a;").group())
print(re.match(fullvarible, "protected const int a;").group())
print(re.match(fullvarible, "protected const int a[10];").group())

# function declared
parmeter = r'(\((' + rf'({instance})?' + varible + rf'({barcket})?' + ',?' + r')*\)\s*)'
funct = fullvar + parmeter + r'(\{.+\;return .+\;\})'

functconsta = fullvar + parmeter + rf'({const})?\s*' + r'(\{.+\;return .+\;\})'
funstatic = varstatic + parmeter + r'(\{.+\;return .+\;\})'

print(re.match(funct, "public int a(static int a[],int b[],int c[]){ dsdf;return a+b+c;}").group())
print(re.match(funct, "public int a(int a[],const int b,static int c){gjgdr;return a+b+c;}").group())
print(re.match(funct, "public int a(){ dsdf;return a+b+c;}").group())
print(re.match(functconsta, "public int a() const { dsdf;return a+b+c;}").group())
print(re.match(funstatic, "public static int a() { dsdf;return a+b+c;}").group())

# void function declared
voidfun = access_modifiers + rf'({static})?\s*' + r'void\s*' + ID + parmeter + r'\s*(\{.+\;\}\s*)'
voidfunconst = access_modifiers + r'void\s*' + ID + parmeter + rf'\s*({const})?\s*' + r'\s*(\{.+\;\}\s*)'

print(re.match(voidfun, "public static void a(int a,int b,int c) {a+b+c;}").group())
print(re.match(voidfunconst, "public void a(int a,int b,int c) const {a+b+c;}").group())

# class declared and inhert
cls = rf'(({access_modifiers})?\s*({instance})?class\s*{ID}\s*)'
cls2 = rf'(({access_modifiers})?\s*{instance}?\s*class\s*{ID}\s*\;)'

memberclass = rf'({funct}|{voidfun}|{fullvarible}|{voidfunconst}|{funstatic}|{functconsta})*\s*'

# class inheritance
inher = cls + rf'(\:?\s*{ID})*(\,{ID})*\s*' + r'\{.*\}'

# class in C# pattern
classpattern = rf'(({cls2}|{cls})' + rf'(\:?{ID})*(\,{ID})*\s*' + r'(\{' + memberclass + r'\})?)'
print(re.match(classpattern, "public class a {public void a(int a,int b,int c){a+b+c;}}").group())
print(re.match(classpattern, "public class a {public int a(int a,int b,int c){a+b+c;return a;}}").group())
print(re.match(classpattern, "public class a {public int a;}").group())
print(re.match(classpattern, "public class a:newclass {public int a;}").group())
print(re.match(classpattern, "public class a:adjgj,djgaj {public int a;}").group())
print(re.match(classpattern, "public class a{}").group())
print(re.match(classpattern, "public class a;").group())

pattern = re.compile(classpattern)

print(pattern.match("public class a {public void a(int a,int b,int c) const {a+b+c;}}").group())
print(pattern.match("public class a {public static int a(int a,int b,int c){a+b+c;return a;}}").group())
print(pattern.match("public class a {public static int a;}").group())
print(pattern.match("public class a: newclass {public int a;}").group())
print(pattern.match("public class a: adjgj,djgaj {public int a;}").group())
print(pattern.match("public class a{}").group())
print(pattern.match("public class a;").group())
print(pattern.match("public static class a;").group())
print(pattern.match("public const class a;").group())
print(pattern.match("public static class a {public int a(int a,int b,int c) {a+b+c;return a;}}").group())
print(pattern.match("static class a;").group())
