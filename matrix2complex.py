import matplotlib.pyplot as plt 
import numpy as np
# from RealImageArray2Complex import array2complex
def matrix2complex(r,i):
    r_row_len = len(r)
    i_row_len = len(i)
    r_col_len = len(r[0])
    i_col_len = len(i[0])
    # print(r_row_len,i_row_len,r_col_len,i_col_len)
    x_row_len = min(r_row_len,i_row_len)
    x_col_len = min(r_col_len,i_col_len)
    x = [[complex(0,0)] * (x_col_len) for _ in range(x_row_len)] #* (x_row_len)
    # print(x)
    for row in range(0,x_row_len ):
        for col in range(0,x_col_len ):
            x[row][col] = complex(r[row][col],i[row][col])
            # print("row = ",row," col = ",col," r = ",r[row][col]," i= ",i[row][col]," x = ",x[row][col], "\t\tmatrix[0][0] = ",x[0][0])
            pass
        pass
        # x[row] = array2complex(r[row],i[row])
    pass
    # print(x)
    return x
    pass