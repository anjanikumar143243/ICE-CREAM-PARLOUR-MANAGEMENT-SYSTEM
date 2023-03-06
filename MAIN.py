"""
Ice-cream Parlor Management System
Description: Through this project user can manage the different types of ice-creams. User will first create the database for ice creams and then after that certain operations can be performed depending upon the requirement of user. 

Modules Required:
1.Display Ice-creams list
2.Add new ice-cream data
3.Update the record of the ice-cream
4.Search any ice-cream 
5.Delete any ice-cream record.
"""


import ADD
import UPDATE
import DELETE
import SEARCH

def start():
    while(True):
        print("        Welcome to the ICE CREAM PARLOUR MANAGEMENT SYSTEM     ")
        print("------------------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Add A New Ice-Cream")
        print("Enter 3. To Update Record ")
        print("Enter 4. To Search Ice-Cream")
        print("Enter 5. To Delete Record ")
        print("Enter 6. To exit")
        try:
            a=int(input("Select a choice from 1-6: "))
            print()
            if(a==1):
                with open('record.txt',"r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
            elif(a==2):
                ADD.Add()
            elif(a==3):
                UPDATE.Update()
            elif(a==4):
                SEARCH.Search()
            elif(a==5):
                DELETE.Delete()
            elif(a==6):
                print("THANK YOU FOR USING ICE CREAM PARLOUR MANAGEMENT SYSTEM!")
                break
            else:
                print("Please enter a valid choice from 1-6!")
        except ValueError:
            print("Please input as suggested!")
start()
