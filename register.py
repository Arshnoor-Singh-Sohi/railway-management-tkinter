from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import cx_Oracle
import re
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTRATION TAB")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # #To remove max tab issue
        # self.root.resizable(False,False)
        # BG IMAGE
        self.bg=ImageTk.PhotoImage(file="images/bg_pic1.png")
        bg=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1) #250


        #left imgae
        self.left=ImageTk.PhotoImage(file="images/railway_clipart1.png")
        left=Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        #Register Frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",25,"bold"),bg="white",fg="red").place(x=50,y=30)

        #--------------------------------Row1----------------------------------------------

        f_name=Label(frame1, text="FIRST NAME", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_fname.place(x=50, y=130, width=250)

        l_name=Label(frame1, text="LAST NAME", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_lname.place(x=370, y=130, width=250)

        #--------------------------------Row2----------------------------------------------

        contact=Label(frame1, text="CONTACT NO.", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=50, y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_contact.place(x=50,y=200,width=250)

        username=Label(frame1, text="USERNAME", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=370, y=170)
        self.txt_username=Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_username.place(x=370, y=200, width=250)

        #--------------------------------Row3----------------------------------------------

        question=Label(frame1, text="GENDER", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=50, y=240)

        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","MALE","FEMALE","OTHER")
        self.cmb_quest.place(x=50, y=270, width=250)
        self.cmb_quest.current(0)

        age=Label(frame1, text="AGE", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=370, y=240)
        self.txt_age=Entry(frame1, font=("times new roman", 15), bg="lightgrey")
        self.txt_age.place(x=370, y=270, width=250)

        #--------------------------------Row4----------------------------------------------

        password=Label(frame1, text="PASSWORD.", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=50, y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1, text="CONFIRM PASSWORD", font=("times new roman", 15, "bold"), bg="white", fg="#141466").place(x=370, y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #-------------Terms and conditions-----------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I AGREE THE TERMS AND CONDITIONS",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("timws new eoman",12)).place(x=50,y=380)

        self.btn_img=ImageTk.PhotoImage(file="images/register1.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)

        btn_signin=Button(self.root,text="SIGN IN",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=200,y=460,width=180)

    def login_window(self):
        self.root.destroy()
        import login

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_username.delete(0, END)
        self.txt_age.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    def register_data(self):

        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_username.get() == "" or self.cmb_quest.get() == "Select" or self.txt_age.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.txt_password.get() != self.txt_cpassword.get() :
            messagebox.showerror("Error","Password & Confirm Password should be same.",parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error","Please agree our terms & conditions",parent=self.root)
        else:
            try:
                con = cx_Oracle.connect("railway/railway007")
                cur = con.cursor()
                #To fetch email if already exists
                em = self.txt_username.get()
                stat = "select * from registration where email = :email"
                cur.execute(stat ,{'email':em})
                row = cur.fetchone()
                print(row)
                if row != None:
                    messagebox.showerror("Error", "User already exist,Please try with another email", parent=self.root)
                else:

                    cur.execute("insert into registration (FIRST_NAME,LAST_NAME,CONTACT_NUMBER,EMAIL,GENDER,AGE,PASSWORD) values (:1,:2,:3,:4,:5,:6,:7)",
                                (self.txt_fname.get(),
                                 self.txt_lname.get(),
                                 self.txt_contact.get(),
                                 self.txt_username.get(),
                                 self.cmb_quest.get(),
                                 self.txt_age.get(),
                                 self.txt_password.get()
                                ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("SUCCESS", "Registered Successfull", parent=self.root)
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

root  = Tk()
obj=Register(root)
root.mainloop()