from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recoginition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITON",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1300,height=45)

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
        b1_1=Button(self.root,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
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



        
    #**************attendence********************
    def mark_attendence(self,i,r,n,d):
        with open("kiran.csv", "r+", newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and(n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n}, {d}, {dtString}, {d1}, Preset")

    #**************Face_Recoginition**************

    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbours)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Vasaviade@16082003",database="face_recognizer2")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student whereStudent_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student whereStudent_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student whereStudent_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Name from student whereStudent_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}"(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   
                    cv2.putText(img,f"Roll:{r}"(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}"(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}"(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face:{r}"(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,y]
            
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        #image from desktop
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") 

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome TO face Recognition",img)

            if cv2.waitkey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":
    root=Tk()
    obj=Face_Recoginition(root)
    root.mainloop()