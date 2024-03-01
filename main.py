from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recoginition
from attendence import Attendance
from developer import Developer
from help1 import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image

        img1=Image.open(r"smartcampuspics\img1.png")
        img1=img1.resize((350,130),Image.ANTIALIAS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=350,height=130)

        #second image

        img2=Image.open(r"smartcampuspics\img2.jpg")
        img2=img2.resize((350,130),Image.ANTIALIAS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=350,y=0,width=350,height=130)

        #third image

        img3=Image.open(r"smartcampuspics\img4.jpg")
        img3=img3.resize((350,130),Image.ANTIALIAS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=700,y=0,width=350,height=130)

        #image 4


        img4=Image.open(r"smartcampuspics\img8.jpg")
        img4=img4.resize((350,130),Image.ANTIALIAS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=1050,y=0,width=350,height=130)

        #background image

        img5=Image.open(r"smartcampuspics\vnr.jpeg")
        img5=img5.resize((1300,500),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        bg_img=Label(self.root,image=self.photoimg5)
        bg_img.place(x=0,y=130,width=1300,height=500)


        #label title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("consolas",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        #=====================time====================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl=Label(title_lbl, font = ("times new roman",14,"bold"),background="white",foreground="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #image button
        #STUDENT BUTTON

        img6=Image.open(r"smartcampuspics\stud.jpg")
        img6=img6.resize((150,150),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.student_details)
        b1.place(x=50,y=50,width=150,height=150)

        b1_1=Button(bg_img,text="student details",cursor="hand2",command=self.student_details,font=("times new roman",8,"bold"),bg="white",fg="blue")
        b1_1.place(x=50,y=180,width=150,height=20)\
        
        #face detection button

        img7=Image.open(r"smartcampuspics\img10.jpg")
        img7=img7.resize((150,150),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=50,width=150,height=150)

        b1_1=Button(bg_img,text="face detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=400,y=180,width=150,height=30)


        #attendance face button

        img8=Image.open(r"smartcampuspics\att.png")
        img8=img8.resize((150,150),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.attendence_data,cursor="hand2")
        b1.place(x=750,y=50,width=150,height=150)

        b1_1=Button(bg_img,text="Attendance",command=self.attendence_data, cursor="hand2",font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=750,y=180,width=150,height=30)

         #help desk

        img9=Image.open(r"smartcampuspics\hd.jpg")
        img9=img9.resize((150,150),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.help_data)
        b1.place(x=1050,y=50,width=150,height=150)

        b1_1=Button(bg_img,text="Help desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=1050,y=180,width=150,height=30)

        # train face button

        img10=Image.open(r"smartcampuspics\img1.png")
        img10=img10.resize((150,150),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.train_data)
        b1.place(x=50,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=50,y=430,width=150,height=30)

        #photos
        img11=Image.open(r"smartcampuspics\photo.jpg")
        img11=img11.resize((150,150),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=400,y=430,width=150,height=30)

        # Developer Face Button

        img12=Image.open(r"smartcampuspics\dev.jpg")
        img12=img12.resize((150,150),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.developer_data)
        b1.place(x=750,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data, font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=750,y=430,width=150,height=30)

        # Exit Face button
        img13=Image.open(r"smartcampuspics\exit.jpg")
        img13=img13.resize((150,150),Image.ANTIALIAS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        b1=Button(bg_img,image=self.photoimg13,cursor="hand2",command=self.iExit)
        b1.place(x=1050,y=300,width=150,height=150)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="white",fg="blue")
        b1_1.place(x=1050,y=430,width=150,height=30)

    def open_img(self):
        os.startfile("data")
    
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure you want to exit this project?", parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return 

#========================Functions buttons==============

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recoginition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

 



if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
