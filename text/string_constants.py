import inspect
import string
import textwrap

sample_text = """
The textwrap module can be used to format text for output in
situations where pretty-printing is desired. It offers
programmatic functionality similar to the paragraph wrapping
or filling features found in many text editors.
"""


def is_str(value):
    return isinstance(value, str)


for name, value in inspect.getmembers(string, is_str):
    if name.startswith('_'):
        continue
    print('%s=%r\n' % (name, value))

# print((sample_text))
# print(textwrap.fill(sample_text, width=100))
#
# dedented_text = textwrap.dedent(sample_text)
# print('Dedented:')
# print(dedented_text)

# dedented_text = textwrap.dedent(sample_text).strip()
# for width in [45, 60]:
#     print('{} Columns: \n'.format(width))
#     print(textwrap.fill(dedented_text, width=width))
#     print()

# dedented_text = textwrap.dedent(sample_text)
# wrapped = textwrap.fill(dedented_text, width=50)
# wrapped += '\n\nSecond paragraph after a blank line.'
# final = textwrap.indent(wrapped, '> ')
#
# print('Quoted block: \n')
# print(final)

dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text, initial_indent='', subsequent_indent=' ' * 4, width=50))

