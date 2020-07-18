try:
    import os
    from tkinter import*
    from tkinter import messagebox
    from PIL import ImageTk,Image
    import psycopg2
except:
    import subprocess
    subprocess.call([sys.executable, "-m", "pip", "install", "pillow"])
    subprocess.call([sys.executable, "-m", "pip", "install", "psycopg2"])

import os
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import psycopg2
from md5 import enc_md5

#create Login window
def Login_window():
    global login_screen
    login_screen = Tk()
    login_screen.geometry("1920x1080+0+0")
    login_screen.title("Account Login")

    #IMAGES
    bg_icon = ImageTk.PhotoImage(file = "login_system/plain_textured.jpg")
    User_icon = PhotoImage(file = "login_system/user_icon.png")
    pass_icon = PhotoImage(file = "login_system/pass_icon.png")
    logo_icon = PhotoImage(file = "login_system/logo.png")

    #set global variable
    global username_login_entry
    global password_login_entry
    global radio_verify

    #set the text variable
    password = StringVar()
    radio_verify = IntVar()

    #login GUI
    Label(login_screen,image = bg_icon).pack()

    title = Label(login_screen,text = "User Login", font = ("courier new",30,"bold"),bg = "LightBlue",fg="grey",bd=10,relief=RAISED)
    title.place(x=0,y=0,relwidth=1)

    Login_Frame = Frame(login_screen,bg = "white",bd=5,relief=GROOVE)
    Login_Frame.place(x = 510,y = 150) 

    Label(Login_Frame,image = logo_icon,bg="white").grid(row=0,columnspan=2,padx=20,pady=10)

    Label(Login_Frame,text = "Username",image = User_icon, compound = LEFT,font = ("courier new",20,"bold"),bg="white").grid(row=1,column=0,padx=10,pady=10)
    username_login_entry = Entry(Login_Frame,bd=3,relief=GROOVE,font = ("",15))
    username_login_entry.grid(row = 1,column = 1,padx = 15)

    Label(Login_Frame,text = "Password",image = pass_icon, compound = LEFT,font = ("courier new",20,"bold"),bg="white").grid(row=2,column=0,padx=10,pady=10)
    password_login_entry = Entry(Login_Frame,textvariable = password,bd=3,relief=GROOVE,font = ("",15),show="*")
    password_login_entry.grid(row = 2,column = 1,padx = 15)

    Radiobutton(Login_Frame,text="I am not robot",font = ("courier new",15,"bold"),value=1,variable=radio_verify,bg="white").grid(row=3,column=0,padx=25,pady=5)

    button = Button(Login_Frame,text = "Log In",command=lambda : user_verify(username_login_entry.get()),width = 20,font=("courier new",14,"bold"),bg="grey",fg="white",bd=3,relief=GROOVE)
    button.grid(row = 4,column = 1)

    Button(Login_Frame,text = "Register",width = 20,command = register,font=("courier new",14,"bold"),bg="grey",fg="white",bd=3,relief=GROOVE).grid(row = 4,column = 0)


    login_screen.mainloop() #runs the GUI


def login_verification():
    print("working..")

def user_verify(user_name):
    #print("name :", user_name)
  
    if radio_verify.get() != 1:
        robot() 

    if radio_verify.get() == 1:
        con = psycopg2.connect(
                dbname = "postgres",
                user="postgres",
                password="prathamesh_98",
                host="localhost",
                port="5432"
                )

        cursor = con.cursor()

        query = '''SELECT user_name FROM databases WHERE user_name=%s'''    
        cursor.execute(query,(user_name,))

        rows = cursor.fetchone()
        if rows == None:
            user_not_found()
        else:
            password = enc_md5(password_login_entry.get())
            password_verify(password)
            

        con.commit()

        con.close()


def password_verify(password):
    
    #print(password)

    con = psycopg2.connect(
                dbname = "postgres",
                user="postgres",
                password="prathamesh_98",
                host="localhost",
                port="5432"
                )

    cursor = con.cursor()

    query = '''SELECT password FROM databases WHERE user_name = 'prathamesh' AND password=%s'''   
    cursor.execute(query,(password,))

    rows = cursor.fetchone()
    if rows == None:
        password_not_recognised()
    else:
        login_success()
            

    con.commit()
    con.close()


def robot():

    global robot_screen
    robot_screen = Toplevel(login_screen)
    robot_screen.title("Error")
    robot_screen.geometry("170x100")

    Label(robot_screen,text="human verfication missing").pack()

    Button(robot_screen,text="OK",command=delete_robot).pack()


def delete_robot():
    robot_screen.destroy()


def login_success():

    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")

    Label(login_success_screen,text = "login successful").pack()

    Button(login_success_screen,text="OK",command=delete_login_success).pack()


def delete_login_success():
    login_success_screen.destroy()

def password_not_recognised():

    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Failure")
    password_not_recog_screen.geometry("150x100")

    Label(password_not_recog_screen,text="Invalid Password").pack()

    Button(password_not_recog_screen,text="OK",command=delete_password_not_recognised).pack()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def user_not_found(): 

    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error")
    user_not_found_screen.geometry("150x100")

    Label(user_not_found_screen,text="User not found").pack()

    Button(user_not_found_screen,text="OK",command=delete_user_not_found_screen).pack()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

    


#create register window
def register():
    global register_screen
    register_screen = Toplevel(login_screen)
    register_screen.title("Register")
    register_screen.geometry("800x700")

    #set global variables
    global username
    global password
    global password_entry
    global username_entry
    global register_Frame
    global tc_verify

    #set variables
    username = StringVar()
    password = StringVar()
    tc_verify = IntVar()


    #images
    small_logo_icon = PhotoImage(file = "login_system/small_logo.png")

    #Registration GUI
    Label(register_screen,bg="white").pack()

    title = Label(register_screen,text = "User Registration", font = ("courier new",20,"bold"),bg = "LightBlue",fg="grey",bd=10,relief=RAISED)
    title.place(x=0,y=0,relwidth=1)

    register_Frame = Frame(register_screen,bg = "white",bd=5,relief=GROOVE)
    register_Frame.place(x = 150 ,y = 100) 

    username_label = Label(register_Frame,text = "New Username",font = ("courier new",20,"bold"),bg="white")
    username_label.grid(row=1,column=0,padx=10,pady=20)
    username_entry = Entry(register_Frame,textvariable = username,bd=3,relief=GROOVE,font = ("",15))
    username_entry.grid(row = 1,column = 1,padx = 15,pady = 20)

    password_label = Label(register_Frame,text = "New Password",font = ("courier new",20,"bold"),bg="white")
    password_label.grid(row=2,column=0,padx=10,pady=20)
    password_entry = Entry(register_Frame,textvariable = password,bd=3,relief=GROOVE,font = ("",15),show="*")
    password_entry.grid(row = 2,column = 1,padx = 15,pady=20)

    Label(register_Frame,text = "terms and conditions*",font=("courier new",12),bg="white").grid(row=3,column=0)
    Radiobutton(register_Frame,text="Agree",value=1,variable=tc_verify,bg="white").grid(row=4,column=0,pady=10)
    Radiobutton(register_Frame,text="Disagree",value=2,variable=tc_verify,bg="white").grid(row=4,column=1,pady=10)

    button = Button(register_Frame,text = "Register",width = 20,command =lambda : register_user(username_entry.get(),password_entry.get()),font=("courier new",14,"bold"),bg="grey",fg="white",bd=3,relief=GROOVE)
    button.grid(row = 5,column = 1)


#saving the data of new user
def register_user(user_name,password):
    #print("name : ",user)
    #print("password : ",password)

    password = enc_md5(password)

    if tc_verify.get() != 1:
        terms()

    if tc_verify.get() == 1:
        con = psycopg2.connect(
            dbname = "postgres",
            user="postgres",
            password="prathamesh_98",
            host="localhost",
            port="5432"
            )

        cursor = con.cursor()
        query = '''INSERT INTO databases(user_name,password) VALUES(%s,%s)'''
        cursor.execute(query,(user_name,password))

        print("data saved")

        con.commit()

        con.close()


def terms():

    global terms_screen
    terms_screen = Toplevel(register_screen)
    terms_screen.title("Error")
    terms_screen.geometry("150x100")

    Label(terms_screen,text="please agree T&C").pack()

    Button(terms_screen,text="OK",command=delete_terms).pack()

    
def delete_terms():
    terms_screen.destroy()

Login_window() #calling function


