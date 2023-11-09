import re
txt = "120 PLNP"
pattern = re.compile(r'PLN')

print(txt)

print(re.sub(pattern, '', txt))