from tkinter import *
from tkinter import messagebox
import random

ventana_juego = Tk()

ventana_juego.title("app")

ventana_juego.geometry("800x700")

ventana_juego.resizable(0,0)

ventana_juego.config(bg="grey")

def nacimiento():
    global toplevel_nacimiento
    toplevel_nacimiento = Toplevel()
    toplevel_nacimiento.title("nacimiento")
    toplevel_nacimiento.resizable(False, False)
    toplevel_nacimiento.geometry("600x500")
    toplevel_nacimiento.config(bg="white")

    frame_nacimiento=Frame(toplevel_nacimiento)
    frame_nacimiento.config(bg="pink", width=600, height=500)
    frame_nacimiento.place(x=0,y=0)

    titulo = Label(frame_nacimiento, text=" naci el 8 de septiembre del 2008 \n en la ciudad de barranquilla atlantico  \n con el documento de identidad  ")
    titulo.config(bg = "pink",fg="black", font=("Helvetica", 20))
    titulo.place(x=10,y=10)

def familia():
    global toplevel_familia
    toplevel_familia = Toplevel()
    toplevel_familia.title("familia")
    toplevel_familia.resizable(False, False)
    toplevel_familia.geometry("600x500")
    toplevel_familia.config(bg="white")



    frame_familia=Frame(toplevel_familia)
    frame_familia.config(bg="blue", width=600, height=500)
    frame_familia.place(x=0,y=0)

    titulo = Label(frame_familia, text=" papa , mama , machete \n hermanos ")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 20))
    titulo.place(x=10,y=10)







def educacion ():
    global toplevel_educacion
    toplevel_educacion = Toplevel()
    toplevel_educacion.title("educacion")
    toplevel_educacion.resizable(False, False)
    toplevel_educacion.geometry("600x500")
    toplevel_educacion.config(bg="white")



    frame_educacion=Frame(toplevel_educacion)
    frame_educacion.config(bg="green", width=600, height=500)
    frame_educacion.place(x=0,y=0)

    titulo = Label(frame_educacion, text="colegio san jose del guanenta ")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 20))
    titulo.place(x=10,y=10)





def amigos ():
    global toplevel_
    toplevel_amigos = Toplevel()
    toplevel_amigos.title("amigos")
    toplevel_amigos.resizable(False, False)
    toplevel_amigos.geometry("600x500")
    toplevel_amigos.config(bg="white")


    frame_amigos=Frame(toplevel_amigos)
    frame_amigos.config(bg="grey", width=600, height=500)
    frame_amigos.place(x=0,y=0)

    titulo = Label(frame_amigos, text=" soreth , juan fernando , julian , soreth   ")
    titulo.config(bg = "grey",fg="black", font=("Helvetica", 20))
    titulo.place(x=10,y=10)






def hobbies ():
    global toplevel_hobbies
    toplevel_hobbies = Toplevel()
    toplevel_hobbies.title("hobbies")
    toplevel_hobbies.resizable(False, False)
    toplevel_hobbies.geometry("600x500")
    toplevel_hobbies.config(bg="white")



    frame_hobbies=Frame(toplevel_hobbies)
    frame_hobbies.config(bg="grey", width=600, height=500)
    frame_hobbies.place(x=0,y=0)

    titulo = Label(frame_hobbies, text="dormir , jugar videojuegos , voleyboll")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 20))
    titulo.place(x=10,y=10)

def horario ():
    global toplevel_horario
    toplevel_horario = Toplevel()
    toplevel_horario.title("horario")
    toplevel_horario.resizable(False, False)
    toplevel_horario.geometry("600x500")
    toplevel_horario.config(bg="white")

    frame_horario=Frame(toplevel_horario)
    frame_horario.config(bg="grey", width=600, height=500)
    frame_horario.place(x=0,y=0)

    titulo = Label(frame_horario, text="existo ")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 20))
    titulo.place(x=10,y=10)





def icfes ():
    global toplevel_icfes
    toplevel_icfes = Toplevel()
    toplevel_icfes.title("icfes")
    toplevel_icfes.resizable(False, False)
    toplevel_icfes.geometry("600x500")
    toplevel_icfes.config(bg="white")


    frame_icfes=Frame(toplevel_icfes)
    frame_icfes.config(bg="grey", width=600, height=500)
    frame_icfes.place(x=0,y=0)

    titulo = Label(frame_icfes, text=" nose que escribir")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 20))
    titulo.place(x=10,y=10)




def vida ():
    global toplevel_vida
    toplevel_vida = Toplevel()
    toplevel_vida.title(" vida")
    toplevel_vida.resizable(False, False)
    toplevel_vida.geometry("600x500")
    toplevel_vida.config(bg="white")


    frame_vida=Frame(toplevel_vida)
    frame_vida.config(bg="grey", width=600, height=500)
    frame_vida.place(x=0,y=0)

    titulo = Label(frame_vida, text=" programar con chatgpt :0" + "\n" + "")
    titulo.config(bg = "grey",fg="white", font=("Helvetica", 20))
    titulo.place(x=10,y=10)

logo = PhotoImage(file="yo.png")
lb_logo = Label(ventana_juego, image=logo, bg="white")
lb_logo.place(x=300,y=10)



titulo = Label(ventana_juego, text="io")
titulo.config(bg = "grey",fg="white", font=("Helvetica", 20))
titulo.place(x=200,y=10)


frame_1 = Button(ventana_juego)
frame_1.config(bg="white",text = "nacimiento",  width = 10 ,height = 2,  command=nacimiento)
frame_1.place(x = 10 , y =10)


frame_2 = Button(ventana_juego)
frame_2.config(bg="white",text ="familia", width = 10 ,height = 2   , command=familia)
frame_2.place(x = 10 , y =80)


frame_3 = Button(ventana_juego)
frame_3.config(bg="white",text ="educacion ",  width = 10 ,height = 2 , command= educacion  )
frame_3.place(x = 10 , y =160)


frame_4 = Button(ventana_juego)
frame_4.config(bg="white" , text= " amigos", width = 10 ,height = 2  , command=amigos )
frame_4.place(x = 10 , y =240)


frame_5 = Button(ventana_juego)
frame_5.config(bg="white",text="hobbies", width = 10 ,height = 2 , command=hobbies)
frame_5.place(x = 10 , y =320)


frame_6 = Button(ventana_juego)
frame_6.config(bg="white", text = "horario", width = 10 ,height = 2 , command=horario)
frame_6.place(x = 10 , y =400)


frame_7 = Button(ventana_juego)
frame_7.config(bg="white",text= "preparacion para icfes",  width = 10 ,height = 2 , command=icfes)
frame_7.place(x = 10 , y =480)


frame_8 = Button(ventana_juego)
frame_8.config(bg="white",text= "proyecto de vida" ,  width = 10 ,height = 2 , command= vida)
frame_8.place(x = 10 , y =560)



ventana_juego.mainloop()