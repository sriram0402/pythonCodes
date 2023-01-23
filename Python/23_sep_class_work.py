"""import pickle
data={'name':'Sriram','age':'20','City':'rocky hill'}
pic_out=open('data.pickle','wb')

pickle.dump(data,pic_out)

pic_out.close()

#unpickling

pic_in=open('data.pickle','rb')
data_in=pickle.load(pic_in)
print(data_in)



file

import csv


file=open('sample_class3.csv','w')
ls1=['Apple','35','Grade A']
ls2=['Berries','80','Grade C']
ls3=['Mangos','65','Grade A']

pen=csv.writer(file)
pen.writerows([ls1,ls2,ls3])

file.close()


file=open("sample_class3.csv")
fileText=csv.reader(file)
lsOfData=list(fileText)
print(lsOfData)
file.close()
"""




import json, requests, sys

location=input("enter location:")
if len(sys.argv)>1:
    locaton=''.json(sys.argv[1:])
    
url='https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=81db19b25f202bfde975b1de71c20387'

res=requests.get(url)
pyObj=json.loads(res.text)



main=pyObj['weather'][0]['main']
temp=pyObj['main']['temp']
minTemp=pyObj['main']['temp_min']
maxTemp=pyObj['main']['temp_max']
feelsLike=pyObj['main']['feels_like']
humidity=pyObj['main']['humidity']
print('Main:',main)
print('Current temp:',temp)
print('Min temp:',minTemp)
print('Max temp:',maxTemp)
print('feels like:',feelsLike)
print("Humidity:",humidity)





