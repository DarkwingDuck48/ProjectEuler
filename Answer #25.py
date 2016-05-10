def fib(x):
    a = 0
    if x < 3:
        return 1
    else:
        if fibanachi[x-2] != " " and fibanachi[x-3] != " ":
            a = fibanachi[x-2]+fibanachi[x-3]
        else:
            a = fib(x-1)+fib(x-2)
        fibanachi.append(a)
        return(a)

fibanachi = [1, 1]
i = 3
while len(str(fib(i))) != 1000:
    i += 1
print(i)
