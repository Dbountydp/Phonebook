from os import name
import mysql.connector as mconnect

sqlcon = mconnect.connect(host="localhost", user='root',
                          password='', database='my_db1')


def check_table():
    query = ' create table if not exists phonebook(id int primary key auto_increment,email varchar(250),name varchar(200),phoneNum varchar(12))'
    cur = sqlcon.cursor()
    cur.execute(query)


def query_ex(query):
    cur = sqlcon.cursor()
    print("\n<---- we are excuteing your request --->\n")
    cur.execute(query)
    return cur

# insert data


def update_data():
    ask_user = input("Email: ")
    forupdate = input("""what do you want to update
                      1.Phone Number
                      2.Email 
                      3.Name  
                        : """)
    if forupdate.strip() == "1":
        phone = input(" New Phone Number: rish")
        query = f'update  phonebook set phonenum="{phone}" where email="{ask_user}"'
        query_ex(query)
        print("Recored is Updated ")


def insert_data():

    email = input("Email: ")
    name = input("Name: ")
    phoneNum = input("Phone Number: ")

    query = f'insert into phonebook(email,name,phonenum) values("{email}","{name}","{phoneNum}")'
    query_ex(query)
    print(" you saved your data in phonebook\n")


# fetch all data
def fetch_data():
    query = 'select * from phonebook'
    data = query_ex(query)
    for ident, email, name, number in data:
        print(f"id: {ident}", f"email: {email}",
              f"name: {name}", f"number {number}", sep="\n")
        print()
# update contect


# remove data
def Remove_data():

    print('Deleteing Contact')

    email = input("Email : ")
    query = f"DELETE FROM phonebook where email='{email}'"

    confrom = input("\n you sure you want Delete it? [yes/no] : \n")
    if confrom.title().strip() == "Yes":

        query_ex(query)

        print(" If Its exits it will be Deleted ")

    elif confrom.title().strip() == "No":

        print(" okay deleteing cancel ")

    else:
        print("Choose the Right Option ")
# show contact
def show_contect():
    name = input("Name: ")
    query = f'select * from phonebook where name="{name}"'
    res = query_ex(query)
    for id, email,name,phone in res:
        print(" Possible result is: ")
            
        print(f'id: {id}',f'Email: {email}',f'Name: {name}',f'Phone Number: {phone}',sep="\n")
    


def welcome():

    print("\n<-----Phonebook------>\n")
    # call calling check_table() to check table
    # if table not exitis it will create a table
    check_table()
    TakeInput = input(""" What do you want 
                1. add New Conntect   
                2. Show all Contect
                3. delete contect
                4. update contect
                5. show a Entity
                : """)

    if TakeInput.strip() == "1":
        insert_data()
        sqlcon.commit()

    elif TakeInput.strip() == "2":
        fetch_data()

    elif TakeInput.strip() == "3":
        Remove_data()
    elif TakeInput.strip() == "4":
        update_data()
    elif TakeInput.strip() == "5":
        show_contect()  

    # elif TakeInput.strip() =="4":

    else:
        print(" plz select 1 or 2")


welcome()
while True:
    reapt = input("<--- Do you want to continue [yes/no]----> \n : ")
    if reapt.title().strip() == "Yes":
        welcome()
    if reapt.title().strip() == "No":
        print(" \n<---- see you again ----->\n")
        break

# res = query_ex('select * from phonebook where name="krishna"')
# if res is None:
#     print("sahdhfah")
# else:
#     for i in res:
#         print(i)

