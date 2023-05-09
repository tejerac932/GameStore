from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from features.background import *

def delete(): 
    global game_info, con,cur,root,games_rented,games_table

    # Window
    root = Toplevel()
    root.title("Game Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # SQLite server
    con = sql.connect("db.db")
    cur = con.cursor()

    # Tables
    games_rented = "games_rented"
    games_table = "games"
   
    # Background
    background  = Background(root,"images/gameover.jpg")
    background.pack(fill=BOTH, expand=YES)

    # Heading
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Delete Game", bg='black', fg='white', font=('System',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    # Input
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.44,relwidth=0.8,relheight=0.05)   
    lb2 = Label(labelFrame,text="Game ID : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.3)
    game_info = Entry(labelFrame)
    game_info.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    # Submit 
    SubmitBtn = Button(root,text="SUBMIT",bg='#397b44', fg='black',command= delete_game)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit
    quitBtn = Button(root,text="QUIT",bg='#983535', fg='black',  command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def delete_game():
    
    gid = game_info.get()
    delete_entry = "delete from "+games_table+" where gid = '"+gid+"'"
    delete_rental = "delete from "+games_rented+" where gid = '"+gid+"'"

    try:
        cur.execute(delete_entry)
        con.commit()
        cur.execute(delete_rental)
        con.commit()
        messagebox.showinfo('Success',"Game Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Game ID")
    
    print(gid)
    game_info.delete(0, END)
    root.destroy()
