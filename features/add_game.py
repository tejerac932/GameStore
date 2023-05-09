from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from features.background import *

def add_game(): 
    
    global game_id ,game_title, game_genre, game_status, con, cur, game_table, root
    
    # Window
    root = Toplevel()
    root.title("Game Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # SQLite server
    con = sql.connect("db.db")
    cur = con.cursor()

    # Tables
    game_table = "games" 
   
    # Background
    background  = Background(root,"images/gameShelf.png")
    background.pack(fill=BOTH, expand=YES)
    
    # Heading 
    headingFrame1 = Frame(root,bg="black",bd=3)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Add Game", bg='#39314b', fg='white', font=('System',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=.85)

    # Labels
    labelFrame = Frame(root,bg='#3d2225')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    lb1 = Label(labelFrame,text="Game ID : ", bg='#3d2225', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    game_id = Entry(labelFrame)
    game_id.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    lb2 = Label(labelFrame,text="Title : ", bg='#3d2225', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    game_title = Entry(labelFrame)
    game_title.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        
    lb3 = Label(labelFrame,text="Genre : ", bg='#3d2225', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    game_genre = Entry(labelFrame)
    game_genre.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    lb4 = Label(labelFrame,text="Status(Avail/issued) : ", bg='#3d2225', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    game_status = Entry(labelFrame)
    game_status.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
        
    # Submit 
    SubmitBtn = Button(root,text="SUBMIT",bg='#397b44', fg='black',command= register_Game)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit
    quitBtn = Button(root,text="QUIT",bg='#983535', fg='black',  command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def register_Game():
    gid = game_id.get()
    title = game_title.get()
    genre = game_genre.get()
    status = game_status.get()
    status = status.lower()
    
    insert_game = "insert into "+game_table+" values ('"+gid+"','"+title+"','"+genre+"','"+status+"')"

    try:
        cur.execute(insert_game)
        con.commit()
        messagebox.showinfo('Success',"Game added to library!")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    print(gid)
    print(title)
    print(genre)
    print(status)
    root.destroy()
