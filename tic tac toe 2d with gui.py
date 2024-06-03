from tkinter import *
from tkinter import messagebox
import random
# we created the main window
game_window = Tk()
game_window.title('Game Window')
game_window.config(background='sky blue')
game_window.geometry('400x400')
new_icon = PhotoImage(file='logo.png')
game_window.iconphoto(True,new_icon)
icon = PhotoImage(file='tic tac 2.png')
# now we will add labels:
game_name = Label(game_window,
                  font=('arial',30),
                  text='Tic Tac Toe',
                  fg='green',
                  bg='pink',
                  pady=10,
                  padx=10,
                  relief=RAISED,
                  bd=20,
                  image=icon,
                  compound=BOTTOM)
game_name.pack()

#now we will add buttons:

matrix = [['','',''],
          ['','',''],
          ['','','']]
player_list = ['player1','player2']
selected_player = random.choice(player_list)
input=0
def game_draw():
    global input
    if input == 9 and winner() is not True:
        messagebox.showinfo('Draw','Oops!!...Game Draw')
        return True
def game_start():
    b1.config(state=ACTIVE)
    b2.config(state=ACTIVE)
    b3.config(state=ACTIVE)
    b4.config(state=ACTIVE)
    b5.config(state=ACTIVE)
    b6.config(state=ACTIVE)
    b7.config(state=ACTIVE)
    b8.config(state=ACTIVE)
    b9.config(state=ACTIVE)
def restart():
    global input
    b1['text'] = ''
    b2['text'] = ''
    b3['text'] = ''
    b4['text'] = ''
    b5['text'] = ''
    b6['text'] = ''
    b7['text'] = ''
    b8['text'] = ''
    b9['text'] = ''
    input = 0
    game_start()

def winner():
    winner = True
    if b1['text'] == b2['text'] and b1['text'] == b3['text'] and b1['text']!='':
        messagebox.showinfo('winner',f"The player {b1['text']} won the game.")
        return winner
    if b4['text'] == b5['text'] and b4['text'] == b6['text'] and b4['text']!='':
        messagebox.showinfo('winner',f"The player {b4['text']} won the game.")
        return winner
    if b7['text'] == b8['text'] and b7['text'] == b9['text'] and b7['text']!='':
        messagebox.showinfo('winner',f"The player {b7['text']} won the game.")
        return winner
    if b1['text'] == b4['text'] and b1['text'] == b7['text'] and b1['text']!='':
        messagebox.showinfo('winner',f"The player {b1['text']} won the game.")
        return winner
    if b2['text'] == b5['text'] and b2['text'] == b8['text'] and b2['text']!='':
        messagebox.showinfo('winner',f"The player {b2['text']} won the game.")
        return winner
    if b3['text'] == b6['text'] and b3['text'] == b9['text'] and b3['text']!='':
        messagebox.showinfo('winner',f"The player {b3['text']} won the game.")
        return winner
    if b1['text'] == b5['text'] and b1['text'] == b9['text'] and b1['text']!='':
        messagebox.showinfo('winner',f"The player {b1['text']} won the game.")
        return winner
    if b3['text'] == b5['text'] and b3['text'] == b7['text'] and b3['text']!='':
        messagebox.showinfo('winner',f"The player {b3['text']} won the game.")
        return winner
    else:
        return False
def click(btn):
    global selected_player,input
    selected_player = player_list[(player_list.index(selected_player) + 1) % 2]
    prev_player = player_list[(player_list.index(selected_player) + 1) % 2]
    label.config(text=prev_player + ' is playing')
    if btn == '.!frame.!button' and b1['text'] != "" or btn == '.!frame.!button2' and b2[
        'text'] != "" or btn == '.!frame.!button3' and b3['text'] != "" or btn == '.!frame.!button4' and b4[
        'text'] != "" or btn == '.!frame.!button5' and b5['text'] != "" or btn == '.!frame.!button6' and b6[
        'text'] != "" or btn == '.!frame.!button7' and b7['text'] != "" or btn == '.!frame.!button8' and b8[
        'text'] != "" or btn == '.!frame.!button9' and b9['text'] != "":
        selected_player = player_list[(player_list.index(selected_player) + 1) % 2]
        label.config(text='Already marked')
        messagebox.showwarning('Warning', 'Box already marked')
    if btn == '.!frame.!button' and b1['text']=="":
        b1.config(text=selected_player)
        input+=1

    elif btn =='.!frame.!button2' and b2['text']=="":
        b2.config(text=selected_player)
        input += 1

    elif btn =='.!frame.!button3' and b3['text']=="":
        b3.config(text=selected_player)
        input += 1

    elif btn =='.!frame.!button4' and b4['text']=="":
        b4.config(text=selected_player)
        input += 1

    elif btn=='.!frame.!button5' and b5['text']=="":
        b5.config(text=selected_player)
        input += 1

    elif btn=='.!frame.!button6' and b6['text']=="":
        b6.config(text=selected_player)
        input += 1

    elif btn=='.!frame.!button7' and b7['text']=="":
        b7.config(text=selected_player)
        input += 1

    elif btn=='.!frame.!button8' and b8['text']=="":
        b8.config(text=selected_player)
        input += 1

    elif btn=='.!frame.!button9' and b9['text']=="":
        b9.config(text=selected_player)
        input += 1
    game_draw()
    winner()

label = Label(game_window,
              text= "Start clicking",
              font=('arial',20),
              fg = 'green',
              pady=5,
              padx=5,
              bg = 'pink')
label.pack(side=BOTTOM)
start = Button(game_window,
               text='Start the game',
               font=('comic saans',15),
               fg= 'black',
               bg='white',
               command=game_start)
start.place(x =10,y =10)
restart_button = Button(game_window,
                        text='Restart',
                        font=('comic sans',15),
                        fg='black',
                        bg='white',
                        command=restart)
restart_button.place(x=30,y=60)
frame = Frame(game_window)
frame.pack(padx=40,pady=40)
# creating 9 buttons for 9 places.
b1 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            activeforeground='green',
            activebackground='pink',
            height=4,
            width=10,
            state=DISABLED,
            command= lambda:click(str(b1)))

b1.grid(row=0,column=0)
b2 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            height=4,
            activeforeground='green',
            activebackground='pink',
            width=10,
            state=DISABLED,
            bg='pink',
            command=lambda:click(str(b2)))

b2.grid(row=0,column=1)
b3 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda :click(str(b3)))

b3.grid(row=0,column=2)
b4 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda:click(str(b4)))

b4.grid(row=1,column=0)
b5 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            width=10,
            command=lambda :click(str(b5)))

b5.grid(row=1,column=1)
b6 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda :click(str(b6)))

b6.grid(row=1,column=2)
b7 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda:click(str(b7)))

b7.grid(row=3,column=0)
b8 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            height=4,
            width=10,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            bg='pink',
            command=lambda:click(str(b8)))

b8.grid(row=3,column=1)
b9 = Button(frame,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            width=10,
            command=lambda:click(str(b9)))

b9.grid(row=3,column=2)

game_window.mainloop()
