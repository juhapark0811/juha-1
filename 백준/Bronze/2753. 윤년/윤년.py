a = int(input())
b = 0
if a % 4 == 0:
  b = 1
if a % 100 == 0: 
  b = 0
if a % 400 == 0:
  b = 1
print(b)