s = "teachermode"
t = "e"

find_t = []

for index, value in enumerate(s):
    if value == t:
        find_t.append(index)

if len(find_t) == 0:
    print("검색할 문자 {}가 존재하지 않습니다".format(t))
    exit()
    
print(s)
    
j = 0
idx = 0
k = find_t[idx]
if len(find_t) >= 2:
    idx += 1
    q = find_t[idx]
else:
    q = k
for i in s:
    if j == q:
       k = q
       if idx < len(find_t) - 1: 
            idx += 1
            q = find_t[idx]
    print(abs(k - j), end='')
    j += 1
