def Update():
    with open('record.txt',"r+") as f:
        a=input("ENTER THE NAME OF ICE CREAM TO BE UPDATED FROM THE LIST: ")
        b=input("ENTER THE NEW NAME OF ICE CREAM: ")
        l=f.read()
        x=l.split()

    with open('record.txt',"w") as f:
        for j in range(len(x)):
            if x[j]==a:
                x[j]=b
        for j in x:
            f.write(j)
            f.write("\n")
        print("RECORD UPDATED SUCESSFULLY!")