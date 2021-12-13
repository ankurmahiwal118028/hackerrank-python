if __name__ == '__main__':
    X = int(input())
    Y = int(input())
    Z = int(input())
    N = int(input())

    array = list()
    for i in range(0,X+1):
        for j in range(0,Y+1):
            for k in range(0,Z+1):
                if (i+j+k<N):
                  array.append([i,j,k])


    print(list)
