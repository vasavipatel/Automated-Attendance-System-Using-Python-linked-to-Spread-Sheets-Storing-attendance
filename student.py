from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        #=======variables====
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semister=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


         #first image

        img1=Image.open(r"C:\smartcampusproject\smartcampuspics\vnr logo.jpg")
        img1=img1.resize((200,150),Image.LANCZOS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=200,height=150)

        #second image

        img2=Image.open(r"C:\smartcampusproject\smartcampuspics\class1.jpg")
        img2=img2.resize((350,130),Image.Resampling.LANCZOS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=200,y=0,width=350,height=130)

        #third image

        img3=Image.open(r"C:\smartcampusproject\smartcampuspics\class2.jpg")
        img3=img3.resize((350,130),Image.Resampling.LANCZOS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=550,y=0,width=350,height=130)

        #image 4


        img4=Image.open(r"C:\smartcampusproject\smartcampuspics\class3.jpg")
        img4=img4.resize((350,130),Image.Resampling.LANCZOS)
        #ANTIALIAS used to chhange image from high resoution to low resolution
        self.photoimg4=ImageTk.PhotoImage(img4)

        f_lbl=Label(self.root,image=self.photoimg4)
        f_lbl.place(x=900,y=0,width=350,height=130)


        #background image

        img5=Image.open(r"C:\smartcampusproject\smartcampuspics\vnr.jpeg")
        img5=img5.resize((1300,500),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)


        bg_img=Label(self.root,image=self.photoimg5)
        bg_img.place(x=0,y=130,width=1300,height=500)


        #label title
        title_lbl=Label(bg_img,text="Student management system",font=("consolas",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1250,height=450)

        #left side label frame


        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=430)


        """img_left=Image.open(r"C:\smartcampusproject\smartcampuspics\class2.jpg")
        img_left=img_left.resize((590,100),Image.Resampling.LANCZOS)"""
        #ANTIALIAS used to chhange image from high resoution to low resolution
        #self.photoimg_left=ImageTk.PhotoImage(img_left)

       # f_lbl=Label(Left_frame,image=self.photoimg_left)
       # f_lbl.place(x=5,y=0,width=590,height=100)


        #current course INFORMATION

        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=0,width=590,height=125)
        #department

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("select dept","CSE","ECE","MECH","CIVIL","IT","CSDS","CSCY","CSBS","CS-IOT","EIE","EEE","CS-ML","AIML","AIDS")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white",)
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="read only",width=17)
        course_combo["values"]=("Select Course","BTECH","MBA","PG","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=17)
        year_combo["values"]=("Select Year","2019-2023","2020-2024","2021-2025","2022-2026")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=10,sticky=W)

        #semister

        semister_label=Label(current_course_frame,text="Semister",font=("times new roman",12,"bold"),bg="white")
        semister_label.grid(row=1,column=2,padx=10,sticky=W)

        semister_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semister,font=("times new roman",12,"bold"),state="read only",width=17)
        semister_combo["values"]=("Select Semister","sem-1","sem-2","sem-3","sem-4","sem-5","sem-6","sem-7","sem-8")
        semister_combo.current(0)
        semister_combo.grid(row=1,column=3,padx=10,sticky=W)

        #class student information

        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current student information",font=("times new roman",12,"bold"))
        class_Student_frame.place(x=5,y=130,width=590,height=272)
        #student id

        studentId_label=Label(class_Student_frame,text="StudentId",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.va_std_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=2,sticky=W)

        #student name

        studentName_label=Label(class_Student_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=2,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=2,sticky=W)

        #class division

        class_div_label=Label(class_Student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=2,sticky=W)

        class_div_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_div,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=2,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=18)
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,sticky=W)

        #rollno

        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=2,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=2,sticky=W)

        #Gender

        gender_label=Label(class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=2,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,sticky=W)

        #DOB

        dob_label=Label(class_Student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=2,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=2,sticky=W)

        #Email

        email_label=Label(class_Student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=2,sticky=W)

        #phone

        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=2,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=2,sticky=W)

        #adress

        address_label=Label(class_Student_frame,text="Adress",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=2,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=2,sticky=W)

        #Teeacher name

        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=2,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=2,sticky=W)


        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)

        #self.var_radio2=StringVar()
        radionbtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=5,column=1)

        #bbuttons frame 
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=583,height=40)

        #save button

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",12,"bold"),width=15,bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        #update button

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",12,"bold"),width=15,bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        #delete button

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",12,"bold"),width=15,bg="red",fg="white")
        delete_btn.grid(row=0,column=2)

        #reset button

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",12,"bold"),width=15,bg="yellow",fg="black")
        reset_btn.grid(row=0,column=3)

        #one more frame

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=220,width=583,height=40)

        #take photo sample

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset, text="take photo sample",font=("times new roman",12,"bold"),width=31,bg="orange",fg="black")
        take_photo_btn.grid(row=0,column=0)

        #update photo sample

        update_photo_btn=Button(btn_frame1,text="update photo sample",font=("times new roman",12,"bold"),width=31,bg="orange",fg="black")
        update_photo_btn.grid(row=0,column=1)

        #right frame

        Right_frame=Label(main_frame,bd=2,bg="white",relief=RIDGE,text=" ",font=("times new roman",12,"bold"))
        Right_frame.place(x=620,y=10,width=620,height=430)

        # ============SEARCH SYSTEM============

        #search frame

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=0,width=590,height=72)

        #search label

        search_label=Label(Search_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=2,sticky=W)

        #search combo

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="read only",width=12)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.grid(row=0,column=1,padx=2,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=19,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=2,sticky=W)

        search_btn=Button(Search_frame,text="Search",font=("times new roman",10,"bold"),width=14,bg="red",fg="white")
        search_btn.grid(row=0,column=3,padx=1)

        showAll_btn=Button(Search_frame,text="Show all",font=("times new roman",10,"bold"),width=14,bg="yellow",fg="black")
        showAll_btn.grid(row=0,column=4,padx=1)


        # ==========TABLE FRAME=========

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=75,width=590,height=250)

        #scroll bar
        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","roll","name","div","dob","email","phone","address","teacher","gender","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semister")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table.pack(fill="both",expand=1)

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #======function declaration=====

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
                #messagebox.showinfo("success","welcome",parent=self.root)
                conn=mysql.connector.connect(host="localhost",username="root",password="Vasaviade@16082003",database="face_recognizer2") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semister.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                    
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","student data added",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"due to :{str(es)}",parent=self.root)



    #========fetch data=======
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Vasaviade@16082003",database="face_recognizer2")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)

            conn.connect()
        conn.close()

    #=============get cursor=================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semister.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #=============update function=============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required, including Student ID",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details:",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Vasaviade@16082003",database="face_recognizer2")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semister=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semister.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.va_std_id.get()
                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #==============delete function==============
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Vasaviade@16082003",database="face_recognizer2") 
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)  
                    
    #==============reset function==============
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semister.set("Select Semister"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #============Generate data set or Take photo Samples=========
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Vasaviade@16082003",database="face_recognizer2")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s, course=%s, Year=%s, Semister=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semister.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.va_std_id.get()==id+1
                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #==========load predefined data on face frontals from opencv=======
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimun Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                     
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generationg data sets completed!!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



if __name__ =="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()