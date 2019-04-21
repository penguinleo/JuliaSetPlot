def matrix2array(x):
    x_row_len = len(x)
    x_col_len = len(x[0])
    # print('input matrix size:','row length = ',x_row_len,'col length = ',x_col_len)
    a = [0] *(x_row_len * x_col_len)
    a_row_len = len(a)
    # a_col_len = len(a[0])
    # print('output array size:','length = ',a_row_len)
    for i in range(0,x_row_len * x_col_len ):
        row = int(i/x_col_len)
        col = int(i%x_col_len)
        # print('i=',i,'row=',row,'col=',col,'x = ',x[row][col])
        a[i] = x[row][col]
        pass
    pass
    return a