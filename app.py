#realizzare un applicazione con python che permetta tramite un interfaccia grafica di effettuare operazioni sulla tabella degli utenti del proprio progetto
#operazioni ricerca inserimento creazione modifica
#interfaccia grafica usata nel nostro progetto è TKINTER
#ambiente di sviluppo è visual studio code

import tkinter as tk 
import pymssql as sql

conn = sql.connect(server='192.168.40.16\SQLEXPRESS', user='biagioni.jacopo', password='xxx123##', database='biagioni.jacopo') 

window = tk.Tk()
window.geometry("600x600")
window.title("Hello TkInter!")
window.configure(background="white")

username_sql = tk.Entry(window)
password_sql = tk.Entry(window)
username2_sql = tk.Entry(window)
password2_sql = tk.Entry(window)
ricerca_sql = tk.Entry(window)

def second_function():
    text = "Nuovo Messaggio! Nuova Funzione!"
    text_output = tk.Label(window, text=text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, padx=50, sticky="W")

def ciao_utente():
    text = box.get()
    text_output = tk.Label(window, text = text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=3, sticky="W")

def InsertUsers():
    conn.cursor()
    cursor.execute = 'INSERT INTO Utenti VALUES %(username_sql)s, %(password_sql)s'

    conn.commit()
    conn.close()

    button = tk.Button(window, text='Inserisci', command=InsertUsers)
    button.pack()

def DeleteUsers():
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Utenti WHERE Username=%(username_sql)s and Password=%(password)s')
    conn.commit()
    conn.close()

    button2 = tk.Button(window, text='Elimina', command=DeleteUsers)
    button2.pack()

def ModificaUsers():
    cursor = conn.cursor()
    cursor.execute('UPDATE Utenti SET Username=%(username2_sql)s WHERE Username=%(username_sql)s')
    conn.commit()
    conn.close()

    button3 = tk.Button(window, text='Modifica Utente', command=ModificaUsers)
    button3.pack()

def ModificaPassword():
    cursor = conn.cursor()
    cursor.execute('UPDATE Utenti SET Password=%(password2_sql)s WHERE Password=%(password_sql)s')
    conn.commit()
    conn.close()

    button4 = tk.Button(window, text='Modifica Password', command=ModificaPassword)
    button4.pack()

def Ricerca():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Utenti WHERE Username or Password LIKE %'%(ricerca_sql)s'%")
    conn.commit()
    conn.close()

    button5 = tk.Button(window, text='Ricerca', command=Ricerca)
    button5.pack()

userInput = tk.Label(window, text='Username').grid(row=0)   
box = tk.Entry(window)
box.grid(row=0, column=1, sticky='W')

userButton = tk.Button(text='Username', command=ciao_utente)
userButton.grid(row=0, column=2, )

second_button = tk.Button(text="Seconda Funzione", command=second_function)
second_button.grid(row=1, column=0, pady=20, sticky="W")


if __name__ == "__main__":
    window.mainloop()