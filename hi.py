a = [1,2,3,4]
a.reverse()
for i in a:
    print(i)

print(len(a))

a[2] = "hi"

for i in a:
    print(i)

a.remove(1)

for i in a:
    print(i)

if 1 in a:
    print("true")
else:
    print("false")
