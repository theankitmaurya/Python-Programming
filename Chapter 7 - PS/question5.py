# Write a program to find the sum of first n natural numbers using while loop.

i = 0
sum = 0
n = int(input("Enter the number: "))

while(i <= n):
    sum += i
    i += 1

print(sum)
