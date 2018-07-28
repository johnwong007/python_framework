
from io import BytesIO

f = BytesIO()

f.write('hello')

f.write(' ')

f.write('world')

print(f.getvalue())

print(f.getvalue())
help(f)
