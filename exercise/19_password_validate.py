# password regex validation

import re 

pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
string = 'sup3r@p4s$word5'

check = pattern.fullmatch(string)
print(check)