from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from features.background import *

def return_game(): 
    
    global game_info,SubmitBtn,quitBtn,con,cur,root,labelFrame, lb1

    # Window
    root = Toplevel()
    root.title("Drop Box")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # SQLite
    con = sql.connect("db.db")
    cur = con.cursor()

    # Background
    background  = Background(root,"images/returnBox.png")
    background.pack(fill=BOTH, expand=YES)
    
    # Heading 
    headingFrame1 = Frame(root,bg="black",bd=3)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Return Game", bg='#fee8f5', fg='black', font=('System',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=.85)
    
    labelFrame = Frame(root,bg='#78a0c3')
    labelFrame.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.1)   
        
    # Input
    lb1 = Label(labelFrame,text="Game ID : ", bg='#78a0c3', fg='black')
    lb1.place(relx=0.05,rely=0.3)
        
    game_info = Entry(labelFrame)
    game_info.place(relx=0.3,rely=0.3, relwidth=0.62)
    
    # Submit 
    SubmitBtn = Button(root,text="SUBMIT",bg='#397b44', fg='black',command= Return)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit
    quitBtn = Button(root,text="QUIT",bg='#983535', fg='black',  command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
      
    root.mainloop()


def Return():

    gids = [] 
    rent_table = "games_rented"
    game_table = "games"
    gid = game_info.get()
    extract_gid = "select gid from "+rent_table

    try:
        cur.execute(extract_gid)
        con.commit()

        for i in cur:
            gids.append(i[0])
        
        if int(gid) in gids:
            checkAvail = "select status from "+game_table+" where gid = '"+gid+"'"
            cur.execute(checkAvail)
            con.commit()
            
            for i in cur:
                check = i[0]
                
            if check == 'issued':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Game ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Game IDs")
    
    rent_query = "delete from "+rent_table+" where gid = '"+gid+"'"
    updateStatus = "update "+game_table+" set status = 'avail' where gid = '"+gid+"'"

    try:
        if int(gid) in gids and status == True:
            cur.execute(rent_query)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Game Returned Successfully")
        else:
            gids.clear()
            messagebox.showinfo('Message',"Please check the game ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    
    gids.clear()
    root.destroy()
