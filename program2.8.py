import re
p = input("enter s:")
s = input("enter p:")

p = r"{}".format(p)
p = re.compile(p)
if p.fullmatch(s):
    print("true")
else:
    print("false")
