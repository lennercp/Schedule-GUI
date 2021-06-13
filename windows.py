from tkinter import *
from tkinter import font
from contacts import contacts

class windows():
    def __init__(self):
        self.conts = contacts()
        self.menu()

    def menu(self):
        root = Tk()
        root.geometry('300x180')
        root.title('menu')

        myFont = font.Font(family = 'Helvetica', size = 16)

        def newcontact():
            root.destroy()
            self.newContact()

        def listcontacts():
            root.destroy()
            self.listContacts()
            
        def searchContact():
            root.destroy()
            self.searchContact()
        
        new_contact = Button(root, text='Novo contato', fg = 'green', command = newcontact, font = myFont, width = 20)
        new_contact.pack()

        list_contacts = Button(root, text='Listar contatos', fg = 'green', command = listcontacts, font = myFont, width = 20)
        list_contacts.pack(pady=15)

        search_contact = Button(root, text='Buscar contato', fg = 'green', command = searchContact,font = myFont, width = 20)
        search_contact.pack()

        root.mainloop()

#==============================================================================================================================
    def newContact(self):
        root = Tk()
        root.geometry('250x170')
        root.title('Novo contato')

        myFont = font.Font(family = 'Helvetica', size = 16)

        frame1 = Frame(root)
        frame1.pack()
        frame2 = Frame(root)
        frame2.pack(pady=10)
        frame3 = Frame(root)
        frame3.pack()
        frame4 = Frame(root)
        frame4.pack(padx = 0,pady=10)
        

        def back():
            root.destroy()
            self.menu()

        def validate():
            validate = self.conts.add_cont(new_name.get().title(), new_num.get().title())
            if validate:
                alert.pack_forget()
                a,b = self.conts.list_conts()
                new_name.delete(0,"end")
                new_num.delete(0,"end")
                new_name.insert(0,"")
                new_num.insert(0,"")
                print(a,b)

            elif len(new_num.get()) != 11:
                alert["text"] = "Padrão de números errado!"
                alert.pack()
            else:
                alert["text"] = "Contato já existente!"
                alert.pack()

        label1 = Label(frame1, text='Novo contato', font = myFont, fg = 'green')
        label1.pack()

        alert = Label(frame1, text='Contato já existente', fg='red')

        label2 = Label(frame2, text='Nome:')
        label2.pack(side = LEFT, padx = 25)

        new_name = Entry(frame2)
        new_name.pack(side = RIGHT)

        label3 = Label(frame3, text='Número(DDD):')
        label3.pack(side = LEFT, padx = 4)

        new_num = Entry(frame3)
        new_num.pack(side = RIGHT)

        btn_back = Button(frame4, text = 'Voltar', fg = 'red', command = back)
        btn_back.pack(side = LEFT, padx = 40)

        btn_next = Button(frame4, text = 'Adicionar', fg = 'green', command = validate)
        btn_next.pack(side = RIGHT,padx = 35)

#==============================================================================================================================
    def listContacts(self):
        root = Tk()
        root.geometry('250x70')
        root.title('Listar Contatos')

        myFont = font.Font(family = 'Helvetica', size = 16)
        width = 60
        frames = []

        def back():
            root.destroy()
            self.menu()

        def add_contacts():
            root.destroy()
            self.newContact()

        if not len(self.conts.dic):
            label = Label(text='Não há contatos!!!',fg = 'red', font = myFont)
            label.pack()

            lastframe = Frame(root, width=175, height=30)
            lastframe.pack()
            lastframe.pack_propagate(0)

            Button(lastframe, text = 'Voltar', command = back, fg = 'red').pack(side = LEFT)
            Button(lastframe, text = 'Adicionar contato', command = add_contacts, fg = 'green').pack(side = RIGHT)
        else:
            width += (len(self.conts.dic) * 20)
            size = '250x' + str(width)
            root.geometry(size)

            cabecalho = Frame(root, width = 185, height = 30, borderwidth=5) 
            cabecalho.pack()
            cabecalho.pack_propagate(0)
            
            contact = Label(cabecalho,text='Contatos', borderwidth=5)
            contact.pack(side = LEFT)
            
            numbers = Label(cabecalho,text='Números', borderwidth=5)
            numbers.pack(side = RIGHT)

            keys, elements = self.conts.list_conts()
            for c in range(len(self.conts.dic)):
                frames.append(Frame(root, width = 200, height = 20, relief = RAISED, borderwidth= '2'))
                frames[c].pack(padx=0, pady=0)
                frames[c].pack_propagate(0)

                #contacts names
                Label(frames[c], text=keys[c]).pack(side = LEFT)

                #concacts numbers
                num_text = f'({elements[c][:2]}){elements[c][2:7]}-{elements[c][7:]}'
                Label(frames[c], text=num_text).pack(side = RIGHT)


            lastframe = Frame(root)
            lastframe.pack()
            btn_backs = Button(lastframe, text = 'Voltar', command = back, fg = 'red')
            btn_backs.pack(side = LEFT)

#==============================================================================================================================
    def searchContact(self):
        root = Tk()
        root.geometry('250x80')
        root.title('Buscar contato')

        myFont = font.Font(family = 'Helvetica', size = 14)

        def back():
            root.destroy()
            self.menu()

        def search():
            label2 = Label(frame2)
            if search_contact.get().title() not in self.conts.dic:
                label2['text'] = 'Esse contato é inexistente!'
                label2['font'] = myFont
                label2.pack()
            else:
                num_text = self.conts.dic.get(search_contact.get().title())
                num_text_formated = f'({num_text[:2]}){num_text[2:7]}-{num_text[7:]}'

                label2['text'] = f'{search_contact.get().title()} -> {num_text_formated}'
                label2.pack()

                change.pack(side = RIGHT)
        
        def change_contact():
            changepag = Tk()
            changepag.geometry('200x100')
            changepag.title('Alterar contato')

            def update():
                self.conts.updatecont(search_contact.get().title(), name.get().title(), num.get())

                root.destroy()
                changepag.destroy()
                self.menu()

            frame1 = Frame(changepag)
            frame1.pack()
            Label(frame1, text = 'Novo nome').pack(side = LEFT, padx=6)
            name = Entry(frame1)
            name.pack(side = RIGHT)

            frame2 = Frame(changepag)
            frame2.pack()
            Label(frame2, text = 'Novo número').pack(side = LEFT)
            num = Entry(frame2)
            num.pack(side = RIGHT)

            Button(changepag, text = 'Alterar', command = update, fg = 'green').pack()
            
        
        frame1 = Frame(root, width = 200, height = 30)
        frame1.pack()
        frame1.pack_propagate(0)
        

        label1 = Label(frame1, text = 'Nome do contato:')
        label1.pack(side = LEFT)

        search_contact = Entry(frame1, width = 100)
        search_contact.pack(side = RIGHT)

        frame2 = Frame(root)
        frame2.pack()
        lastframe = Frame(root, width = 200, height = 30)
        lastframe.pack()
        lastframe.pack_propagate(0)

        Button(lastframe, text = 'Voltar', command = back, fg = 'red').pack(side = LEFT)
        change = Button(lastframe, text = 'Alterar', command = change_contact, fg = 'gray')
        Button(lastframe, text = 'Buscar', command = search, fg = 'green').pack(side = RIGHT)

        
        # Button(lastframe, text = 'Alterar contato', fg = 'green').pack(side = RIGHT)

m = windows() 