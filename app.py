# Gruppo: Biagioni e Gallo

import tkinter as tk 
import pymssql as sql

#conn = sql.connect(server='192.168.40.16\SQLEXPRESS', user='biagioni.jacopo', password='xxx123##', database='biagioni.jacopo') 

window = tk.Tk()
window.geometry("600x600")
window.title("Hello TkInter!")
window.configure(background="white")

username_entry = tk.Entry(window)
password_entry = tk.Entry(window)
username2_entry = tk.Entry(window)
password2_entry = tk.Entry(window)
ricerca_entry = tk.Entry(window)


def InsertUsers():
    window2 = tk.Tk()
    window2.title('Elimina dati')
    window2.configure(width=1000, height=800)
    
    label1 = tk.Label(window2, text="Username:", font=("Helvetica", 16))
    label1.place(x=80, y=130)
    entry1 = tk.Entry(window2)
    entry1.place(x=240, y=130)

    label2 = tk.Label(window2, text="Password:", font=("Helvetica", 16))
    label2.place(x=80, y=320)
    entry2 = tk.Entry(window2, show='*')
    entry2.place(x=240, y=320)

    tk.Button(window2, text="Submit").place(x=180, y=380)
    cursor = conn.cursor()
    cursor.execute = ("INSERT INTO Utenti VALUES (%(username_sql)s, %(password_sql)s)")

    conn.commit()
    conn.close()

button = tk.Button(window, text='Inserisci', command=InsertUsers)
button.pack()   


def DeleteUsers():
    window3 = tk.Tk()
    window3.title('Elimina dati')
    window3.configure(width=1000, height=800)
    
    label1 = tk.Label(window3, text="Username:", font=("Helvetica", 16))
    label1.place(x=80, y=130)
    entry1 = tk.Entry(window3)
    entry1.place(x=240, y=130)

    label2 = tk.Label(window3, text="Password:", font=("Helvetica", 16))
    label2.place(x=80, y=320)
    entry2 = tk.Entry(window3, show='*')
    entry2.place(x=240, y=320)

    tk.Button(window3, text="Submit").place(x=180, y=380)


    cursor = conn.cursor()
    cursor.execute('DELETE FROM Utenti WHERE Username=%(username_sql)s and Password=%(password)s')
    conn.commit()

    conn.close()


button2 = tk.Button(window, text='Elimina', command=DeleteUsers)
button2.pack()


def ModificaUsers():
    window4 = tk.Tk()
    window4.title('Elimina dati')
    window4.configure(width=1000, height=800)
    
    label1 = tk.Label(window4, text="Username:", font=("Helvetica", 16))
    label1.place(x=80, y=130)
    entry1 = tk.Entry(window4)
    entry1.place(x=240, y=130)

    tk.Button(window4, text="Submit").place(x=180, y=300)

    cursor = conn.cursor()
    cursor.execute('UPDATE Utenti SET Username=%(username2_sql)s WHERE Username=%(username_sql)s')
    conn.commit()
    conn.close()

button3 = tk.Button(window, text='Modifica Utente', command=ModificaUsers)
button3.pack()

def ModificaPassword():
    window5 = tk.Tk()
    window5.title('Elimina dati')
    window5.configure(width=1000, height=800)

    label2 = tk.Label(window5, text="Password:", font=("Helvetica", 16))
    label2.place(x=80, y=320)
    entry2 = tk.Entry(window5, show='*')
    entry2.place(x=240, y=320)

    tk.Button(window5, text="Submit").place(x=180, y=380)

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





if __name__ == "__main__":
    window.mainloop()