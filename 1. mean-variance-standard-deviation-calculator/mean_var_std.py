import numpy as np

def calculate(list):
  if len(list)<9:
    raise ValueError ("List must contain nine numbers.")
  calculations={}
  arr=np.array(list).reshape(3,3)
  calcs=(np.mean , np.var ,np.std , np.max , np.min  ,np.sum)
  dictions={'mean':[],
            'variance': [],
            'standard deviation': [],
            'max': [],
            'min': [],
            'sum':[]}

  for index, key in enumerate (dictions.keys()):
    axis1=[];axis2=[]
    for i in range(3):
         #columns
        axis1.append(calcs[index](arr[:,i:i+1]).tolist())
         #rows
        axis2.append(calcs[index](arr[i]).tolist())
    lst=[axis1,axis2, calcs[index](arr.tolist())]
    dictions[key]=lst
  calculations=dictions
    
  return calculations