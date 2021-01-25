Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
from tkinter import ttk  #this module provide combobox 
import pymysql
from tkinter import messagebox
from datetime import datetime
today=datetime.today()
entrytime=datetime.today()


class Parking:
    def __init__(self,root):
        self.root=root
        self.root.title("Parking Management System")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Parking Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#bad411",fg="blue")
        title.pack(side=TOP,fill=X)
        
        #----varible declaration---#
        self.ID_var=StringVar()
        self.Name_var=StringVar()
        self.Mobile_no_var=StringVar()
        self.Vehicle_No_var=StringVar()
        self.Vehicle_Type_var=StringVar()
        self.Entry_Time_var=StringVar()
        self.Exit_Time_var=StringVar()
#         self.Search_By=StringVar()
#         self.Search_txt=StringVar()
        
        
        
        
        
        
        
        
        
        #-------Manage frame-------#
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#8ededb")
        Manage_Frame.place(x=20,y=100,width=450,height=580)
        m_title=Label(Manage_Frame,text="Customer Entry:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        lbl_Id=Label(Manage_Frame,text="ID:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_Id.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_Id=Entry(Manage_Frame,textvariable=self.ID_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Id.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Name=Label(Manage_Frame,text="Name:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_Name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txt_Name=Entry(Manage_Frame,textvariable=self.Name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        lbl_Mobile=Label(Manage_Frame,text="Mobile No:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_Mobile.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txt_Mobile=Entry(Manage_Frame,textvariable=self.Mobile_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Mobile.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        
        lbl_vtype=Label(Manage_Frame,text="Vehicle Type:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_vtype.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        combo_vtype=ttk.Combobox(Manage_Frame,textvariable=self.Vehicle_Type_var,font=("times new roman",13,"bold"),state="readonly")
        combo_vtype['values']=("2W type","3W type","4W type","other")
        combo_vtype.grid(row=4,column=1,padx=20,pady=10,sticky="w")
        
        
        lbl_vno=Label(Manage_Frame,text="Vehicle No:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_vno.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txt_vno=Entry(Manage_Frame,textvariable= self.Vehicle_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_vno.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        
        lbl_entrytime=Label(Manage_Frame,text="Entry time:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_entrytime.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        txt_entrytime=Entry(Manage_Frame,textvariable=self.Entry_Time_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_entrytime.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        
        lbl_exittime=Label(Manage_Frame,text="Exit time:",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_exittime.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        txt_exittime=Entry(Manage_Frame,textvariable=self.Exit_Time_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_exittime.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        
        #button frame#
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#8ededb")
        btn_Frame.place(x=15,y=500,width=420)
        
        Addbtn=Button(btn_Frame,text="ADD INFO",width=10,command=self.add_customers).grid(row=0,column=0,padx=10)
        updatebtn=Button(btn_Frame,text="UPDATE",width=10,command=self.manage_data).grid(row=0,column=1,padx=10)
#         historybtn=Button(btn_Frame,text="history",width=10).grid(row=0,column=2,padx=10)
        deletebtn=Button(btn_Frame,text="DELETE",width=10,command=self.Delete_data).grid(row=0,column=2,padx=10)
        clearbtn=Button(btn_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10)
        amountbtn=Button(btn_Frame,text="BILL",width=10,command=self.new_Window).grid(row=1,column=3,padx=10)
        datebtn=Button(btn_Frame,text="Exit Time",width=10,command=self.current_time).grid(row=1,column=0,padx=10)
        Edatebtn=Button(btn_Frame,text="Entry Time",width=10,command=self.current_time2).grid(row=1,column=1,padx=10)
        
        
        #---------detail frame--------#
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#8ededb")
        Detail_Frame.place(x=500,y=100,width=900,height=580)
        
        lbl_search=Label(Detail_Frame,text="DETAILS OF CUSTOMERS",bg="#8ededb",fg="blue",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
#         combo_search=ttk.Combobox(Detail_Frame,textvariable=self.Search_By,font=("times new roman",13,"bold"),state="readonly")
#         combo_search["value"]=("ID","Name","Mobile No","Vehicle No")
#         combo_search.grid(row=0,column=1,padx=20,pady=10)
        
#         txt_search=Entry(Detail_Frame,textvariable=self.Search_txt,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
#         txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
#         searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.Search_data).grid(row=0,column=3,padx=10,pady=10)
#         showallbtn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        
        #----table frame---#
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#8ededb")
        Table_Frame.place(x=10,y=70,width=822,height=500)
        
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.customer_Table=ttk.Treeview(Table_Frame,columns=("ID","Name","Mobileno","vehicleno","vehicletype","entrytime","exittime"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.customer_Table.xview)
        scroll_y.config(command=self.customer_Table.yview)
        self.customer_Table.heading("ID",text="ID")
        self.customer_Table.heading("Name",text="Name")
        self.customer_Table.heading("Mobileno",text="Mobileno")
        self.customer_Table.heading("vehicletype",text="Vehicletype")
        self.customer_Table.heading("vehicleno",text="Vehicleno")
        self.customer_Table.heading("entrytime",text="Entrytime")
        self.customer_Table.heading("exittime",text="Exittime")
        self.customer_Table['show']='headings'
        self.customer_Table.column("ID",width=100)
        self.customer_Table.column("Name",width=100)
        self.customer_Table.column("Mobileno",width=100)
        self.customer_Table.column("vehicletype",width=100)
        self.customer_Table.column("vehicleno",width=100)
        self.customer_Table.column("entrytime",width=100)
        self.customer_Table.column("exittime",width=100)
        self.customer_Table.column("Mobileno",width=150)
        self.customer_Table.pack(fill=BOTH,expand=1)
        self.customer_Table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        self.fetch_data()
    def add_customers(self):
        if self.ID_var.get()=="" or self.Name_var.get()=="":
            messagebox.showerror("Error","insert details!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
            cur=con.cursor()
            cur.execute("insert into customers values(%s,%s,%s,%s,%s,%s,%s)",(self.ID_var.get(),
                                                                              self.Name_var.get(),
                                                                              self.Mobile_no_var.get(),
                                                                              self.Vehicle_No_var.get(),
                                                                              self.Vehicle_Type_var.get(),
                                                                              self.Entry_Time_var.get(),
                                                                              self.Exit_Time_var.get()
                                                                               ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.Showinfo("Success","Record has been inserted")
    
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur=con.cursor()
        cur.execute("select * from customers")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.customer_Table.delete(*self.customer_Table.get_children())
            for row in rows:
                self.customer_Table.insert('',END,values=row)
            con.commit()
        con.close()
        
    def clear(self):
        self.ID_var.set("")
        self.Name_var.set("")
        self.Mobile_no_var.set("")
        self.Vehicle_No_var.set("")
        self.Entry_Time_var.set("")
        self.Exit_Time_var.set("")
    
    def get_cursor(self,ev):
        cursor_row=self.customer_Table.focus()
        contents=self.customer_Table.item(cursor_row)
        row=contents['values']
        self.ID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Mobile_no_var.set(row[2])
        self.Vehicle_No_var.set(row[3])
        self.Vehicle_Type_var.set(row[4])
        self.Entry_Time_var.set(row[5])
        self.Exit_Time_var.set(row[6])
    def manage_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur=con.cursor()
        cur.execute("update customers set Name=%s,Mobile_no=%s,Vehicle_No=%s,Vehicle_Type=%s,Entry_Time=%s,Exit_Time=%s where ID=%s",(
                                                                                                                                      self.Name_var.get(),
                                                                                                                                      self.Mobile_no_var.get(),
                                                                                                                                      self.Vehicle_No_var.get(),
                                                                                                                                      self.Vehicle_Type_var.get(),
                                                                                                                                      self.Entry_Time_var.get(),
                                                                                                                                      self.Exit_Time_var.get(),
                                                                                                                                      self.ID_var.get()
                                                                                                                                       ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def Delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur=con.cursor()
        cur.execute("delete from customers where ID=%s",self.ID_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        

    def current_time(self):
        self.Exit_Time_var.set(today)
        return
    def current_time2(self):
        self.Entry_Time_var.set(entrytime)
        return
        
    
    
    
    def new_Window(self):
        self.newWindow=Toplevel(self.root)
        self.app=Window2(self.newWindow)
class Window2:
    def __init__(self,root):
        self.root=root
        self.root.maxsize(500,300)
        self.root.minsize(350,250)
        self.root.title("Recipt")
        
        fm = Frame(self.root, width=300, height=100, bg="white")
        fm.pack(side=TOP, expand=NO, fill=BOTH)
        text1=Label(fm,text="PMS Reciept",font=("Verdana",22),relief=GROOVE,border=0,bg="white")
        text1.pack()
        fm1 = Frame(self.root, width=300, height=25, bg="white")
        fm1.pack(side=TOP, expand=NO, fill=BOTH)
        fm2 = Frame(self.root, width=300, height=250, bg="white")
        fm2.pack(side=TOP, expand=NO, fill=BOTH)
        fm4 = Frame(self.root, width=300, height=25, bg="white")
        fm4.pack(side=TOP, expand=NO, fill=BOTH)
        fm3 = Frame(self.root, width=300, height=100, bg="white")
        fm3.pack(side=TOP, expand=NO, fill=BOTH)
        fm5 = Frame(self.root, width=300, height=100, bg="white")
        fm5.pack(side=TOP, expand=TRUE, fill=BOTH)
#name label
        name_label=Label(fm2,text="Name : ",font=("Verdana",20),relief=GROOVE,border=0,bg="white")
        name_label.grid(row=0,column=0,sticky=W)
        v_label=Label(fm2,text="V.type : ",font=("Verdana",20),relief=GROOVE,border=0,bg="white")
        v_label.grid(row=1,column=0,sticky=W)
        vno_label=Label(fm2,text="V.No : ",font=("Verdana",20),relief=GROOVE,border=0,bg="white")
        vno_label.grid(row=2,column=0,sticky=W)
        vno2_label=Label(fm2,text="Amount : ",font=("Verdana",20),relief=GROOVE,border=0,bg="white")
        vno2_label.grid(row=3,column=0,sticky=W)
#entry box
        name_var=StringVar()
        name_entrybox=Entry(fm2,width=24,textvariable = name_var,font=("Verdana",20))
        name_entrybox.grid(row=0,column=1)
        name_entrybox.focus()
        v_var=StringVar()
        v_entrybox=Entry(fm2,width=24,textvariable = v_var,font=("Verdana",20))
        v_entrybox.grid(row=1,column=1)
        v_entrybox.focus()
        vno_var=StringVar()
        vno_entrybox=Entry(fm2,width=24,textvariable = vno_var,font=("Verdana",20))
        vno_entrybox.grid(row=2,column=1)
        vno_entrybox.focus()
        vno2_var=StringVar()
        vno2_entrybox=Entry(fm2,width=24,textvariable = vno2_var,font=("Verdana",20))
        vno2_entrybox.grid(row=3,column=1)
        vno2_entrybox.focus()
        print_button=Button(fm3,text="Print Details",bg="white",command=print)
        print_button.pack(side = RIGHT,expand=NO,fill="x")

        



        
   

        

        
        
        
root=Tk()
ob=Parking(root)
root.mainloop()