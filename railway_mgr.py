from cProfile import label
from email import message
from email.mime import image
from platform import release
from struct import pack
from sys import maxsize
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor, dot, title, up, width
# import tkinter.font as TkFont
from tkinter import ttk
# from webbrowser import BackgroundBrowser
# import cx_Oracle
from PIL import Image, ImageTk


class manage():
    def _init_(self, winmanager):
        self.winmanager = winmanager
        self.winmanager.title('Manager page')
        self.winmanager.geometry('1350x700+0+0')
        # self.winmanager.minsize(1255,944)
        # self.winmanager.maxsize(1255,944)
        l1 = Label(self.winmanager, text="welcome")
        l1.pack()

        # Variables to use
        self.from_var = StringVar()
        self.to_var = StringVar()
        self.trainno_var = StringVar()
        self.stationcode_var = StringVar()
        self.arrivaltime_var = StringVar()
        self.departuretime_var = StringVar()
        self.class_var = StringVar()
        self.general_var = StringVar()
        self.movieactress_var = StringVar()
        self.moviedirector_var = StringVar()
        self.movielength_var = StringVar()
        self.movieseats_var = StringVar()
        self.movietheatre_var = StringVar()

        self.login_image = ImageTk.PhotoImage(file="images/nature.jpg")
        login_label = Label(self.winmanager, image=self.login_image)
        login_label.place(x=0, y=0, relwidth=1, relheight=1)

        title_frame = Frame(self.winmanager)
        title_frame.pack()
        registration_text = Label(title_frame, text='RAILWAY/..../Managing', font=("magneto", 30, "bold"), bd=5,
                                  borderwidth=13, bg='#7d1515', relief=RAISED)
        # registration_text.place(x=20,y=0,relx=1,rely=1)
        registration_text.pack()

        # LeftSideFrame//////////////////////////////////////////////////////////////////
        f1 = Frame(self.winmanager, bd=4, relief=RAISED, borderwidth=7, bg='#5e6269')
        f1.place(x=30, y=135, width=420, height=640)

        f1.columnconfigure(0, weight=3)
        f1.columnconfigure(1, weight=3)

        from_label = Label(f1, text='FROM :-', font=("magneto", 12, "bold"), bd=5, relief=RAISED, bg='#6f747d',
                           width=15)
        from_label.grid(row=0, column=0, padx=0, pady=14)

        from_label_entry = Entry(f1, textvariable=self.from_var, width=30, relief=SUNKEN, bg='#7d1515', bd=5,
                                 fg='white', font=("times", 10, "bold"))
        from_label_entry.grid(row=0, column=1, padx=5, pady=5)

        to_label = Label(f1, text='TO', font=("magneto", 12, "bold"), bd=5, relief=RAISED, bg='#6f747d', width=15)
        to_label.grid(row=1, column=0, padx=0, pady=8)

        to_entry = Entry(f1, textvariable=self.to_var, width=30, relief=SUNKEN, bg='#7d1515', bd=5, fg='white',
                         font=("times", 10, "bold"))
        to_entry.grid(row=1, column=1, padx=5, pady=5)

        train_label = Label(f1, text='TRAIN NO :-', font=("magneto", 12, "bold"), bd=5, relief=RAISED, bg='#6f747d',
                            width=15)
        train_label.grid(row=2, column=0, pady=8)

        train_label_entry = Entry(f1, textvariable=self.trainno_var, width=30, relief=SUNKEN, bg='#7d1515', bd=5,
                                  fg='white', font=("times", 10, "bold"))
        # train_label_entry.insert(0,'male or female')
        train_label_entry.grid(row=2, column=1, padx=5, pady=5)

        station_code = Label(f1, text='STATION CODE :-', font=("magneto", 12, "bold"), bd=5, relief=RAISED,
                             bg='#6f747d', width=15)
        station_code.grid(row=3, column=0, pady=8)

        station_code_entry = Entry(f1, textvariable=self.stationcode_var, width=30, relief=SUNKEN, bg='#7d1515', bd=5,
                                   fg='white', font=("times", 10, "bold"))
        station_code_entry.grid(row=3, column=1, padx=5, pady=5)

        arrival_time = Label(f1, text='ARRIVAL TIME :-', font=("magneto", 12, "bold"), bd=5, relief=RAISED,
                             bg='#6f747d', width=15)
        arrival_time.grid(row=4, column=0, pady=8)

        arrival_time_entry = Entry(f1, textvariable=self.arrivaltime_var, width=30, relief=SUNKEN, bg='#7d1515', bd=5,
                                   fg='white', font=("times", 10, "bold"))
        arrival_time_entry.grid(row=4, column=1, padx=5, pady=5)

        departure_time = Label(f1, text='DEPARTURE TIME :-', font=("magneto", 12, "bold"), bd=5, relief=RAISED,
                               bg='#6f747d', width=15)
        departure_time.grid(row=5, column=0, pady=8)

        departure_time_entry = Entry(f1, textvariable=self.departuretime_var, width=30, relief=SUNKEN, bg='#7d1515',
                                     bd=5, fg='white', font=("times", 10, "bold"))
        departure_time_entry.grid(row=5, column=1, padx=5, pady=5)

        class_type = Label(f1, text='CLASS :-', font=("magneto", 12, "bold"), bd=5, relief=RAISED, bg='#6f747d',
                           width=15)
        class_type.grid(row=6, column=0, pady=8)

        class_type_entry = ttk.Combobox(f1, textvariable=self.class_var, width=20, font=("times new roman", 13, "bold"))
        class_type_entry['values'] = ('AC TIER (1A)', 'AC TIER (2A)', 'AC TIER (3A)', 'NON AC')
        class_type_entry.grid(row=6, column=1, padx=5, pady=5)
        # movie_director_entry=ttk.Combobox(f1,textvariable=self.moviedirector_var,width=30,relief=SUNKEN,bg='#7d1515',bd=5,fg='white',font=("times",10,"bold"))
        # movie_director_entry.grid(row=6,column=1,padx=5,pady=5)

        general_type = Label(f1, text='GENERAL :-', font=("magneto", 12, "bold"), bd=5, relief=RAISED, bg='#6f747d',
                             width=15)
        general_type.grid(row=7, column=0, pady=8)

        general_type_entry = ttk.Combobox(f1, textvariable=self.general_var, width=20,
                                          font=("times new roman", 13, "bold"))
        general_type_entry['values'] = ('LOWER BERTH /SR.CITIZEN', 'DIVYAANG', 'TATKAL', 'PREMIUM TATKAL')
        general_type_entry.grid(row=7, column=1, padx=5, pady=5)

        insert_button = Button(f1, text='INSERT', bd=6, borderwidth=6, bg='#ad1a1a', width=15,
                               font=("magneto", 12, "bold"), command=self.add_data)
        insert_button.grid(row=10, column=0, padx=5, pady=10)

        update_button = Button(f1, text='UPDATE', bd=6, borderwidth=6, bg='#ad1a1a', width=15,
                               font=("magneto", 12, "bold"), command=self.update_data)
        update_button.grid(row=10, column=1, padx=5, pady=20)

        delete_button = Button(f1, text='DELETE', bd=6, borderwidth=6, bg='#ad1a1a', width=15,
                               font=("magneto", 12, "bold"), command=self.delete_data)
        delete_button.grid(row=11, column=0, padx=5, pady=5)

        clear_button = Button(f1, text='CLEAR', bd=6, borderwidth=6, bg='#ad1a1a', width=15,
                              font=("magneto", 12, "bold"), command=self.clear_data)
        clear_button.grid(row=11, column=1, padx=5, pady=5)

        quit_buttom = Button(self.winmanager, text="QUIT AND GO BACK", bd=7, borderwidth=9, bg='#ad1a1a', width=22,
                             font=("magneto", 14, "bold"), command=self.quit)
        quit_buttom.place(x=880, y=720)

        # TreeviewFrame///////////////////////////////////////////////////////////////////
        f2 = Frame(self.winmanager, bd=4, borderwidth=12, relief=RIDGE, bg='#5e6269')
        f2.place(x=590, y=136, width=900, height=560)
        scroll_x = Scrollbar(f2, orient=HORIZONTAL)
        scroll_y = Scrollbar(f2, orient=VERTICAL)

        self.TRAIN_Table = ttk.Treeview(f2, columns=(
        "FROM", "TO", "STATION_CODE", "ARRIVAL_TIME", "DEPARTURE_TIME", "CLASS", "GENERAL", "TRAIN_NO"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.TRAIN_Table.xview)
        scroll_y.config(command=self.TRAIN_Table.yview)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=("times new roman", 15, "bold"), fieldbackground='#ad1a1a',
                        background='#ad1a1a')
        style.configure("Treeview", background='#5e6269', fieldbackground='#5e6269', fieldforground="white",
                        forground="white")
        # style.theme_use("vista")

        self.TRAIN_Table.heading("FROM", text="FROM")
        self.TRAIN_Table.heading("TO", text="TO")
        self.TRAIN_Table.heading("STATION_CODE", text="STATION_CODE")
        self.TRAIN_Table.heading("ARRIVAL_TIME", text="ARRIVAL_TIME")
        self.TRAIN_Table.heading("DEPARTURE_TIME", text="DEPARTURE_TIME")
        self.TRAIN_Table.heading("CLASS", text="CLASS")
        self.TRAIN_Table.heading("GENERAL", text="GENERAL")
        self.TRAIN_Table.heading("TRAIN_NO", text="TRAIN_NO")

        self.TRAIN_Table['show'] = "headings"
        self.TRAIN_Table.column("FROM", width=80)
        self.TRAIN_Table.column("TO", width=150)
        self.TRAIN_Table.column("STATION_CODE", width=170)
        self.TRAIN_Table.column("ARRIVAL_TIME", width=180)
        self.TRAIN_Table.column("DEPARTURE_TIME", width=200)
        self.TRAIN_Table.column("CLASS", width=150)
        self.TRAIN_Table.column("GENERAL", width=80)
        self.TRAIN_Table.column("TRAIN_NO", width=160)

        self.TRAIN_Table.bind("<ButtonRelease-1>", self.get_data)

        self.TRAIN_Table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    # Class Methods///////////////////////////////////////////////////////////////////////////////

    def add_data(self):
        if self.from_var.get() == "" or self.to_var.get() == "" or self.trainno_var.get() == "" or self.stationcode_var.get() == "" or self.arrivaltime_var.get() == "" or self.delete_data.get() == "" or self.class_var.get() == "" or self.general_var.get() == "":
            messagebox.showerror("Error", "All (*) Fields Are Required!!!", parent=self.winmanager)

            f = self.from_var.get()
            t = self.to_var.get()
            tr = self.trainno_var.get()
            st = self.stationcode_var.get()
            ar = self.arrivaltime_var.get()
            dep = self.departuretime_var.get()
            cl = self.class_var.get()
            gn = self.general_var.get()

        # else:
        #     I=self.movieid_var.get()
        #     N=self.moviename_var.get()
        #     TY=self.movietype_var.get()
        #     DA=self.movierdate.get()
        #     AT=self.movieactor_var.get()
        #     AR=self.movieactress_var.get()
        #     DI=self.moviedirector_var.get()
        #     L=self.movielength_var.get()
        #     S=eval(self.movieseats_var.get())
        #     TH=self.movietheatre_var.get()
        #      # Connecting to the DATABASE
        #     con=cx_Oracle.connect('cinema/danish30')
        #     print(con.version)
        #     cursor=con.cursor()
        #     try:
        #         cursor.execute("INSERT INTO movie_details VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)",(I,N,TY,DA,AT,AR,DI,L,S,TH))
        #     except cx_Oracle.IntegrityError:
        #         messagebox.showerror("ALREADY EXISTED","MOVIE ALREADY EXISTED")

        #     else:
        #         con.commit()
        #         self.fetch_data()
        #         con.close()
        #         a=messagebox.showinfo("COMPLETED","MOVIE ADDED SUCCESFULLY")
        #         # if (a=='ok'):
        #     b=messagebox.askyesno("PERMISSION","GO BACK TO THE LOGIN PAGE")
        #     if(b=='yes'):
        #         self.winmanager.quit()

    def get_data(self, event):
        print()
        # cursor_row=self.TRAIN_Table.focus()
        # contents=self.TRAIN_Table.item(cursor_row)
        # row=contents['values']
        # self.movieid_var.set(row[0])
        # self.moviename_var.set(row[1])
        # self.movietype_var.set(row[2])
        # self.movierdate.set(row[3])
        # self.movieactor_var.set(row[4])
        # self.movieactress_var.set(row[5])
        # self.moviedirector_var.set(row[6])
        # self.movielength_var.set(row[7])
        # self.movieseats_var.set(row[8])
        # self.movietheatre_var.set(row[9])

    def fetch_data(self):
        print()
        # con=cx_Oracle.connect("cinema/danish30")
        # cur=con.cursor()
        # cur.execute("select * from Movie_Details")
        # rows = cur.fetchall()
        # if (rows)!=0:
        #     self.TRAIN_Table.delete(*self.TRAIN_Table.get_children())
        #     for row in rows:
        #         self.TRAIN_Table.insert('',END,values=row)
        #     con.commit()
        # con.close()

    def update_data(self):
        print()
        # if self.movieid_var.get()=="" or self.moviename_var.get()==""or self.movietype_var.get()==""or self.movierdate.get()==""or self.movieactor_var.get()=="" or self.movieactress_var.get()=="" or self.moviedirector_var.get()=="" or self.movielength_var.get()=="" or self.movieseats_var.get()=="" or self.movietheatre_var.get()=="":
        #      messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmanager)

        # else:
        #     I=self.movieid_var.get()
        #     N=self.moviename_var.get()
        #     TY=self.movietype_var.get()
        #     DA=self.movierdate.get()
        #     AT=self.movieactor_var.get()
        #     AR=self.movieactress_var.get()
        #     DI=self.moviedirector_var.get()
        #     L=self.movielength_var.get()
        #     S=eval(self.movieseats_var.get())
        #     TH=self.movietheatre_var.get()
        #      # Connecting to the DATABASE
        #     con=cx_Oracle.connect('cinema/danish30')
        #     print(con.version)
        #     cursor=con.cursor()
        #     try:
        #         cursor.execute("UPDATE MOVIE_DETAILS SET MOVIE_NAME= :1,MOVIE_TYPE= :2,RELEASE_DATE= :3,ACTOR= :4,ACTORESS= :5,DIRECTOR= :6,LENGTH= :7 ,SEATS= :8,THEATRE= :9 WHERE MOVIE_ID LIKE '%s'"%I,(N,TY,DA,AT,AR,DI,L,S,TH))

        #         con.commit()
        #         self.fetch_data()
        #         con.close()
        #     except cx_Oracle.IntegrityError:
        #         messagebox.showerror("ALREADY EXISTED","MOVIE ALREADY EXISTED IN THE LIST")

        #     else:

        #         messagebox.showinfo("SUCCESS","RECORD UPDATED SUCCESFULLY")
        #         # if (a=='ok'):
        #     b=messagebox.askyesno("PERMISSION","GO BACK TO THE LOGIN PAGE")
        #     if(b=='yes'):
        #         self.winmanager.quit()

    def delete_data(self):
        print()
        # I=self.movieid_var.get()
        # if I=="":
        #     messagebox.showerror("Error","Movie ID is Required to Delete the record!!",parent=self.winmanager)
        # else:
        #     con=cx_Oracle.connect("cinema/danish30")
        #     cur=con.cursor()
        #     cur.execute("Delete From Movie_Details where MOVIE_ID = :id",id=I)
        #     #rows = cur.fetchall()
        #     con.commit()
        #     self.fetch_data()
        #     con.close()
        #     messagebox.showinfo("Success","Record Deleted Successfully",parent=self.winmanager)

    def clear_data(self):
        print()

        # if self.movieid_var.get()=="" or self.moviename_var.get()==""or self.movietype_var.get()==""or self.movierdate.get()==""or self.movieactor_var.get()=="" or self.movieactress_var.get()=="" or self.moviedirector_var.get()=="" or self.movielength_var.get()=="" or self.movieseats_var.get()=="" or self.movietheatre_var.get()=="":

        #     messagebox.showerror("Error","All (*) Fields Are Required!!!",parent=self.winmanager)

        # self.movieid_var.set('')
        # self.moviename_var.set('')
        # self.movietype_var.set('')
        # self.movierdate.set('')
        # self.movieactor_var.set('')
        # self.movieactress_var.set('')
        # self.moviedirector_var.set('')
        # self.movielength_var.set('')
        # self.movieseats_var.set('')
        # self.movietheatre_var.set('')
        # # messagebox.showinfo("Success","Fields Cleared Successfully",parent =self.winmanager)

    def quit(self):
        print()
        # self.winmanager.destroy()


root0 = Toplevel()
ob = manage()
root0.mainloop()

if __name__ == "main":
    winmanager = Tk()
    ob = manage(winmanager)
    winmanager.mainloop()








