def Add():
    with open('record.txt',"a") as f:
        a=input("ENTER THE NAME OF THE NEW ICE CREAM TO BE ADDED IN THE LIST: ")
        f.write("\n")
        f.write(a)
        print("RECORD ADDED SUCESSFULLY!")
