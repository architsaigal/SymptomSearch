import mysql.connector as mydb
from prettytable import PrettyTable
from matplotlib import pyplot as plt

db = mydb.connect(host="localhost",user="root",passwd="root")

cur = db.cursor(buffered=True)

def CreateDatabase():
    cur.execute("CREATE DATABASE IF NOT EXISTS HALLOTHON;")

def UseDatabase():
    cur.execute("USE HALLOTHON;")

def CreateTable():
    cur.execute("""CREATE TABLE IF NOT EXISTS DISEASES(DISEASE VARCHAR(30), SYMPTOM1 VARCHAR(30), SYMPTOM2 VARCHAR(30), SYMPTOM3 VARCHAR(30),
                   SYMPTOM4 VARCHAR(30),PRIMARY KEY(DISEASE))""")
    db.commit()
            
def ShowTables():
    cur.execute("SHOW TABLES;")
    rows=cur.fetchall()
    y=PrettyTable(["Table Name"])
    for i in rows:
        y.add_row([i])
    print(y)

def DescribeTable():
    cur.execute("DESC DISEASES;")
    rows=cur.fetchall()
    y=PrettyTable(["Field","Type","Null","Key","Default","Extra"])
    for a,b,c,d,e,f in rows:
        y.add_row([a,b,c,d,e,f])
    print(y)

def InsertData():
    d= input("Enter Disease: ")
    s1= input("Enter Symptom 1: ")
    s2= input("Enter Symptom 2: ")
    s3= input("Enter Symptom 3: ")
    s4= input("Enter Symptom 4: ")
    cur.execute("INSERT INTO DISEASES VALUES('{}','{}','{}','{}','{}');".format(d,s1,s2,s3,s4))
    print("Data Inserted")
    db.commit()

def DisplayAllData():
    cur.execute("SELECT * FROM DISEASES")
    rows=cur.fetchall()
    y=PrettyTable(["Disease","Symptom 1","Symptom 2","Symptom 3", "Symptom 4"])
    for a,b,c,d,e in rows:
        y.add_row([a,b,c,d,e])
    print(y)

def SearchForDisease():
    count=0
    L=[]
    print("Enter a minimum of 2 symptoms and NA if Not Applicable")
    s1= input("Enter Symptom 1: ")
    s2= input("Enter Symptom 2: ")
    s3= input("Enter Symptom 3: ")
    s4= input("Enter Symptom 4: ")
    t1= cur.execute("SELECT DISEASE FROM DISEASES WHERE SYMPTOM1='{}' OR SYMPTOM2='{}' OR SYMPTOM3='{}' OR SYMPTOM4='{}';".format(s1,s1,s1,s1))
    rows=cur.fetchall()
    y = PrettyTable(["Possible Disease"])
    for a in rows:
        L.append(a)
        print(L)
        y.add_row([a])
    print(y)
    t2= cur.execute("SELECT DISEASE FROM DISEASES WHERE SYMPTOM1='{}' OR SYMPTOM2='{}' OR SYMPTOM3='{}' OR SYMPTOM4='{}';".format(s2,s2,s2,s2))
    rows=cur.fetchall()
    y = PrettyTable(["Possible Disease"])
    for a in rows:
        L.append(a)
        print(L)
        y.add_row([a])
    print(y)
    t3= cur.execute("SELECT DISEASE FROM DISEASES WHERE SYMPTOM1='{}' OR SYMPTOM2='{}' OR SYMPTOM3='{}' OR SYMPTOM4='{}';".format(s3,s3,s3,s3))
    rows=cur.fetchall()
    y = PrettyTable(["Possible Disease"])
    for a in rows:
        L.append(a)
        print(L)
        y.add_row([a])
    print(y)
    t4= cur.execute("SELECT DISEASE FROM DISEASES WHERE SYMPTOM1='{}' OR SYMPTOM2='{}' OR SYMPTOM3='{}' OR SYMPTOM4='{}';".format(s4,s4,s4,s4))
    rows=cur.fetchall()
    y = PrettyTable(["Possible Disease"])
    for a in rows:
        L.append(a)
        print(L)
        y.add_row([a])
    print(y)
    print(L.count(('Covid',)))
    D={'Covid':L.count(('Covid',)),'Dengue':L.count(('Dengue',)), 'Influenza':L.count(('Influenza',)), 'Jaundice':L.count(('Jaundice',)),
       'Malaria':L.count(('Malaria',)), 'Typhoid':L.count(('Typhoid',)),'Thyroid':L.count(('Thyroid',)),'Cholera':L.count(('Cholera',))}
    print(D)
    print(list(D.values()))
    print(list(D.keys()))
    for i in D:
        if D[i]==4:
            print(i)
        elif D[i]==3:
            print(i)
        elif D[i]==2:
            print(i)

    numb= list(D.values())
    plt.axis('equal')
    plt.title("Disease Risk Chart")
    dis= list(D.keys())
    plt.pie(numb, labels=dis, colors=['r','b','g','c','y','b'],autopct="%1.2f%%")
    plt.show()

    
#__main__

while True:
    print("1. Create Database Hallothon")
    print("2. Create Table")
    print("3. Show Created Tables: ")
    print("4. View Table Structure")
    print("5. Insert Disease Data")
    print("6. Display All The Data")
    print("7. Search for a Disease")
    
    print("99. Exit")

    choice= int(input("Enter option: "))

    if choice==1:
        CreateDatabase()

    elif choice==2:
        UseDatabase()
        CreateTable()

    elif choice==3:
        UseDatabase()
        ShowTables()

    elif choice==4:
        UseDatabase()
        DescribeTable()

    elif choice==5:
        UseDatabase()
        InsertData()

    elif choice==6:
        UseDatabase()
        DisplayAllData()

    elif choice==7:
        UseDatabase()
        SearchForDisease()

    
    elif choice==99:
        break
    
    
db.commit()
    
    
