from tkinter import *
import random
from tkinter.messagebox import showerror,showinfo
import sqlite3


class Application(Toplevel):
        

    def __init__(self, master=None):

        Toplevel.__init__(self, master)

        
        self.geometry("1520x790+0+0")
        self.title ("E-Corp Login")



        self.resizable(False, False)


        self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
        self.left.pack(side=TOP)


        self.photo1 = PhotoImage(file='ecorp.png')
        self.photo1=(self.photo1).subsample(2,2)
        self.pic = Label(self.left, font=('arial' , 1 , 'bold'), image= self.photo1,bg='lightblue')
        self.pic.place(x=-0, y=0)



        self.heading = Label(self.left,font=('arial' , 100 , 'bold'), text="E-Corp", fg='black', bg='lightblue' ,anchor='w')
        self.heading.place(x=550, y=0)



        self.username = Label(self.left, text="Username: ", font=('arial 30 bold'), fg='black', bg='lightblue')
        self.username.place(x=546, y=350)
        


        self.password = Label(self.left, text="Password: ", font=('arial 30 bold'), fg='black', bg='lightblue')
        self.password.place(x=550, y=410)
       



        self.username_ent = Entry(self.left,font=('arial' , 20 ))
        self.username_ent.place(x=755, y=360)



        self.password_ent = Entry(self.left, font=('arial' , 20 ),show='*')
        self.password_ent.place(x=755, y=420)



        self.login = Button(self.left,font=('arial' , 17 , 'bold'), text="LOGIN", bg='lightgreen',width=8,command=self._login_btn_clicked)
        self.login.place(x=940, y=480)



        
        
    def _login_btn_clicked(self):

            username = self.username_ent.get()
            password = self.password_ent.get()

            conn=sqlite3.connect('E_corp.db')
            c=conn.cursor()
            c.execute("SELECT * FROM manager WHERE username=? AND password=?",(username,password))

            

            if c.fetchall():

                    conn.close()
                    showinfo("Login Success", "Welcome to dashboard "+username)
                    

                    Button(self, text="Go to main page")
                    self.destroy()
                    Manager()
                    #self.deiconify()
                    

                    
            else:

                    conn=sqlite3.connect('E_corp.db')
                    c=conn.cursor()
                    c.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
                    
                    if c.fetchall():
                            conn.close()
                            showinfo("Login Success", "Welcome back "+username)
                            
                    #self.withdraw()
                            Button(self, text="Go to main page")
                            self.destroy()
                            user()
                            #self.deiconify()
                            #self.withdraw()
                            

                    else:

                             showerror("Login error", "Incorrect username or Password")
                             #self.withdraw()

                             #self.deiconify()






class Manager(Toplevel):
        def __init__(self,master=None):
                Toplevel.__init__(self, master)
                self.geometry("1520x790+0+0")
                self.title ("E-Corp ADMIN")



                self.resizable(False, False)


                self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
                self.left.pack(side=TOP)


                self.photo1 = PhotoImage(file='ecorp.png')
                self.photo1=(self.photo1).subsample(2,2)
                self.pic = Label(self.left, font=('arial' , 1 , 'bold'), image= self.photo1,bg='lightblue')
                self.pic.place(x=-0, y=80)


                self.loadimage = PhotoImage(file="add-user.png").subsample(3,3)
                self.add_user_btn =Button(self, image=self.loadimage,command=self.adduser_window)
                self.add_user_btn["bg"] = "lightblue"
                self.add_user_btn["border"] = "0"
                self.add_user_btn.place(x=550,y=80)
                self.add_user_label=Label(self.left,text="Add user", font=('arial 20 bold'), fg='black', bg='lightblue')
                self.add_user_label.place(x=570,y=260)
                
                
                self.loadimage2 = PhotoImage(file="remove-user.png").subsample(3,3)
                self.rem_user_btn =Button(self, image=self.loadimage2,command=self.callrem)
                self.rem_user_btn["bg"] = "lightblue"
                self.rem_user_btn["border"] = "0"
                self.rem_user_btn.place(x=800,y=80)
                self.rem_user_label=Label(self.left,text="Remove user", font=('arial 20 bold'), fg='black', bg='lightblue')
                self.rem_user_label.place(x=810,y=260)


                self.loadimage3 = PhotoImage(file="up_user.png").subsample(3,3)
                self.up_user_btn =Button(self, image=self.loadimage3,command=self.callupuser)
                self.up_user_btn["bg"] = "lightblue"
                self.up_user_btn["border"] = "0"
                self.up_user_btn.place(x=1050,y=80)
                self.up_user_label=Label(self.left,text="Update user", font=('arial 20 bold'), fg='black', bg='lightblue')
                self.up_user_label.place(x=1065,y=260)
                

                self.loadimage4 = PhotoImage(file="logout.png").subsample(3,3)
                self.logout_btn =Button(self, image=self.loadimage4,command=self.closeit)
                self.logout_btn["bg"] = "lightblue"
                self.logout_btn["border"] = "0"
                self.logout_btn.place(x=1300,y=190)
                self.logout_label=Label(self.left,text="Logout", font=('arial 20 bold'), fg='black', bg='lightblue')
                self.logout_label.place(x=1310,y=385)


                self.loadimage5 = PhotoImage(file="add-to-cart.png").subsample(3,3)
                self.add_prod_btn =Button(self, image=self.loadimage5,command=self.calladdprod)
                self.add_prod_btn["bg"] = "lightblue"
                self.add_prod_btn["border"] = "0"
                self.add_prod_btn.place(x=550,y=80+260)
                self.add_prod_label=Label(self.left,text="Add Product", font=('arial 20 bold'), fg='black', bg='lightblue')
                self.add_prod_label.place(x=560,y=260+260)
                
                
                self.loadimage6 = PhotoImage(file="rem-pro.png").subsample(3,3)
                self.rem_prod_btn =Button(self, image=self.loadimage6,command=self.callrempro)
                self.rem_prod_btn["bg"] = "lightblue"
                self.rem_prod_btn["border"] = "0"
                self.rem_prod_btn.place(x=800,y=80+260)
                self.rem_prod_label=Label(self.left,text="Remove Product", font=('arial 20 bold'), fg='black', bg='lightblue')
                self.rem_prod_label.place(x=790,y=260+260)


                self.loadimage7 = PhotoImage(file="update_prod.png").subsample(3,3)
                self.up_prod_btn =Button(self, image=self.loadimage7,command=self.callupprod)
                self.up_prod_btn["bg"] = "lightblue"
                self.up_prod_btn["border"] = "0"
                self.up_prod_btn.place(x=1050,y=80+260)
                self.up_prod_label=Label(self.left,text="Update Product", font=('arial 20 bold'), fg='black', bg='lightblue')
                self.up_prod_label.place(x=1050,y=260+260)


                self.newadminbtn=Button(self,bg="lightgreen",text="Add new admin",font=('arial 15 bold'),fg='white',command=self.admin_entry)
                self.newadminbtn.place(x=1300,y=650)


        def admin_entry(self):
                adminadd(self)



        def callrempro(self):

                remprod(self)


        def callupprod(self):
                upprod(self)
        def calladdprod(self):
                addprod(self)


        def callupuser(self):
                upuser(self)
        
        def callrem(self):
                remuser(self)

        def adduser_window(self):
                adduser(self)

        def closeit(self):
                self.destroy()
                Application()
                








class adminadd(Toplevel):
        def __init__(self,master=None):
                Toplevel.__init__(self, master)
                self.geometry("500x500+550+80")
                self.title ("E-Corp ADMIN")

                self.resizable(False, False)




                self.u_name=Entry(self,font=('arial',20))
                self.u_name.place(x=165,y=40)
                self.l=Label(self,font=('arial' , 20 ),text="Username: ")
                self.l.place(x=20,y=40)
                        
                self.passw=Entry(self,font=('arial',20),show="*")
                self.passw.place(x=165,y=100)
                self.lb=Label(self,font=('arial' , 20 ),text="Password: ")
                self.lb.place(x=20,y=100)


                self.btn=Button(self,font=('arial' , 20 , 'bold'), text="Add user", bg='lightgreen',height=1,width=10,command=self.add_new_admin)
                self.btn.place(x=300,y=170)
                        



        def add_new_admin(self):
                uname=self.u_name.get()
                pwd=self.passw.get()


                if(self.checkentry(uname)==True):


                        conn=sqlite3.connect('E_corp.db')
                        conn.cursor()

                        

                        my_data=(uname,pwd)

                        print(my_data)

                        q="INSERT INTO manager VALUES(?,?)"


                        success_flg = True
                        try:
                                conn.execute(q,my_data)
                                conn.commit()
                                conn.close()

                        
                        except:
                                success_flg = False
                                print("error")

                        
                        if(success_flg==True):
                                self.withdraw()
                                showinfo("seccess","Admin added successfully")

                else:
                        showerror("Error","Username already taken")    





        def checkentry(self,name):
                conn=sqlite3.connect('E_corp.db')
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                
                ids = c.execute('SELECT username FROM manager where username=?',(name,)).fetchall()
                conn.commit()

                conn.close()
                if len(ids)==0:
                        return True

                else:
                        return False


        








class adduser(Toplevel):
        def __init__(self,master=None):
                Toplevel.__init__(self, master)
                self.geometry("500x500+550+80")
                self.title ("E-Corp ADMIN")

                self.resizable(False, False)




                self.first_name=Entry(self,font=('arial',20))
                self.first_name.place(x=165,y=40)
                self.l=Label(self,font=('arial' , 20 ),text="Firstname: ")
                self.l.place(x=20,y=40)
                        
                self.last_name=Entry(self,font=('arial',20))
                self.last_name.place(x=165,y=100)
                self.lb=Label(self,font=('arial' , 20 ),text="Lastname: ")
                self.lb.place(x=20,y=100)
                        


                self.username=Entry(self, font=('arial' , 20 ))
                self.username.place(x=165,y=160)
                self.l1=Label(self,font=('arial' , 20 ),text="Username: ")
                self.l1.place(x=20,y=160)
                self.passwd=Entry(self, font=('arial' , 20 ),show='*')
                self.passwd.place(x=165,y=220)
                self.l2=Label(self,font=('arial' , 20 ),text="Password: ")
                self.l2.place(x=20,y=220)
                self.email=Entry(self, font=('arial' , 20 ))
                self.email.place(x=165,y=280)
                self.l3=Label(self,font=('arial' , 20 ),text="E-mail : ")
                self.l3.place(x=20,y=280)

                self.btn=Button(self,font=('arial' , 20 , 'bold'), text="Add user", bg='lightgreen',height=1,width=10,command=self.adduserdata)
                self.btn.place(x=300,y=340)







        def adduserdata(self):

                uname=self.username.get()
                pwd=self.passwd.get()
                fname=self.first_name.get()
                lname=self.last_name.get()
                mail=self.email.get()


                if(self.checkentry(uname)==True):
                        #print("hj")

                        conn=sqlite3.connect('E_corp.db')
                        conn.cursor()

                        

                        my_data=(fname,lname,mail,uname,pwd)

                        print(my_data)

                        q="INSERT INTO users VALUES(?,?,?,?,?)"


                        success_flg = True
                        try:
                                conn.execute(q,my_data)
                                conn.commit()
                                conn.close()

                        
                        except:
                                success_flg = False
                                print("error")

                        
                        if(success_flg==True):
                                self.withdraw()
                                showinfo("seccess","User added successfully")

                else:
                        showerror("Error","Username already taken")    

                        
                        

        def checkentry(self,name):
                conn=sqlite3.connect('E_corp.db')
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                
                ids = c.execute('SELECT username FROM users where username=?',(name,)).fetchall()
                conn.commit()

                conn.close()
                if len(ids)==0:
                        return True

                else:
                        return False


        







class upuser(Toplevel):
        def __init__(self,master=None):
                Toplevel.__init__(self, master)
                self.geometry("500x500+550+80")
                self.title ("E-Corp ADMIN")

                self.resizable(False, False)


                self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
                self.left.pack(side=TOP)


                self.first_name=Entry(self,font=('arial',20))
                self.first_name.place(x=165,y=40)
                self.l=Label(self,font=('arial' , 20 ),text="Firstname: ")
                self.l.place(x=20,y=40)
                        
                self.last_name=Entry(self,font=('arial',20))
                self.last_name.place(x=165,y=100)
                self.lb=Label(self,font=('arial' , 20 ),text="Lastname: ")
                self.lb.place(x=20,y=100)
                        


                self.username=Entry(self, font=('arial' , 20 ))
                self.username.place(x=165,y=160)
                self.l1=Label(self,font=('arial' , 20 ),text="Username: ")
                self.l1.place(x=20,y=160)
                self.email=Entry(self, font=('arial' , 20 ))
                self.email.place(x=165,y=220)
                self.l3=Label(self,font=('arial' , 20 ),text="E-mail : ")
                self.l3.place(x=20,y=220)

                self.btn=Button(self,font=('arial' , 20 , 'bold'), text="Update user", bg='lightgreen',height=1,width=10,command=self.upuserdata)
                self.btn.place(x=300,y=280)







        def upuserdata(self):

                uname=self.username.get()

                fname=self.first_name.get()
                lname=self.last_name.get()
                mail=self.email.get()

                
                
                
                if(self.checkentry(uname)==True):
                        showerror("Error404","No such user")
                        

                else:

                        conn=sqlite3.connect('E_corp.db')
                        conn.cursor()

                        

                        my_data=(fname,lname,mail,uname)

                        print(my_data)

                        q="UPDATE users SET fname=?,lname=?,email=? WHERE username=?"


                        success_flg = True
                        try:
                                conn.execute(q,my_data)
                                conn.commit()
                                conn.close()

                        
                        except:
                                success_flg = False
                                print("error")
                                conn.close()

                        
                        if(success_flg==True):
                                self.withdraw()
                                showinfo("seccess","User updated successfully")


        def checkentry(self,uname):
                conn=sqlite3.connect('E_corp.db')
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                ids = c.execute('SELECT * FROM users WHERE username=?',(uname,)).fetchall()
                conn.commit()

                conn.close()
                if len(ids)==0:
                        return True

                else:
                        return False


class remuser(Toplevel):

        def __init__(self,master=None):

                Toplevel.__init__(self, master)
                self.geometry("500x400+550+80")
                self.title ("E-Corp ADMIN")

                self.resizable(False, False)


                self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
                self.left.pack(side=TOP)


                self.uname=Entry(self,font=('arial',20))
                self.uname.place(x=165,y=40)
                self.l=Label(self,font=('arial' , 20 ),text="Username: ")
                self.l.place(x=20,y=40)

                self.btn=Button(self,font=('arial' , 20 , 'bold'), text="Remove user", bg='red',height=1,width=10,command=self.remuserdata)
                self.btn.place(x=70,y=120)


        def remuserdata(self):
                name=str(self.uname.get())






                if(self.checkentry(name)==True):
                        showerror("Error404","No such user")


                else:

                        conn=sqlite3.connect('E_corp.db')

                        
                        mydata=(name,)


                        success_flg=True

                        try:
                                conn.execute("DELETE FROM users where username=?",mydata)
                                conn.commit()
                                conn.close()

                        
                        except sqlite3.Error as my_error:
                                success_flg = False
                                print("error",my_error)

                        
                        if(success_flg==True):
                                self.destroy()
                                showinfo("Success","User Removed successfully")

                        else:
                                showerror("error","no user found")

        def checkentry(self,uname):
                conn=sqlite3.connect('E_corp.db')
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                ids = c.execute('SELECT * FROM users WHERE username=?',(uname,)).fetchall()
                conn.commit()

                conn.close()
                if len(ids)==0:
                        return True

                else:
                        return False




class addprod(Toplevel):
        def __init__(self,master=None):
                Toplevel.__init__(self, master)
                self.geometry("500x500+550+80")
                self.title ("E-Corp ADMIN")

                self.resizable(False, False)


                self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
                self.left.pack(side=TOP)


                self.pid=Entry(self,font=('arial',20))
                self.pid.place(x=165,y=40)
                self.l=Label(self,font=('arial' , 20 ),text="Prod-ID: ",bg="lightblue")
                self.l.place(x=20,y=40)
                        
                self.p_name=Entry(self,font=('arial',20))
                self.p_name.place(x=165,y=100)
                self.lb=Label(self,font=('arial' , 16 ),text="ProductName: ",bg="lightblue")
                self.lb.place(x=20,y=105)
                        


                self.pdesc=Entry(self, font=('arial' , 20 ))
                self.pdesc.place(x=165,y=160)
                self.l1=Label(self,font=('arial' , 16 ),text="Description: ",bg="lightblue")
                self.l1.place(x=20,y=165)

                self.rate=Entry(self, font=('arial' , 20 ))
                self.rate.place(x=165,y=220)
                self.l2=Label(self,font=('arial' , 20 ),text="Price: ",bg="lightblue")
                self.l2.place(x=10,y=220)

                self.btn=Button(self,font=('arial' , 20 , 'bold'), text="Add Product", bg='lightgreen',height=1,width=10,command=self.addproddata)
                self.btn.place(x=300,y=340)







        def addproddata(self):

                id=int(self.pid.get())
                name=self.p_name.get()
                des=self.pdesc.get()
                price=float(self.rate.get())



                if(self.checkentry(id)==True):

                        conn=sqlite3.connect('E_corp.db')
                        conn.cursor()

                        

                        my_data=(id,name,price,des)

                        print(my_data)

                        q="INSERT INTO product VALUES(?,?,?,?)"


                        success_flg = True
                        try:
                                conn.execute(q,my_data)
                                conn.commit()
                                conn.close()

                        
                        except:
                                success_flg = False
                                print("error")

                        
                        if(success_flg==True):
                                self.destroy()
                                showinfo("Success","Product added successfully")

                else:
                        showerror("Error","Product already present")
                        
                        


        def checkentry(self,idh):

                conn=sqlite3.connect('E_corp.db')
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                
                ids = c.execute('SELECT pid FROM product where pid=?',(idh,)).fetchall()
                conn.commit()

                conn.close()
                if len(ids)==0:
                        return True

                else:
                        return False







class upprod(Toplevel):
        def __init__(self,master=None):
                Toplevel.__init__(self, master)
                self.geometry("500x500+550+80")
                self.title ("E-Corp ADMIN")

                self.resizable(False, False)


                self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
                self.left.pack(side=TOP)





                self.pid=Entry(self,font=('arial',20))
                self.pid.place(x=175,y=40)
                self.l=Label(self,font=('arial' , 20 ),text="Prod-ID: ")
                self.l.place(x=20,y=40)
                        
                self.p_name=Entry(self,font=('arial',20))
                self.p_name.place(x=175,y=100)
                self.lb=Label(self,font=('arial' , 15 ),text="ProductName: ")
                self.lb.place(x=20,y=100)
                        


                self.pdesc=Entry(self, font=('arial' , 20 ))
                self.pdesc.place(x=175,y=160)
                self.l1=Label(self,font=('arial' , 17 ),text="Description: ")
                self.l1.place(x=20,y=160)

                self.rate=Entry(self, font=('arial' , 20 ))
                self.rate.place(x=175,y=220)
                self.l2=Label(self,font=('arial' , 20 ),text="Price: ")
                self.l2.place(x=20,y=220)





                self.btn=Button(self,font=('arial' , 15 , 'bold'), text="Update Product", bg='lightgreen',height=1,width=15,command=self.upproddata)
                self.btn.place(x=300,y=280)







        def upproddata(self):

                id=int(self.pid.get())
                name=self.p_name.get()
                des=self.pdesc.get()
                price=float(self.rate.get())



                if(self.checkentry(id)==True):

                        conn=sqlite3.connect('E_corp.db')
                        conn.cursor()

                        

                        my_data=(name,des,price,id)

                        print(my_data)

                        q="UPDATE product SET pname=?,pdesc=?,price=? WHERE pid=?"


                        success_flg = True
                        try:
                                conn.execute(q,my_data)
                                conn.commit()
                                conn.close()

                        
                        except:
                                success_flg = False
                                print("error")
                                conn.close()

                        
                        if(success_flg==True):
                                self.withdraw()
                                showinfo("Success","Product updated successfully")



                else:
                        showerror("Error","No such product.")


        def checkentry(self,idh):

                conn=sqlite3.connect('E_corp.db')
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                
                ids = c.execute('SELECT pid FROM product where pid=?',(idh,)).fetchall()
                conn.commit()

                conn.close()
                if len(ids)==0:
                        return False

                else:
                        return True



class remprod(Toplevel):

        def __init__(self,master=None):

                Toplevel.__init__(self, master)
                self.geometry("500x400+550+80")
                self.title ("E-Corp ADMIN")

                self.resizable(False, False)


                self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
                self.left.pack(side=TOP)


                self.id=Entry(self,font=('arial',20))
                self.id.place(x=165,y=40)
                self.l=Label(self,font=('arial' , 20 ),text="Prod_id: ")
                self.l.place(x=20,y=40)

                self.btn=Button(self,font=('arial' , 20 , 'bold'), text="Remove Product", bg='red',height=1,width=15,command=self.remproddata)
                self.btn.place(x=70,y=120)


        def remproddata(self):
                name=int(self.id.get())



                if(self.checkentry(name)==True):
                        showerror("Error","No such product.")


                else:


                        conn=sqlite3.connect('E_corp.db')

                        
                        mydata=(name,)


                        success_flg=True

                        try:
                                conn.execute("DELETE FROM product where pid=?",mydata)
                                conn.commit()
                                conn.close()

                        
                        except sqlite3.Error as my_error:
                                success_flg = False
                                print("error",my_error)

                        
                        if(success_flg==True):
                                self.withdraw()
                                showinfo("Success","Product Removed successfully")


        
        def checkentry(self,idh):

                conn=sqlite3.connect('E_corp.db')
                conn.row_factory = lambda cursor, row: row[0]
                c = conn.cursor()
                
                ids = c.execute('SELECT pid FROM product where pid=?',(idh,)).fetchall()
                conn.commit()

                conn.close()
                if len(ids)==0:
                        return True

                else:
                        return False

                        


class user(Toplevel):
        def __init__(self,master=None):
                Toplevel.__init__(self, master)
                self.geometry("1520x790+0+0")
                self.title ("E-Corp User-panel")



                self.resizable(False, False)


                self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
                self.left.pack(side=TOP)


                self.photo1 = PhotoImage(file='ecorp.png')
                self.photo1=(self.photo1).subsample(2,2)
                self.pic = Label(self.left, font=('arial' , 1 , 'bold'), image= self.photo1,bg='lightblue')
                self.pic.place(x=10, y=80)








                self.loadimage = PhotoImage(file="receipt.png").subsample(2,2)
                self.add_user_btn =Button(self, image=self.loadimage,command=self.billing)
                self.add_user_btn["bg"] = "lightblue"
                self.add_user_btn["border"] = "0"
                self.add_user_btn.place(x=600,y=80)
                self.add_user_label=Label(self.left,text="Create Bill", font=('arial 28 bold'), fg='black', bg='lightblue')
                self.add_user_label.place(x=630,y=340)

                self.loadimage2 = PhotoImage(file="settings.png").subsample(2,2)
                self.rem_user_btn =Button(self, image=self.loadimage2,command=self.billing)
                self.rem_user_btn["bg"] = "lightblue"
                self.rem_user_btn["border"] = "0"
                self.rem_user_btn.place(x=1000,y=80)

                self.rem_user_label=Label(self.left,text="User-Settings", font=('arial 28 bold'), fg='black', bg='lightblue')
                self.rem_user_label.place(x=1010,y=340)




        def billing(self):
                print("helllo world")



                



class Root(Toplevel):
        

    def __init__(self, master=None):
    
        Toplevel.__init__(self, master)
        
        
        self.geometry("1520x790+0+0")
        self.title ("E-Corp System")
        

        
        self.resizable(False, False)

        
        self.left = Frame(self, width= 1600, height= 900, bg='lightblue',relief=SUNKEN)
        self.left.pack(side=TOP)

       
        self.photo1 = PhotoImage(file='ecorp.png')
        self.photo1=(self.photo1).subsample(2,2)
        self.pic = Label(self.left, font=('arial' , 1 , 'bold'), image= self.photo1,bg='lightblue')
        self.pic.place(x=20, y=50)



        self.heading = Label(self.left,font=('arial' , 100 , 'bold'), text="E-Corp", fg='black', bg='lightblue' ,anchor='w')
        self.heading.place(x=550, y=0)

        self.mainIcon=PhotoImage(file="user.png").subsample(2,2)
        self.mainIcon2=PhotoImage(file="group-profile-users.png").subsample(2,2)
        
        self.bt1=Button(self,font=('arial',20,'bold'),text="ADMIN",image=self.mainIcon,compound=TOP,command=self.mic,bg="lightblue")
        self.bt1.place(x=550,y=250)
        self.bt1["border"]="0"
        self.bt2=Button(self,text="USER",font=('arial',20,'bold'),image=self.mainIcon2,compound=TOP,command=self.niv,bg="lightblue")
        self.bt2["border"]="0"
        self.bt2.place(x=900,y=250)




    def mic(self):
            print("button pressed")
            self.withdraw()
            Application(self)
            self.deiconify()

    def niv(self):
            self.withdraw()
            Application(self)
            self.deiconify()

