import re
txt = "#120 PLN"
pattern = re.compile(r'PLN|#')
# II sposób z wykorzystaniem podwójnego wzorca
# pattern_2 = re.compile(r'#')
print(txt)

a = re.sub(pattern, '', txt)
print(a)
# II sposób
# print(re.sub(pattern_2, '', a))
