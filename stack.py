a=input("enter the string:")
stack=[]
reverse=""
for i in range(len(a)):
    stack.append(a[i])
while(len(stack)>=1):
    a=stack.pop()
    reverse=reverse+a
print("Reverse of the String:",reverse)
    
