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
