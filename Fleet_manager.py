Names = ["James T", "Spock", "Leonard", "Nyota", "Pavel"]
Ranks = ["Captain", "Officer", "Officer", "Officer", "Officer"]
Divisions = ["Command", "Science", "Science", "Operations", "Command"]
IDs = ["0001","0002","0003", "0004", "0005"]
   
def main():
    ## Asking the user for their name and what th require to be done by the system
    First_name = input("What is your first name ")
    last_name = input("What is your last name")
    print("Welcome", First_name + last_name,
          "\n 1. Check curent memebrs"
          "\n 2. new a member"
          "\n 3. Remove a member "
          "\n 4. Update the Ranks "
          "\n 5. Search Crew"
          "\n 6. Filter by divisions "
          "\n 7. Calculate payroll"
          "\n 8. Count officers Ranks ")
   
## User validation
   
   
    # init_database(Names, Ranks, Division, IDs)
    while True:
        print("Welcome", First_name + last_name,
          "\n 1. Check curent memebrs"
          "\n 2. New a member"
          "\n 3. Remove a member "
          "\n 4. Update the Ranks "
          "\n 5. Search Crew"
          "\n 6. Filter by divisions "
          "\n 7. Calculate payroll"
          "\n 8. Count officers Ranks ")
   
        Option = int(input("Pick from the options above what you would like to do "))
        while Option > 8 or Option < 0:
            Option = int(input("Pick from the options above what you would like to do "))


## Taking theusers input ad taking it to the right function
        if Option == 1:
            Display_roster(Names, Ranks, Divisions, IDs)
        elif Option == 2:
            Add_member(Names, Ranks, Divisions, IDs)
        elif Option == 3:
            Remove_member(Names, Ranks, Divisions, IDs)
        elif Option == 4:
            Update_Ranks(Names, Ranks, IDs)
        elif Option == 5:
            Search_Crew(Names, Ranks, Divisions, IDs)
        elif Option == 6:
            Filter_by_division(Names, Divisions)
        elif Option == 7:
            Calculate_payroll(Ranks)
        elif Option == 8:
            Count_officers(Ranks)
        else:
            print("Shutting down")

            break
       

def Display_roster(Names, Ranks, Divisions, IDs):
    print("Current team members")
    for i in range(len(Names)):
            print(Names[i] + " - " , Ranks[i] , " - " , Divisions[i] , " - " , IDs[i])
   


def Add_member(Names, Ranks, Divisions, IDs):
    New_Name = str(input("What is the new Members name ")).title()
    New_Rank = str(input("What is their Rank ")).title()
    New_Division = str(input("what division are they in ")).title()
    New_IDs = str(input("what is there ID code"))
    Names.append(New_Name)
    Ranks.append(New_Rank)
    Divisions.append(New_Division)
    IDs.append(New_IDs)
    return Names, Ranks, Divisions, IDs
     
def Remove_member(Names, Ranks, Divisions, IDs):
    Remove_member = input("Pick name to change: ").title()  
    idex = Names.index(Remove_member)
    Names.pop(idex)
    Ranks.pop(idex)
    Divisions.pop(idex)
    print("Removed,", Remove_member)
    return Names, Ranks, Divisions, IDs

def Update_Ranks(Names, Ranks, IDs):
    try:
        
        index = str(input("enter the ID of the officer for a rank change "))
        for i in range(len(IDs)):
            if IDs[i] == index:
                print(f"Updating rank for {Names[i]} (Current:{Ranks[i]})")
                New_ranks = input("Enter the new rank: ").title()
                Ranks[i] = New_ranks
                print(f"Rank has been updated for {Names[i]} (Rank has been updated to {New_ranks})")
        else:
            print("Changed")
    except:
        print("Change Rank")
    return Names, Ranks, IDs

def Search_Crew(Names, Ranks):
    print("What are you searching for \n 1) The Names of the crew members \n 2) The Ranks and the amount of people with that rank \n 3) The divisions in the crew  ")
    choice = int(input("Which would you like to carry out in this protocal"))
    if choice == 1:
        print("Names of the crew members ")
        Number= 1
        for i in range(len(Names)):
            print(Number, "Crew member: " ,Names[i])
            Number = Number + 1
    elif choice == 2:
        print("The ranks of the crew ")
        select = int(input(" 1) Finding the ranks \n 2.  People with those ranks "))
        if select == 1:
            print("THe Ranks of the in the crew  \n Captian \n Officer \n Lieutenant \n Esign \n ")
            rank_selection = input("which rank: ").title()
            for i in range(len(Ranks)):
                if rank_selection == Ranks[i]:
                    print(Names[i], "-", Ranks[i] )
                else:
                    break  

        elif choice == 2:
            try:
                rselect = input("which rank: ").title()
                for rank in range(len(Ranks)):
                    count = 0
                    if Ranks[rank] == rselect:
                        count = count + 1

                        print("The rank of ", rselect, "has ", count, "members")    
            except:
                print("Rank is not shown ")
       
       
        else:
            print("Not an option")


           




main()
