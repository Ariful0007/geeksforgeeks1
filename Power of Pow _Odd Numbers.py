for _ in range(int(input())):
    n = int(input())
    temp = n
    sum=0
    for i in range(1,(n*2)):
        if i % 2 ==1 :
            sum = sum + (i*i)

    print(sum)


if __name__ == '__main__':
    pass
