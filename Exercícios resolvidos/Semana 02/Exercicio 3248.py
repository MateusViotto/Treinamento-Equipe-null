count = 0
n = int(input())
seq = input().split(" ")

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if seq[k] < seq[j] < seq[i]:
                count += 1
print(count)