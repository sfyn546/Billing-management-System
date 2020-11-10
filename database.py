from tkinter import *
import mysql.connector

root=Tk()
root.title("E-corp")
root.geometry("400x400")

#database
db=mysql.connector.connect(host='localhost',user='root',passwd='')

#create cursor
c=db.cursor()

c.execute("show databases")
r=c.fetchone()
#create table
print(r)

    #print("yep")
#c.execute("INSERT INTO users VALUES('Mohd','Sufiyan','ms676@gmail.com','nerd','12345')")

#c.execute("DROP TABLE product")
#c.execute("CREATE TABLE product(pid INT,pname TEXT,price REAL,pdesc TEXT)")
#r=conn.execute("SELECT fname FROM users where lname='Sufiyan'")
#k=r.fetchone
#print(k)

#conn.row_factory = lambda cursor, row: row[0]
#c = conn.cursor()
#ids = c.execute('SELECT * FROM users where username ="nerd"').fetchall()
#print(ids)


#manager -username and password
#users- username and password
#product-pid,pname,price,pdescription







root.mainloop()
