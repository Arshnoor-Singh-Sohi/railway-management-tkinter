from tkinter import *
from tkinter import ttk, messagebox
import cx_Oracle
import random
class Booking:
    def __init__(self):
        self.root = root
        self.root.title("TICKET BOOKING SYSTEM")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        title = Label(self.root, text="WELCOME, PLEASE BOOK YOUR TICKET HERE", bd=10, relief=GROOVE, font=("times new roman",40,"bold"), bg="#021e2f", fg="Orange")#fg=textcolor
        title.pack(side=TOP, fill=X)

        #------------ALL VARIABLES-------------
        self.From_var = StringVar()
        self.To_var = StringVar()
        self.TrainNo_var = StringVar()
        self.St_Code_var = StringVar()
        self.A_Time_var = StringVar()
        self.D_Time_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        self.ticket_no = StringVar()
        #------------MANAGER FRAME-------------
        Manage_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#373E98")
        Manage_Frame.place(x=20,y=100,width=475,height=580)

        m_title = Label(Manage_Frame,text="Book Train ",bg="#373E98",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        #------From
        lbl_from = Label(Manage_Frame, text="From", bg="#373E98", fg="white",font=("times new roman", 20, "bold"))
        lbl_from.grid(row=1, column=0, pady=10, padx=20, sticky="W")

        txt_from = Entry(Manage_Frame,textvariable=self.From_var,font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_from.grid(row=1, column=1, pady=10, sticky="W")
        #-------To
        lbl_to = Label(Manage_Frame, text="To", bg="#373E98", fg="white",font=("times new roman", 20, "bold"))
        lbl_to.grid(row=2, column=0, pady=10, padx=20, sticky="W")

        txt_to = Entry(Manage_Frame,textvariable=self.To_var,font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_to.grid(row=2, column=1, pady=10, sticky="W")
        #-------TrainNo
        lbl_train_no = Label(Manage_Frame, text="TrainNo.  ", bg="#373E98", fg="white",font=("times new roman", 20, "bold"))
        lbl_train_no.grid(row=3, column=0, pady=10, padx=20, sticky="W")

        txt_train_no = Entry(Manage_Frame,textvariable=self.TrainNo_var,font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_train_no.grid(row=3, column=1, pady=10, sticky="W")
        #-------St-Code
        lbl_station_code = Label(Manage_Frame, text="St-Code", bg="#373E98", fg="white",font=("times new roman", 20, "bold"))
        lbl_station_code.grid(row=4, column=0, pady=10, padx=20, sticky="W")

        txt_station_code = Entry(Manage_Frame,textvariable=self.St_Code_var,font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_station_code.grid(row=4, column=1, pady=10, sticky="W")
        #--------A-Time
        lbl_arrivaltime = Label(Manage_Frame, text="A-Time", bg="#373E98", fg="white",font=("times new roman", 20, "bold"))
        lbl_arrivaltime.grid(row=5, column=0, pady=10, padx=20, sticky="W")

        txt_arrivaltime = Entry(Manage_Frame,textvariable=self.A_Time_var,font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_arrivaltime.grid(row=5, column=1, pady=10, sticky="W")
        #--------D-Time
        lbl_departuretime = Label(Manage_Frame, text="D-Time", bg="#373E98", fg="white",font=("times new roman", 20, "bold"))
        lbl_departuretime.grid(row=6, column=0, pady=10, padx=20, sticky="W")

        txt_departuretime = Entry(Manage_Frame,textvariable=self.D_Time_var,font=("times new roman", 20, "bold"),bd=5,relief=GROOVE)
        txt_departuretime.grid(row=6, column=1, pady=10, sticky="W")

        #-------BUTTON FRAME----------------
        btn_Frame = Frame(Manage_Frame,bd=4,relief=RIDGE,bg="orange")
        btn_Frame.place(x=30,y=500,width=400)

        bookbtn = Button(btn_Frame,text="BOOK TICKET",width=20,height=2,command=self.add_train_info).grid(padx=120,pady=10)


        # ------------DETAIL FRAME-------------
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#373E98")
        Detail_Frame.place(x=500, y=100, width=770, height=580)

        lbl_search = Label(Detail_Frame, text="Search By", bg="#373E98", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="W")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=15,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values'] = ('From_', 'To_')
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10 ,padx=20 , sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=10,pady=5,command=self.fetch_data_to_searchby).grid(row=0, column=4, padx=10, pady=10)

        #---------Table Frame--------------
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="orange")
        Table_Frame.place(x=10, y=70, width=745, height=500)

        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Train_table = ttk.Treeview(Table_Frame,columns=("From","To","TrainNo","St-Code","A-Time","D-Time"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Train_table.xview)
        scroll_y.config(command=self.Train_table.yview)
        self.Train_table.heading("From",text="From")
        self.Train_table.heading("To",text="To")
        self.Train_table.heading("TrainNo",text="TrainNo")
        self.Train_table.heading("St-Code",text="St-Code")
        self.Train_table.heading("A-Time",text="A-Time")
        self.Train_table.heading("D-Time",text="D-Time")
        self.Train_table['show'] = 'headings'
        # Train_table.column("From",width=50) ---- IF YOU WANT TO ADJUST THE WIDTH
        self.Train_table.pack(fill=BOTH,expand=1)
        self.Train_table.bind("<ButtonRelease-1>", self.get_data_via_cursor) #event
        self.fetch_data_to_searchby()

    def add_train_info(self): #had to give two arguments
        if self.From_var.get() == "" or self.To_var.get() == "" or self.TrainNo_var.get() == "" or self.St_Code_var.get() == "" or self.A_Time_var.get == "" or self.D_Time_var.get() == "":
            messagebox.showerror("Error","All fields are required")
        else:
            self.ticket_no = str(random.randint(100,10000)) + str(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
            con = cx_Oracle.connect("railway/railway007")
            self.ticket_no,
            self.From_var.get(),
            self.To_var.get(),
            self.TrainNo_var.get(),
            self.St_Code_var.get(),
            self.A_Time_var.get(),
            self.D_Time_var.get()
            cur = con .cursor()
            cur.execute("insert into ticket (ticket_no,from_,to_,train_no,station_code,arrival_time,departure_time) values (:1,:2,:3,:4,:5,:6,:7)",
                        (       self.ticket_no,
                                self.From_var.get(),
                                self.To_var.get(),
                                self.TrainNo_var.get(),
                                self.St_Code_var.get(),
                                self.A_Time_var.get(),
                                self.D_Time_var.get()
                        ))
            con.commit()

            # self.clear()
            con.close()
            messagebox.showinfo("TICKET NUMBER", "Your Ticket Number is "+self.ticket_no)
            messagebox.showinfo("Success","Train has been booked")
            self.root.destroy()

    #To show data from Train_table to horizontal section view ---- trieview
    def fetch_data_to_searchby(self):
        con = cx_Oracle.connect("railway/railway007")
        cur = con.cursor()
        cur.execute("select * from manager")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Train_table.delete(*self.Train_table.get_children())
            for row in rows:
                self.Train_table.insert('',END,values=row)
            con.commit()
        con.close()

    #TO get data from horizontal to Train_table
    def get_data_via_cursor(self,event):#takes 1 positional argument
        cursor_row = self.Train_table.focus()
        contents = self.Train_table.item(cursor_row)
        row = contents['values'] #will return list
        self.From_var.set(row[0])
        self.To_var.set(row[1])
        self.TrainNo_var.set(row[2])
        self.St_Code_var.set(row[3])
        self.A_Time_var.set(row[4])
        self.D_Time_var.set(row[5])


    def search_data(self):
        con = cx_Oracle.connect("railway/railway007")
        cur = con.cursor()
        cur.execute("select * from manager where " + str(self.search_by.get()) + " Like '" + str(self.search_txt.get() +"'"))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Train_table.delete(*self.Train_table.get_children())
            for row in rows:
                self.Train_table.insert('', END, values=row)
            con.commit()
        con.close()

root = Tk()
ob = Booking()
root.mainloop()