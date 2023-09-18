from tkinter import Tk , Canvas,Label,Button,Event
from time import strftime

ventana = Tk()
ventana.config(bg='gray') # este es el color 
ventana.geometry('400x400')# crea el tamaño de la ventana
ventana.overrideredirect(1)#elimina los bordes dependiendo del valor , 1 es si y 0 no , easy peace... creo..
#lo malo es que elimina los botones para cerrar la ventana jaja , pero con alguna funcion y un bind se arregla creo..x2 
ventana.resizable(width=False, height=False)#sirve para que no se pueda ajusta la ventana
ventana.wm_attributes('-transparentcolor', 'gray')# simil al alpha pero solo toca el fondo
# ventana.attributes('-alpha',0.0)  # -alpha hace que le de transparencia dependiendo del valor asignado 
#  si es 0.0 es trasnparente , si es 1.0 no lo es 
ventana.title('Reloj prototipo pete')


def obtener_tiempo():
    hora = strftime('%H:%M:%S')# h es hora , M minuto y S segundos
    dia = strftime('%A')# A es para el nombre del dia actual
    fecha = strftime('%d:%m:%Y') 
    zona = strftime('%Z')
    x = texto_hora.winfo_height()
    t = int((x-5)*0.32)
    if dia =='Monday': # como los dias aparecen en ingles , el condicional los pasa a español 
       dia = 'Lunes'
    elif dia =='Tuesday':
       dia = 'Martes'
    elif dia =='Wednesday':
       dia = 'Miercoles'
    elif dia =='Thursday':
       dia = 'Jueves'
    elif dia =='Friday':
       dia = 'Viernes'
    elif dia =='Saturday':
       dia = 'Sábado'
    elif dia =='Sunday':
       dia = 'Domingo'
    texto_hora.config(text=hora, font = ('Radioland', t))
    texto_dia.config(text=dia )
    texto_fecha.config(text=fecha)	
    texto_zona.config(text=zona)
    texto_hora.after(1000, obtener_tiempo)
#la funcion salir es por si le elimino los bordes  y quiero cerrra la ventana

def salir(*args):
   ventana.destroy()
   ventana.quit()

def iniciar(Event):
   global x, y
   x = Event.x
   y = Event.y

def parar(Event):
   global x, y
   x=None
   y=None

def mover(Event):
   global x, y
   deltax = Event.x - x 
   deltay = Event.y - y 
   ventana.geometry("+%s+%s" % (ventana.winfo_x() + deltax,ventana.winfo_y() + deltay))
   ventana.update()


# con los metodos bind se configuran las teclas a las funciones de arriba
ventana.bind("<ButtonPress-1>",iniciar)
ventana.bind("<ButtonRelease-1>",parar)
ventana.bind("<B1-Motion>",mover)
ventana.bind("<Escape>",salir)


# los label muestran en la pantalla la hora etc..
texto_hora = Label(ventana,  fg = 'white', bg='gray' ,font=('Fuggles',20))
texto_hora.grid(row=0,sticky="nsew", ipadx=5, ipady=20)
texto_dia = Label(ventana,  fg = 'white',  bg='gray', font = ('Fuggles',20))
texto_dia.grid(row=1,sticky="nsew")
texto_fecha = Label(ventana,  fg = 'white',  bg='gray', font = ('Arial',20, 'bold'))
texto_fecha.grid(row=2,sticky="nsew")
texto_zona= Label(ventana,fg='white',bg='gray',font=('Arial',25))
texto_zona.grid(row=3,sticky='nsew' )
obtener_tiempo()
ventana.mainloop() 
