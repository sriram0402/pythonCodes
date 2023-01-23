def check(i):
    if(i=="\n"):
        return False;
    elif(i.startswith("FirstName, LastName")):
        return False;
    else:
        return True;

def main():

    file=open("CS638_B.txt","r")
    Dict={}
    a='1'

    for i in file:
        if check(i):
            Dict['638BS'+str(a)]=i.rstrip()
            a=int(a)+1


    f=open('Student_Details.txt','w')
    f.write("ID\t\tName\n\n")
    for key,value in Dict.items():
        f.write('%s\t\t%s\n' % (key, value))

    f=open('Student_Details.txt','r')
    print(f.read())

main()
