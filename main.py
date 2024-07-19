from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk 
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        
        # ===================variables===================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar() 
        z = random.randint(1000,9999)
        self.bill_no.set(z) 
        self.search_bill=StringVar()
        self.c_email=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()
        
        
        # Product Categories list
        self.Category=["select option","Clothing","LifeStyle","Mobiles"]
        
        self.SubCatClothing=["Pant","T-shirt","Shirt"]
        self.pant=["Levis","Mufti","Spykar"]
        self.price_levis=5000
        self.price_mufti=700
        self.price_spykar=8000
        
        self.T_shirt=['Polo','Roadster','Jack&Jones']
        self.price_Polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700
        
        self.Shirt=['Peter England','Louis Phillipe','Park Avenue']
        self.price_PeterEngland=2100
        self.price_LouisPhillipe=2700
        self.price_ParkAvenue=1740
        
        self.SubCatLifeStyle=["Bath Soap","Face Creame","Hair Oil"]
        self.Bath_soap=['LifeBuy','Lux','Santoor','Pearl']
        self.price_life=20
        self.price_lux=20
        self.price_santoor=20
        self.price_pearl=30
        
        self.Face_cream=['Fair&Lovely','Ponds','Olay','Garnier']
        self.price_fair=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=30
        
        self.Hair_oil=['Parachute','Jashmin','Bajaj']
        self.price_para=25
        self.price_jashmin=22
        self.price_bajaj=30
        
        self.SubCatMobiles=["iPhone","Samsung","Xiome","RealMe","One+"]
        self.Iphone=['Iphone_x','Iphone_11','Iphone_12']
        self.price_ix=40000
        self.price_i11=60000
        self.price_i12=85000
        
        self.Samsung=['Sumsung M16','Sumsung M12','Sumsung M21']
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000
        
        self.Xiome=['Red11','Redme-12','RedmePro']
        self.price_r11=11000
        self.price_r12=12000
        self.price_rpro=9000
        
        self.RealMe=['RealMe 12','RealMe 13','RealMe Pro']
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000
        
        self.OnePlus=['OnePlus1','OnePlus2','OnePlus3']
        self.price_o1=45000
        self.price_o2=60000
        self.price_o3=45800
        
        
        
        
        # image1
        img = Image.open("image/b1.webp")
        img = img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        lb1_img = Label(self.root,image=self.photoimg)
        lb1_img.place(x=500,y=0,width=500,height=130)
        
        
        #  image2
        img_1 = Image.open("image/b1.webp")
        img_1 = img_1.resize((500,130),Image.LANCZOS)
        self.photoimg_1=ImageTk.PhotoImage(img_1)
        
        lb2_img = Label(self.root,image=self.photoimg_1)
        lb2_img.place(x=1000,y=0,width=500,height=130)
        
        
        # image3
        img_2 = Image.open("image/b1.webp")
        img_2 = img_2.resize((500,130),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
        
        lb3_img = Label(self.root,image=self.photoimg_2)
        lb3_img.place(x=0,y=0,width=500,height=130)
        
        
        # title
        lb1_title = Label(self.root,text="BILLING SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        lb1_title.place(x=0,y=130,width=1530,height=45)
        
        
        def time():
            string = strftime('%H:%M:%S %p')
            lb1.config(text=string)
            lb1.after(1000,time)
        
        lb1=Label(lb1_title,font=('times new roman',16,'bold'),background='white',foreground="red")
        lb1.place(x=0,y=(-15),width=120,height=50)
        time()
        
        Main_Frame = Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
        
        
        
        # Customer LabelFrame
        Cust_Frame = LabelFrame(Main_Frame, text="Customer", font=("times new roman", 12, "bold"), bg="white", fg="red")
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        # Mobile No. Label and Entry
        self.lbl_mob = Label(Cust_Frame, text="Mobile No.", font=("arial", 12, "bold"), bg="white")
        self.lbl_mob.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame,textvariable=self.c_phone ,font=("times new roman", 10, "bold"), width=24)
        self.entry_mob.grid(row=0, column=1, padx=5, pady=2)

        # Customer Name Label and Entry
        self.lblCustName = Label(Cust_Frame, text="Customer Name", font=("arial", 12, "bold"), bg="white")
        self.lblCustName.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame, textvariable=self.c_name,font=("times new roman", 10, "bold"), width=24)
        self.txtCustName.grid(row=1, column=1, padx=5, pady=2)

        # Email Label and Entry
        self.lblEmail = Label(Cust_Frame, text="Email", font=("arial", 12, "bold"), bg="white")
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame,textvariable=self.c_email, font=("times new roman", 10, "bold"), width=24)
        self.txtEmail.grid(row=2, column=1, padx=5, pady=2)
        
        
        # # Product LabelFrame
        Product_Frame = LabelFrame(Main_Frame,text="Product",font=("times new roman",12,"bold"),bg="white",fg="red")
        Product_Frame.place(x=370,y=5,width=620,height=140)
        
        # Category
        self.lblCategory = Label(Product_Frame, text="Select Categories", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=("arial", 10, "bold"),width=24,state="readonly")
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0,column=1,sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)
        
        
        # Subcategory
        self.lblSubCategory = Label(Product_Frame, text="Sub Category", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame,value=[""],font=("arial", 10, "bold"),width=24,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W, padx=5, pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.Product_add)
        
        # Product name
        self.lblproduct = Label(Product_Frame, text="Product Name", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblproduct.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=("arial", 10, "bold"),width=24,state="readonly")
        self.ComboProduct.grid(row=2,column=1,sticky=W, padx=5, pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)
        
        # Price
        self.lblPrice = Label(Product_Frame, text="Price", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblPrice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.ComboPrice=ttk.Combobox(Product_Frame,textvariable=self.prices,font=("arial", 10, "bold"),width=24,state="readonly")
        self.ComboPrice.grid(row=0,column=3,sticky=W, padx=5, pady=2)
        
        
        # Quantity
        self.lblQty = Label(Product_Frame, text="Qty", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblQty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=("arial", 10, "bold"),width=26)
        self.ComboQty.grid(row=1,column=3,sticky=W, padx=5, pady=2)
        
        
        
        # Middle Frame
        
        Middle_Frame=Frame(Main_Frame,bd=10)
        Middle_Frame.place(x=10,y=150,width=980,height=340)
        
        # image1
        img4 = Image.open("image/a1.jpg")
        img4 = img4.resize((490,340),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lb1_img4 = Label(Middle_Frame,image=self.photoimg4)
        lb1_img4.place(x=0,y=0,width=490,height=340)
        
        
        #  image2
        img_5 = Image.open("image/a1.jpg")
        img_5 = img_5.resize((490,340),Image.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)
        
        lb2_im5 = Label(Middle_Frame,image=self.photoimg_5)
        lb2_im5.place(x=490,y=0,width=490,height=340)
        
        
        # Search
        Search_Frame=Frame(Main_Frame,bd=2,bg="white")
        Search_Frame.place(x=1020,y=10,width=500,height=40)
        
        self.lblBill = Label(Search_Frame, text="Bill Number", font=("arial", 12, "bold"), bg="red",fg="white",bd=4)
        self.lblBill.grid(row=0, column=0, sticky=W, padx=1)
        
        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=("arial", 12, "bold"),width=24)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=5,pady=2)
        
        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=("arial",10,"bold"),bg="red",fg="white",width=14,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)

        # Right frame bill area
        # Right LabelFrame
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=1000,y=45,width=480,height=440)
        
        
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        
        
        # Bill Counter LabelFrame
        
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)
        
        self.lblSubTotal = Label(Bottom_Frame, text="Sub Total", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblSubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=("arial", 10, "bold"),width=26)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W, padx=5, pady=2)
        
        
        self.lbl_tax = Label(Bottom_Frame, text="Gov. Tax", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=("arial", 10, "bold"),width=26)
        self.txt_tax.grid(row=1,column=1,sticky=W, padx=5, pady=2)
        
        
        self.lblAmountTotal = Label(Bottom_Frame, text="Total", font=("arial", 12, "bold"), bg="white",bd=4)
        self.lblAmountTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=("arial", 10, "bold"),width=26)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W, padx=5, pady=2)
        
        
        # Button Frame
        
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)
        
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,text="Add To Cart",font=("arial",12,"bold"),bg="orangered",fg="white",width=14,height=3,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)
        
        self.BtnGenerate_Bill=Button(Btn_Frame,command=self.gen_bill,text="Generate Bill",font=("arial",12,"bold"),bg="orangered",fg="white",width=14,height=3,cursor="hand2")
        self.BtnGenerate_Bill.grid(row=0,column=1)
        
        self.BtnSave=Button(Btn_Frame,text="Save",command=self.save_bill,font=("arial",12,"bold"),bg="orangered",fg="white",width=14,height=3,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)
        
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,text="Print",font=("arial",12,"bold"),bg="orangered",fg="white",width=14,height=3,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)
        
        self.BtnClear=Button(Btn_Frame,command=self.clear,text="Clear",font=("arial",12,"bold"),bg="orangered",fg="white",width=14,height=3,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)
        
        self.BtnExit=Button(Btn_Frame,text="Exit",command=self.root.destroy,font=("arial",12,"bold"),bg="orangered",fg="white",width=14,height=3,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()
        
        
        self.l=[]
    # ====================Function Declaration=======================
    
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t\t Welcome to Punam's Mini MALL")
        self.textarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email : {self.c_email.get()}")
        
        self.textarea.insert(END,"\n==================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQty\t\tPrice")
        self.textarea.insert(END,"\n==================================================\n")
        
    
    
        
    def AddItem(self):
        Tax=1
        self.n = self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product Name")
        else :
            self.textarea.insert(END,f"\n  {self.product.get()}\t\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))            
            
    
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,"\n==================================================")
            self.textarea.insert(END,f"\n Sub Amount : \t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount : \t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount : \t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n==================================================")
            
            
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+"txt",'w')
            f1.write(self.bill_data)
            f1.close()
            
            
    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,'print')
        
    
    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}",'r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
            
        if found=="no":
            messagebox.showerror('Error',"Invalid Bill No.")
                
    
    def clear(self):
        self.textarea.delete(1.0, END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        self.bill_no.set("")
        z = random.randint(1000, 9999)
        self.bill_no.set(z)
        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(0)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set("")
        self.total.set("")
        self.welcome()
        
        
        
        
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)
            
        if self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)
            
            
    def Product_add(self,event=""):
        if self.ComboSubCategory.get()=="Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="T-shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)
        
        # LifeStyle
        if self.ComboSubCategory.get()=="Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Face Creame":
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)
    

        # Mobiles
        if self.ComboSubCategory.get()=="iPhone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="Xiome":
            self.ComboProduct.config(value=self.Xiome)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)
            
        if self.ComboSubCategory.get()=="One+":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)
            
        
        
    def price(self,event=""):
        
        # pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Spykar":
            self.ComboPrice.config(value=self.price_spykar)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # T-shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_Polo)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # Shirt
        
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_PeterEngland)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_LouisPhillipe)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_ParkAvenue)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        
        # Lifestyle
        
        # Bath Soap
        if self.ComboProduct.get()=="LifeBuy":
            self.ComboPrice.config(value=self.price_life)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Pearl":
            self.ComboPrice.config(value=self.price_pearl)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # Face cream
        
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # Hair Oil
        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Jashmin":
            self.ComboPrice.config(value=self.price_jashmin)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)
            

        # Mobiles
        
        # iPhone
        if self.ComboProduct.get()=="Iphone_x":
            self.ComboPrice.config(value=self.price_ix)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Iphone_11":
            self.ComboPrice.config(value=self.price_i11)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Iphone_12":
            self.ComboPrice.config(value=self.price_i12)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # Samsung
        if self.ComboProduct.get()=="Sumsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Sumsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="Sumsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        # Xiome
        if self.ComboProduct.get()=="Red11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Redme-12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="RedmePro":
            self.ComboPrice.config(value=self.price_rpro)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        
        
        # RealMe
        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
            
        # One+
        if self.ComboProduct.get()=="OnePlus1":
            self.ComboPrice.config(value=self.price_o1)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="OnePlus2":
            self.ComboPrice.config(value=self.price_o2)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        if self.ComboProduct.get()=="OnePlus3":
            self.ComboPrice.config(value=self.price_o3)
            self.ComboPrice.current(0)
            self.qty.set(1)
            
        
        
        
            
        
            
            

if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()
    
