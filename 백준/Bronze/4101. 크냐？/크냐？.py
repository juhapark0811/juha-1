while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
                break
        if a > b:
                print("Yes")
        elif a < b or a == b:
                print("No")