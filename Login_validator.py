import pymysql as pyms
my_con = pyms.connect(host='127.0.0.1', user='root', passwd=('adedamola19.'), db=("login_db"))
print("Connection Successful")

myCousor=my_con.cursor()
print("done")

myCousor.execute( "CREATE DATABASE login_db")
print("db created successfully")

myCousor.execute("CREATE  TABLE login_tb(fullname VARCHAR(40), email_address VARCHAR(60), old_password VARCHAR(12), new_password VARCHAR(12))")
print("table created successfully")

# #populating the table
fullname = input("enter your fullname: ")
email_address = input("enter your email address")
old_password = input("enter your password: ")
new_password =  input("enter your new password: ")
my_query = "INSERT INTO login_tb (fullname, email_address, old_password, new_password) VALUES(%s, %s, %s, %s)"
# my_query="UPDATE login_tb SET new_password=%s WHERE old_password=%s"
val= (fullname, email_address, old_password, new_password)
myCousor.execute(my_query, val)
my_con.commit()
print()
print(myCousor.rowcount, "records inserted successfully")

# # login validator

count = 0
while count < 3:
    fullname=input("enter your fullname: ")
    new_password=input("enter your password: ")
    my_query= "SELECT fullname, new_password FROM login_tb WHERE fullname=%s AND new_password=%s"
    val= (fullname, new_password)
    myCousor.execute(my_query, val)
    reg= myCousor.fetchone()
    if reg:
        print("logged in successfully")
        break
    else:
        count +=1
        remaining = 3 - count
        if remaining > 0:
             print(f"invalid credentials! you have {3-count} login attempt")
        else:
            print("you have exceeded your login limit.")
            print("forgot password")
            fullname = input("enter your fullname again: ")
            email_address = input("enter your email: ")
            my_query = "SELECT * FROM login_tb WHERE fullname=%s AND email_address=%s"
            val = (fullname, email_address)
            myCousor.execute(my_query, val)
            user = myCousor.fetchone()
            # time.sleep(10)
            # count= 0

            if user:
                new_password = input("enter a newpassword: ")
                my_query = "UPDATE login_tb SET new_password=%s WHERE fullname=%s AND email_address=%s"
                val=(new_password, fullname, email_address)
                myCousor.execute(my_query, val)
                my_con.commit()
                print(myCousor.rowcount, "record update successfully")
            else:
              print(" User not found. Cannot reset password.")
  
           