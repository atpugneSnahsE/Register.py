from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("registration form")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.bg=ImageTk.PhotoImage(file="images\IMG (3).jpg")
        bg=Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)
        self.left=ImageTk.PhotoImage(file="images\IMG (10).jpg")
        left=Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480, y=100, width= 700, height=500)
        
        title=Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=50, y=30)
        
       
        f_name=Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=50, y=100)
        self.txt_fname=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=50, y=130, width=250)
        
        l_name=Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=370, y=100)
        self.txt_lname=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_lname.place(x=370, y=130, width=250)
        
        contact=Label(frame1, text="Mobile no.", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=50, y=160)
        self.txt_contact=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=50, y=200, width=250)
        
        email=Label(frame1, text="email", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=370, y=160)
        self.txt_email=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=370, y=200, width=250)
        
        department=Label(frame1, text="Department", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=50, y=230)
        self.txt_department=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_department.place(x=50, y=270, width=250)
        
        Subject=Label(frame1, text="Subject", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=370, y=230)
        self.txt_subject=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_subject.place(x=370, y=270, width=250)
        
        Semester=Label(frame1, text="Semester", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=50, y=300)
        self.txt_semester=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_semester.place(x=50, y=340, width=250)
        
        Section=Label(frame1, text="Section", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=370, y=300)
        self.txt_section=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_section.place(x=370, y=340, width=250)
        
        Sex=Label(frame1, text="Sex", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=50, y=370)
        self.txt_sex=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_sex.place(x=50, y=410, width=250)
        
        Age=Label(frame1, text="Age", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=370, y=370)
        self.txt_age=Entry(frame1,font=("times new roman", 15), bg="lightgray")
        self.txt_age.place(x=370, y=410, width=250)

        self.btn_img=ImageTk.PhotoImage(file="images/btn.jpg")
        btn_register=Button(frame1, image=self.btn_img,bd=0, cursor="hand2",command=self.register_data).place(x=380, y=440)

    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_department.get()=="" or self.txt_subject.get()=="" or self.txt_semester.get()=="" or self.txt_section.get()=="" or self.txt_sex.get()=="" or self.txt_age.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            messagebox.showinfo("Success", "Registration Successful", parent=self.root)

              
root=Tk()
obj=register(root)
root.mainloop()