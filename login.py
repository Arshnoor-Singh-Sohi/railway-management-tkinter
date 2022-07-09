from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from tkinter import ttk,messagebox
from datetime import *
import time
from math import *
import cx_Oracle
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Railway Login Page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        #BACKGROUND COLORS---------------------
        left_label = Label(self.root, bg="#08A3D2", bd=0)
        left_label.place(x=0, y=0, relheight=1, width=600)

        right_label = Label(self.root, bg="#031F3C", bd=0)
        right_label.place(x=600, y=0, relheight=1, relwidth=1)

        #FRAMES--------------------------------
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)

        email=Label(login_frame,text="USERNAME",font=("times new roman",18,"bold"),bg="white",fg="grey").place(x=250,y=150)
        self.txt_username=Entry(login_frame, font=("times new roman", 15, "bold"), bg="lightgrey")
        self.txt_username.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white",fg="grey").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 15, "bold"),show='*', bg="lightgrey")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)


        self.btn_reg = Button(login_frame,cursor="hand2",command=self.register_window,text="Register New Account?",font=("times new roman",14),bg="white",bd=0,fg="#B00857").place(x=250,y=320)
        self.btn_forget = Button(login_frame,cursor="hand2",command=self.forget_password_window,text="Forget Password?",font=("times new roman",14),bg="white",bd=0,fg="red").place(x=450,y=320)

        self.btn_login = Button(login_frame,command=self.login, text="LOGIN", font=("times new roman", 20, "bold"), fg="white", bg="#B00857",cursor="hand2").place(x=250, y=380, width=180, height=40)



        #CLOCK---------------------------------
        self.lbl = Label(self.root, text="CLOCK", font=("Book Antiqua", 25, "bold"), fg="white", compound=BOTTOM, bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)

        self.working()

    def reset(self):
        self.txt_new_password.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_username.delete(0, END)
        self.txt_pass_.delete(0, END)

    def forget_password(self):
        if self.txt_contact.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                con = cx_Oracle.connect("railway/railway007")
                cur = con.cursor()

                em = self.txt_username.get()
                cont = self.txt_contact.get()
                cur.execute("select * from registration where email = :email and contact_number = :contact", {'email': em,'contact': cont})
                # To fetch email and password for user
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter the correct contact number.", parent=self.root2)
                else:
                    npass = self.txt_new_password.get()
                    cur.execute("update registration set password = :new_pass where email = :email ",{'new_pass': npass,'email': em})
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset,Please login with new password",parent = self.root2)
                    self.reset()
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)


    def forget_password_window(self):
        if self.txt_username.get() == "":
            messagebox.showerror("Error","Please enter the username to rest your password.",parent=self.root)
        else:
            try:
                con = cx_Oracle.connect("railway/railway007")
                cur = con.cursor()

                em = self.txt_username.get()
                cur.execute("select * from registration where email = :email ",{'email':em })
                #To fetch email and password for user
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter your valid username to rest your password.",parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("400x350+440+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()  # focuses on the currently open window
                    self.root2.grab_set()  # grab untile user closes it

                    t = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), bg="white",fg="red").place(x=0, y=20, relwidth=1)

                    contact = Label(self.root2, text="CONTACT NO.", font=("times new roman", 15, "bold"), bg="white",fg="#141466").place(x=50, y=100)
                    self.txt_contact = Entry(self.root2, font=("times new roman", 15), bg="lightgrey")
                    self.txt_contact.place(x=50, y=130, width=250)

                    new_password = Label(self.root2, text="NEW PASSWORD", font=("times new roman", 15, "bold"),bg="white", fg="#141466").place(x=50, y=170)
                    self.txt_new_password = Entry(self.root2, font=("times new roman", 15), bg="lightgrey")
                    self.txt_new_password.place(x=50, y=200, width=250)

                    btn_change_password = Button(self.root2, text="Reset Password",command=self.forget_password, bg="red", fg="white",font=("times new roman", 15, "bold")).place(x=120, y=270)


            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_username.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con = cx_Oracle.connect("railway/railway007")
                cur = con.cursor()

                em = self.txt_username.get()
                ps = self.txt_pass_.get()
                cur.execute("select * from registration where email = :email and password = :password",{'email':em, 'password' :ps })
                #To fetch email and password for user
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid EMAIL or PASSWORD", parent=self.root)
                elif self.txt_username.get() == "Manager007@gmail.com" and self.txt_pass_.get() == "manager007":
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    import manager
                else:
                    messagebox.showinfo("Success","Welcome",parent = self.root)
                    self.root.destroy()
                    import Booking
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to:{str(es)}", parent=self.root)


    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8,25,35))
        draw = ImageDraw.Draw(clock)
        #For clock image
        bg = Image.open("images/darkclock.jpg")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        #Formula To Rotate the Anti-Clock
        #angle_in_radians = angle_in_degrees * math.pi /180
        #line_lenght = 100
        #center_x = 250
        #center_y = 250
        #end_x = center_x + line_lenght * math.cos(angle_in_radians)
        #end_y = center_y + line_lenght * math.sin(angle_in_radians)

        #For Hour line image
        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="#DF005E", width=4)
        #For Minute line image
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="white", width=3)
        #For Second line image
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="black")
        clock.save("images/clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360

        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root = Tk()
obj = Login(root)
root.mainloop()








