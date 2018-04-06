import numpy as np
import matplotlib.pyplot as plt

#PARAMS
dataFile    ='data.txt'
dim         = 2
alpha       = 0.1
tetha       = np.random.rand(dim)
m           = 15
type_num    ='f'

#FUNCTION
def get_h_one(var_x,var_tetha):
    return var_tetha[0]+var_tetha[1]*var_x
    
def get_h(var_x,var_tetha):
    result=[]
    for i in range(0,m):
        result.append( var_tetha[0]+ (var_tetha[1] * var_x[i]) )
    return result
    

def get_error(var_y,var_h):
    global m
    diference = var_y - var_h 
    for i in range(0,m):
        diference[i]= diference[i]*diference[i]
    return sum(diference)/(2.0*m)

def multiplicar_vectores(vec_1,vec_2):
    global m
    vec_res=[]
    for i in range(0,m):
        vec_res.append(vec_1[i]*vec_2[i]*-1)
    return vec_res

def change_tethas(var_x,var_y,var_h):
    global m
    global alpha
    global tetha

    tetha[0]=tetha[0]-alpha*sum(var_y-var_h)*(-1.0)/m 
    tetha[1]=_range = range(0,50)
counter =0


while(error > 0.01):
    change_tethas(arrays_x[0],arrays_x[1],h)
    h= get_h(arrays_x[0],tetha)
    error=get_error(arrays_x[0],h)
    plt.plot(_range, [get_h_one(i,tetha) for i in _range])
    plt.plot(arrays_x[0],arrays_x[1],"ro")
    plt.axis([1.3 , 2, 0, 80])
    #plt.savefig(str(counter)+'result.png')
    plt.close(1)
    counter=counter+1
    print error
tetha[1]-alpha*sum( multiplicar_vectores( var_y-var_h,var_x ))/m




data = np.loadtxt( dataFile, dtype=type_num, delimiter=',' )
arrays_x = data.transpose()


h= get_h(arrays_x[0],tetha)
error=get_error(arrays_x[0],h)

_range = range(0,50)
counter =0


while(error > 0.01):
    change_tethas(arrays_x[0],arrays_x[1],h)
    h= get_h(arrays_x[0],tetha)
    error=get_error(arrays_x[0],h)
    plt.plot(_range, [get_h_one(i,tetha) for i in _range])
    plt.plot(arrays_x[0],arrays_x[1],"ro")
    plt.axis([1.3 , 2, 0, 80])
    #plt.savefig(str(counter)+'result.png')
    plt.close(1)
    counter=counter+1
    print error

#plt.show()
