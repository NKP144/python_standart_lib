import string

s = 'Пример строки для перевода буквы каждого слова в верхний регистр'
print(s)
print(string.capwords(s))
print(s.title())

list1 = s.split()
list2 = [s.capitalize() for s in list1]
s2 = ' '.join(list2)
print(s2)
#-------------------------------------------------------------------------#

values = {'var': 'foo'}
t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""

print('INTERPOLATION:', s % values)

s = """
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""

print('FORMAT', s.format(**values))
#-------------------------------------------------------------------------------#

