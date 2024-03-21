def spiral(m,n,a):
    '''
    m - no of rows
    n - no of columns
    a - matrix
    '''
    k = 0
    l = 0
    '''
    k - starting row index
    m - ending row index
    '''

    while(k<m and l<n):
        # Print the first row from the remaining rows
        for i in range(l,n):
            print(a[k][i],end=" ")
        k+=1

        # Print the last column from the remaining columns
        for i in range(k,m):
            print(a[i][n-1],end=" ")
        n-=1

        if(k<m):
        # Print the last row from the remaining rows
            for i in range(n-1,l-1,-1):
                print(a[m-1][i],end=" ")
            m-=1

        if(l<n):
        # Print the first column from the remaining columns
            for i in range(m-1,k-1,-1):
                print(a[i][l],end=" ")
            l+=1

a = []
count = 1
for i in range(4):
    l = []
    for j in range(4):
        l.append(count)
        count+=1
    a.append(l)

spiral(4,4,a)


