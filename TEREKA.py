
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import tkinter.filedialog
import datetime
from backend import datacon
from sqlalchemy.orm import sessionmaker



# tkinter.filedialog.asksaveasfilename()
# tkinter.filedialog.asksaveasfile()
# tkinter.filedialog.askopenfilename()
# tkinter.filedialog.askopenfile()
# tkinter.filedialog.askdirectory()
# tkinter.filedialog.askopenfilenames()
# tkinter.filedialog.askopenfiles()

class root(Tk):
    def __init__(self):
        super(root, self).__init__()


        self.ntbook()
        self.topmen()
        self.sales_ui()
        self.shopmmangement()





    def saveCommodity(self):
        try:
            self.haha = datacon()
            self.haha.reg_new_commodity(self.com_name.get(),self.com_who_price.get(),
                                        self.com_unit_price.get(),
                                        self.com_quantity.get(),
                                        self.com_sup_contact.get())
            messagebox.showinfo("Views method", f"{self.com_name.get()} successfully saved")
            self.com_name.delete(0,END)
            self.com_who_price.delete(0,END)
            self.com_unit_price.delete(0,END)
            self.com_quantity.delete(0,END)
            self.com_sup_contact.delete(0,END)

        except:
            messagebox.showerror("error 404", "failed to connect to database")

    def saveuser(self):
        try:
            self.haha = datacon()
            self.haha.reg_new_commodity(self.com_name.get(), self.com_who_price.get(),
                                        self.com_unit_price.get(),
                                        self.com_quantity.get(),
                                        self.com_sup_contact.get())
            messagebox.showinfo("Views method", f"{self.com_name.get()} successfully saved")
            # self.com_sup_contact.delete(0, END)

        except:
            messagebox.showerror("error 404", "failed to connect to database")

    def kanso(self):
            messagebox.askokcancel("Cancle", "are you sure you wa")

    def item_selected(self):
        for self.selected_item in self.fees_t.selection():
            self.item = self.fees_t.item(self.selected_item)
            self.record = self.item['values']
            # show a message
            self.messagebox.showinfo(title='Information', message=','.join(self.record))

    def donothing(self):
        messagebox.showinfo("dev notes",
                            "Application still under development,please contact developer j0nahwalakira650@gmail.com to have feature activated")

    def donothing1(self):
        self.filewin = Toplevel(self)
        self.button = Button(self.filewin, text="Do nothing button")
        self.button.pack()
    def check_price(self):
        messagebox.showinfo("pricing","the price checking method")

    def new_commodity(self):
        self.main1 = Toplevel(self)

        self.a = Label(self.main1, text="Commodity Name")
        self.a.place(relheight=0.1, relwidth=0.3, relx=0, rely=0)
        self.b = Label(self.main1, text="Whole_sale_price:")
        self.b.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.1)
        self.c = Label(self.main1, text="Unit_price:")
        self.c.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.2)
        self.d = Label(self.main1, text="Quantity")
        self.d.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.3)
        self.dd1 = Label(self.main1, text="supplier_contact")
        self.dd1.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.4)
        self.dt = Label(self.main1, text="Date")
        self.dt.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.5)
        self.mnth = Entry(self.main1)
        self.mnth.place(relheight=0.08, relwidth=0.2, relx=0.32, rely=0.5)
        self.yr = Entry(self.main1)
        self.yr.place(relheight=0.08, relwidth=0.2, relx=0.53, rely=0.5)
        self.dy = Entry(self.main1)
        self.dy.place(relheight=0.08, relwidth=0.2, relx=0.74, rely=0.5)
        self.com_name = Entry(self.main1)
        self.com_name.place(relheight=0.08, relwidth=0.6, relx=0.32, rely=0)
        self.com_who_price = Entry(self.main1)
        self.com_who_price .place(relheight=0.08, relwidth=0.6, relx=0.32, rely=0.1)
        self.com_unit_price = Entry(self.main1)
        self.com_unit_price.place(relheight=0.08, relwidth=0.6, relx=0.32, rely=0.2)
        self.com_quantity = Entry(self.main1)
        self.com_quantity.place(relheight=0.08, relwidth=0.6, relx=0.32, rely=0.3)
        self.com_sup_contact = Entry(self.main1)
        self.com_sup_contact .place(relheight=0.08, relwidth=0.6, relx=0.32, rely=0.4)
        self.dat = Label(self.main1, text='now')
        self.dat.place(relheight=0.1, relwidth=0.3, relx=0.32, rely=0.6)
        self.savebutton = Button(self.main1, text="Save", command=lambda: self.saveCommodity())
        self.savebutton.place(relheight=0.15, relwidth=0.2, relx=0.32, rely=0.7)
        self.canclebutton = Button(self.main1, text="Cancle", command=self.kanso)
        self.canclebutton.place(relheight=0.15, relwidth=0.2, relx=0.54, rely=0.7)

    def new_user(self):
        self.main1 = Toplevel(self)
        self.a = Label(self.main1, text="First Name")
        self.a.place(relheight=0.1, relwidth=0.3, relx=0, rely=0)
        self.b = Label(self.main1, text="Last Name")
        self.b.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.1)
        self.c = Label(self.main1, text="Email Id")
        self.c.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.2)
        self.d = Label(self.main1, text="Contact Number")
        self.d.place(relheight=0.1, relwidth=0.3, relx=0, rely=0.3)
        self.a1 = Entry(self.main1)
        self.a1.place(relheight=0.15, relwidth=0.6, relx=0.32, rely=0)
        self.b1 = Entry(self.main1)
        self.b1.place(relheight=0.15, relwidth=0.6, relx=0.32, rely=0.1)
        self.c1 = Entry(self.main1)
        self.c1.place(relheight=0.15, relwidth=0.6, relx=0.32, rely=0.2)
        self.d1 = Entry(self.main1)
        self.d1.place(relheight=0.15, relwidth=0.6, relx=0.32, rely=0.3)
        self.savebutton = Button(self.main1, text="Save User", command=lambda :self.saveuser())
        self.savebutton.place(relheight=0.15, relwidth=0.2, relx=0.32, rely=0.5)
        self.canclebutton2 = Button(self.main1, text="Cancle", command=self.kanso)
        self.canclebutton2.place(relheight=0.15, relwidth=0.2, relx=0.54, rely=0.5)
    def topmen(self):
        self.title("Davinci shop  uganda  0753049317 jonahwalakira650@gmail.com")
        # self.bgimg1 = PhotoImage(file="backimage.png")
        # self.bglb1 = Label(self.frame, image=self.bgimg1)
        # self.bglb1.place(relwidth=1, relheight=1)
        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New Commodity", command=self.new_commodity)
        self.filemenu.add_command(label="New_User", command=self.new_user)
        self.filemenu.add_command(label="Close", command=self.donothing)

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="NEW", menu=self.filemenu)
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.donothing)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help Index", command=self.donothing)
        self.helpmenu.add_command(label="About...", command=self.donothing)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=self.menubar)
    def ntbook(self):
        self.notebook1 = ttk.Notebook(self)
        self.ff = Frame(self.notebook1)
        self.notebook1.add(self.ff, text="Billing")
        # imagelb = Label(ff, image=PhotoImage("images.png")).place(relheight=1, relwidth=1)
        self.fx = Frame(self.notebook1)
        self.notebook1.add(self.fx, text="Manage_stock")
        self.notebook1.place(relheight=1, relwidth=1)



    def sales_ui(self):
        self.topframe = Frame(self.ff).place(relheight=0.25, relwidth=0.9, relx=0.05)
        self.itemnameLb = Label(self.ff, text="Item Name ").place(relheight=0.08, relwidth=0.2, relx=0.1)
        self.example = ttk.Combobox(self.ff,
                               values=[
                                   "tingting",
                                   "big_bans",
                                   "bans",
                                   "football"],
                               postcommand=self.check_price)
        self.example['state'] = "normal"
        self.example.place(relheight=0.1, relwidth=0.6, relx=0.35)

        self.quantityLb = Label(self.ff, text=" Quantity ").place(relheight=0.08, relwidth=0.2, rely=0.1, relx=0.1)
        self.w = Spinbox(self.ff, from_=0, to=1240)
        self.w.place(relheight=0.08, relwidth=0.15, rely=0.1, relx=0.35)
        self.Unit_priceLb = Label(self.ff, text=" Unit price/= ").place(relheight=0.1, relwidth=0.15,
                                                              rely=0.1, relx=0.55)
        self.Add_to_bill_button = Button(self.ff, text="Add to Bill").place(relheight=0.1, relwidth=0.15,
                                                                  rely=0.1, relx=0.75)

        self.billfram = Frame(self.ff)
        self.billfram.place(relwidth=0.5, relheight=0.5, rely=0.3, relx=0.05)
        self.d = Label(self.ff, text="Client_id").place(relheight=0.08, relwidth=0.1, relx=00.07, rely=0.35)
        self.a1 = Entry(self.ff).place(relheight=0.08, relwidth=0.3, relx=0.2, rely=0.35)
        self.d = Label(self.ff, text="Payment-mode").place(relheight=0.08, relwidth=0.1, relx=00.07, rely=0.45)
        self.payi = ttk.Combobox(self.ff,
                            values=[
                                "Cash",
                                "Debt",
                            ],

                            )
        self. payi['state'] = "readonly"
        self. payi.place(relheight=0.08, relwidth=0.15, relx=0.2, rely=0.45)
        self.removebutton1 = Button(self.ff, text="Edit bill").place(relheight=0.08, relwidth=0.1, relx=0.39, rely=0.45)

        self.amountpaidlb = Label(self.ff, text="amount paid").place(relheight=0.08, relwidth=0.1, relx=00.07, rely=0.55)
        self.a11 = Entry(self.ff).place(relheight=0.08, relwidth=0.3, relx=0.2, rely=0.55)

        self.confirmbutton = Button(self.ff, text="Confirm bill").place(relheight=0.08, relwidth=0.1, relx=0.2, rely=0.65)
        self.canclebutton = Button(self.ff, text="Refresh").place(relheight=0.08, relwidth=0.1, relx=0.38, rely=0.65)

        self.txtfd=Text(self.ff).place(relwidth=0.3, relheight=0.5, rely=0.27, relx=0.6)

    def shopmmangement(self):

        self.Detailsframe = LabelFrame(self.fx, text="Student/class Fess Details")
        self.Detailsframe.place(relheight=0.2, relwidth=0.9, relx=0.05)

        self.idlb = ttk.Label(self.Detailsframe, text="Product Name:")
        self.idlb.place(relheight=0.7, relwidth=0.1)
        self.stuentv = StringVar()
        self.stuent = ttk.Entry(self.Detailsframe, textvariable=self.stuentv)
        self.stuent.place(relheight=0.5, relwidth=0.5, rely=0.0, relx=0.15)
        self.feesbtn = ttk.Button(self.Detailsframe, text="Stock shop", command=lambda: self.donothing())
        self.feesbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0)
        self.Uniformbtn = ttk.Button(self.Detailsframe, text="New Product", command=lambda: self.new_commodity())
        self.Uniformbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.15)
        self.paperworkbtn = ttk.Button(self.Detailsframe, text="Update item stock", command=self.donothing)
        self.paperworkbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.25)

        self.Daycarebtn = ttk.Button(self.Detailsframe, text="view sales by staff", command=self.donothing)
        self.Daycarebtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.35)

        self.viewbtn = ttk.Button(self.Detailsframe, text="view item sold", command=self.donothing)
        self.viewbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.45)

        self.viewbtn2 = ttk.Button(self.Detailsframe, text="view sales", command=lambda: self.donothing1())
        self.viewbtn2.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.55)

        self.refreshbtn = ttk.Button(self.Detailsframe, text="Refresg", command=lambda: self.fill_table_content())
        self.refreshbtn.place(relheight=0.2, relwidth=0.1, rely=0.6, relx=0.75)

        self.CA = tk.StringVar()
        self.qzichoiceKombo = ttk.Combobox(self.Detailsframe, textvariable=self.CA)
        self.qzichoiceKombo['state'] = 'readonly'
        self.qzichoiceKombo['values'] = (
            'Day care', 'Babby', ' Middle', 'Top', 'P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7')
        self.qzichoiceKombo.current()
        self.qzichoiceKombo.place(relheight=0.5, relwidth=0.2, rely=0.0, relx=0.65)

        self.Registerframe = LabelFrame(self.fx, text="Class details")
        self.Registerframe.place(relheight=0.73, relwidth=0.9, relx=0.05, rely=0.23)

        self.columnsi = ('Product_id', 'Product_name', 'Buying_price', 'selling_price', 'In_Stock')
        self.fees_t = ttk.Treeview(self.Registerframe, columns=self.columnsi, show='headings')
        self.fees_t.heading('Product_id', text='Product_id')
        self.fees_t.heading('Product_name', text='Product_name')
        self.fees_t.heading('Buying_price', text='Buying_price')
        self.fees_t.heading('selling_price', text='selling_price')
        self.fees_t.heading('In_Stock', text='In_Stock')
        self.fees_t.place(relheight=1, relwidth=0.92)
        self.scrollbar = ttk.Scrollbar(self.Registerframe, orient=tk.VERTICAL, command=self.fees_t.yview)

        self.fees_t.bind('<<TreeviewSelect>>', self.item_selected)
        self.fees_t.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(relheight=1, relwidth=0.08, relx=0.92)

    #method to add tabkecontent to uer interce
    def fill_table_content(self):
        self.contacts = []
        # for n in range(1, 1000):
        #     self.contacts.append((f'{n}', f'Product_name{n}', f'{n}', f'{n}', f'{n}'))
        #     for contact in self.contacts:
        #         self.fees_t.insert('', tk.END, values=contact)
        try:
            self.dbc=datacon()
            self.tabledata=self.dbc.view_newcomt_d()
            self.fees_t.delete(*self.fees_t.get_children())
            for row in self.tabledata:
                self.contacts.append(row)
                self.fees_t.insert('', tk.END, values=row)


        except:
            messagebox.showerror("erro,","content load eeror")







z=root()
z.mainloop()
