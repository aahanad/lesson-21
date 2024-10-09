from tkinter import*
import random
screen=Tk()
screen.geometry=("600x900")
screen.title("Rock,Paper,Scissors✂📝🌑")
screen.config(bg="MistyRose2")
winner=""
c_score=0
c_selection=""
p_score=0
p_selection=""
def gameplay(game_input):
    global c_score,c_selection,p_score,p_selection,winner
    p_selection=game_input
    options=["rock","paper","scissor"]
    c_selection=random.choice(options)
    if p_selection==c_selection:
        winner="Tie"
    elif p_selection=="rock"and c_selection=="paper":
        winner="computer"
        c_score=c_score+1
    elif p_selection=="paper" and c_selection=="rock":
        winner="player"
        p_score=p_score+1
    elif p_selection=="scissor" and c_selection=="rock":
        winner="computer"
        c_score=c_score+1
    elif p_selection=="scissor" and c_selection=="paper":
        winner="player"
        p_score=p_score+1
    elif p_selection=="rock" and c_selection=="scissor":
        winner="player"
        p_score=p_score+1
    elif p_selection=="paper" and c_selection=="scissor":
        winner="computer"
        c_score=c_score+1
    you_select.config(text=f"you selected: {p_selection}")
    comp_select.config(text=f"computer selected:{c_selection}")
    you_score.config(text=f"you score:{p_score}")
    comp_score.config(text=f"computer score:{c_score}")
    winish.config(text=winner+" won!!!!!!")


title=Label(screen,text="Welcome to Rock,Paper,scissors!🌑📄✂!!!!!!!!!!!!!!",bg="MistyRose2",fg="orchid3",font=("Lola",15,"bold"))
title.grid(row=1,column=1,padx=10,pady=20)
winish=Label(screen,text=winner+" won!!!!!!",bg="MistyRose2",fg="orchid3",font=("Lola",12,"bold"))
winish.grid(row=2,column=1,padx=10,pady=0)
options=Label(screen,text="💥your options are:",bg="MistyRose2",fg="LightCoral",font=("Lola",14))
options.grid(row=3,column=0,padx=10,pady=0)
pick=Button(screen,text="Paper📄",bg="thistle",fg="DeepSkyBlue2",font=("lola",10),width=20,command=lambda:gameplay("paper"))

pick.grid(row=4,column=0,padx=10,pady=10)
pick1=Button(screen,text="Rock🌑",bg="thistle",fg="DeepSkyBlue2",font=("lola",10),width=20,command=lambda:gameplay("rock"))
pick1.grid(row=4,column=1,padx=10,pady=10)
pick2=Button(screen,text="Scissors✂",bg="thistle",fg="DeepSkyBlue2",font=("lola",10),width=20,command=lambda:gameplay("scissor"))
pick2.grid(row=4,column=2,padx=10,pady=10)
score=Label(screen,text="🔮score:",bg="MistyRose2",fg="LightCoral",font=("Lola",14))
score.grid(row=5,column=0,padx=10,pady=40)
you_select=Label(screen,text=f"you selected: {p_selection}",bg="MistyRose2",fg="LightCoral",font=("Lola",14))
you_select.grid(row=6,column=0,padx=45,pady=30)
you_score=Label(screen,text=f"you score:{p_score}",bg="MistyRose2",fg="LightCoral",font=("Lola",14))
you_score.grid(row=6,column=1,padx=60,pady=30)
comp_select=Label(screen,text=f"computer selected:{c_selection}",bg="MistyRose2",fg="LightCoral",font=("Lola",14))
comp_select.grid(row=7,column=0,padx=45,pady=45)
comp_score=Label(screen,text=f"computer score:{c_score}",bg="MistyRose2",fg="LightCoral",font=("Lola",14))
comp_score.grid(row=7,column=1,padx=60,pady=30)



screen.mainloop()
#complete the buttons and labels stttututututfffff
