from tkinter import *
from features.background import *
from features.add_game import add_game
from features.view_game import View
from features.delete_game import delete
from features.Rent import rent_game
from features.Return import return_game

# Window
root = Tk()
root.title("Store Front")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Background
background = Background(root,"images/gameShop.jpg")
background.pack(fill=BOTH, expand=YES)

# Heading
headingFrame1 = Frame(root,bg="#229c84",bd=3)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \nDuster's Game Shop", bg='#24213e', fg='white', font=('System',17))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=.85)

# Menu options
add = Button(root,text="Add Game",bg='#2f7734', fg='white',font=('System',12),activebackground="#45ae4c", command=add_game)
add.place(relx=0.2,rely=0.4, relwidth=0.2,relheight=0.1)

delete_games = Button(root,text="Delete Game ",bg='#7a0000', fg='white', font=('System',12),activebackground="#c70000",command=delete)
delete_games.place(relx=0.6,rely=0.4, relwidth=0.2,relheight=0.1)
    
view_games = Button(root,text="View Games",bg='#034a74', fg='white', font=('System',12),activebackground="#057abf",command=View)
view_games.place(relx=0.2,rely=0.6, relwidth=0.2,relheight=0.1)
    
rent_games = Button(root,text="Rent Game",bg='#735e27', fg='white', font=('System',12),activebackground="#ac8d3a", command=rent_game)
rent_games.place(relx=0.6,rely=0.6, relwidth=0.2,relheight=0.1)
    
return_games = Button(root,text="Return Game",bg='#e6e6e6', fg='black', font=('System',12),command = return_game)
return_games.place(relx=0.4,rely=0.75, relwidth=0.2,relheight=0.1)


root.mainloop()