from tkinter import *
from tkinter import messagebox
import random
# we created the main window
game_window = Tk()
game_window.title('Game Window')
game_window.config(background='beige')
game_window.geometry('400x400')
new_icon = PhotoImage(file='logo.png')
game_window.iconphoto(True,new_icon)
icon = PhotoImage(file='tic tac 2.png')
# now we will add labels:
game_name = Label(game_window,
                  font=('arial',30),
                  text='Tic Tac Toe',
                  fg='green',
                  bg='sky blue',
                  pady=10,
                  padx=10,
                  relief=SUNKEN,
                  bd=20,
                  image=icon,
                  compound=BOTTOM)
game_name.pack()
input = 0
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
    # these are condition for buttons 10 to 18
    if b10['text'] == b11['text'] and b10['text'] == b12['text'] and b10['text']!='':
        messagebox.showinfo('winner',f"The player {b10['text']} won the game.")
        return winner
    if b13['text'] == b14['text'] and b13['text'] == b15['text'] and b13['text']!='':
        messagebox.showinfo('winner',f"The player {b13['text']} won the game.")
        return winner
    if b16['text'] == b17['text'] and b16['text'] == b18['text'] and b16['text']!='':
        messagebox.showinfo('winner',f"The player {b16['text']} won the game.")
        return winner
    if b10['text'] == b13['text'] and b10['text'] == b16['text'] and b10['text']!='':
        messagebox.showinfo('winner',f"The player {b10['text']} won the game.")
        return winner
    if b11['text'] == b14['text'] and b11['text'] == b17['text'] and b11['text']!='':
        messagebox.showinfo('winner',f"The player {b11['text']} won the game.")
        return winner
    if b12['text'] == b15['text'] and b12['text'] == b18['text'] and b12['text']!='':
        messagebox.showinfo('winner',f"The player {b12['text']} won the game.")
        return winner
    if b10['text'] == b14['text'] and b10['text'] == b18['text'] and b10['text']!='':
        messagebox.showinfo('winner',f"The player {b10['text']} won the game.")
        return winner
    if b12['text'] == b14['text'] and b12['text'] == b16['text'] and b12['text']!='':
        messagebox.showinfo('winner',f"The player {b12['text']} won the game.")
        return winner
    # These are conditions for buttons 19 to 27
    if b19['text'] == b20['text'] and b19['text'] == b21['text'] and b19['text']!='':
        messagebox.showinfo('winner',f"The player {b19['text']} won the game.")
        return winner
    if b22['text'] == b23['text'] and b22['text'] == b24['text'] and b22['text']!='':
        messagebox.showinfo('winner',f"The player {b22['text']} won the game.")
        return winner
    if b25['text'] == b26['text'] and b25['text'] == b27['text'] and b25['text']!='':
        messagebox.showinfo('winner',f"The player {b25['text']} won the game.")
        return winner
    if b19['text'] == b22['text'] and b19['text'] == b25['text'] and b19['text']!='':
        messagebox.showinfo('winner',f"The player {b19['text']} won the game.")
        return winner
    if b20['text'] == b23['text'] and b20['text'] == b26['text'] and b20['text']!='':
        messagebox.showinfo('winner',f"The player {b20['text']} won the game.")
        return winner
    if b21['text'] == b24['text'] and b21['text'] == b27['text'] and b21['text']!='':
        messagebox.showinfo('winner',f"The player {b21['text']} won the game.")
        return winner
    if b19['text'] == b23['text'] and b19['text'] == b27['text'] and b19['text']!='':
        messagebox.showinfo('winner',f"The player {b19['text']} won the game.")
        return winner
    if b21['text'] == b23['text'] and b21['text'] == b25['text'] and b25['text']!='':
        messagebox.showinfo('winner',f"The player {b25['text']} won the game.")
        return winner
    # These are extra conditions for 3d
    if b1['text'] == b10['text'] and b1['text'] == b19['text'] and b1['text']!='':
        messagebox.showinfo('winner',f"The player {b1['text']} won the game.")
        return winner
    if b2['text'] == b11['text'] and b2['text'] == b20['text'] and b2['text']!='':
        messagebox.showinfo('winner',f"The player {b2['text']} won the game.")
        return winner
    if b3['text'] == b12['text'] and b3['text'] == b21['text'] and b3['text']!='':
        messagebox.showinfo('winner',f"The player {b3['text']} won the game.")
        return winner
    if b4['text'] == b13['text'] and b4['text'] == b22['text'] and b4['text']!='':
        messagebox.showinfo('winner',f"The player {b4['text']} won the game.")
        return winner
    if b5['text'] == b14['text'] and b5['text'] == b23['text'] and b5['text']!='':
        messagebox.showinfo('winner',f"The player {b5['text']} won the game.")
        return winner
    if b6['text'] == b15['text'] and b6['text'] == b24['text'] and b6['text']!='':
        messagebox.showinfo('winner',f"The player {b6['text']} won the game.")
        return winner
    if b7['text'] == b16['text'] and b7['text'] == b25['text'] and b7['text']!='':
        messagebox.showinfo('winner',f"The player {b7['text']} won the game.")
        return winner
    if b8['text'] == b17['text'] and b8['text'] == b26['text'] and b8['text']!='':
        messagebox.showinfo('winner',f"The player {b8['text']} won the game.")
        return winner
    if b9['text'] == b18['text'] and b9['text'] == b27['text'] and b9['text']!='':
        messagebox.showinfo('winner',f"The player {b9['text']} won the game.")
        return winner
    if b1['text'] == b14['text'] and b1['text'] == b27['text'] and b1['text']!='':
        messagebox.showinfo('winner',f"The player {b1['text']} won the game.")
        return winner
    if b21['text'] == b14['text'] and b21['text'] == b7['text'] and b21['text']!='':
        messagebox.showinfo('winner',f"The player {b21['text']} won the game.")
        return winner
    if b2['text'] == b14['text'] and b2['text'] == b26['text'] and b2['text']!='':
        messagebox.showinfo('winner',f"The player {b2['text']} won the game.")
        return winner
    if b7['text'] == b17['text'] and b7['text'] == b27['text'] and b7['text']!='':
        messagebox.showinfo('winner',f"The player {b7['text']} won the game.")
        return winner
    if b1['text'] == b13['text'] and b1['text'] == b25['text'] and b1['text']!='':
        messagebox.showinfo('winner',f"The player {b1['text']} won the game.")
        return winner
    if b3['text'] == b15['text'] and b3['text'] == b27['text'] and b3['text']!='':
        messagebox.showinfo('winner',f"The player {b3['text']} won the game.")
        return winner
    if b3['text'] == b14['text'] and b3['text'] == b25['text'] and b3['text']!='':
        messagebox.showinfo('winner',f"The player {b3['text']} won the game.")
        return winner
    if b3['text'] == b11['text'] and b3['text'] == b19['text'] and b3['text']!='':
        messagebox.showinfo('winner',f"The player {b3['text']} won the game.")
        return winner
    if b1['text'] == b11['text'] and b1['text'] == b21['text'] and b1['text']!='':
        messagebox.showinfo('winner',f"The player {b1['text']} won the game.")
        return winner
    if b7['text'] == b13['text'] and b7['text'] == b19['text'] and b7['text']!='':
        messagebox.showinfo('winner',f"The player {b7['text']} won the game.")
        return winner
    if b9['text'] == b17['text'] and b9['text'] == b25['text'] and b9['text']!='':
        messagebox.showinfo('winner',f"The player {b9['text']} won the game.")
        return winner
    if b9['text'] == b15['text'] and b9['text'] == b21['text'] and b9['text']!='':
        messagebox.showinfo('winner',f"The player {b9['text']} won the game.")
        return winner
    if b8['text'] == b14['text'] and b8['text'] == b19['text'] and b8['text']!='':
        messagebox.showinfo('winner',f"The player {b8['text']} won the game.")
        return winner
    if b4['text'] == b14['text'] and b4['text'] == b24['text'] and b4['text']!='':
        messagebox.showinfo('winner',f"The player {b4['text']} won the game.")
        return winner
    if b6['text'] == b14['text'] and b6['text'] == b22['text'] and b6['text']!='':
        messagebox.showinfo('winner',f"The player {b6['text']} won the game.")
        return winner
    if b9['text'] == b14['text'] and b9['text'] == b19['text'] and b9['text']!='':
        messagebox.showinfo('winner',f"The player {b9['text']} won the game.")
        return winner

    else:
        return False
def game_draw():
    global input
    if input == 27 and winner() is not True:
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
    b10.config(state=ACTIVE)
    b11.config(state=ACTIVE)
    b12.config(state=ACTIVE)
    b13.config(state=ACTIVE)
    b14.config(state=ACTIVE)
    b15.config(state=ACTIVE)
    b16.config(state=ACTIVE)
    b17.config(state=ACTIVE)
    b18.config(state=ACTIVE)
    b19.config(state=ACTIVE)
    b20.config(state=ACTIVE)
    b21.config(state=ACTIVE)
    b22.config(state=ACTIVE)
    b23.config(state=ACTIVE)
    b24.config(state=ACTIVE)
    b25.config(state=ACTIVE)
    b26.config(state=ACTIVE)
    b27.config(state=ACTIVE)
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
    b10['text'] = ''
    b11['text'] = ''
    b12['text'] = ''
    b13['text'] = ''
    b14['text'] = ''
    b15['text'] = ''
    b16['text'] = ''
    b17['text'] = ''
    b18['text'] = ''
    b19['text'] = ''
    b20['text'] = ''
    b21['text'] = ''
    b22['text'] = ''
    b23['text'] = ''
    b24['text'] = ''
    b25['text'] = ''
    b26['text'] = ''
    b27['text'] = ''
    input = 0
    game_start()

player_list = ['Uzair','fatima']
selected_player = random.choice(player_list)
def click(btn):
    global selected_player, input
    selected_player = player_list[(player_list.index(selected_player)+1) % 2]
    next_player = player_list[(player_list.index(selected_player) + 1) % 2]
    label.config(text=next_player + ' is playing')
    if  btn == '.!frame.!button' and b1['text']!="" or btn =='.!frame.!button2' and b2['text']!="" or btn =='.!frame.!button3' and b3['text']!="" or btn =='.!frame.!button4' and b4['text']!="" or btn=='.!frame.!button5' and b5['text']!="" or btn=='.!frame.!button6' and b6['text']!="" or btn=='.!frame.!button7' and b7['text']!="" or btn=='.!frame.!button8' and b8['text']!="" or btn=='.!frame.!button9' and b9['text']!="" or btn == '.!frame2.!button' and b10['text']!="" or btn =='.!frame2.!button2' and b11['text']!="" or btn =='.!frame2.!button3' and b12['text']!="" or btn =='.!frame2.!button4' and b13['text']!="" or btn=='.!frame2.!button5' and b14['text']!="" or btn=='.!frame2.!button6' and b15['text']!="" or btn=='.!frame2.!button7' and b16['text']!="" or btn=='.!frame2.!button8' and b17['text']!="" or btn=='.!frame2.!button9' and b18['text']!="" or btn == '.!frame3.!button' and b19['text']!="" or btn =='.!frame3.!button2' and b20['text']!="" or btn =='.!frame3.!button3' and b21['text']!="" or btn =='.!frame3.!button4' and b22['text']!="" or btn=='.!frame3.!button5' and b23['text']!="" or btn=='.!frame3.!button6' and b24['text']!="" or btn=='.!frame3.!button7' and b25['text']!="" or btn=='.!frame3.!button8' and b26['text']!="" or btn=='.!frame3.!button9' and b27['text']!="":
        selected_player = player_list[(player_list.index(selected_player) + 1) % 2]
        label.config(text='Already marked')
        messagebox.showwarning('Warning','Box already marked')
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
    if btn == '.!frame2.!button' and b10['text']=="":
        b10.config(text=selected_player)
        input+=1

    elif btn =='.!frame2.!button2' and b11['text']=="":
        b11.config(text=selected_player)
        input += 1

    elif btn =='.!frame2.!button3' and b12['text']=="":
        b12.config(text=selected_player)
        input += 1

    elif btn =='.!frame2.!button4' and b13['text']=="":
        b13.config(text=selected_player)
        input += 1

    elif btn=='.!frame2.!button5' and b14['text']=="":
        b14.config(text=selected_player)
        input += 1

    elif btn=='.!frame2.!button6' and b15['text']=="":
        b15.config(text=selected_player)
        input += 1

    elif btn=='.!frame2.!button7' and b16['text']=="":
        b16.config(text=selected_player)
        input += 1

    elif btn=='.!frame2.!button8' and b17['text']=="":
        b17.config(text=selected_player)
        input += 1

    elif btn=='.!frame2.!button9' and b18['text']=="":
        b18.config(text=selected_player)
        input += 1
    if btn == '.!frame3.!button' and b19['text']=="":
        b19.config(text=selected_player)
        input+=1

    elif btn =='.!frame3.!button2' and b20['text']=="":
        b20.config(text=selected_player)
        input += 1

    elif btn =='.!frame3.!button3' and b21['text']=="":
        b21.config(text=selected_player)
        input += 1

    elif btn =='.!frame3.!button4' and b22['text']=="":
        b22.config(text=selected_player)
        input += 1

    elif btn=='.!frame3.!button5' and b23['text']=="":
        b23.config(text=selected_player)
        input += 1

    elif btn=='.!frame3.!button6' and b24['text']=="":
        b24.config(text=selected_player)
        input += 1

    elif btn=='.!frame3.!button7' and b25['text']=="":
        b25.config(text=selected_player)
        input += 1

    elif btn=='.!frame3.!button8' and b26['text']=="":
        b26.config(text=selected_player)
        input += 1

    elif btn=='.!frame3.!button9' and b27['text']=="":
        b27.config(text=selected_player)
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
frame1 = Frame(game_window)
frame1.place(x=800,y=275)
frame2 = Frame(game_window)
frame2.pack(padx=10,pady=10)
frame3 = Frame(game_window)
frame3.place(x=200,y=275)
b1 = Button(frame1,
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
b2 = Button(frame1,
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
b3 = Button(frame1,
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
b4 = Button(frame1,
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
b5 = Button(frame1,
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
b6 = Button(frame1,
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
b7 = Button(frame1,
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
b8 = Button(frame1,
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
b9 = Button(frame1,
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

# Here starts the second interface.
b10 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            activeforeground='green',
            activebackground='pink',
            height=4,
            width=10,
            state=DISABLED,
            command= lambda:click(str(b10)))

b10.grid(row=0,column=0)
b11 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            height=4,
            activeforeground='green',
            activebackground='pink',
            width=10,
            state=DISABLED,
            bg='pink',
            command=lambda:click(str(b11)))

b11.grid(row=0,column=1)

b12 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda :click(str(b12)))

b12.grid(row=0,column=2)
b13 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda:click(str(b13)))

b13.grid(row=1,column=0)
b14 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            width=10,
            command=lambda :click(str(b14)))

b14.grid(row=1,column=1)
b15 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda :click(str(b15)))

b15.grid(row=1,column=2)
b16 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda:click(str(b16)))

b16.grid(row=3,column=0)
b17 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            height=4,
            width=10,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            bg='pink',
            command=lambda:click(str(b17)))

b17.grid(row=3,column=1)
b18 = Button(frame2,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            width=10,
            command=lambda:click(str(b18)))
b18.grid(row=3,column=2)



b19 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            activeforeground='green',
            activebackground='pink',
            height=4,
            width=10,
            state=DISABLED,
            command= lambda:click(str(b19)))

b19.grid(row=0,column=0)

# Here starts the third interface.
b20 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            height=4,
            activeforeground='green',
            activebackground='pink',
            width=10,
            state=DISABLED,
            bg='pink',
            command=lambda:click(str(b20)))

b20.grid(row=0,column=1)
b21 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda :click(str(b21)))

b21.grid(row=0,column=2)
b22 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda:click(str(b22)))

b22.grid(row=1,column=0)
b23 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            width=10,
            command=lambda :click(str(b23)))

b23.grid(row=1,column=1)
b24 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda :click(str(b24)))

b24.grid(row=1,column=2)
b25 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            activeforeground='green',
            activebackground='pink',
            state=DISABLED,
            width=10,
            command=lambda:click(str(b25)))

b25.grid(row=3,column=0)
b26 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            height=4,
            width=10,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            bg='pink',
            command=lambda:click(str(b26)))

b26.grid(row=3,column=1)
b27 = Button(frame3,
            text="",
            font=('arial',10),
            fg='green',
            bg='pink',
            height=4,
            state=DISABLED,
            activeforeground='green',
            activebackground='pink',
            width=10,
            command=lambda:click(str(b27)))

b27.grid(row=3,column=2)


game_window.mainloop()
