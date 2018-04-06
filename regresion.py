import numpy as np
import matplotlib.pyplot as plt
from time import sleep


#PARAMS
dataFile    ='data.txt'
dim         = 2
alpha       = 0.015
tetha       = np.random.rand(dim)
m           = 15
type_num    ='f'

#FUNCTION


def get_h(_X, _T ):
    temp=[]
    for i in range(m):
        t=[1]
        for j in range(0,dim-1):
            t.append(_X[j][i])
        temp.append(t) 
    temp = np.array(temp)
    temp =temp.transpose()
    result= _T.transpose().dot(temp)
    return result

def get_error(_X,_H):
    global m
    error=0
    for i in range(0,m):
        val = _X[dim-1][i]
        error = error+ ( val - _H[i])**2 
    return error/(2*m)
    
def multiplicar_vectores(vec_1,vec_2):
    global m
    vec_res=[]
    for i in range(0,m):
        vec_res.append(vec_1[i]*vec_2[i]*-1)
    return vec_res

def change_tethas( _T, _alpha, _X , _H):
    temp_tetha =np.zeros(2)
    temp_tetha[0]=_T[0]- (_alpha*sum( _X[dim-1] - _H )*(-1))/m
    for i in range(1,dim):
        temp_tetha[i]=_T[i] - (_alpha*sum(multiplicar_vectores( _X[dim-1] - _H, _X[i] )) /m)
    
    return temp_tetha


data = np.loadtxt( dataFile, dtype=type_num, delimiter=',' )
arrays_x = data.transpose()
h   = get_h(arrays_x,tetha)
error = get_error(arrays_x,h)

_range = range(0,50)
counter =0

def get_h_one(var_x,var_tetha):
    return var_tetha[0]+var_tetha[1]*var_x

while error > 0.01   :
    tetha =change_tethas(tetha,alpha,arrays_x,h)
    h= get_h(arrays_x,tetha)
    error=get_error(arrays_x,h)
    plt.plot(_range, [get_h_one(i,tetha) for i in _range])
    plt.plot(arrays_x[0],arrays_x[1],"ro")
    plt.axis([1 , 3, 0, 100])
    plt.savefig(str( counter) +'result.png')
    plt.close(1)
    counter=counter+1
    print error , tetha[1]
    



