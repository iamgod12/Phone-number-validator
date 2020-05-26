num=input("ENter Mobile Number ")
if(num.isdigit()):
    if(len(num)<10):
        print("Number must contain atleast 10 digits")
    else:
        start=int(len(num)-3)
        ll=num[len(num)-3:len(num)]
        
        print("*"*start+ ll )
else:
    print("Number must contain digits only")
