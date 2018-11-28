from tkinter import *
from tkinter import ttk

def Abrir():
    VentAbrir=Tk()
    VentAbrir.geometry("300X300+50+50")
    VentAbrir.title("ventana")
    VentAbrir.mainloop()

def Fbinomial():
	fig, ax = plt.subplots(1,1)

	#Parametros
	n = 10
	p = 0.6
	mean, var, skew, kurt = binom.stats(n,p, moments='mvsk')

	#PMF
	x = np.arange(binom.ppf(0.01, n,p), binom.ppf(0.99, n,p))
	ax.plot(x, binom.pmf(x,n,p), 'bo', ms=8, label='binom pmf')
	ax.vlines(x, 0, binom.pmf(x,n,p), colors='r', lw=5, alpha=0.5)

	#Check CDF y PPF
	prob = binom.cdf(x,n,p)
	np.allclose(x, binom.ppf(prob,n,p))

	#Random
	r = binom.rvs(n,p,size=1000)

	#Mostrar grafica
	plt.show()

def Fhipergeo():
	#fig, ax = plt.subplots(1,1)

	#Parametros
	[x, y, z] = [20, 7, 12]
	rv = hypergeom(x, y, z)
	X = np.arange(0, y+1)
	pmf1 = rv.pmf(X)

	#Graficas
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(X, pmf1, 'bo')
	ax.vlines(X, 0, pmf1, lw=2)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	plt.show()

	#Metodo directo
	prb = hypergeom.cdf(X,x,y,z)

	#Random
	ran = hypergeom.rvs(x,y,z,size=10)

def Fpoisson():
	fig, ax = plt.subplots(1,1)

	#Parametros
	mu = 0.6
	mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')

	#PMF
	x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))
	ax.plot(x, poisson.pmf(x,mu), 'bo', ms=8, label='poisson pmf')
	ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)

	#Check CDF y PPF
	prob = poisson.cdf(x, mu)
	np.allclose(x,poisson.ppf(prob,mu))

	#Random
	r = poisson.rvs(mu, size=1000)

	#Mostrar grafica
	plt.show()

ventana = Tk()
pestañas=ttk.Notebook(ventana)
ventana.geometry("600x600+10+10")
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
xvah= StringVar() #Variable aleatoria x
N=StringVar()	#Tamaño de la poblacion
K=StringVar()	#Exito
n=StringVar()	#muestra
Etiqueta=Label(Hiper,text="Variable Aleatoria :",font=("Arial",12)).place(x=10, y=10)
xvah = Entry(Hiper,textvariable=xvah).place(x=150 , y=10)

Etiqueta_N=Label(Hiper,text="Tamaño de la poblacion",font=("Arial",12)).place(x=10, y=50)
N = Entry(Hiper, textvariable=N).place(x=190 , y=50)

Etiqueta_k=Label(Hiper,text="Exito:",font=("Arial",12)).place(x=10, y=90)
K = Entry(Hiper,textvariable=K).place(x=100 , y=90)

Etiqueta_n=Label(Hiper,text="Tamaño de la muestra",font=("Arial",12)).place(x=10, y=130)
n = Entry(Hiper, textvariable=N).place(x=190 , y=130)

do=Button(Hiper, text = "Realizar!",font =("Arial", 10), width=10).place(x=500, y=35)
	##Binomial
n= StringVar()
b=StringVar()
Etiqueta_n=Label(bino,text="Tamaño de la poblacion",font=("Arial",12)).place(x=10, y=50)
n = Entry(bino, textvariable=N).place(x=190 , y=50)

Etiqueta_b=Label(bino,text="Exito:",font=("Arial",12)).place(x=10, y=90)
b = Entry(bino,textvariable=K).place(x=100 , y=90)

do=Button(bino, text = "Realizar!",font =("Arial", 10), width=10).place(x=500, y=35)

	##Poisson
xva= StringVar()
Media=StringVar()
Tiempo=StringVar()
Etiqueta=Label(Pooi,text="Variable Aleatoria :",font=("Arial",12)).place(x=10, y=10)
xva = Entry(Pooi, textvariable=xva).place(x=150 , y=10)

Etiqueta_Mediana=Label(Pooi,text="Media/Varianza/evento:",font=("Arial",12)).place(x=10, y=50)
Media = Entry(Pooi, textvariable=Media).place(x=190 , y=50)

Etiqueta_Tiempo=Label(Pooi,text="Tiempo :",font=("Arial",12)).place(x=10, y=90)
Tiempo = Entry(Pooi, textvariable=xva).place(x=100 , y=90)

do=Button(Pooi, text = "Realizar!",font =("Arial", 10), width=10).place(x=500, y=35)
#Ejecutar programa
ventana.config(menu=BarraMenu)
ventana.mainloop()