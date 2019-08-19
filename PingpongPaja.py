t = int(input())

while t!=0:
    x, y, k = map(int, input().split())

    if((x+y)//k % 2 ==0):
        print('Chef')
    else:
        print('Paja')
    t-=1;