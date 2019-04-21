def complexarray2plotdata(x):
    x_row_len = len(x)
    # x_col_len = len(x[0])
    r = [0] * (x_row_len )# * (x_row_len)
    i = [0] * (x_row_len )# * (x_row_len)
    for row in range(0,x_row_len):
        r[row] = x[row].real
        i[row] = x[row].imag
        # print('row=',row,'col=',col,'x = ',x[row][col],'r = ',r[row][col],'i = ',i[row][col])
        pass
    pass
    # print("x size",len(x))
    # print("r size",len(r))
    # print("i size",len(i))
    return r,i