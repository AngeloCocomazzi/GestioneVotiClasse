'''Creato da Cocomazzi Angelo'''
import time#caricata per problemi dovuti alla scrittura del file
from tkinter import *
from tkinter import messagebox #per il funzionamento dei message box fuori dall'idle
import pickle
#import os
import subprocess#per la gestione dei sottoprocessi


aperto=False
f=0;c=0;s=0;a=0;media=0
elenco = []
lista = []
materia = ["italiano","storia","tpsit","sistemi","informatica","gpo","inglese","matematica","francese","tedesco","greco","latino","filosofia","educazione fisica","biologia","elettronica","chimica","fisica","scienze","diritto"]
voti=[]
alunno=[]

class Alunno :
    nome = ""
    cognome = ""
    esito = ""

    def __init__ (self,n,c,e):
        self.nome = n
        self.cognome = c
        self.esito = e
        

class App:

    def __init__(self,finestra):
        
        finestra.protocol("WM_DELETE_WINDOW", self.domanda)#cattura evento X rossa finestra
        
        self.quadro1 = Frame(finestra)
        self.quadro2 = Frame(finestra)
        
        finestra["background"]="#1E90FF"
        finestra.resizable(False, False)    # rende la finestra non ridimensionabile asse x e y
        finestra.geometry("220x300+400+300")#grandezza finsestra + coordinate per la posizione su schermo
        
        self.start()


    def start (self):
        #finestra.unbind("<Return>")#eliminare la funzione dell'invio
        self.quadro1.destroy()
        self.quadro2.destroy()
        self.quadro1 = Frame(finestra)
        
        finestra.title("Pagina principale")
        
        self.quadro1.configure(bg="#00BFFF")
        self.quadro1.pack()

        home = Label(self.quadro1,text="Home Page", relief=GROOVE,width=30,
                     bg="#00008B",fg="white",font=("Helvetica",20))
        
        home.pack()
        
        
        puls1 = Button(self.quadro1,text="Inserimento voto",borderwidth=1,
                            background="grey",foreground="white",command=self.caricaFile)#sceltaMaterie)  #self.inserimentoVoto                 
        puls1.pack(ipadx=10,pady=25,padx=30,ipady=2)

        puls2 = Button(self.quadro1,text="Risultato finale",borderwidth=1,
                            background="grey",foreground="white",command=self.risultFinale)                    
        puls2.pack(ipadx=16,ipady=2)

        puls3 = Button(self.quadro1,text="Visualizza file",borderwidth=1,
                            background="grey",foreground="white",command=self.stampaFile)                    
        puls3.pack(ipadx=20,pady=30,ipady=2)

        puls4 = Button(self.quadro1,text="Cancella file",borderwidth=1,
                            background="grey",foreground="white",command=self.delFile)                    
        puls4.pack(ipadx=20,ipady=2)
        
        
        
        pulsexit = Button(self.quadro1,text="Uscita",borderwidth=1,
                            background="#468284",foreground="white",command=self.domanda)                                  
        pulsexit.pack(side="right")

        subprocess.Popen(['cmd','/C','attrib +h -s +r prova.txt'],shell=True)

################################################################################

    def domanda(self):
        if messagebox.askyesno("Chiusura finestra", "Chiudere veramente?"):
            finestra.destroy()

    def caricaFile(self):
        global lista
        global c
        c=0
        subprocess.Popen(['cmd','/C','attrib -h -s -r prova.txt'],shell=True)

        try:#vede se il file esiste o meno
            file = open("prova.txt","rb")

        except:#se il file non esiste chiama la funzione
            print("File non esiste!")
            self.sceltaMaterie()
            return 0
            
        d=0

        while 1:#altrimenti se il file esiste vede se è pieno
            try :
                pers2 = pickle.load(file)
            except:                        
                break


            nome = pers2.nome
            cogn = pers2.cognome

            lista.append([nome,cogn])

            d = d + 1

        file.close()
        
        if d>0:#se il file è pieno chiede se si vuole caricarlo
            if messagebox.askyesno("Carica file", "Il file contiene altri alunni! Caricarli?\nScegliendo no gli alunni verranno cancellati!!"):
                pass
                #print("OK")
                

            else:#se sceglie no cancella file e poi scelta alunni
                lista=[]
                self.delFile()

        self.sceltaMaterie()

        

    def sceltaMaterie(self):
        global elenco
        global voti
        elenco = []
        voti=[]
        #print("clear",elenco)
        
        finestra.title("Scelta materie")
        self.quadro1.destroy()
        self.quadro2.destroy()

        self.quadro1 = Frame(finestra)
        self.quadro1.pack()
        self.quadro1.configure(bg="#00BFFF")
        
        self.quadro2 = Frame(finestra)
        self.quadro2.pack()

        titolo = Label(self.quadro1,text="Scelta Materie", relief=GROOVE,width=30,
                     bg="#00008B",fg="white",font=("Helvetica",18))
        titolo.pack()

        L1 = Label(self.quadro1,text="Materie",bg ="grey",fg="white")
        L1.pack(pady=2)

        scrollbar = Scrollbar(self.quadro1)
        #scrollbar.pack(side = RIGHT, fill=X)

        self.mylist = Listbox(self.quadro1,yscrollcommand = scrollbar.set,selectmode=MULTIPLE)#secondo parametro fa scendere il cursore
        c=0
        for line in range(len(materia)):
           self.mylist.insert(END,materia[c])
           c=c+1

        
        self.mylist.pack(fill = BOTH)
        scrollbar.config(command = self.mylist.yview)
        
        self.mylist.pack()


        pulsconf = Button(self.quadro1,text="Conferma",borderwidth=1,
                       background="#468284",foreground="white",command=self.prova)                                  
        pulsconf.pack(pady=10)

        pulsexit = Button(self.quadro2,text="Indietro",borderwidth=1,
                       background="red",foreground="white",command=self.start)                                  
        pulsexit.pack()





    def prova(self):#funzione creata per il controllo delle materie selezionate

        suppo = 0
        
        suppo = self.mylist.curselection()#ritorna indici indicati

        #print("DDD ",suppo)


        for c in suppo:
            voti.append([materia[c]])


        print("gg ",voti)

        if not voti:
           print("Errore inserimento materie!")
           messagebox.showinfo("Errore !", "Inserire almeno una materia !")
           return -1

        finestra.title("Numero voti")

        self.numeroVoti(suppo)#richiama funzione sottostante
        

    def numeroVoti(self,suppo):
        
        global c
        #print("value ",c)
        
        while c <len(suppo):
            self.quadro1.destroy()
            self.quadro2.destroy()

            self.quadro1 = Frame(finestra)
            self.quadro1.pack()
            self.quadro1.configure(bg="#00BFFF")
            
            self.quadro2 = Frame(finestra)
            self.quadro2.pack()

            titolo = Label(self.quadro1,text="Numero voti", relief=GROOVE,width=30,
                         bg="#00008B",fg="white",font=("Helvetica",18))
            titolo.pack()



            #val = IntVar()
            
            
            pos = suppo[c]
            print("POS ",pos," ",c)
            self.w=c

            L1 = Label(self.quadro1,text=("%s"%materia[pos]),bg ="grey",fg="white")
            L1.pack(pady=5)

            scrollbar = Scrollbar(self.quadro1)
            #scrollbar.pack(side = RIGHT, fill=X)#commentato per nascondere la scrollbar

            self.mylist = Listbox(self.quadro1,yscrollcommand = scrollbar.set,selectmode=SINGLE)
            
            for line in range(1,11):#inserisce le materie nella lista
               self.mylist.insert(END,"Voto : %s"%(line))

            
            self.mylist.pack(fill = BOTH)
            scrollbar.config(command = self.mylist.yview)
            
            self.mylist.pack()
        
        

            pulsconf = Button(self.quadro1,text="Conferma",borderwidth=1,
                           background="#468284",foreground="white",command=lambda c=c:self.salvaVoto(pos,suppo))                                  
            pulsconf.pack(pady=7)

            pulsexit = Button(self.quadro2,text="Indietro",borderwidth=1,
                           background="red",foreground="white",command=self.sceltaMaterie)                                  
            pulsexit.pack()


            return 0

        self.inserisciAlunni()

    def salvaVoto(self,num,suppo):#funzione creata per il salvataggio delle materie con il rispettivo numero di voti per ogni materia

        global c

        n_voti = self.mylist.curselection()#restituisce una tupla con le posizioni selezionate
        n_voti= int(n_voti[0]) 
        #print("valore ",num)
        global elenco
        elenco.append([materia[num],n_voti+1])
        #print("elenc ",elenco)
        c=c+1
        #print("ww ",c)
        self.numeroVoti(suppo)#richiama funzione principale



    def inserisciAlunni(self):
        finestra.title("Inserisci Alunni")
        #print("OK1")
        self.quadro1.destroy()
        self.quadro2.destroy()

        self.quadro1 = Frame(finestra)
        self.quadro1.pack()
        self.quadro1.configure(bg="#00BFFF")
        
        self.quadro2 = Frame(finestra)
        self.quadro2.pack()

        titolo = Label(self.quadro1,text="Inserimento Alunni", relief=GROOVE,width=30,
                     bg="#00008B",fg="white",font=("Helvetica",18))
        titolo.pack()

        L1 = Label(self.quadro1,text="Nome",bg ="grey",fg="white")
        L1.pack(pady=5)
        L1.place(bordermode=INSIDE, x=3, y=43)
        
        self.E1 = Entry(self.quadro1,bd = 2)
        self.E1.pack()
        self.E1.place(bordermode=INSIDE, x=73, y=43)

        L2 = Label(self.quadro1,text="Cognome",bg ="grey",fg="white")
        L2.pack(pady=5)
        L2.place(bordermode=INSIDE, x=3, y=70)

        self.E2 = Entry(self.quadro1,bd = 2)
        self.E2.pack()
        self.E2.place(bordermode=INSIDE, x=73, y=70)
        
        
        pulsann = Button(self.quadro1,text="Annulla",borderwidth=1,
                         background="#468284",foreground="white",command=self.canc)                                  
        pulsann.pack()
        pulsann.place(bordermode=INSIDE, x=45, y=124)

        pulsconf = Button(self.quadro1,text="Conferma",borderwidth=1,
                          background="#468284",foreground="white",command=self.convalidaAlunno)                                  
        pulsconf.pack()
        pulsconf.place(bordermode=INSIDE, x=115, y=124)

        separator = Frame(self.quadro1,height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X,pady=85,side="bottom")
        

        pulsexit = Button(self.quadro2,text="Indietro",borderwidth=1,
                           background="red",foreground="white",command=self.domandaRitorno)                                  
        pulsexit.pack()


    def domandaRitorno(self):
        if messagebox.askyesno("Torna Indietro", "Tornano indietro non potrai piu'inserire alunni!\nContinuare?"):
            self.start()
           
        
    def convalidaAlunno (self,event=None):#secondo parametro aggiunto solo per evento da tastiera
        
        global s
        global a

        s=0
        a=0
        
        nome = self.E1.get()

        cognome = self.E2.get()

        nomsup = nome.strip()#elimina gli spazi dalla stringa

        cognsup = cognome.strip()#elimina gli spazi dalla stringa

        if not(nomsup and cognsup):
           print("Errore inserimento campi!")
           messagebox.showinfo("Errore !", "Compilare tutti i campi!")
           return -1

        nome = nomsup
        cognome = cognsup
        
        x=0

        trovato=False
        
        while x<len(lista):#vede se i nomi sono stati gia utilizzati
            
            if nome == lista [x][0] and cognome == lista [x][1] :
                trovato=True
                print("\nNome e Cognome gia' utilizzati ! ")

            if trovato == True :
                messagebox.showinfo("Errore nome/cognome", "Nome e cognome gia' utilizzati!")
                return -1


            x = x + 1
        
            
        self.votiperMateria()
        

        lista.append([nome,cognome])#salvataggio nomi e cognomi

        
    def votiperMateria(self):
        finestra.title("Inserisci Voto")
        global s
        global a
                
        #print("a ",a," s ",s)
                
        self.quadro1.destroy()
        self.quadro2.destroy()

        self.quadro1 = Frame(finestra)
        self.quadro1.pack()
        self.quadro1.configure(bg="#00BFFF")
        
        self.quadro2 = Frame(finestra)
        self.quadro2.pack()

        titolo = Label(self.quadro1,text="Inserire voto", relief=GROOVE,width=30,
                     bg="#00008B",fg="white",font=("Helvetica",18))
        titolo.pack()



        L1 = Label(self.quadro1,text=("%s"%elenco[s][0]),bg ="grey",fg="white")
        L1.pack(pady=5)

        self.E1 = Entry(self.quadro1,bd = 2)
        self.E1.pack()
    
    

        pulsconf = Button(self.quadro1,text="Conferma",borderwidth=1,
                       background="#468284",foreground="white",command=lambda a=a:self.salvaMedia())                                  
        pulsconf.pack(pady=7)


        #return 0

    def salvaMedia(self):
        global a
        global s
        global elenco
        global alunno
        global media


        n_voti = elenco[s][1]

        asw=0
        voto1=0
        while a < n_voti:

            voto1 = self.E1.get()

            if not voto1:
                messagebox.showinfo("Errore voto", "Voto Errato!!")
                print("Voto errato!")
                return -1

            #print("asd ",voto1)

            self.canc()#cancella le caselle di testo

            aw=0

            while aw < len(voto1):
                
                if (voto1[aw] >= '0' and voto1[aw] <= '9') or voto1[aw]==".":
                    numero = 0
                    aw = aw + 1

                else:
                    numero=1
                    print("\nErrore inserimento !")
                    messagebox.showinfo("Inserimento Errato!", "Errore inserimento numero !")
                    return 0
                    #break
                
            if numero == 0 :

                asw = float(voto1)

                if numero == 0 and asw <= 10:
                    pass
                    print("Ok")
                else:
                    messagebox.showinfo("Inserimento Errato!", "Errore inserimento numero !")
                    return 0
            
            media = media + asw
            
            a = a + 1

            if a >= n_voti:
                self.votiperMateria()
                break

            return 0

        print("media ", media)
        media = media / elenco[s][1]
        media = "%.1f"%media
        media = float(media)
        #print(type (media))
        
        
        alunno.append([elenco[s][0],media])
        a=0
        s=s+1
        media=0
        if s < len(elenco):
            self.votiperMateria()

        else:
            print("alunno ",alunno)

            self.scriviSuFile()#scrittura su file dell'alunno
            
            self.inserisciAlunni()#richiama funzione principale


    def scriviSuFile(self):
        global alunno
        
        alun1 = Alunno(lista[-1][0],lista[-1][1],alunno)#salvataggio nell'oggetto
        
        alunno=[]
        #print("oggetto ",alun1.nome)

        subprocess.Popen(['cmd','/C','attrib -h -s -r prova.txt'],shell=True)

        time.sleep(0.2)#aggiunto per problemi dovuti alla scrittura nel file
                        #apriva il file prima di togliere i parametri di protezione
        
        file = open("prova.txt","ab")
        pickle.dump(alun1,file)
        file.close()

        subprocess.Popen(['cmd','/C','attrib +h -s +r prova.txt'],shell=True)
        
        #print ("aa",lista)

        print("OK scrittura")

        messagebox.showinfo("Inserimento Corretto!", "Alunno inserito correttamente !")
        
        return 0

    def canc (self):
        try:
            self.E1.delete(0, END)
            self.E2.delete(0, END)
            
        except:
            pass


    def risultFinale(self):

        subprocess.Popen(['cmd','/C','attrib -h -s -r prova.txt'],shell=True)

        try:#vede se il file è stato creato
            file = open("prova.txt","rb")
            
        except:#se non esiste non fa andare avanti
            print("File non esiste!")
            messagebox.showinfo("Nessun file!", "Nessun alunno inserito !")
            return 0
        
        file.close()#altrimenti chiude file aperto prima
        
        subprocess.Popen(['cmd','/C','attrib +h -s +r prova.txt'],shell=True)
        
        finestra.title("Risultato finale")
        self.quadro2.destroy()
        self.quadro1.destroy()
        
        self.quadro1 = Frame(finestra)
        self.quadro1.pack()
        self.quadro2 = Frame(finestra)
        self.quadro2.pack()
        self.quadro1.configure(bg="#00BFFF")
        self.quadro2.configure(bg="#1E90FF")

        testo = Label(self.quadro1,text="Menu Risultati", relief=GROOVE,width=50,
                     bg="#00008B",fg="white",font=("Helvetica",18))

        testo.pack()
        

        pulsprom = Button(self.quadro1,text="Alunni Promossi",borderwidth=1,
                       background="grey",foreground="white",command=self.risultPromossi)                                  
        pulsprom.pack(side="top",pady=10,ipadx=10,ipady=4)


        pulsrim = Button(self.quadro1,text="Alunni Rimandati",borderwidth=1,
                       background="grey",foreground="white",command=self.risultRimandati)                                  
        pulsrim.pack(side="top",pady=10,ipady=4,ipadx=7)


        pulsboc = Button(self.quadro1,text="Alunni Bocciati",borderwidth=1,
                       background="grey",foreground="white",command=self.risultBocciati)                                  
        pulsboc.pack(side="top",ipady=4,ipadx=12,pady=10)


        pulsexit = Button(self.quadro2,text="Indietro",borderwidth=1,
                       background="red",foreground="white",command=self.start)                                  
        pulsexit.pack(pady=10,side="bottom")

        

    def risultPromossi (self):
        finestra.title("Alunni promossi")
        self.quadro2.destroy()
        self.quadro1.destroy()
        
        self.quadro1 = Frame(finestra)
        self.quadro1.pack()
        self.quadro1.configure(bg="#00008B")
        
        self.quadro2 = Frame(finestra)
        self.quadro2.pack(fill = X)

        yscrollbar = Scrollbar(self.quadro2,orient=VERTICAL)
        xscrollbar = Scrollbar(self.quadro2,orient=HORIZONTAL)
        
        yscrollbar.pack(side = RIGHT, fill=Y)
        xscrollbar.pack(side = BOTTOM, fill=X)

        mylist = Listbox(self.quadro2,yscrollcommand = yscrollbar.set,xscrollcommand = xscrollbar.set)#secondo parametro fa scendere il cursore

        subprocess.Popen(['cmd','/C','attrib -h -s -r prova.txt'],shell=True)

        file = open("prova.txt","rb")

        promosso = []#lista contenente solo alunni promossi

        while 1:
            try :
                pers2 = pickle.load(file)
            except:
                break

            #print("prova : ",pers2.esito)
            #print("nome : ",pers2.nome)
            #print("cognome : ",pers2.cognome)

            nome = pers2.nome
            cogn = pers2.cognome
            esito_fin = pers2.esito

            m = 0
            deb = 0
            debiti  = []
            
            while m < len(esito_fin):

                if esito_fin[m][1] <6.0:
                    deb = deb + 1
                    debiti.append(esito_fin[m])
                    
                m = m + 1

            if deb == 0:#vede se i debiti sono == a 0
                promosso.append([nome,cogn])


        file.close()
        
        for line in promosso:#carica lista
           mylist.insert(END, "Alunno : " + str(line))

        if not promosso:#se lista vuota stampa frase di default
            mylist.insert(END, "             Nessun alunno promosso!")
            

        L1 = Label(self.quadro1,text="Promossi" ,relief=GROOVE,width=30,
                     bg="#00008B",fg="white",font=("Helvetica",16),bd=0)
        L1.pack(pady=5)
        
        mylist.pack(fill = BOTH)
        yscrollbar.config(command = mylist.yview)#se non impostato la lista non scende di posizione
        xscrollbar.config(command = mylist.xview)#se non impostato la lista non scende di posizione

        
        pulsexit = Button(self.quadro1,text="Indietro",borderwidth=1,
                       background="red",foreground="white",command=self.risultFinale)                                  
        pulsexit.pack(side="bottom")

        #print("om")
           

    def risultRimandati (self):

        self.quadro2.destroy()
        self.quadro1.destroy()
        
        self.quadro1 = Frame(finestra)
        self.quadro1.pack()
        self.quadro1.configure(bg="#00008B")
        
        self.quadro2 = Frame(finestra)
        self.quadro2.pack(fill = X)

        yscrollbar = Scrollbar(self.quadro2,orient=VERTICAL)
        xscrollbar = Scrollbar(self.quadro2,orient=HORIZONTAL)
        
        yscrollbar.pack(side = RIGHT, fill=Y)
        xscrollbar.pack(side = BOTTOM, fill=X)

        mylist = Listbox(self.quadro2,yscrollcommand = yscrollbar.set,xscrollcommand = xscrollbar.set)#secondo parametro fa scendere il cursore

        subprocess.Popen(['cmd','/C','attrib -h -s -r prova.txt'],shell=True)

        file = open("prova.txt","rb")

        rimandati = []#lista contenente solo alunni rimandati

        while 1:
            try :
                pers2 = pickle.load(file)
            except:
                break

            #print("prova : ",pers2.esito)
            #print("nome : ",pers2.nome)
            #print("cognome : ",pers2.cognome)

            nome = pers2.nome
            cogn = pers2.cognome
            esito_fin = pers2.esito

            m = 0
            deb = 0
            debiti  = []
            
            while m < len(esito_fin):

                if esito_fin[m][1] <6.0:
                    deb = deb + 1
                    debiti.append(esito_fin[m])
                    
                m = m + 1


            if deb >0 and deb <= 2:#vede se i debiti sono compresi tra l'intervallo [1;2]
                rimandati.append([nome,cogn,debiti])


        file.close()
        
        for line in rimandati:#carica lista
           mylist.insert(END, "Alunno : " + str(line))

        if not rimandati:#se lista vuota stampa frase di default
            mylist.insert(END, "             Nessun alunno rimandato!")
           

        L1 = Label(self.quadro1,text="Rimandati" ,relief=GROOVE,width=30,
                     bg="#00008B",fg="white",font=("Helvetica",16),bd=0)
        L1.pack(pady=5)
        
        mylist.pack(fill = BOTH)
        
        yscrollbar.config(command = mylist.yview)#se non impostato la lista non scende di posizione
        xscrollbar.config(command = mylist.xview)#se non impostato la lista non scende di posizione

        pulsexit = Button(self.quadro1,text="Indietro",borderwidth=1,
                       background="red",foreground="white",command=self.risultFinale)                                  
        pulsexit.pack(side="bottom")


    def risultBocciati (self):
        
        self.quadro2.destroy()
        self.quadro1.destroy()
        
        self.quadro1 = Frame(finestra)
        self.quadro1.pack()
        self.quadro1.configure(bg="#00008B")
        
        self.quadro2 = Frame(finestra)
        self.quadro2.pack(fill = X)

        yscrollbar = Scrollbar(self.quadro2,orient=VERTICAL)
        xscrollbar = Scrollbar(self.quadro2,orient=HORIZONTAL)
        
        yscrollbar.pack(side = RIGHT, fill=Y)
        xscrollbar.pack(side = BOTTOM, fill=X)

        mylist = Listbox(self.quadro2,yscrollcommand = yscrollbar.set,xscrollcommand = xscrollbar.set)#secondo parametro fa scendere il cursore


        subprocess.Popen(['cmd','/C','attrib -h -s -r prova.txt'],shell=True)

        file = open("prova.txt","rb")
        #d=0
        bocciato = []

        while 1:#cicla finche' il file non e' vuoto
            try :
                pers2 = pickle.load(file)
            except:
                break

            #print("prova : ",pers2.esito)
            #print("nome : ",pers2.nome)
            #print("cognome : ",pers2.cognome)

            nome = pers2.nome
            cogn = pers2.cognome
            esito_fin = pers2.esito

            m = 0
            deb = 0
            debiti  = []
            
            while m < len(esito_fin):

                if esito_fin[m][1] <6.0:
                    deb = deb + 1
                    debiti.append(esito_fin[m])
                    
                m = m + 1

            if deb > 2 :#vede se i debiti sono maggiori di 2
                bocciato.append([nome,cogn,deb])


        file.close()
        
        for line in bocciato:#carica lista
           mylist.insert(END, "Alunno : " + str(line))

        if not bocciato:#se lista vuota stampa frase di default
            mylist.insert(END, "              Nessun alunno bocciato!")

        L1 = Label(self.quadro1,text="Bocciati" ,relief=GROOVE,width=30,
                     bg="#00008B",fg="white",font=("Helvetica",16),bd=0)
        L1.pack(pady=5)
        
        mylist.pack(fill = BOTH)
        
        yscrollbar.config(command = mylist.yview)#se non impostato la lista non scende di posizione
        xscrollbar.config(command = mylist.xview)#se non impostato la lista non scende di posizione
                         
        pulsexit = Button(self.quadro1,text="Indietro",borderwidth=1,
                       background="red",foreground="white",command=self.risultFinale)                                  
        pulsexit.pack(side="bottom")



    def stampaFile (self):
        subprocess.Popen(['cmd', '/C','attrib +h +r prova.txt'],shell=True)

        subprocess.Popen(['cmd', '/C','start','prova.txt'],shell=True)#apre il file


    def delFile(self):
        #prima modalita di nascondere una finestra
        CREATE_NO_WINDOW = 0x08000000
        subprocess.call('attrib -h -s -r ./prova.txt', creationflags=CREATE_NO_WINDOW)

        #seconda modalita di nascondere una finestra///assegnazione non obbligatoria
        b = subprocess.Popen(['cmd', '/C','del','prova.txt'],shell=True)
        #print("\n",b)
        print("File cancellato!")
        
        

finestra = Tk()
App = App(finestra)
finestra.mainloop()
