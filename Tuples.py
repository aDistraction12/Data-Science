att=()
start = True
while(start):
    name = input("Enter your name : ")
    roll = input("Enter your Rollno : ")
    lec = input("Enter your lec attended : ")
    stud = ("name: "+name,"roll no : "+roll,"lec attended : "+lec)
    att += stud
    req = int(input("enter 1 to insert more data or enter 2 to see the available data: "))
    if(req==1):
        start = True
    else:
        print(att)
        start = False


