import mysql.connector
import pandas as pd
global t1
conn = mysql.connector.connect(host='localhost', database='school', user='root', password='1234',autocommit=True)
cursor = conn.cursor()
def add_students():
    print('\n\nAdd New Student Screen')
    print('-'*120)
    a = input('Enter student Name : ')
    while True:
        b = int(input('Enter student Class : '))
        if b>12 or b<0:
            print("enter the value from 1 to 12")
            continue
        else:
            break
    while True:
        s = input('Enter student section :')
        if s>='A' and s<='Z' :
            break
        else:
            print("Enter a value from A to Z only ")
            continue
    insert = ("insert into student(name,class,section)""values(%s,%s,%s)")
    data= (a,b,s)
    cursor.execute(insert,data)
    print('\nNew Student added successfully \n\n')
    while True:
        print('Add New marks Screen')
        print('\n')
        cursor.execute('select * from marks')
        row2 = cursor.fetchall()
        df2 = pd.DataFrame(row2)
        last = df2[0].iloc[-1]
        laste = int(last)+1
        adm = laste
        while True:
            phy1 = int(input('Enter marks in Physics : '))
            chem1 =int(input('Enter marks in Chemistry : '))
            math1= int(input('Enter marks in maths : '))
            eng1 = int(input('Enter marks in English : '))
            comp1 = int(input('Enter marks in Computer : '))
            if phy1 >100 or chem1>100 or math1>100 or eng1>100 or comp1>100 or phy1<0 or chem1<0 or math1<0 or eng1<0 or comp1<0:
                print("\n\n!please enter the marks from 0 to 100 range!!\n\n")
                continue
            else :
                break
        val = (adm,phy1,chem1,math1,eng1,comp1)
        sql = "insert into marks (ad,phy,chem,math,eng,comp) values(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql,val)
        print('\nNew Marks added successfully\n\n')
        break
def search():
    name=input('Enter the name of the student: ')
    query="select name from student where name='"+name+"'"
    cursor.execute(query)
    rows=cursor.fetchall()
    a=0
    for i in rows:
        print("The given student is present\n\n")
        a = a+1
        break
    if a==0:
        print("\nThe studnet is not present\n\n")
def mod_st():
    print('Modify Student Information - Screen')
    print('-'*120)
    while True:
        cursor.execute('select * from student')
        row2 = cursor.fetchall()
        df2 = pd.DataFrame(row2)
        last = df2[0].iloc[-1]
        laste = int(last)
        adm1 = laste
        admno = input('Enter admission No (!from 101 and so on ):')
        if int(admno) < 101 or int(admno) > adm1 :
            print("\n!!please enter the admin no from 101 to ",adm1,"!!\n")
            continue
        else:
            break
    print('\n1.   Name  ')
    print('\n2.   Class  ')
    print('\n3.   Section  ')
    print('\n\n')
    choice = int(input('Enter your number of choice :'))
    field=''
    if choice ==1:
        field ='name'
    if choice == 2:
        field = 'class'
    if choice == 3:
        field = 'section'
    value =input('Enter new value :')
    sql ='update student set '+field+' ="'+value +'" where admno ='+admno+';'
    cursor.execute(sql)
    print('\nStudent Record Updated\n\n')
def mod_ma():
    print('Modify Student Information - Screen')
    print('-'*120)
    while True:
        cursor.execute('select * from marks')
        row2 = cursor.fetchall()
        df2 = pd.DataFrame(row2)
        last = df2[0].iloc[-1]
        laste = int(last)
        adm = laste
        admno = input('Enter admission No (!from 101 and so on): ')
        if int(admno) < 101 or int(admno) > adm :
            print("\n!!please enter the admin no from 101 to ",adm,"!!\n")
            continue
        else:
            break
    print('\n1.   physics  ')
    print('\n2.   chemistry  ')
    print('\n3.   math  ')
    print('\n4.   english')
    print('\n5.   computer')
    print('\n\n')
    choice = int(input('Enter your choice :'))
    field=''
    if choice ==1:
        field ='phy'
    if choice == 2:
        field = 'chem'
    if choice == 3:
        field = 'math'
    if choice == 4:
        field ='eng'
    if choice == 5:
        field = 'comp'
    value =input('Enter new value :')
    sql ='update marks set '+field+' ="'+value +'" where ad ='+admno+';'
    cursor.execute(sql)
    conn.close()
    print('\n\n\n Student Record Updated\n\n')
def report():
    cursor.execute('SELECT * FROM student')
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    cursor.execute('select * from marks')
    row2 = cursor.fetchall()
    df2 = pd.DataFrame(row2)
    na= input("enter the name of the student: ")
    if na in df.values:
        print("present")
        temp = df.loc[df[1] == na]
        temp = temp.squeeze()
        tadmno = temp.loc[0]
        temp2=df2.loc[df2[0]==tadmno]
        temp2=temp2.squeeze()
        avg = ((temp2.loc[1]+temp2.loc[2]+temp2.loc[3]+temp2.loc[4]+temp2.loc[5])/500)*100
        print("\n\n""          Sree Vidyanikethan International School, Tirupati          ""\n\n")
        print("student name :        ",(temp.loc[1]))
        print("student admission no  " ,(temp.loc[0]))
        print("class :               ",(temp.loc[2]))
        print("section :             ",(temp.loc[3]))
        print("\nmarks of the student: \n")
        print("physics :             ",(temp2.loc[1]))
        print("chemistry :           ",(temp2.loc[2]))
        print("math :                ",(temp2.loc[3]))
        print("english :             ",(temp2.loc[4]))
        print("computer :            ",(temp2.loc[5]))
        print("percentage :          ",(avg))
        if avg>30:
            print("The student passed")
        else:
            print("The student failed")
    else:
        print("\nThe given student is not there in the database or you have entered the wrong input")
while True:
    print("\n\nmenu\n")
    print("press 1 to add a new student and add marks for the new students: ")
    print("press 2 to search for the student: ")
    print("press 3 to modify student record: ")
    print("press 4 to modify student marks: ")
    print("press 5 to get student record: ")
    print("press 6 to exit the program: \n")
    t=input("enter your choice: ")
    print('\n')
    if t.isdigit() == True :
        if t=='1':
            add_students()
        if t=='2':
            search()
        if t=='3':
            mod_st()
        if t=='4':
            mod_ma()
        if t=='5':
            report()
        if t=='6':
            print("Thank You")
            break
    elif t.isdigit != True:
        print("wrong input") 
        print("!!Enter a number from 1 to 6!!")
        continue
    else:
        print("wrong input")
        
