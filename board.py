'''
🤔realcond和seqcond维度相同，到底是什么关系？，很多seqcond变成了全0，但也有例外
'''

import numpy as np

real_50=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/50Real.npy')
seq_50=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/50Seq.npy')

realcond=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/RealCond.npy')
seqcond=np.load('/Users/cesar/Library/Mobile Documents/com~apple~CloudDocs/Desktop/同步储存/Sports Analytics/hoop_transformer/BasketballGAN-master/data/SeqCond.npy')

'''seq=np.round(seq_,decimals=4)
np.set_printoptions(suppress=True, precision=4)'''
np.set_printoptions(suppress=True, precision=4)
np.set_printoptions(threshold=np.inf)


#print(realcond[1,:,:])
#print(seqcond[1,:,:])

for i in range (real_50.shape[0]):
    for j in range(real_50.shape[1]):
        for m in range(real_50.shape[2]):
            if not real_50[i,j,m,3]== 0. :
                print(real_50[i,j,m,:])

print(real_50[20,20,:,:])
print(seqcond[1,:,:])
'''print(seq_50[:,-1,:])
print(realcond[:,-1,:])
print(seqcond[:,-1,:])'''

print('50Real:',real_50.shape)
print('50seq',seq_50.shape)
print('realcond:',realcond.shape)
print('seqcond',seqcond.shape)


'''
index=np.where(realcond != seqcond)
indexx=np.where(realcond[index]!=seqcond[index])

#print(len(indexx))

for i in range(len(index[0])):
    #print(index[0][i],index[1][i],index[2][i])
    if np.all(realcond[index[0][i]][index[1][i]]==0):
    
        print(realcond[index[0][i]][index[1][i]]) 
        print(seqcond[index[0][i]][index[1][i]])
        print('-------------------')'''


'''
x=[]
y=[]
for i in range (realcond.shape[0]):
    for j in range(realcond.shape[1]):
        if realcond[i,j,5]==1 :
            #print(realcond[i,:,:])
            #print('-------------------')
            x.append(real_50[i,j,0,0])
            y.append(real_50[i,j,0,1])
            
print(sum(x)/len(x))
print(sum(y)/len(y))
'''
        
'''
print('x_max',np.max(seq[:,:,0::2]))
print('x_min',np.min(seq[:,:,0::2]))
print('y_max',np.max(seq[:,:,1::2]))
print('y_min',np.min(seq[:,:,1::2]))
'''