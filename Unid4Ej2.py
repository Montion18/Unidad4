from tkinter import *
from tkinter import ttk
import requests
class App:
    __root=None
    __dolares=None
    __pesos=None
    __precio=None

    def mostrar(self,*args):
        try:
            cambio=int(self.__pesos.get())*float(self.__precio)
            Label(self.__root,text="es equivalente a {:.2f} pesos".format(cambio)).grid(row=2,column=0)
        except ValueError:
            pass

    def __init__(self):
        url='https://www.dolarsi.com/api/api.php?type=dolar'
        r=requests.get(url)
        lista=r.json()
        i=0

        while i<len(lista) and lista[i]['casa']['nombre'] != 'Oficial':
            i+=1
        if i<len(lista):
            self.__precio=lista[i]['casa']['venta'].replace(',','.')
        self.__root=Tk()
        self.__root.geometry("400x200")
        self.__root.title("Conversor de moneda")
        self.__pesos=StringVar()
        self.__dolaresEntry=Entry(self.__root,textvariable=self.__pesos)
        self.__dolaresEntry.grid(row=0,column=0)
        self.__dolares=Label(self.__root,text="Dolares")
        self.__dolares.grid(row=0,column=2)
        self.__pesos.trace('w',self.mostrar)
        
        salir=Button(self.__root,text="Salir",command=lambda:self.__root.quit())
        salir.grid(row=2,column=3)
        self.__root.mainloop()

    def conversor(self):
        pass

if __name__=='__main__':
    app=App()