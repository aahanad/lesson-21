from tkinter import*
screen=Tk()
screen.geometry=("600x900")
screen.title("Rock,Paper,Scissors✂📝🌑")
screen.config(bg="MistyRose2")
winner="..."
title=Label(screen,text="Welcome to Rock,Paper,scissors!🌑📄✂!!!!!!!!!!!!!!",bg="MistyRose2",fg="orchid3",font=("Lola",15,"bold"))
title.grid(row=1,column=1,padx=140,pady=50)
winish=Label(screen,text=winner+"won!!!!!!1",bg="MistyRose2",fg="orchid3",font=("Lola",12,"bold"))
winish.grid(row=2,column=1,padx=160,pady=5)
options=Label(screen,text="💥your options are:",bg="MistyRose2",fg="LightCoral",font=("Lola",14))
options.grid(row=3,column=0,padx=50,pady=0)
pick=Button(screen,text="Rock🌑",bg="thistle",fg="DeepSkyBlue2",font=("lola",7))
pick.grid(row=4,column=1,padx=10,pady=0)

screen.mainloop()
#complete the buttons and labels stttututututfffff