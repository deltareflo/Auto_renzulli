import tkinter as tk
from tkinter import ttk
import tkinter.font
from tkinter import messagebox
class Esencial(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        #entry globales
        #variables para los entry
        self.anno=tk.StringVar()
        self.nombre_label=tk.StringVar()
        #self.nombre_label.set("Nombre")
        self.nombre_text=tk.StringVar()
        
        self.titulo_text=tk.StringVar()
        self.titulo_label=tk.StringVar()
        
        self.fuente=tkinter.font.Font(family='Times New Roman', size=12)
        #configuracion de los entry
        self.name_entry = ttk.Entry(self, width=100, textvariable=self.nombre_text)
        self.name_entry.grid(column=1, row=0, padx=5,pady=5, columnspan=5)
        self.agno_entry = ttk.Entry(self, width=100,textvariable=self.anno)
        self.agno_entry.grid(column=1, row=1, padx=5,pady=5, columnspan=5)
        self.titulo_entry = ttk.Entry(self, width=100, textvariable=self.titulo_text)
        self.titulo_entry.grid(column=1, row=2, padx=5,pady=5, columnspan=5)
        config=tkinter.font.Font(family='Times New Roman', size=12, slant='italic')
        self.titulo_entry.config(font=config)
        self.name_entry.config(font=self.fuente)
        self.agno_entry.config(font=self.fuente)
        
        #configuracion de los labels
        self.nombre = ttk.Label(self, text=self.nombre_label)
        self.nombre.grid(column=0, row=0, padx=5,pady=5, sticky="E")
        self.agno = ttk.Label(self, text="Año:")
        self.agno.grid(column=0, row=1, padx=5,pady=5, sticky="E")
        self.titulo = ttk.Label(self, text="Titulo:")
        self.titulo.grid(column=0, row=2, padx=5,pady=5, sticky="E")
        #botones
        
    def nombres(self):
        saludo=""
        if self.name_entry.get()=='':
            return saludo
            #messagebox.showerror(title="Referencias con normas APA", message='Ups! Parece que olvidaste rellenar el campo de nombre')
        else:    
            #Obtengo el nombre y lo invierto
            autors=self.name_entry.get()
            autores=autors.split(',')
            exten=len(autores)-1
        
            for i in range(len(autores)):
                autor=autores[i].split()
                autor.reverse()
                nom=autor[1]
                if exten==0:
                    saludo=saludo+autor[0]+", "+nom[0]+". "
                elif exten==1:
                    if i<exten:
                
                        saludo=saludo+autor[0]+", "+nom[0]+". "
                #print(i)
                    else:
                
                        saludo=saludo+"y "+autor[0]+", "+nom[0]+". "
                #print("y Adios")
                else:
                    if i<(exten-1):
                            saludo=saludo+autor[0]+", "+nom[0]+"., "
                #print(i)
                    elif i<exten:
                            saludo=saludo+autor[0]+", "+nom[0]+". "
                    else:
                        saludo=saludo+"y "+autor[0]+", "+nom[0]+". "
            return saludo
    
class LibroFrame(Esencial):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        #variables entry
        self.nombre_label.set("Nombre y apellido:")
        self.anno.set("2015")
        self.nombre_text.set("Roberto Hernandez, Carlos Fernandez, Pilar Baptista")
        self.titulo_text.set("Metodología de la investigación")
        self.edicion_text=tk.StringVar()
        self.edicion_text.set("6")
        self.volumen_text=tk.StringVar()
        self.volumen_text.set("4")
        self.editorial_text=tk.StringVar()
        self.editorial_text.set("Mc Graw-Hill")
        self.url_text=tk.StringVar()
        self.url_text.set("")
        self.subt_text=tk.StringVar()
        self.subt_text.set("")
        
        #entry
        self.subt_entry = ttk.Entry(self, width=100,textvariable=self.subt_text)
        self.subt_entry.grid(column=1, row=3, padx=5,pady=5, columnspan=5)
        self.edicion_entry = ttk.Entry(self, width=20, textvariable=self.edicion_text)
        self.edicion_entry.grid(column=1, row=4, padx=5,pady=5)
        self.volumen_entry = ttk.Entry(self, width=20, textvariable=self.volumen_text)
        self.volumen_entry.grid(column=3, row=4, padx=5,pady=5)
        self.editorial_entry = ttk.Entry(self, width=20,textvariable=self.editorial_text)
        self.editorial_entry.grid(column=5, row=4, padx=5,pady=5, columnspan=5)
        self.url_entry = ttk.Entry(self, width=100,textvariable=self.url_text)
        self.url_entry.grid(column=1, row=5, padx=5,pady=5, columnspan=5)
        self.T = tk.Text(self, height=4, width=100,  state="normal", font=('Times New Roman', 12))
        self.SS = tk.Scrollbar(self)
        self.SS.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.SS.set)
        self.T.grid(column=1, row=9, padx=5, pady=5, columnspan=5)
        self.SS.grid(column=6, row=9)
        #labels
        self.subt = ttk.Label(self, text="Subtitulo:")
        self.subt.grid(column=0, row=3, padx=5,pady=5, sticky="E")
        self.edicion = ttk.Label(self, text="N° Edición:")
        self.edicion.grid(column=0, row=4, padx=5,pady=5, sticky="E")
        self.volumen = ttk.Label(self, text="Vólumen:")
        self.volumen.grid(column=2, row=4, padx=5,pady=5, sticky="E")
        self.editorial = ttk.Label(self, text="Editorial:")
        self.editorial.grid(column=4, row=4, padx=5,pady=5, sticky="E")
        self.url = ttk.Label(self, text="URL o DOI:")
        self.url.grid(column=0, row=5, padx=5, pady=5, sticky="E")
        
        self.nombre.config(textvariable=self.nombre_label)
        
        self.edicion_entry.config(font=self.fuente)
        self.volumen_entry.config(font=self.fuente)
        self.editorial_entry.config(font=self.fuente)
        self.url_entry.config(font=self.fuente)
        self.subt_entry.config(font=self.fuente)
        
        #botones
        self.referencia_button = ttk.Button(
            self, text="Obtener referencia", command=self.referencia)
        self.referencia_button.grid(column=0, row=7, padx=5,pady=5)
        self.borrar_button = ttk.Button(
            self, text="Borrar", command=self.borrado)
        self.borrar_button.grid(column=1, row=7, padx=5,pady=5)
    def borrado(self):
        self.name_entry.delete(0,'end')
        self.agno_entry.delete(0,'end')
        self.titulo_entry.delete(0,'end')
        self.editorial_entry.delete(0,'end')
        self.url_entry.delete(0,'end')
        self.subt_entry.delete(0,'end')
        self.edicion_entry.delete(0,'end')
        self.volumen_entry.delete(0,'end')
        
   
    def referencia(self):
        try:
            autor=self.nombres()
            print(autor)
            agnos=self.agno_entry.get()
            if agnos=="":
                agnos="s.f"

            print(agnos)   
            titulos=self.titulo_entry.get()
            subtitulo=self.subt_entry.get()
            if subtitulo=="":
                subtitulos=subtitulo
                
            else:
                subtitulos=": {} ".format(subtitulo.capitalize())
            print(subtitulos)
            volumen=self.volumen_entry.get()
            edi=self.edicion_entry.get()
            if edi=="" and volumen=="":
                edicion=edi
            elif volumen=="":
                edicion="( {}a ed.). ".format(edi)
            elif edi=="":
                edicion="( vol. {}). ".format(volumen)

            else:
                edicion="( {}a ed., vol. {}). ".format(edi, volumen)
            print(edicion)    
            editor=self.editorial_entry.get()
            
            enlace=self.url_entry.get()
            
            #self.var_str.set(autor+"("+agnos+"). "+titulos+". "+"ed"+ciudades+". "+pais+":"+editor)
            referencia=autor+"("+agnos+"). "+titulos.capitalize()+subtitulos+". "+edicion+editor+". "+enlace
            self.T.insert(tk.END, referencia)
            self.name_entry.delete(0,'end')
            self.agno_entry.delete(0,'end')
            self.titulo_entry.delete(0,'end')
            self.edicion_entry.delete(0,'end')
            self.editorial_entry.delete(0,'end')
            self.subt_entry.delete(0,'end')
            self.url_entry.delete(0,'end')
            self.volumen_entry.delete(0,'end')
        except:
            messagebox.showerror(title="Referencias con normas APA", message='Ups! Parece que olvidaste rellenar algunos campos')
class RevistaFrame(Esencial):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        #variables
        self.anno.set("2019")
        self.nombre_label.set("Nombre y apellido:")
        self.volumen_text=tk.StringVar()
        self.volumen_text.set("6")
        self.revista_text=tk.StringVar()
        self.revista_text.set("")
        self.nro_text=tk.StringVar()
        self.nro_text.set("4")
        self.pagina_text=tk.StringVar()
        self.pagina_text.set("12-40")
        self.url_text=tk.StringVar()
        self.url_text.set("")
        #labels
        self.revista = ttk.Label(self, text="Nombre revista")
        self.revista.grid(column=0, row=3, padx=5,pady=5, sticky="E")
        self.volumen = ttk.Label(self, text="Vólumen")
        self.volumen.grid(column=0, row=5, padx=5,pady=5, sticky="E")
        self.nro = ttk.Label(self, text="Nro o edición")
        self.nro.grid(column=2, row=5, padx=5,pady=5, sticky="E")
        self.pag = ttk.Label(self, text="Páginas")
        self.pag.grid(column=4, row=5, padx=5,pady=5, sticky="E")
        self.url = ttk.Label(self, text="URL o DOI:")
        self.url.grid(column=0, row=6, padx=5, pady=5, sticky="E")
        self.nombre.config(textvariable=self.nombre_label)
        #entry
        self.revista_entry= ttk.Entry(self, width=100, textvariable=self.revista_text)
        self.revista_entry.grid(column=1, row=3, padx=5, pady=5, columnspan=5)
        self.volumen_entry = ttk.Entry(self, width=20, textvariable=self.volumen_text)
        self.volumen_entry.grid(column=1, row=5, padx=5, pady=5)
        self.nro_entry= ttk.Entry(self, width=20, textvariable=self.nro_text)
        self.nro_entry.grid(column=3, row=5, padx=5, pady=5)
        self.pag_entry = ttk.Entry(self, width=20, textvariable=self.pagina_text)
        self.pag_entry.grid(column=5, row=5, padx=5, pady=5)
        self.url_entry = ttk.Entry(self, width=100,textvariable=self.url_text)
        self.url_entry.grid(column=1, row=6, padx=5,pady=5, columnspan=5)
        
        self.volumen_entry.config(font=self.fuente)
        self.pag_entry.config(font=self.fuente)
        self.revista_entry.config(font=self.fuente)
        self.nro_entry.config(font=self.fuente)
        self.url_entry.config(font=self.fuente)
        self.T = tk.Text(self, height=4, width=100,  state="normal", font=('Times New Roman', 12))
        self.SS = tk.Scrollbar(self)
        self.SS.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.SS.set)
        self.T.grid(column=1, row=9, padx=5, pady=5, columnspan=5)
        self.SS.grid(column=6, row=9)
        #botones
        self.referencia_button = ttk.Button(
            self, text="Obtener referencia", command=self.referencia)
        self.referencia_button.grid(column=0, row=7, padx=5,pady=5)
        self.borrar_button = ttk.Button(
            self, text="Borrar", command=self.borrado)
        self.borrar_button.grid(column=1, row=7, padx=5,pady=5)
        
        
        
    def borrado(self):
        self.name_entry.delete(0,'end')
        self.agno_entry.delete(0,'end')
        self.titulo_entry.delete(0,'end')
        self.revista_entry.delete(0,'end')
        self.nro_entry.delete(0,'end')
        self.pag_entry.delete(0,'end')
        self.url_entry.delete(0,'end')
        self.volumen_entry.delete(0,'end')
    def referencia(self):
        try:
            autor=self.nombres()
            print(autor)
            agnos=self.agno_entry.get()
            if agnos=="":
                agnos="s.f"

            titulos=self.titulo_entry.get()
            numero=self.nro_entry.get()
            revista=self.revista_entry.get()
            volumenes=self.volumen_entry.get()
            enlace=self.url_entry.get()
            if numero=="" and volumenes=="":
                edicion=""
            elif numero!="" and volumenes=="":
                edicion="({}). ".format(numero)
            elif numero=="" and volumenes!="":
                edicion=" Vol. {}. ".format(volumenes)   
            else:
                edicion="{}({}). ".format(volumenes, numero)
            pag=self.pag_entry.get()
            if pag!="":
                pagina="{}. ".format(pag)
            else:
                pagina=pag   
            
            
            #self.var_str.set(autor+"("+agnos+"). "+titulos+". "+"ed"+ciudades+". "+pais+":"+editor)
            referencia=autor+"("+agnos+"). "+titulos.capitalize()+". "+ revista+edicion+pagina+enlace
            self.T.insert(tk.END, referencia)
            self.name_entry.delete(0,'end')
            self.agno_entry.delete(0,'end')
            self.titulo_entry.delete(0,'end')
            self.nro_entry.delete(0,'end')
            self.volumen_entry.delete(0,'end')
            self.pag_entry.delete(0,'end')
            self.revista_entry.delete(0,'end')
            self.url_entry.delete(0,'end')
        except:
            messagebox.showerror(title="Referencias con normas APA", message='Ups! Parece que olvidaste rellenar algunos campos')
class LegalFrame(Esencial):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        self.nombre_label.set("Organismo:")
        self.publi_text=tk.StringVar()
        self.url_text=tk.StringVar()
        
        #label
        self.fuentes = ttk.Label(self, text="Fuente:")
        self.fuentes.grid(column=0, row=5, padx=5,pady=5, sticky="E")
        self.publi = ttk.Label(self, text="Publicación")
        self.publi.grid(column=0, row=6, padx=5,pady=5, sticky="E")
        self.link = ttk.Label(self, text="URL")
        self.link.grid(column=0, row=7, padx=5,pady=5, sticky="E")
        self.nombre.config(textvariable=self.nombre_label)
        #entry
        self.publi_entry = ttk.Entry(self, width=100, textvariable=self.publi_text)
        self.publi_entry.grid(column=1, row=6, padx=5, pady=5, columnspan=4)
        self.link_entry = ttk.Entry(self, width=100, textvariable=self.url_text)
        self.link_entry.grid(column=1, row=7, padx=5, pady=5, columnspan=4)
        self.publi_entry.config(font=self.fuente)
        self.link_entry.config(font=self.fuente)
        self.T = tk.Text(self, height=4, width=100,  state="normal", font=('Times New Roman', 12))
        self.SS = tk.Scrollbar(self)
        self.SS.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.SS.set)
        self.T.grid(column=1, row=9, padx=5, pady=5, columnspan=5)
        self.SS.grid(column=6, row=9)
        #botones
        self.referencia_button = ttk.Button(
            self, text="Obtener referencia", command=self.referencia)
        self.referencia_button.grid(column=0, row=8, padx=5,pady=5)
        self.borrar_button = ttk.Button(
            self, text="Borrar", command=self.borrado)
        self.borrar_button.grid(column=1, row=8, padx=5,pady=5)
    def borrado(self):
        self.name_entry.delete(0,'end')
        self.agno_entry.delete(0,'end')
        self.titulo_entry.delete(0,'end')
        self.publi_entry.delete(0,'end')
        self.link_entry.delete(0,'end')
        
    def referencia(self):
        try:
            autor=self.name_entry.get()
            print(autor)
            agnos=self.agno_entry.get()
            if agnos=="":
                agnos="s.f"

            titulos=self.titulo_entry.get()
            publicacion=self.publi_entry.get()
            enlace=self.link_entry.get()  
            
            
            #self.var_str.set(autor+"("+agnos+"). "+titulos+". "+"ed"+ciudades+". "+pais+":"+editor)
            referencia=autor+"("+agnos+"). "+titulos.capitalize()+". "+ publicacion + ". "+ enlace
            self.T.insert(tk.END, referencia)
            self.name_entry.delete(0,'end')
            self.agno_entry.delete(0,'end')
            self.titulo_entry.delete(0,'end')
            self.publi_entry.delete(0,'end')
            self.link_entry.delete(0,'end')
            
        except:
            messagebox.showerror(title="Referencias con normas APA", message='Ups! Parece que olvidaste rellenar algunos campos')
class TesisFrame(Esencial):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        self.anno.set("2020")
        self.nombre_text.set("Pablo Recalde, Patricia Zalazar")
        self.titulo_text.set("Eficacia programa Intemo+")
        self.tipo_text=tk.StringVar()
        self.tipo_text.set("grado")
        self.instituto_text=tk.StringVar()
        self.instituto_text.set("Universidad Nacional de Asunción")
        self.repo_text=tk.StringVar()
        self.url_text=tk.StringVar()
        self.nombre_label.set("Autor/a:")
        #label
        
        self.tipo = ttk.Label(self, text="Tipo de tesis:")
        self.tipo.grid(column=0, row=4, padx=5,pady=5, sticky="E")
        self.instituto = ttk.Label(self, text="Universidad:")
        self.instituto.grid(column=0, row=5, padx=5,pady=5, sticky="E")
        self.repo = ttk.Label(self, text="Repositorio:")
        self.repo.grid(column=0, row=6, padx=5,pady=5, sticky="E")
        self.link = ttk.Label(self, text="URL")
        self.link.grid(column=0, row=7, padx=5,pady=5, sticky="E")
        self.nombre.config(textvariable=self.nombre_label)
        #entry
        
        self.tipo_entry = ttk.Entry(self, width=100, textvariable=self.tipo_text)
        self.tipo_entry.grid(column=1, row=4, padx=5, pady=5, columnspan=4)
        self.instituto_entry = ttk.Entry(self, width=100, textvariable=self.instituto_text)
        self.instituto_entry.grid(column=1, row=5, padx=5, pady=5, columnspan=4)
        self.repo_entry = ttk.Entry(self, width=100, textvariable=self.repo_text)
        self.repo_entry.grid(column=1, row=6, padx=5, pady=5, columnspan=4)
        self.link_entry = ttk.Entry(self, width=100, textvariable=self.url_text)
        self.link_entry.grid(column=1, row=7, padx=5, pady=5, columnspan=4)
        self.tipo_entry.config(font=self.fuente)
        self.instituto_entry.config(font=self.fuente)
        self.link_entry.config(font=self.fuente)
        self.repo_entry.config(font=self.fuente)
        self.T = tk.Text(self, height=4, width=100,  state="normal", font=('Times New Roman', 12))
        self.SS = tk.Scrollbar(self)
        self.SS.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.SS.set)
        self.T.grid(column=1, row=9, padx=5, pady=5, columnspan=5)
        self.SS.grid(column=6, row=9)
        #botones
        self.referencia_button = ttk.Button(
            self, text="Obtener referencia", command=self.referencia)
        self.referencia_button.grid(column=0, row=8, padx=5,pady=5)
        self.borrar_button = ttk.Button(
            self, text="Borrar", command=self.borrado)
        self.borrar_button.grid(column=1, row=8, padx=5,pady=5)

    def borrado(self):
        self.name_entry.delete(0,'end')
        self.agno_entry.delete(0,'end')
        self.titulo_entry.delete(0,'end')
        self.tipo_entry.delete(0,'end')
        self.instituto_entry.delete(0,'end')
        self.repo_entry.delete(0,'end')
        self.link_entry.delete(0,'end')
    def referencia(self):
        try:
            autor=self.nombres()
            print(autor)
            agn=self.agno_entry.get()
            if agn=="":
                agnos=". (s.f). "
            else:
                agnos=". ({}). ".format(agn)
            print(agnos)
            titulos=self.titulo_entry.get()
            universidad=self.instituto_entry.get()
            tipo=self.tipo_entry.get()
            if tipo=="":
                raise ValueError("No se introduzco el tipo de tesis")
            else:
                tipos="[Tesis de {}, {}]. ".format(tipo.capitalize(), universidad)
            print(tipos)
            repositor=self.repo_entry.get()
            if repositor=="":
                repositorio=""
            else:
                repositorio="{}. ".format(repositor)
            print(repositorio)
            enlace=self.link_entry.get()  
            
            
            #self.var_str.set(autor+"("+agnos+"). "+titulos+". "+"ed"+ciudades+". "+pais+":"+editor)
            referencia=autor+agnos+titulos.capitalize()+". "+ tipos + repositorio.capitalize()+ enlace
            self.T.insert(tk.END, referencia)
            
            self.name_entry.delete(0,'end')
            self.agno_entry.delete(0,'end')
            self.titulo_entry.delete(0,'end')
            self.tipo_entry.delete(0,'end')
            self.instituto_entry.delete(0,'end')
            self.repo_entry.delete(0,'end')
            self.link_entry.delete(0,'end')
            
        except:
            messagebox.showerror(title="Referencias con normas APA", message='Ups! Parece que olvidaste rellenar algunos campos')  
class WebFrame(Esencial):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        self.link = ttk.Label(self, text="URL")
        self.link.grid(column=0, row=5)
        self.link_entry = ttk.Entry(self, width=30)
        self.link_entry.grid(column=1, row=5, sticky="ew")
        self.grid(sticky="nsew")
        self.T = tk.Text(self, height=4, width=100,  state="normal", font=('Times New Roman', 12))
        self.SS = tk.Scrollbar(self)
        self.SS.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.SS.set)
        self.T.grid(column=1, row=9, padx=5, pady=5, columnspan=5)
        self.SS.grid(column=6, row=9)
class AudioFrame(Esencial):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        self.link = ttk.Label(self, text="URL")
        self.link.grid(column=0, row=5)
        self.link_entry = ttk.Entry(self, width=30)
        self.link_entry.grid(column=1, row=5, sticky="ew")
        self.grid(sticky="nsew")
        self.T = tk.Text(self, height=4, width=100,  state="normal", font=('Times New Roman', 12))
        self.SS = tk.Scrollbar(self)
        self.SS.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.SS.set)
        self.T.grid(column=1, row=9, padx=5, pady=5, columnspan=5)
        self.SS.grid(column=6, row=9)
class Application(ttk.Frame):
    
    def __init__(self, mi_frame):
        
        main_window.title("Referencias bibliográficas según Normas APA")
        super().__init__(mi_frame)
        mi_frame.columnconfigure(0, weight=1)
        mi_frame.rowconfigure(0, weight=1)
        self.notebook = ttk.Notebook(self)
        
        self.libro_frame = LibroFrame(self.notebook)
        self.notebook.add(
            self.libro_frame, text="Libros", padding=20, sticky="nsew")
        
        self.revista_frame = RevistaFrame(self.notebook)
        self.notebook.add(
            self.revista_frame, text="Revistas", padding=20, sticky="nsew")
        self.ebook_frame = LegalFrame(self.notebook)
        self.notebook.add(
            self.ebook_frame, text="Textos legales", padding=20, sticky="nsew")
        self.tesis_frame = TesisFrame(self.notebook)
        self.notebook.add(
            self.tesis_frame, text="Tesis", padding=20, sticky="nsew")
        self.web_frame = WebFrame(self.notebook)
        self.notebook.add(
            self.web_frame, text="Páginas web", padding=20, sticky="nsew")
        self.audio_frame = AudioFrame(self.notebook)
        self.notebook.add(
            self.audio_frame, text="Medios audiovisuales", padding=10, sticky="nsew")
        self.notebook.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
        #self.geometry("170x200+30+30")
        #self.pack(expand=True, fill=tk.BOTH)
        self.grid(sticky="nsew")
main_window = tk.Tk()
mi_frame=tk.Frame(main_window, width=600, height=400)
mi_frame.config(bd=25)
mi_frame.config(bg="blue")
app = Application(mi_frame)
mi_frame.pack(expand=True, fill=tk.BOTH)
main_window.mainloop()