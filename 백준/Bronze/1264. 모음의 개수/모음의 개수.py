while True:
        a = input()
        if a == "#":
                break
        b = 0
        for i in a:
                if i in "aeiouAEIOU":
                        b+=1
        print(b)