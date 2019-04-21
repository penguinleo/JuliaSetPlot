from juliasearch import juliasearch
from matrix2complex import matrix2complex
from complexarray2plotdata import complexarray2plotdata
from matrix2array import matrix2array
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import colors
from colormap import colormap
from listnorm import listnorm
import numpy as np 



sample_r = np.linspace(-1.7,1.7,500)
sample_i = np.linspace(-1.7,1.7,500)
mesh_r,mesh_i = np.meshgrid(sample_r,sample_i)
sample = matrix2complex(mesh_r,mesh_i)
print(len(sample),len(sample[0]))
# y,g = juliasearch(sample,complex(-0.835, -0.2321),50)
# y,g = juliasearch(sample,complex(-0.835, 0),50)
# y,g = juliasearch(sample,complex(0.3, -0.03),50)
# y,g = juliasearch(sample,complex(-0.835, -0.01),50)
# y,g = juliasearch(sample,complex(-0.1, -0.8),50)
# y,g = juliasearch(sample,complex(1, 0),50)
# y,g = juliasearch(sample,complex(-1, 0),50)
# y,g = juliasearch(sample,complex(0, 1),50)
# y,g = juliasearch(sample,complex(0, -1),50)
# y,g = juliasearch(sample,complex(0.1992, -0.55),50)
# y,g = juliasearch(sample,complex(-0.535, -0.55),50)
y,g = juliasearch(sample,complex(-0.2, -0.75),100)
print('we just find',len(y))
yr,yi = complexarray2plotdata(y)

# fig1 = plt.figure(1)
# # plt.subplot(121)
# plt.plot(mesh_r,mesh_i,marker = '+',markersize = 0.1,c ='#F0F8FF')
# plt.xlabel('real')
# plt.ylabel('imag')
# plt.title('sample zone')

# # subf1=plt.subplot(122)
# plt.plot(yr,yi,'r+',markersize=0.1)
# plt.xlabel('real')
# plt.ylabel('imag')
# plt.title('julia set')
# # plt.show()


# fig2 = plt.figure(2)
r_array_3d = matrix2array(mesh_r)
i_array_3d = matrix2array(mesh_i)
# ax = fig2.gca(projection='3d')
# ax.plot(r_array_3d, i_array_3d,g,'g+',markersize=0.1)
# plt.show()

fig3 = plt.figure(3)
# cn = colormap(g)
cn = listnorm(g)
array_len = len(r_array_3d)
plt.scatter(r_array_3d,i_array_3d,c=g,marker='.')
# plt.colorbar()
plt.grid(True)
plt.xlabel('real')
plt.ylabel('imag')
plt.title('color julia')
# for x in range(0,array_len):
#     # print(x)
#     plt.plot(r_array_3d[x],i_array_3d[x],'g.',markersize=1,c = cn[x])
#     pass
plt.show()