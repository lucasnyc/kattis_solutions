for i in range(int(input())):
    c,d = map(int,input.split()):
    if d == 1:
        print(f'{c} 1/1')
    elif d == 2:
        print(f'{c} 1/2')
    else:
        counter = 0
        while d > 0:
            d//=2
            counter +=1
        if d % 2 == 0:
            return 
