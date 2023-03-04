def Search():
    with open('record.txt',"r+") as f:
        a=input("ENTER THE NAME OF ICE CREAM TO BE SEARCHED FROM THE LIST: ")
        l=f.read()
        x=l.split()
        if a in x:
            print(a," ICE-CREAM IS AVAILABLE!")
        else:
            print(a," ICE-CREAM IS NOT AVAILABLE AT THE MOMENT!")