from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from student import Student

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1200,height=50)

        img_top=Image.open(r"smartcampuspics\dev.jpg")
        img_top=img_top.resize((470,250),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=60,width=470,height=250)

        img_top1=Image.open(r"smartcampuspics\dev.jpg")
        img_top1=img_top1.resize((470,250),Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(self.root,image=self.photoimg_top1)
        f_lbl.place(x=400,y=60,width=470,height=250)

        img_top2=Image.open(r"smartcampuspics\dev.jpg")
        img_top2=img_top2.resize((470,250),Image.ANTIALIAS)
        self.photoimg_top2=ImageTk.PhotoImage(img_top2)

        f_lbl=Label(self.root,image=self.photoimg_top2)
        f_lbl.place(x=800,y=60,width=470,height=250)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=300,width=1300,height=40) 

        img_top3=Image.open(r"smartcampuspics\dev.jpg")
        img_top3=img_top3.resize((470,250),Image.ANTIALIAS)
        self.photoimg_top3=ImageTk.PhotoImage(img_top3)

        f_lbl=Label(self.root,image=self.photoimg_top3)
        f_lbl.place(x=0,y=350,width=470,height=250)

        img_top4=Image.open(r"smartcampuspics\dev.jpg")
        img_top4=img_top4.resize((470,250),Image.ANTIALIAS)
        self.photoimg_top4=ImageTk.PhotoImage(img_top4)

        f_lbl=Label(self.root,image=self.photoimg_top4)
        f_lbl.place(x=400,y=350,width=470,height=250)

        img_top5=Image.open(r"smartcampuspics\dev.jpg")
        img_top5=img_top5.resize((470,250),Image.ANTIALIAS)
        self.photoimg_top5=ImageTk.PhotoImage(img_top5)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=800,y=350,width=470,height=250)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)


        # ============= Train the classifier and save============
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()

#instal numpy -> open command prompt -> paste(pip install numpy) -> statisfied
'''#in main.py file#
        
in Train face button
include command in button element
command=self.train_data'''
