import numpy as np
import scipy as sp
from scipy.stats import binom, hypergeom, chisquare, poisson
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

def Fbinomial():
	#Parametros
	n = n2.get()
	p = p2.get()
	mean, var, skew, kurt = binom.stats(n,p, moments='mvsk')
	x = np.arange(binom.ppf(0.01, n,p), binom.ppf(0.99, n,p))

	#Operaciones
	prob = binom.pmf(x,n,p)
	print('Probabilidades individuales para binomial: ',prob)

	#Graficar
	fig, ax = plt.subplots(1,1)
	ax.plot(x, prob, 'bo', ms=8, label='Binomial')
	ax.vlines(x, 0, prob, colors='r', lw=5, alpha=0.5)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	#ax.legend(loc='best', frameon=False)
	plt.show()

def Fhipergeo():
	#Parametros
	N = N1.get()
	k = n1.get()
	n = k1.get()

	#Operaciones
	X = np.arange(0, n+1)
	prob = hypergeom.pmf(X,N,k,n)
	print('Probabilidades individuales para Hipergeometrica: ',prob)
        
	#Graficar
	fig, ax = plt.subplots(1,1)
	ax.plot(X, prob, 'bo', ms=8, label='Hipergeométrica')
	ax.vlines(X, 0, prob, colors='g', lw=2, alpha=0.5)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	#ax.legend(loc='best', frameon=False)
	plt.show()

def Fpoisson():
	#Parametros
	mu = simLambda.get()
	k = xva3.get()
	mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')

	#Operaciones
	x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
	prob = poisson.pmf(x, mu)
	print('Probabilidades individuales para Poisson: ',prob)

	#Graficar
	fig, ax = plt.subplots(1,1)
	ax.plot(x, prob, 'bo', ms=8, label='Poisson')
	ax.vlines(x, 0, prob, colors='b', lw=5, alpha=0.5)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	#ax.legend(loc='best', frameon=False)
	plt.show()


def Abrir():
    VentAbrir=Tk()
    VentAbrir.geometry("300X300+50+50")
    VentAbrir.title("ventana")
    VentAbrir.mainloop() #Cuando se abre otra ventana

ventana = Tk()
pestañas=ttk.Notebook(ventana)
ventana.geometry("350x250")
ventana.title("Menu")
#Creacion de menu#
##barra de menu##
BarraMenu=Menu(ventana)
###opciones de menu###
MenuArchivo=Menu(BarraMenu)
MenuEdicion=Menu(BarraMenu)
###comandos de menu###
MenuArchivo.add_command(label="Abrir" , command=Abrir)
MenuArchivo.add_command(label="Nuevo")
MenuArchivo.add_command(label="Guardar")
MenuArchivo.add_command(label="Cerrar")
MenuArchivo.add_separator()
MenuArchivo.add_command(label="Salir", command=ventana.destroy)
#Agregar los menus a la barra de menu#
MenuEdicion.add_command(label="Copiar")
MenuEdicion.add_command(label="Pegar")
MenuEdicion.add_command(label="Deshacer")
MenuEdicion.add_command(label="Rehacer")
#Agregar Menus 
BarraMenu.add_cascade(label="Archivo",menu=MenuArchivo)
BarraMenu.add_cascade(label="Edicion",menu=MenuEdicion)

#Pestañas#
pestañas.pack(fill='both',expand='yes')
Hiper=ttk.Frame(pestañas)
bino=ttk.Frame(pestañas)
Pooi=ttk.Frame(pestañas)
pestañas.add(Hiper,text='Hipergeometrica')
pestañas.add(bino,text='Binomial')
pestañas.add(Pooi,text='Poisson')

#Cuerpo de las pestañas#

	##Hipergeometrica##
##Etiqueta=Label(Hiper,text="Variable Aleatoria :",font=("Arial",12)).place(x=10, y=10)
##xva1= IntVar() #Variable aleatoria x
##inputxva1 = Entry(Hiper,textvariable=xva1).place(x=150 , y=10)

Etiqueta_N=Label(Hiper,text="Tamaño de la poblacion:",font=("Arial",12)).place(x=10, y=10)
N1=DoubleVar()	#Tamaño de la poblacion
input_N1 = Entry(Hiper, textvariable=N1).place(x=190 , y=10)

Etiqueta_k=Label(Hiper,text="Exito:",font=("Arial",12)).place(x=10, y=50)
k1=DoubleVar()	#Exito
input_k1 = Entry(Hiper,textvariable=k1).place(x=190 , y=50)

Etiqueta_n=Label(Hiper,text="Tamaño de la muestra:",font=("Arial",12)).place(x=10, y=90)
n1=DoubleVar()	#muestra
input_n1 = Entry(Hiper, textvariable=n1).place(x=190 , y=90)

do=Button(Hiper, text = "Realizar!",command=Fhipergeo, font =("Arial", 10), width=10)
do.place(x=120, y=170)

	##Binomial
Etiqueta_n=Label(bino,text="Tamaño de la poblacion:",font=("Arial",12)).place(x=10, y=10)
n2 = DoubleVar()
input_n2 = Entry(bino, textvariable=n2).place(x=190 , y=10)

Etiqueta_b=Label(bino,text="Exito:",font=("Arial",12)).place(x=10, y=50)
p2 = DoubleVar()
input_p2 = Entry(bino,textvariable=p2).place(x=190 , y=50)

do=Button(bino, text = "Realizar!",command=Fbinomial, font =("Arial", 10), width=10)
do.place(x=120, y=170)

	##Poisson
Etiqueta=Label(Pooi,text="Variable Aleatoria:",font=("Arial",12)).place(x=10, y=10)
xva3= DoubleVar()
input_xva3 = Entry(Pooi, textvariable=xva3).place(x=190 , y=10)

Etiqueta_Mediana=Label(Pooi,text="Lambda:",font=("Arial",12)).place(x=10, y=50)
simLambda=DoubleVar()
input_simLambda = Entry(Pooi, textvariable=simLambda).place(x=190 , y=50)

do=Button(Pooi, text = "Realizar!", command=Fpoisson, font =("Arial", 10), width=10)
do.place(x=120, y=170)


#Ejecutar programa
ventana.config(menu=BarraMenu)
ventana.mainloop()
