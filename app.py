#realizzare un applicazione con python che permetta tramite un interfaccia grafica di effettuare operazioni sulla tabella degli utenti del proprio progetto
#operazioni ricerca inserimento creazione modifica
#interfaccia grafica usata nel nostro progetto è TKINTER
#ambiente di sviluppo è visual studio code

import tkinter as tk 
import pymssql

conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='biagioni.jacopo', password='xxx123##', database='biagioni.jacopo') 

window = tk.Tk()
window.geometry("600x600")
window.title("Hello TkInter!")
window.configure(background="white")

username_sql = tk.Entry(window)
password_sql = tk.Entry(window)

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
    cursor.execute = 'INSERT INTO Utenti VALUES (%s, %s)', (username_sql, password_sql)

    conn.commit()
    conn.close()

    button = tk.Button(window, text='Inserisci', command=InsertUsers)
    button.pack()

def DeleteUsers():
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Utenti WHERE Username=%(username_sql)s and Password=%(password)s')
    conn.commit()
    conn.close()

userInput = tk.Label(window, text='Username').grid(row=0)   
box = tk.Entry(window)
box.grid(row=0, column=1, sticky='W')

userButton = tk.Button(text='Username', command=ciao_utente)
userButton.grid(row=0, column=2, )

second_button = tk.Button(text="Seconda Funzione", command=second_function)
second_button.grid(row=1, column=0, pady=20, sticky="W")


if __name__ == "__main__":
    window.mainloop()