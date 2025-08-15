from tkinter import *
from tkinter import messagebox
import random

ventana_juego = Tk()

ventana_juego.title("io")

ventana_juego.geometry("800x700")

ventana_juego.resizable(0,0)

ventana_juego.config(bg="grey")



frame_1 = Button(ventana_juego)
frame_1.config(bg="white",text = "nacimiento",  width = 10 ,height = 2)
frame_1.place(x = 10 , y =10)


frame_2 = Button(ventana_juego)
frame_2.config(bg="white",text ="familia", width = 10 ,height = 2)
frame_2.place(x = 10 , y =80)


frame_3 = Button(ventana_juego)
frame_3.config(bg="white",text ="educacion ",  width = 10 ,height = 2)
frame_3.place(x = 10 , y =160)


frame_4 = Button(ventana_juego)
frame_4.config(bg="white" , text= " amigos", width = 10 ,height = 2)
frame_4.place(x = 10 , y =240)


frame_5 = Button(ventana_juego)
frame_5.config(bg="white",text="hobbies", width = 10 ,height = 2)
frame_5.place(x = 10 , y =320)

frame_6 = Button(ventana_juego)
frame_6.config(bg="white", text = "horario", width = 10 ,height = 2)
frame_6.place(x = 10 , y =400)


frame_7 = Button(ventana_juego)
frame_7.config(bg="white",text= "preparacion para icfes",  width = 10 ,height = 2)
frame_7.place(x = 10 , y =480)


frame_8 = Button(ventana_juego)
frame_8.config(bg="white",text= "proyecto de vida" ,  width = 10 ,height = 2)
frame_8.place(x = 10 , y =560)





ventana_juego.mainloop()