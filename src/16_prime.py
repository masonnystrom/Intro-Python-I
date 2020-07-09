def prime(x,y):
    for num in range(x,y):
        if num > 1:
            for n in range(2,num):
                if (num % n) == 0:
                    break
                else:
                    if n == num//2 +1:
                        print(num)

prime(1,100)
