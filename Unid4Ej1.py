from tkinter import *
from tkinter import ttk

class App:
    __root=None
    __altura=None
    __peso=None
    __IMC=None

    def check(self):
        global op
        global labelimc
        op=Label(self.__root)
        labelimc=Label(self.__root,text="Tu indice de Masa Corporal (IMC) es {:.2f} Kg/m2".format(self.__IMC),font=("Arial",11),bg="spring green")
        labelimc.grid(row=8,column=0,padx=20,pady=20,columnspan=10)
        if self.__IMC<18.5:
            op=Label(self.__root,text="Peso inferior al normal",font=("Arial",15),bg="spring green")
            op.grid(row=10,column=0,padx=20,pady=20,columnspan=10)

        elif self.__IMC>18.5 and self.__IMC<24.9:
            op=Label(self.__root,text="Peso Normal",font=("Arial",15),bg="spring green")
            op.grid(row=10,column=0,padx=20,pady=20,columnspan=10)
        elif self.__IMC>25.0 and self.__IMC<29.9:
            op=Label(self.__root,text="Peso superior al normal",font=("Arial",15),bg="spring green")
            op.grid(row=10,column=0,padx=20,pady=20,columnspan=10)
        elif self.__IMC>30.0:
            op=Label(self.__root,text="Obesidad",font=("Arial",15),bg="spring green")
            op.grid(row=10,column=0,padx=20,pady=20,columnspan=10)
        
    def limpiartodo(self):
        self.__alturaEntry.delete(0,END)
        self.__pesoEntry.delete(0,END)
        op.grid_forget()
        labelimc.grid_forget()
    def Calculo(self):
        try:
            alt=int(self.__alturaEntry.get())
            peso=float(self.__pesoEntry.get())
            self.__IMC=peso/(alt/100)**2
            self.check()
        except ValueError:
            Label(self.__root,text="ERROR ingrese solo numeros",foreground="black",background="red").grid()

    def __init__(self):
        self.__root=Tk()
        op=Label(self.__root)
        self.__root.geometry("750x400")
        self.__root.title("Calculadora de IMC")
        self.__root.config(background="white")
        titulo=ttk.Label(self.__root,font=("Arial",20),text="Calculadora de IMC",foreground="black",background="white")
        titulo.grid(sticky="n",row=0,column=1)
        self.__altura=StringVar()
        self.__peso=StringVar()

        alturalabel=ttk.Label(self.__root,text="Altura: ",font=(10),foreground="grey19",background="white")
        alturalabel.grid(sticky='w',row=2,column=0,pady=30)
        self.__alturaEntry=ttk.Entry(self.__root,textvariable=self.__altura)
        self.__alturaEntry.grid(sticky='w',row=2,column=1,pady=20,ipadx=70)
        self.__alturaEntry.focus()

        cmlabel=ttk.Label(self.__root,text="cm",font=(10),foreground="grey10",background="grey")
        cmlabel.grid(row=2,column=2,sticky='w')

        pesolabel=ttk.Label(self.__root,text="Peso: ",font=(10),width=8,foreground="grey19",background="white")
        pesolabel.grid(sticky='w',row=4,column=0,pady=20)
        self.__pesoEntry=ttk.Entry(self.__root,width=8,textvariable=self.__peso)
        self.__pesoEntry.grid(sticky='w',row=4,column=1,ipadx=107,pady=20)
        
        kglabel=ttk.Label(self.__root,text="kg",font=(10),foreground="grey10",background="grey")
        kglabel.grid(row=4,column=2)

        calcular=Button(self.__root,text="Calcular",bg="lime green",fg="white",font=(22),command=lambda:self.Calculo())
        calcular.grid(row=6,column=0,ipadx=60,padx=40)

        limpiar=Button(self.__root,text="Limpiar",bg="lime green",fg="white",font=(22),command=lambda:self.limpiartodo())
        limpiar.grid(row=6,column=1,ipadx=60,padx=28)

        
        self.__root.mainloop()



if __name__=='__main__':
    app=App()