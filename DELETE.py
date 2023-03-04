def Delete():
    with open('record.txt',"r+") as f:
        a=input("ENTER THE NAME OF ICE CREAM TO BE REMOVED FROM THE LIST: ")
        l=f.read()
        x=l.split()
        x.remove(a)

    with open('record.txt',"w") as f:
        for j in x:
            f.write(j)
            f.write("\n")
        print("RECORD DELETED SUCESSFULLY!")

    '''Renaming the file'''
    #  old_name="1.txt"
    # new_name="2.txt"
    # os.rename(old_name,new_name)
