from tkinter import *
from tkcalendar import *
import pymysql
from tkinter import ttk, messagebox


class FormMysql:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire")
        self.root.geometry("1920x1080+0+0")

        # Champs du formulaire
        frame1 = Frame(self.root, bg="grey")
        frame1.place(x=500, y=200, width=700, height=500)

        title = Label(frame1, text="Formulaire", font=('time new rom', 20, "bold"), bg="grey", fg="white").place(x=50,
                                                                                                                y=30)

        # prenom
        txt_prenom = Label(frame1, text="Prénom", font=("time new roman", 15), bg="grey", fg="white").place(x=50, y=100)
        self.ecr_prenom = Entry(frame1, font=("times new roman", 15), bg="white")
        self.ecr_prenom.place(x=50, y=130, width=250)

        # nom
        txt_nom = Label(frame1, text="Nom", font=("time new roman", 15), bg="grey", fg="white").place(x=370, y=100)
        self.ecr_nom = Entry(frame1, font=("times new roman", 15), bg="white")
        self.ecr_nom.place(x=370, y=130, width=250)

        # email
        txt_email = Label(frame1, text="Adresse Mail", font=("time new roman", 15), bg="grey", fg="white").place(x=50,
                                                                                                                y=170)
        self.ecr_email = Entry(frame1, font=("times new roman", 15), bg="white")
        self.ecr_email.place(x=50, y=200, width=250)

        # téléphone
        var = IntVar()
        txt_tel = Label(frame1, text="Numéro de téléphone", font=("time new roman", 15), bg="grey", fg="white").place(
            x=370, y=170)
        self.ecr_tel = Entry(frame1, font=("times new roman", 15), bg="white")
        self.ecr_tel.place(x=370, y=200, width=250)

        # Sexe
        txt_sexe = Label(frame1, text="Sexe", font=("time new roman", 15), bg="grey", fg="white").place(x=50, y=240)
        self.ecr_sexe = ttk.Combobox(frame1, font=("time new roman", 15), state='readonly')
        self.ecr_sexe["values"] = ("Homme", "Femme")
        self.ecr_sexe.place(x=50, y=270, width=250)
        self.ecr_sexe.current(0)

        # Age
        txt_age = Label(frame1, text="Âge", font=("time new roman", 15), bg="grey", fg="white").place(x=370, y=240)
        self.ecr_age = DateEntry(frame1, font=("times new roman", 15), state="readonly", bg="white",
                                 date_pattern="dd/mm/yy")
        self.ecr_age.place(x=370, y=270, width=250)

        btn = Button(frame1, text="Valider", font=("times new roman", 15, "bold"), command=self.formulaire_donnee,
                     bg="black", fg="white").place(x=300, y=400)


    def reini(self):
        self.ecr_prenom.delete(0, END)
        self.ecr_nom.delete(0, END)
        self.ecr_email.delete(0, END)
        self.ecr_tel.delete(0, END)
        self.ecr_sexe.current(0)
        self.ecr_age.delete(0, END)

    def formulaire_donnee(self):
        if self.ecr_prenom.get()==""or self.ecr_nom.get()==""or self.ecr_email.get()==""or self.ecr_tel.get()==""or self.ecr_sexe.get()==""or self.ecr_age.get()=="":
            messagebox.showerror("Erreur", "Remplissez tous les champs", parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="projet python")
                cur = con.cursor()
                cur.execute("select * from formulaire where Mail=%s", self.ecr_email.get())
                row = cur.fetchone()

                if row != None:
                    messagebox.showerror("Erreur", "Ce mail existe déjà. Essayez un autre email.", parent=self.root)
                else:
                    cur.execute("insert into formulaire (Prenom, Nom, Mail, Tel, Sexe, Age) values(%s, %s, %s, %s, %s, %s)",
                                (self.ecr_prenom.get(),
                                 self.ecr_nom.get(),
                                 self.ecr_email.get(),
                                 self.ecr_tel.get(),
                                 self.ecr_sexe.get(),
                                 self.ecr_age.get(),
                                 ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ajout Effectué !", parent=self.root)
                    self.reini()
            except Exception as es:
                messagebox.showerror("Erreur", f"Erreur de Connexion : {str(es)}", parent=self.root)

root = Tk()
obj = FormMysql(root)
root.mainloop()
