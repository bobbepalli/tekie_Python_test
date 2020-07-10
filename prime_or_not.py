n = int(input()) # dynamic input value
if n <= 1:
    print("false")
else:
    for x in range(2,n): # checking n value is divible by given range(2,n)
        if n%x == 0:
            print("false")
            break
    else:
        print("true")