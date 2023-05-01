#condition and loop 
#if statement
a=2
b=4
def comparison(a,b): #a,b are the parameters of functions
    if a>b:
        print(f"{a} is greater than {b}")
    elif a==b:
        print(f"{a} is equal to {b}")
    else:
        print(f"{a} is less than {b}")
x=comparison(10, 10) # 10 is the argument
print(x)
x=comparison(10, 20)# 10 and 20 are the arguments of the function
print(x)
x=comparison(20, 10)
print(x)
#while statement
i=1
while i<10:
    print(i)
    i +=1    
    if i>8:
        break 
names = ["hatim", "maha", "zakaria"]
x= None
for x in names: 
    if x=="maha": 
        name=x
        break
print(x)
#range
for x in range(2,6):
    print(x)
for x in range(2, 22, 3):
    print(x)
