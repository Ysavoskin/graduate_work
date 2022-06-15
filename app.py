from tkinter import *
import main
import tkinter.messagebox as mb

root = Tk()


text = Label(root, width=40, height=2, text="Выберите 1 команду", font="Arial 20 bold")
text.pack()

master_frame = Frame(root)
master_frame.pack()

command_frame = Frame(master_frame)
command_frame.grid(row=0, column=0)
spisok = []
team1_name = ''
team2_name = ''


def bar():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = bar_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = bar_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def atm():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = atm_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = atm_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def rm():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = rm_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = rm_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def val():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = val_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = val_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def get():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = get_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = get_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def sev():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = sev_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = sev_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def atb():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = atb_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = atb_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def esp():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = esp_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = esp_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def soc():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = soc_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = soc_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def eibar():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = eibar_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = eibar_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def alaves():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = alaves_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = alaves_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def betis():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = betis_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = betis_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def leganes():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = leganes_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = leganes_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def levante():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = levante_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = levante_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def vil():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = vil_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = vil_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def celta():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = celta_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = celta_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def valladolid():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = valladolid_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = valladolid_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def girona():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = girona_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = girona_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def huesca():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = huesca_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = huesca_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)

def vallecano():
    global team1_name, team2_name
    if team1_name == '' and team2_name == '':
        text['text'] = 'Выберите 2 команду'
        team1_name = vallecano_button['text']
    elif team2_name == '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        team2_name = vallecano_button['text']
    elif team2_name != '' and team1_name != '':
        text['text'] = 'Перейдите к результату'
        pass
    print(team1_name, team2_name)


def finish():
    global team1_name, team2_name
    root2 = Tk()
    a = str(dip.result(team1_name, team2_name))
    print(a)
    label = Label(root2, width=50, height=5, text=a, font="Arial 14 bold")
    label.pack()
    team1_name = ''
    team2_name = ''
    root2.mainloop()



bar_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/bar.gif")
atm_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/atm.gif")
rm_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/rm.gif")
val_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/val.gif")
get_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/get.gif")
sev_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/sev.gif")
atb_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/atb.gif")
esp_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/esp.gif")
soc_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/soc.gif")
eibar_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/eibar.gif")
alaves_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/alaves.gif")
betis_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/betis.gif")
leganes_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/leganes.gif")
levante_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/levante.gif")
vil_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/vil.gif")
celta_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/celta.gif")
valladolid_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/valladolid.gif")
girona_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/girona.gif")
huesca_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/huesca.gif")
vallecano_img = PhotoImage(file="C:/Users/yurar/PycharmProjects/diplom/logos/vallecano.gif")

bar_button = Button(command_frame, text="Barcelona", width=100, height=100, image=bar_img, command=bar)
atm_button = Button(command_frame, text="Ath Madrid", width=100, height=100, image=atm_img, command=atm)
rm_button = Button(command_frame, text="Real Madrid", width=100, height=100, image=rm_img, command=rm)
val_button = Button(command_frame, text="Valencia", width=100, height=100, image=val_img, command=val)
get_button = Button(command_frame, text="Getafe", width=100, height=100, image=get_img, command=get)
sev_button = Button(command_frame, text="Sevilla", width=100, height=100, image=sev_img, command=sev)
atb_button = Button(command_frame, text="Ath Bilbao", width=100, height=100, image=atb_img, command=atb)
esp_button = Button(command_frame, text="Espanol", width=100, height=100, image=esp_img, command=esp)
soc_button = Button(command_frame, text="Sociedad", width=100, height=100, image=soc_img, command=soc)
eibar_button = Button(command_frame, text="Eibar", width=100, height=100, image=eibar_img, command=eibar)
alaves_button = Button(command_frame, text="Alaves", width=100, height=100, image=alaves_img, command=alaves)
betis_button = Button(command_frame, text="Betis", width=100, height=100, image=betis_img, command=betis)
leganes_button = Button(command_frame, text="Leganes", width=100, height=100, image=leganes_img, command=leganes)
levante_button = Button(command_frame, text="Levante", width=100, height=100, image=levante_img, command=levante)
vil_button = Button(command_frame, text="Villarreal", width=100, height=100, image=vil_img, command=vil)
celta_button = Button(command_frame, text="Celta", width=100, height=100, image=celta_img, command=celta)
valladolid_button = Button(command_frame, text="Valladolid", width=100, height=100, image=valladolid_img, command=valladolid)
girona_button = Button(command_frame, text="Girona", width=100, height=100, image=girona_img, command=girona)
huesca_button = Button(command_frame, text="Huesca", width=100, height=100, image=huesca_img, command=huesca)
vallecano_button = Button(command_frame, text="Vallecano", width=100, height=100, image=vallecano_img, command=vallecano)

finish_button = Button(root, text="результат", width=30, height=2, font="Arial 12 bold", command=finish)
finish_button.pack()

bar_button.grid(row=3, column=0)
atm_button.grid(row=3, column=1)
rm_button.grid(row=3, column=2)
val_button.grid(row=3, column=3)
get_button.grid(row=3, column=4)
sev_button.grid(row=4, column=0)
atb_button.grid(row=4, column=1)
esp_button.grid(row=4, column=2)
soc_button.grid(row=4, column=3)
eibar_button.grid(row=4, column=4)
alaves_button.grid(row=5, column=0)
betis_button.grid(row=5, column=1)
leganes_button.grid(row=5, column=2)
levante_button.grid(row=5, column=3)
vil_button.grid(row=5, column=4)
celta_button.grid(row=6, column=0)
valladolid_button.grid(row=6, column=1)
girona_button.grid(row=6, column=2)
huesca_button.grid(row=6, column=3)
vallecano_button.grid(row=6, column=4)



root.mainloop()
