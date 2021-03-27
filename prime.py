def isPrime(num):
#
# put your code here
#
    cnt = 0
    for k in range(2, num + 1):
        if num % k == 0:
            cnt += 1
    if cnt == 1:
        return True

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
