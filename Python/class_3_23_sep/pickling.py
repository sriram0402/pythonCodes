import pickle
data={'name':'Sriram','age':'20','City':'rocky hill'}
pic_out=open('data.pickle','wb')

pickle.dump(data,pic_out)

pic_out.close()

#unpickling

pic_in=open('data.pickle','rb')
data_in=pickle.load(pic_in)
print(data_in)
