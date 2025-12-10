line = int(input())
i = 0
a = ' '
while i < line:
        print(a * (line-i - 1) + '*' * (i*2+1))
        i = i + 1