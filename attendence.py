from tkinter import*
from tkinter import ttk 
from PIL import Image,ImageTk 
from tkinter import messagebox
import mysql.connector
#from time import strftime
#from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        #============variables=============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendence=StringVar()




        # first imag
        img=Image.open(r"C:\smartcampusproject\smartcampuspics\class3.jpg") 
        img=img.resize((300,200), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img) 

        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=300,height=200)

        # second image
        img1=Image.open(r"C:\smartcampusproject\smartcampuspics\class4.jpg")
        img1=img1.resize((300,200), Image.ANTIALIAS)
        self.photoimg1=ImageTk. PhotoImage(img1)

        f_lbl=Label(self.root, image=self.photoimg1) 
        f_lbl.place(x=300, y=0, width=300, height=200)

        img2=Image.open(r"C:\smartcampusproject\smartcampuspics\class1.jpg")
        img2=img2.resize((300,200), Image.ANTIALIAS)
        self.photoimg2=ImageTk. PhotoImage(img2)

        f_lbl=Label(self.root, image=self.photoimg2) 
        f_lbl.place(x=600, y=0, width=300, height=200)
        


    
        # bg image
        img3=Image.open(r"C:\smartcampusproject\smartcampuspics\vnr logo.jpg")
        img3=img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200, width=1450, height=600)
    
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman",27,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=45)
    
        main_frame=Frame (bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=45, width=1300,height=500)
    
        # left label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times nes roman",10,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=370)

        img_left=Image.open(r"C:\smartcampusproject\smartcampuspics\class1.jpg")
        img_left=img_left.resize((400,130), Image.ANTIALIAS) 
        self.photoing_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame, image=self.photoing_left)
        f_lbl.place(x=5,y=0,width=400, height=130)

        left_inside_frame=Frame (Left_frame,bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=10,y=130, width=580,height=220)

        

        # Labels entry
        # attendance id
        attendanceId_label=Label(left_inside_frame, text="AttendanceId:", font=("times new roman",13, "bold"),bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 13, "bold")) 
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name
        rollLabel=Label(left_inside_frame, text="Roll:", font=("conicsansns",11, "bold"),bg="white")
        rollLabel.grid(row=1, column=2, padx=10, pady=5)

        atten_roll=ttk.Entry(left_inside_frame, width=22,textvariable=self.var_atten_name, font=("conicsansns", 13, "bold")) 
        atten_roll.grid(row=1, column=3, padx=10, pady=0)

        # Date
        nameLabel=Label(left_inside_frame, text="Name:", font=("conicsansns",11, "bold"),bg="white")
        nameLabel.grid(row=2, column=0)

        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22, font=("conicsansns", 13, "bold")) 
        atten_name.grid(row=2, column=1,pady=8)
        

        # Dep
        depLabel=Label(left_inside_frame, text="Department:", font=("conicsansns",11, "bold"),bg="white")
        depLabel.grid(row=3, column=2)

        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22, font=("conicsansns", 13, "bold")) 
        atten_dep.grid(row=3, column=3,pady=8)

        # attendence
        attendenceLabel=Label(left_inside_frame, text="Attendence Status", font=("conicsansns",11, "bold"),bg="white")
        attendenceLabel.grid(row=4, column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendence, font="conicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=4,column=1,pady=2)
        self.atten_status.current(0)

        #buttons frame 
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=583,height=40)

        #save button

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,font=("times new roman",12,"bold"),width=15,bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        #update button

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete button

        delete_btn=Button(btn_frame,text="Update",font=("times new roman",12,"bold"),width=15,bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        #reset button

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),width=15,bg="yellow",fg="black")
        reset_btn.grid(row=0,column=3)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student details",font=("times new roman",10,"bold"))
        Right_frame.place(x=630,y=10,width=600,height=370)

        table_frame=Frame (Right_frame, bd=2, relief=RIDGE, bg="white") 
        table_frame.place(x=5,y=5, width=585,height=335)


        # ==========scroll bar table=============== 
        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame, column=("id", "roll", "name", "department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X) 
        scroll_y.pack(side=RIGHT, fill=Y)
    
        scroll_x.config(command=self.AttendaceReportTable.xview) 
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Attendace ID")
        self.AttendaceReportTable.heading("roll", text="Roll") 
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date") 
        self.AttendaceReportTable.heading("attendance", text="Attendance")  
    
        self.AttendaceReportTable["show"]="headings"  

        self.AttendaceReportTable.column("id",width=100)    
        self.AttendaceReportTable.column ("roll", width=100)
        self.AttendaceReportTable.column ("name", width=100)
        self.AttendaceReportTable.column("department", width=100)
        self.AttendaceReportTable.column("time", width=100) 
        self.AttendaceReportTable.column ("date", width=100)
        self.AttendaceReportTable.column("attendance", width=100) 
          
        self.AttendaceReportTable.pack (fill=BOTH, expand=1)

    

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

    #============fetch data================
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendanceReportTable.get_childern())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i) 
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to" + os.path.basename(fln)+"sucessfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To: (str(es))", parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendence.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendence.set("")
#Name
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()