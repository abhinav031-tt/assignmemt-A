
n = int(input("Enter the value of 'num': "))
num1 = 0
num2 = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  num1 = num2
  num2 = sum
  sum = num1 + num2