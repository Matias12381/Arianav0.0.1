from tkinter import * 
import tkinter as tk
import sqlite3

root = tk.Tk()
root.title('Arianav0.0.1')
root.geometry("1000x1000")

#database 
conn = sqlite3.connect('teste.db')

#creat cursor
c = conn.cursor()

#Tabela database 
#c.execute(" CREATE TABLE addresses (nome text, agrupamento text, idade integer, ano integer )")





#submit
def submit():
    conn = sqlite3.connect('teste.db')
    c  = conn.cursor()
    #insert in the table 
    c.execute("INSERT INTO addresses VALUES (:nome, :agrupamento, :idade, :ano)",
            {
                'nome': nome.get(),
                'agrupamento': agrupamento.get(),
                'idade': idade.get(),
                'ano': ano.get(),
            })
    conn.commit()
    conn.close()
    nome.delete(0,END)
    agrupamento.delete(0,END)
    idade.delete(0,END)
    ano.delete(0,END)
    
def pedir():
    conn = sqlite3.connect('teste.db')
    c  = conn.cursor()
    #query the database
    c.execute("SELECT *, oid FROM addresses")
    lista = c.fetchall()
    print(lista)
    lista1 = ''
    for lista in lista: 
        lista1 += str(lista) + "\n"
    pedir_lista = Label(root, text=lista1)
    pedir_lista.grid(row=8, column=0, columnspan=2)
    conn.commit()
    conn.close()


#text box
nome = Entry(root, width=140)
nome.grid(row=0, column=1, padx=20) 
agrupamento = Entry(root, width=140)
agrupamento.grid(row=1, column=1) 
idade  = Entry(root, width=140)
idade.grid(row=2, column=1 ) 
ano = Entry(root, width=140)
ano.grid(row=3, column=1) 

#delete_box.grid(row=9, column=1)
#Crewat text box 
nome_label = Label(root, text='Nome')
nome_label.grid(row=0, column=0)
agrupamento_label = Label(root, text='Agrupamento')
agrupamento_label.grid(row=1, column=0)
idade_label = Label(root, text='Idade')
idade_label.grid(row=2, column=0)
ano_label = Label(root, text='Ano')
ano_label.grid(row=3, column=0)
#button
submit_btn=Button(root, text="Guardar", command=submit)
submit_btn.grid(row=5, column=1, pady=10, padx=10, ipadx=100)

#Database button 
db_btn=Button(root, text="Lista de Crianças", command=pedir)
db_btn.grid(row=7, column=1, pady=10, padx=10, ipadx=137)

#create a delete button
#del_btn=Button(root, text="deletar ", command=apagar)
#del_btn.grid(row=9, column=2, columnspan=2, pady=10, padx=10, ipadx=135)
#commit changes
conn.commit()

#close connection 
conn.close()






root.mainloop()


