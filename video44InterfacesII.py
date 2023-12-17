from tkinter import *
ventana= Tk()
ventana.title("Prueba de cámara gráfica")
#ventana.resizable()
ventana.iconbitmap("live.ico")
ventana.geometry("650x350")
ventana.config(bg="black")

#ahora el contenedor
miFrame=Frame()
#se crea un texto dentro del frame o contenedor 
texto=Label(miFrame,text="Inicio")
texto.place(x=50,y=50)
texto.config(bg="Blue",foreground="white" , justify="center",font="Bold")
#ahora agregamos una caja de texto en otros lenguajes llamados textbox aca se llaman Entry
cuadro=Entry(miFrame)
cuadro.place(x=100,y=100)
#otro texto
texto2=Label(miFrame,text="Contraseña",font="Bold")
texto2.place(x=120,y=150)
#fin del otro label 
miFrame.pack(side="right",anchor="n") #para darle al frame una locación especifica.
miFrame.config(bg="Blue")
miFrame.config(width="650",height="350")
miFrame.config(cursor="hand2")


ventana.mainloop()