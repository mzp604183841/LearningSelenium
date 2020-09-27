from io import StringIO, BytesIO

f1 = StringIO()
f1.write('hello world')
print(f1.getvalue())

f2 = StringIO('hello!\nhi!\ngoodBye!')
while True:
    s = f2.readline()
    print(s.strip())
    if s == '':
        break
