set1 = set()
set2 = set()
ser = [1,2,3,2,5,2,3,6,7,2,3,4,1,8]
ser2 = [2,4,5,3,6,2,4,6,2,4,2,6,3,4]
for x in ser:
    set1.add(x)

for x in ser2:
    set2.add(x)


print(set1)
print(set2)
set3 = set()
for x in set1:
    if x in set2:
        set3.add(x)

print(set3)