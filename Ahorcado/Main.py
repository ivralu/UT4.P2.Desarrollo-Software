import tkinter as tk;
from tkinter import messagebox;
import random;

class ahorcado():

    def __init__(self):

        self.letrasUsadas=[]

        self.raiz = tk.Tk()

        self.raiz.config(width=1000, height = 600, bg="blue",relief = "groove",bd=10)

 

        self.juegoFrame = tk.Frame(self.raiz)

        self.juegoFrame.config (width=1000, height = 600,relief = "sunken",bd=15)

        self.juegoFrame.grid_propagate(False)

        self.juegoFrame.pack()

        self.lbl1 = tk.Label(self.juegoFrame,text= "Introduce una letra", font=("Verdana", 24),).grid(row=0, column=0,padx=10,pady=10)

        self.letraObtenida=tk.StringVar()

        self.letra= tk.Entry(self.juegoFrame,width=1,font=("Verdana", 24),textvariable=self.letraObtenida)

        self.letra. grid(row=0, column=1,padx=10,pady=10)

        self.letraObtenida.trace("w", lambda *args: self.limitador(self.letraObtenida))

 

        self.letra.focus()

        self.probarLetra = tk.Button(self.juegoFrame,text="Probar",bg="yellow",command=self.probarLetraFuncion).grid(row=1,column=0,pady=10)

        self.palabra = self.lee_archivo()

        self.guiones = [tk.Label(self.juegoFrame,text="_",font=("verdana",30)) for  _ in self.palabra ]

        inicialX=200

        for i in range(len(self.palabra)):

            self.guiones[i].place(x=inicialX,y=400)

            inicialX+=50

        self.vidas = 7

        self.lbl2=tk.Label(self.juegoFrame,text= f"{self.vidas} vidas.", font=("Verdana", 24),)

        self.lbl2.grid(row=0, column=80,padx=10,pady=10)

 

 

        self.raiz.mainloop()

 

 

    def lee_archivo(self):

        archivo = open("palabras.txt")

        conjuntoPalabras= list(archivo.read().split("\n"))

        palabra = conjuntoPalabras[random.randint(0,len(conjuntoPalabras)-1)].lower()

        archivo.close()

        return palabra

 

    def probarLetraFuncion(self):

 

        self.letrasUsadas.append(self.letraObtenida.get())

        print(self.letrasUsadas)

        if self.letraObtenida.get() in self.palabra:

            if self.palabra.count(self.letraObtenida.get())>0:

                for i in range(len(self.palabra)):

                    if self.palabra[i]==self.letraObtenida.get():

                        self.guiones[i].config(text=""+self.letraObtenida.get())

                else:

                    self.guiones[self.palabra.index(self.letraObtenida.get())].config(text=""+self.letraObtenida.get())

        else:

            self.vidas-=1

            self.lbl2.configure(text=f"{self.vidas} vidas.")

            if self.vidas==0:

                messagebox.showwarning(title="Derrota",message="Se te acabaron las vidas")

        self.letra.delete(0,1)

 

    def limitador(self,entrada):

        if len(entrada.get()) > 0:

            entrada.set(entrada.get()[:1])

 

juego=ahorcado()