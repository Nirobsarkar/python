contacts= {
"ANNI": 7256849217,
"ALIX": 7595968473,
"HYPNOX": 7532985414,
"VISHAL": 9971011068,
"DIVYANSH": 8076996289,
"NIROB": 7428556861,
"NILOY": 7528485513,
"VISHU": 8429883791,
"GETHU": 8522903783,
"ARYAN": 9455903382,
"SHUDHANSHU": 8594307790,
"SAI": 7525605609,
"JABIR": 7288937131,
"ALIF": 8508385322,
"SHRUTHI": 7677339203,
"AKANSHA": 8459043910,
"PRIYA": 7485100593,
"NIDI": 8549039912,
}

def single_search():
    name=input(">>>Enter the name of the contact you wish to search for: ").upper()
    if name in contacts:
        print(f"\n{name}: {contacts[name]}")
    else:
        b=input("\nNo such contact found\nIf you wish to add one, type 'Yes' else type 'No': ").lower()
        if b=="yes":
            new_contact(name)
            print(f"{name}: {contacts[name]}")
        elif b=="no":
            pass
        else:
            print("Enter either yes or no")

def multiple_search():
    result={}
    s1=[]
    s=0
    name1=input(">>>Enter the names of the contacts seperated by comma: ").split(",")
    for i in name1:
        i=i.upper()
        if i in contacts:
            result[i]=contacts[i]
        else:
            s1.append(i)
            s+=1
    if s>0:
        c=(input(f"\nCouldn't find contacts {s1} . \nDo you wish to add them? Enter Yes or No: ")).lower()
        if c=="yes":
            for i in s1:
                new_contact(i)
                if i in contacts:
                    result[i]=contacts[i]
            print()
            print(result)
        elif c=="no":
            print()
            if result=={}:
                pass
        else:
            print("\n Invalid argument")
    else:
        print()
        print(result)

def new_contact(contact_name):
    print()
    contact_number=int(input(">>>Enter their contact number: "))
    contacts[contact_name]=contact_number

choice=int(input("Would you like to: \n\n1. Search for a single contact \n2. List all the contacts \n3. Search for multiple contacts \n \n>>>Enter your choice: "))

if choice==1:
    single_search()

elif choice==2:
    print()
    print(contacts)

elif choice==3:
    multiple_search()

else:
    print("Choose from the given options!")