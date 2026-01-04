import random

arr = [[0] * 5 for _ in range(5)]

sum_list = []
l_diag = 0
r_diag = 0
for i in range(0, 5):
    sum = 0
    for j in range(0, 5):
         val = random.randrange(1, 100)
         arr[i][j] = val
         sum += val
         if j == 4:
             sum_list.append(sum)
             l_diag += arr[i][i]
             r_diag += arr[i][4 - i]

sum_list.append(l_diag)
sum_list.append(r_diag)

for i in range(0, 5):
    print(f"{arr[i]} \t {i + 1}행합계 : {sum_list[i]}")
print(f"\n왼쪽대각선합계 : {l_diag}\n오른쪽대각선합계 : {r_diag}")

sum_list.sort(reverse=True)
print(f"\n\n가장 큰 합계 : {sum_list[0]}")
