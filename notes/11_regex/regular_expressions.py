# regular expressions

import re 

pattern = re.compile('this')
string = 'this search inside of this string!'

# a = re.search('this', string)

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.group())
print(b)
print(c)
print(d)

# advanced patterns 
 # regex101.com

pattern2 = re.compile(r"([a-zA-Z]).([a])")
string2 = 'this search inside of this string!'

# a = re.search('this', string)

a2 = pattern2.search(string2)
b2 = pattern2.findall(string2)
c2 = pattern2.fullmatch(string2)
d2 = pattern2.match(string2)

print(a2.group())
print(b2)

# use case
# email valifation 

pattern3 = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string3 = 'b@b.com'

a3 = pattern3.search(string3)
print(a3)