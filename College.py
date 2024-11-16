from tkinter import*
from tkinter import ttk 
import random 
import time 
import datetime
from tkinter import messagebox
import mysql.connector

class College:
    def __init__(self,root):
        self.root=root
        self.root.title("College Management System")
        self.root.geometry("1530x900+0+0")
        self.root.config(bg="lightblue")
        
        self.CollegeNames = StringVar()
        self.StudentName = StringVar()
        self.AcademicYear = StringVar()
        self.Degree = StringVar()
        self.Department = StringVar()
        self.EnrollmentNo = StringVar()       
        self.Email = StringVar()
        self.PhoneNo = StringVar()
        self.Semester = StringVar()
        self.Grades = StringVar()
        self.Attendance = StringVar()
        self.NameCollege = StringVar()
        self.FacultyName = StringVar()
        self.FacultyEnrollmentNo = StringVar()
        self.FacultyPhone = StringVar()
        self.FacultyEmail = StringVar()
        self.FacultyDepartment = StringVar()
        self.FacultyAttendance = StringVar()
        self.NameaCollege = StringVar()
        self.AdminName = StringVar()
        self.AdminEnrollmentNo = StringVar()
        self.AdminEmail = StringVar()
        self.AdminPhone = StringVar()
        self.AdminDepartment = StringVar()
        self.AdminAttendance = StringVar()
        
        
        
        lbltitle = Label(self.root,bd=15,relief=RIDGE,text="COLLEGE MANAGEMENT SYSTEM",fg="black",bg="white",font=("times new roman",50,"bold"), background="lightpink")
        lbltitle.pack(side=TOP, fill=X)
        
        ####################### DATA FRAME ############
        
        DataFrame=Frame(self.root,bd=10,relief=RIDGE , bg="lightblue")
        DataFrame.place(x=0,y=100,width=1520,height=400)
        
        DataFrameLeft = LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,font=("times new roman",14,"bold"),text="Student Information" , bg="cyan")  
        DataFrameLeft.place(x=0,y=5,width=490,height=370)
        
        DataFrameCenter = LabelFrame(DataFrame,bd=8,relief=RIDGE,padx=0,pady=10,font=("times new roman",16,"bold"),text="Faculty Information" , bg="cyan")
        DataFrameCenter.place(x=500,y=5,width=485,height=370)
        
        
        DataFrameRight = LabelFrame(DataFrame,bd=5,relief=RIDGE,padx=10,
                                    font=("times new roman",16,"bold"),text="Admin Information", bg="cyan")
        DataFrameRight.place(x=990,y=5,width=490,height=370)
       
        
        
        # ============================== BUTTON ==========================
        
        ButtonFrame=Frame(self.root,bd=20,relief=RIDGE, bg="black")
        ButtonFrame.place(x=0,y=530,width=1520,height=70)
        
        # ========================= DETAILS FRAME ==========================
        
        DetailsFrame=Frame(self.root,bd=20,relief=RIDGE, bg="black")
        DetailsFrame.place(x=0,y=600,width=1520,height=180)
        
        # ===================== VALIDATION FUNCTION ===================
        def validate_phone_number(new_value):
            return new_value.isdigit() or new_value == ""
        vcmd = (root.register(validate_phone_number),'%p')
        
        
        
        
        # =============================== DATA FROM LEFT ========================
        

        lblCollegeNames = Label(DataFrameLeft,text="College Name:",font=("times new roman",13,"bold"),padx=2,pady=4)
        lblCollegeNames.grid(row=0,column=0,sticky=W)
        
        comCollegeNames = ttk.Combobox(DataFrameLeft,textvariable=self.CollegeNames,font =("times new roman",13,"bold"),width=33 , background="blue")
        comCollegeNames["values"]=("Bennett University","Amity University","IIT Delhi","University of Hyderabad","University of Singapore","Oxford University")
        comCollegeNames.grid(row=0,column=1)
        comCollegeNames.config(background="yellow")     
        
        lblStudentName = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Student Name:",padx=2, pady=4)
        lblStudentName.grid(row = 1, column=0,sticky=W)
        txtStudentName = Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.StudentName,width=35 ,bg="orange")
        txtStudentName.grid(row=1 , column=1)
        
        lblAcademicYear = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Academic Year:",padx=2,pady=4)
        lblAcademicYear.grid(row = 2, column=0,sticky=W)
        txtAcademicYear = Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.AcademicYear,width=35 ,bg= "yellow")
        txtAcademicYear.grid(row=2 , column=1)
        
        lblDegree = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Degree:" ,padx=2,pady=4)
        lblDegree.grid(row=3,column=0,sticky=W)
        
        comDegree = ttk.Combobox(DataFrameLeft,textvariable=self.Degree,font =("times new roman",13,"bold"),width=33 , background="blue")
        comDegree["values"]=("Undergraduate","Postgraduate","Phd","MBA","Law","Nursing","BSc","MSc")
        comDegree.grid(row=3,column=1)
        comDegree.config(background="yellow")
        
        
        
        lblDeparment = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Department:" ,padx=2,pady=4)
        lblDeparment.grid(row=4,column=0,sticky=W)
        
        comDepartment = ttk.Combobox(DataFrameLeft,textvariable=self.Department,font =("times new roman",13,"bold"),width=33 , background="blue")
        comDepartment["values"]=("Computer Science and Technology","Mechanical Engineering","Chemical Engineering","Electrical Engineering","Electronic Engineering","Civil Engineering","C.A","Management")
        comDepartment.grid(row=4,column=1)
        comDepartment.config(background="yellow")
        
       
        
        lblEnrollmentNo = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Enrollment No:",padx=2 , pady=4)
        lblEnrollmentNo.grid(row = 5, column=0,sticky=W)
        txtEnrollmentNo = Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.EnrollmentNo,width=35 , bg="orange")
        txtEnrollmentNo.grid(row=5 , column=1)
        
        lblEmail = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Email:",padx=2,pady=4)
        lblEmail.grid(row = 6, column=0,sticky=W)
        txtEmail = Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.Email,width=35 , bg="yellow")
        txtEmail.grid(row=6 , column=1)
        
        
        lblPhone = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="PhoneNo:" ,padx=2,pady=4)
        lblPhone.grid(row=7,column=0,sticky=W)
        
        comPhone = ttk.Combobox(DataFrameLeft,textvariable=self.PhoneNo,font =("times new roman",13,"bold"),width=33 , background="blue")
        comPhone["values"]=("+91","+44","+92","+65","+1","+86")
        comPhone.grid(row=7,column=1)
        comPhone.config(background="yellow")
        
        lblSemester = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Semester:",padx=2 , pady=4)
        lblSemester.grid(row = 8, column=0,sticky=W)
        txtSemester = Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.Semester,width=35 , bg="yellow")
        txtSemester.grid(row=8 , column=1)
        
        lblGrades = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Grades:",padx=2 , pady=4)
        lblGrades.grid(row = 9, column=0,sticky=W)
        txtGrades = Entry(DataFrameLeft,font=("times new roman",13,"bold"),textvariable=self.Grades,width=35 , bg="orange")
        txtGrades.grid(row=9 , column=1)
        
        
        lblAttendance = Label(DataFrameLeft,font=("times new roman",13,"bold"),text="Attendance:" ,padx=2,pady=4)
        lblAttendance.grid(row=10,column=0,sticky=W)
        
        comAttendance = ttk.Combobox(DataFrameLeft,textvariable=self.Attendance,font =("times new roman",13,"bold"),width=33 , background="blue")
        comAttendance["values"]=("Absent","Present")
        comAttendance.grid(row=10,column=1)
        comAttendance.config(background="yellow")
        
        # ===================================== DataFrameCenter =================================
        
        lblNameCollege = Label(DataFrameCenter,text="College Name:",font=("times new roman",13,"bold"),padx=2,pady=10)
        lblNameCollege.grid(row=0,column=0,sticky=W)
        
        comNameCollege = ttk.Combobox(DataFrameCenter,textvariable=self.NameCollege,font =("times new roman",13,"bold"),width=32 , background="blue")
        comNameCollege["values"]=("Bennett University","Amity University","IIT Delhi","University of Hyderabad","University of Singapore","Oxford University")
        comNameCollege.grid(row=0,column=1)
        comNameCollege.config(background="yellow")     
        
        lblFacultyName = Label(DataFrameCenter,font=("times new roman",13,"bold"),text="Faculty Name:",padx=2, pady=10)
        lblFacultyName.grid(row = 1, column=0,sticky=W)
        txtFacultyName = Entry(DataFrameCenter,font=("times new roman",13,"bold"),textvariable=self.FacultyName,width=34 ,bg="orange")
        txtFacultyName.grid(row=1 , column=1)
        
        lblFacultyEnrollmentNo = Label(DataFrameCenter,font=("times new roman",13,"bold"),text="Enrollment No:",padx=2 , pady=10)
        lblFacultyEnrollmentNo.grid(row = 2, column=0,sticky=W)
        txtFacultyEnrollmentNo = Entry(DataFrameCenter,font=("times new roman",13,"bold"),textvariable=self.FacultyEnrollmentNo,width=34 , bg="yellow")
        txtFacultyEnrollmentNo.grid(row=2 , column=1)
        
        lblFacultyEmail = Label(DataFrameCenter,font=("times new roman",13,"bold"),text="Email:",padx=2 , pady=10)
        lblFacultyEmail.grid(row = 3, column=0,sticky=W)
        txtFacultyEmail = Entry(DataFrameCenter,font=("times new roman",13,"bold"),textvariable=self.FacultyEmail,width=34 , bg="orange")
        txtFacultyEmail.grid(row=3 , column=1)
        
        lblFacultyPhone = Label(DataFrameCenter,font=("times new roman",13,"bold"),text="PhoneNo:" ,padx=2,pady=10)
        lblFacultyPhone.grid(row=4,column=0,sticky=W)
        
        comFacultyPhone = ttk.Combobox(DataFrameCenter,textvariable=self.FacultyPhone,font =("times new roman",13,"bold"),width=32 , background="blue")
        comFacultyPhone["values"]=("+91","+44","+92","+65","+1","+86")
        comFacultyPhone.grid(row=4,column=1)
        comFacultyPhone.config(background="yellow")
        
        lblFacultyDeparment = Label(DataFrameCenter,font=("times new roman",13,"bold"),text="Department:" ,padx=2,pady=10)
        lblFacultyDeparment.grid(row=5,column=0,sticky=W)
        
        comFacultyDepartment = ttk.Combobox(DataFrameCenter,textvariable=self.FacultyDepartment,font =("times new roman",13,"bold"),width=32 , background="blue")
        comFacultyDepartment["values"]=("Computer Science and Technology","Mechanical Engineering","Chemical Engineering","Electrical Engineering","Electronic Engineering","Civil Engineering","C.A","Management")
        comFacultyDepartment.grid(row=5,column=1)
        comFacultyDepartment.config(background="yellow")
        
        
        lblFacultyAttendance = Label(DataFrameCenter,font=("times new roman",13,"bold"),text="Attendance:" ,padx=2,pady=10)
        lblFacultyAttendance.grid(row=10,column=0,sticky=W)
        
        comFacultyAttendance = ttk.Combobox(DataFrameCenter,textvariable=self.FacultyAttendance,font =("times new roman",13,"bold"),width=33 , background="blue")
        comFacultyAttendance["values"]=("Absent","Present")
        comFacultyAttendance.grid(row=10,column=1)
        comFacultyAttendance.config(background="orange")
        
        
        
        
    #  ================================== DATA FROM RIGHT ====================================
        
        lblNameaCollege = Label(DataFrameRight,text="College Name:",font=("times new roman",13,"bold"),padx=2,pady=10)
        lblNameaCollege.grid(row=0,column=0,sticky=W)
        
        comNameaCollege = ttk.Combobox(DataFrameRight,textvariable=self.NameaCollege,font =("times new roman",13,"bold"),width=32 , background="blue")
        comNameaCollege["values"]=("Bennett University","Amity University","IIT Delhi","University of Hyderabad","University of Singapore","Oxford University")
        comNameaCollege.grid(row=0,column=1)
        comNameaCollege.config(background="yellow")     
        
        lblAdminName = Label(DataFrameRight,font=("times new roman",13,"bold"),text="Admin Name:",padx=2, pady=10)
        lblAdminName.grid(row = 1, column=0,sticky=W)
        txtAdminName = Entry(DataFrameRight,font=("times new roman",13,"bold"),textvariable=self.AdminName,width=34 ,bg="orange")
        txtAdminName.grid(row=1 , column=1)
        
        lblAdminEnrollmentNo = Label(DataFrameRight,font=("times new roman",13,"bold"),text="Enrollment No:",padx=2 , pady=10)
        lblAdminEnrollmentNo.grid(row = 2, column=0,sticky=W)
        txtAdminEnrollmentNo = Entry(DataFrameRight,font=("times new roman",13,"bold"),textvariable=self.AdminEnrollmentNo,width=34 , bg="yellow")
        txtAdminEnrollmentNo.grid(row=2 , column=1)
        
        lblAdminEmail = Label(DataFrameRight,font=("times new roman",13,"bold"),text="Email:",padx=2 , pady=10)
        lblAdminEmail.grid(row = 3, column=0,sticky=W)
        txtAdminEmail = Entry(DataFrameRight,font=("times new roman",13,"bold"),textvariable=self.AdminEmail,width=34 , bg="orange")
        txtAdminEmail.grid(row=3 , column=1)
        
        lblAdminPhone = Label(DataFrameRight,font=("times new roman",13,"bold"),text="PhoneNo:" ,padx=2,pady=10)
        lblAdminPhone.grid(row=4,column=0,sticky=W)
        
        comAdminPhone = ttk.Combobox(DataFrameRight,textvariable=self.AdminPhone,font =("times new roman",13,"bold"),width=32 , background="blue")
        comAdminPhone["values"]=("+91","+44","+92","+65","+1","+86")
        comAdminPhone.grid(row=4,column=1)
        comAdminPhone.config(background="yellow")
        
        lblAdminDeparment = Label(DataFrameRight,font=("times new roman",13,"bold"),text="Department:" ,padx=2,pady=10)
        lblAdminDeparment.grid(row=5,column=0,sticky=W)
        
        comAdminDepartment = ttk.Combobox(DataFrameRight,textvariable=self.AdminDepartment,font =("times new roman",13,"bold"),width=32 , background="blue")
        comAdminDepartment["values"]=("Computer Science and Technology","Mechanical Engineering","Chemical Engineering","Electrical Engineering","Electronic Engineering","Civil Engineering","C.A","Management")
        comAdminDepartment.grid(row=5,column=1)
        comAdminDepartment.config(background="yellow")
        
        
        
        lblAdminAttendance = Label(DataFrameRight,font=("times new roman",13,"bold"),text="Attendance:" ,padx=2,pady=10)
        lblAdminAttendance.grid(row=10,column=0,sticky=W)
        
        comAdminAttendance = ttk.Combobox(DataFrameRight,textvariable=self.AdminAttendance,font =("times new roman",13,"bold"),width=33 , background="blue")
        comAdminAttendance["values"]=("Absent","Present")
        comAdminAttendance.grid(row=10,column=1)
        comAdminAttendance.config(background="orange")
    

        # ================================== BUTTONS ===============================
        
        
        # btnPrescription = Button(ButtonFrame, text="Prescription", bg="lightpink", fg="white", font=("arial", 12, "bold"), width=24, height=2, padx=2, pady=6, anchor=CENTER) 
        # btnPrescription.grid(row=0, column=0) 
        btnSubmitData = Button(ButtonFrame, text="Submit Data", bg="lightblue", bd=5, fg="white", font=("arial", 12, "bold"), width=30, height=2, padx=2, pady=6, anchor=CENTER, command=self.iSubmitData) 
        btnSubmitData.grid(row=0, column=1) 
        btnUpdate = Button(ButtonFrame, text="Update", bg="lightpink", fg="white", bd=5, font=("arial", 12, "bold"), width=29, height=2, padx=2, pady=6, anchor=CENTER, command=self.iUpdate) 
        btnUpdate.grid(row=0, column=2) 
        btnDelete = Button(ButtonFrame, text="Delete", bg="lightblue", fg="white",bd=5, font=("arial", 12, "bold"), width=29, height=2, padx=2, pady=6, anchor=CENTER) 
        btnDelete.grid(row=0, column=3)  
        btnClear = Button(ButtonFrame, text="Clear", bg="lightpink", fg="white", bd=5,font=("arial", 12, "bold"), width=29, height=2, padx=2, pady=6, anchor=CENTER) 
        btnClear.grid(row=0, column=4) 
        btnExit = Button(ButtonFrame, text="Exit", bg="lightblue", fg="white", bd=5, font=("arial", 12, "bold"), width=29, height=2, padx=2, pady=6, anchor=CENTER) 
        btnExit.grid(row=0, column=5)
        
        
        
        # ==================================== TABLE ===================================
        # ==================================== SCROLLBAR ===================================
        
        scroll_x = ttk.Scrollbar(DetailsFrame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame,orient=VERTICAL)
        self.College_table = ttk.Treeview(DetailsFrame,columns=("CollegeName","StudentName","Degree","Department","EnrollmentNo","FacultyName",
                                                                "AdminName","Email","FacultyEmail","AdminEmail","FacultyEnrollmentNo","AdminEnrollmentNo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x = ttk.Scrollbar(command=self.College_table.xview)
        scroll_y = ttk.Scrollbar(command=self.College_table.yview)

        # self.College_table.heading("CollegeNames",text="CollegeNames")
        self.College_table.heading("StudentName",text="Student Name")
        self.College_table.heading("Degree",text="Degree")
        self.College_table.heading("Department",text="Department")
        self.College_table.heading("EnrollmentNo",text="Enrollment No")
        self.College_table.heading("Email",text="Email")
        self.College_table.heading("FacultyName",text="Faculty Name")
        self.College_table.heading("FacultyEmail",text="Faculty Email")
        self.College_table.heading("FacultyEnrollmentNo",text="Faculty EnrollmentNo")
        self.College_table.heading("AdminName",text="Admin Name")
        self.College_table.heading("AdminEmail",text="Admin Email")
        self.College_table.heading("AdminEnrollmentNo",text="Admin EnrollmentNo")
        
        
        self.College_table["show"]="headings"
        
        
        # self.College_table.column("Nameofcollege",width=100)
        self.College_table.column("StudentName",width=100)
        self.College_table.column("Degree",width=100)
        self.College_table.column("Department",width=100)
        self.College_table.column("EnrollmentNo",width=100)
        self.College_table.column("Email",width=100)
        self.College_table.column("FacultyName",width=100)
        self.College_table.column("FacultyEmail",width=100)
        self.College_table.column("FacultyEnrollmentNo",width=100)
        self.College_table.column("AdminName",width=100)
        self.College_table.column("AdminEmail",width=100)
        self.College_table.column("AdminEnrollmentNo",width=100)
        
        
        self.College_table.pack(fill=BOTH,expand=1)
        # self.fatch_data()
        #  ====================== FUNCTIONALLY DECLARATION ================
    def iSubmitData(self):
        if self.Nameofcollege.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error", "All fields are required")
            
    def iUpdate(self):
        if self.Nameofcollege.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error", "All fields are required")
        
            return  # Exit the function if required fields are empty

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Rohit@#$789", database="codewithkiran")
            my_cursor = conn.cursor()
            

            # Insert data into the database
            my_cursor.execute("insert into college values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.CollegeName.get(),
                self.StudentName.get(),
                # self.AcademicYear.get(),
                self.Degree.get(),
                self.Department.get(),
                self.EnrollmentNo.get(),
                # self.EnrollmentNo.get(),
                # self.AcademicYear.get(),
                self.Email.get(),
                # self.PhoneNo.get(),
                # self.Semester.get(),
                # self.Grades.get(),
                self.FacultyName.get(),
                self.FacultyEmail.get(),
                self.FacultyEnrollmentNo.get(),
                self.AdminName.get(),
                self.AdminEmail.get(),
                self.AdminEnrollmentNo.get()
            ))

            conn.commit()
            # self.fatch_data()
            conn.close()
    #         messagebox.showinfo("Success","Record has been inserted")
            
    # def fatch_data(self):
    #     conn = mysql.connector.connect(host="localhost", username="root", password="Rohit@#$789", database="codewithkiran")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("select * from hospital")
    #     rows = my_cursor.fetchall()
    #     if len(rows) != 0:
    #         self.hospital_table.delete(*self.hospital_table.get_children())
    #         for i in rows:
    #             self.hospital_table.insert("",END,values=i)
    #         conn.commit()
    #     conn.close()
        
    # def get_cursor(self):
    #     cursor_row = self.hospital_table.focus()
    #     content = self.hospital_table.focus()
    #     content = self.hospital_table.item(cursor_row)
    #     row = content["values"]
    #     self.Nameoftablets.set(row[0])
        
            
            
            
            
            
            
            

        #     messagebox.showinfo("Success", "Data inserted successfully!")

        # except mysql.connector.Error as err:
        #     messagebox.showerror("Error", f"Database error: {err}")
        # finally:
        #     if conn:
        #         conn.close()  # Close the connection even if there's an error

        # # Refresh the table data (you can implement this using `self.fatch_data()` or a similar function)
        # self.fatch_data()  # Assuming you have a function to fetch data from the database

            
            
       
        
        
        
        
        
        
root=Tk()
ob = College(root)
root.mainloop()