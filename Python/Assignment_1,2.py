
file=open("unique.txt","r")
print(file.read())
uniqueList=[]

def unique(i):
    print('inside;')
    if i not in (file.split()):
        uniqueList.append(i)
ls=file.split()
for i in ls():
    unique(i)
    print('hello')
print(uniqueList)
