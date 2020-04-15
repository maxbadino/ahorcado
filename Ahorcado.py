from tkinter import *
from random import randint
from tkinter.messagebox import *
letrasUsadas=[]

vidas = 7
letrasAcertadas=0

def colocarLetras():
    x=50
    y=150
    contador = 0
    Label(juegoFrame,text= "Letras sin usar").place(x=50,y=100)
    for i in range(26):
        contador+=1
        letrasLabel[i].place(x=x,y=y)
        x+=30
        if contador == 5:
            y+=35
            contador=0
            x=50


def probarLetraFuncion():
    global vidas
    global letrasAcertadas
    letrasUsadas.append(letraObtenida.get())
    print(letrasUsadas)
    letrasLabel[ord(letraObtenida.get())-97].config(text="")

    if letraObtenida.get() in palabra:
        if palabra.count(letraObtenida.get())>1:
            letrasAcertadas+=palabra.count(letraObtenida.get())
            for i in range(len(palabra)):
                if palabra [i] == letraObtenida.get():
                    guiones[i].config(text=""+letraObtenida.get())
        else:
            letrasAcertadas+=1
            guiones[palabra.index(letraObtenida.get())].config(text=""+letraObtenida.get())
        if letrasAcertadas == len(palabra):
            showwarning(title="Ganaste",message="Felcitaciones ganaste!")
    else:
        vidas-=1
        if vidas == 0:
            showwarning(title="Perdiste",message="Se te acabaron las vidas" )
raiz = Tk()
archivo = open("palabras.txt", "r")
conjuntoPalabras = list(archivo.read().split("\n"))
palabra = conjuntoPalabras[randint(0,len(conjuntoPalabras)-1)].lower()
letraObtenida=StringVar()

raiz.config(width=700, height=600, bg="blue", relief="groove", bd=10)
juegoFrame = Frame(raiz)
juegoFrame.config(width=700, height=600, relief="sunken", bd=15)
juegoFrame.grid_propagate(False)
juegoFrame.pack()

Label(juegoFrame,text="Introduce una letra", font=("Verdana", 24)
      ).grid (row=0, column=0,padx=10,pady=10)
letra = Entry(juegoFrame,width=1, font=("Verdana",24),textvariable=letraObtenida
              ).grid(row=0, column=1, padx=10, pady=10)

probarLetra = Button(juegoFrame,text="Probar",bg="yellow",command=probarLetraFuncion
                     ).grid(row=1,column=0,pady=10)

letrasLabel = [Label(juegoFrame,text=chr(j+97),font=("Verdana",15)) for j in range(26)]
colocarLetras()
guiones=[Label(juegoFrame,text="_",font=("verdana",30)) for _ in palabra ]
inicialX=200
for i in range (len(palabra)):
    guiones[i].place(x=inicialX,y=400)
    inicialX+=50


raiz.mainloop()