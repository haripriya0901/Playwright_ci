def factorial(self,num):
    num = ""
    for n in num:
        result = result * n
        print(result)

# factorial()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

string = "haripriya"
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)