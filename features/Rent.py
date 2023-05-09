from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from features.background import *

def rent_game(): 
    
    global rentBtn,labelFrame,lb1,gid_input,rented_to,root,con,cur
    
    # Window
    root = Toplevel()
    root.title("Cashier")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # SQLite
    con = sql.connect("db.db")
    cur = con.cursor()

    # Background
    background  = Background(root,"images/rent.jpg")
    background.pack(fill=BOTH, expand=YES)

    # Heading
    headingFrame1 = Frame(root,bg="#4e1387",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
    headingLabel = Label(headingFrame1, text="Rent Game", bg='#ffe464', fg='black', font=('System',22))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=.85)
    
    # Inputs
    labelFrame = Frame(root,bg='#0a233c')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.3)  
        
    lb1 = Label(labelFrame,text="Game ID : ", bg='#0a233c', fg='white')
    lb1.place(relx=0.05,rely=0.2)     
    gid_input = Entry(labelFrame)
    gid_input.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    lb2 = Label(labelFrame,text="Rented to : ", bg='#0a233c', fg='white')
    lb2.place(relx=0.05,rely=0.6) 
    rented_to = Entry(labelFrame)
    rented_to.place(relx=0.3,rely=0.6, relwidth=0.62)
    
    
     # Submit 
    rentBtn = Button(root,text="RENT",bg='#397b44', fg='black',command= rent)
    rentBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # Quit
    quitBtn = Button(root,text="QUIT",bg='#983535', fg='black',  command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

def rent():
    all_gid = [] 

    game_table = "games"
    rent_table = "games_rented"

    gid = gid_input.get()
    rent_to = rented_to.get()

    rentBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    gid_input.destroy()
    rented_to.destroy()

    extract_gid = "select gid from "+game_table

    try:
        cur.execute(extract_gid)
        con.commit()

        for i in cur:
            all_gid.append(i[0])

        if int(gid) in all_gid:
            checkAvail = "select status from "+game_table+" where gid = '"+gid+"'"
            cur.execute(checkAvail)
            con.commit()

            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error","Game ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Game IDs")
    
    rent_query = "insert into "+rent_table+" values ('"+gid+"','"+rent_to+"')"
    updateStatus = "update "+game_table+" set status = 'issued' where gid = '"+gid+"'"

    try:
        if int(gid) in all_gid and status == True:
            cur.execute(rent_query)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Game Rented Successfully")
            root.destroy()
        else:
            all_gid.clear()
            messagebox.showinfo('Message',"Game Already Rented")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")

    print(gid)
    print(rent_to)
    
    all_gid.clear()