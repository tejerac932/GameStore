from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from features.background import *

def View(): 
    
    # Window
    root = Toplevel()
    root.title("Game Catalog")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # SQLite server
    con = sql.connect("db.db")
    cur = con.cursor()

    # Tables
    game_table = "games" 
   
    # Background
    background  = Background(root,"images/catalog.jpg")
    background.pack(fill=BOTH, expand=YES)
    
    # Heading
    headingFrame1 = Frame(root,bg="#322884",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="View Games", bg='blue', fg='white', font = ('System',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=.85)

    # Table
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    y = 0.25
    Label(labelFrame, text="%-10s %-40s %-20s %-20s"%('GID','Title','Genre','Status'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)

    Label(labelFrame, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    get_games = "select * from "+game_table

    try:
        cur.execute(get_games)
        con.commit()
        for i in cur:
            abbreviation = i[1]
            if len(i[1]) > 30:
                abbreviation = ''
                for word in i[1].split(' '):
                    abbreviation += word[0].upper()
            Label(labelFrame,text="%-10s %-30s %-20s %-20s"%(i[0],abbreviation,i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
            
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="QUIT",bg='#983535', fg='black',  command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()