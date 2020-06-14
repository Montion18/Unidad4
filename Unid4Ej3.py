from tkinter import *
from tkinter import ttk
import datetime
from Manejador import Manejador
class App:
    __root=None
    __hora=None

    def muestra(self,m):
        fila=1
        mlista=m.retornalista()
        dolares=m.retornadolares()
        aux=[]
        for i in range(len(dolares)):
            if dolares[i]['casa']['compra']!="No Cotiza" and dolares[i]['casa']['venta']!=0 and (dolares[i]['casa']['nombre']).count("Dolar")!=0:
                Label(self.__root,text="Casa: {}".format(dolares[i]['casa']['nombre']),font=("Arial",11)).grid(row=fila,column=0,pady=20,padx=15)
                Label(self.__root,text="Compra: {}".format(dolares[i]['casa']['compra']),font=("Arial",11)).grid(row=fila,column=1,pady=20,padx=15)
                Label(self.__root,text="Venta: {}".format(dolares[i]['casa']['venta']),font=("Arial",11)).grid(row=fila,column=2,pady=20,padx=15)
                aux.append(dolares[i])
                fila+=1

        fila=1
        for j in range(len(aux)):
            if mlista[j].getpc() != aux[j]['casa']['compra'] or mlista[j].getpv() != aux[j]['casa']['venta']:
                if datetime.datetime.now().minute<10:
                    hora=str(datetime.datetime.now().hour) +":"+"0"+ str(datetime.datetime.now().minute)
                else:
                    hora=str(datetime.datetime.now().hour) +":"+ str(datetime.datetime.now().minute)
            else:
                hora="---"
            Label(self.__root,text="Ultima Actualizacion: {}".format(hora),font=("Arial",11)).grid(row=fila,column=3,pady=20)
            fila+=1

    def __init__(self):
        m=Manejador()
        m.listar()
        m.agregarprecios()
        self.__root=Tk()
        self.muestra(m)
        self.__root.geometry("800x500")
        self.__root.title("Cotizacion divisas")
        Button(self.__root,text="Actualizar",font=("Arial",11),command=lambda:[m.listar(),self.muestra(m)]).grid(sticky='s')
        self.__root.mainloop()


if __name__=='__main__':
    app=App()