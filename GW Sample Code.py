import tkinter as Tk
 
########################################################################
class MyApp(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title('Glamping World Ordering App')
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        self.root.geometry('700x300')
        title = Tk.Label(self.frame, text = 'Glamping World Customer\nOrder Processing Application', bd = 1, relief = 'solid', font = ('Arial Bold', 20), padx = 50, pady = 15, justify = 'center').pack(pady = 10) #FIXME: Change font & center on page
        start = Tk.Button(self.frame, text="Start Order", activebackground = 'green', command=self.newCust, padx = 5, pady = 3).pack(pady = 20)

    #----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()
 
    #----------------------------------------------------------------------
    def newCust(self):
        """"""
        self.hide()
        otherFrame = Tk.Tk()
        otherFrame.geometry("600x500")
        otherFrame.title("Welcome to Glamping World!")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        back_btn = Tk.Button(otherFrame, text="Back", command=handler, padx = 25, pady = 5).place(relx = 0.01, rely = 0.06)
        help_btn = Tk.Button(otherFrame, text = "Help", pady = 5, padx = 25).place(relx = 0.85, rely = 0.06)

        date_time = Tk.Label(otherFrame, text = 'Date 12/12/9999    Time 24:24').pack(anchor = 'e', padx = 5)

        title = Tk.Label(otherFrame, text = 'Customer Information', bd = 1, relief = 'solid', font = ('Arial Bold', 20), padx = 50, pady = 15, justify = 'center').pack(pady = 50)
        
        f_name = Tk.Label(otherFrame, text = 'First Name:').pack(pady = 10)
        f_name_entry = Tk.Entry(otherFrame).pack()
        l_name = Tk.Label(otherFrame, text = 'Last Name:').pack(pady = 10)
        l_name_entry = Tk.Entry(otherFrame).pack()
        phone = Tk.Label(otherFrame, text = 'Phone:').pack(pady = 10)
        phone_entry = Tk.Entry(otherFrame).pack()
        next_btn = Tk.Button(otherFrame, text = 'Next', pady = 5, padx = 10, command = self.productOrder).pack(padx = 10)
        
    #----------------------------------------------------------------------
    def productOrder(self):
        """"""
        self.hide()
        otherFrame = Tk.Tk()
        otherFrame.geometry("800x800")
        otherFrame.title("Welcome to Glamping World!")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        back_btn = Tk.Button(otherFrame, text="Back", command=handler, padx = 25, pady = 5).place(relx = 0.01, rely = 0.08)
        help_btn = Tk.Button(otherFrame, text = "Help", pady = 5, padx = 25).place(relx = 0.85, rely = 0.08)
        date_time = Tk.Label(otherFrame, text = 'Date 12/12/9999    Time 24:24').place(relx = 0.78, rely = 0.02)

        title = Tk.Label(otherFrame, text = 'Product Information', bd = 1, relief = 'solid', font = ('Arial Bold', 20), padx = 50, pady = 15, justify = 'center').pack(pady = 50)
        
        tkvar = StringVar(otherFrame)
        products = ('Excursion 1', 'Excursion 2', 'Excursion 3', 'T-Shirt', 'Bug Spray')
        tkvar.set('Excursion 1')

        #set up labels for the loan calculator in the left column of the window, align labels left (Sticky=W)
        Label(otherFrame, text = "Product Name").grid(row = 1, column = 1, sticky = W)                     
        Label(otherFrame, text = "Price").grid(row = 2, column = 1, sticky = W)
        Label(otherFrame, text = "Quantity").grid(row = 3, column = 1, sticky = W)
        Label(otherFrame, text = "Subtotal ($)").grid(row = 5, column = 1, sticky = W)
        Label(otherFrame, text = "Discount (%)").grid(row = 4, column = 1, sticky = W)
        Label(otherFrame, text = "Sales Tax").grid(row = 6, column = 1, sticky = W)
        Label(otherFrame, text = "Grand Total ($)").grid(row = 8, column = 1, sticky = W)
        
        # set up the input area for the calculator in the right column, using Entry for textboxes and assigning the values entered to variables
        OptionMenu(otherFrame, tkvar, *products).grid(row = 1, column = 2)
        self.price = StringVar()
        Entry(otherFrame, textvariable = self.price,justify = RIGHT).grid(row = 2, column = 2)
        self.quantity = StringVar()
        Entry(otherFrame, textvariable = self.quantity, justify = RIGHT).grid(row = 3, column = 2)
        self.discount = StringVar()
        Entry(otherFrame, textvariable = self.discount, justify = RIGHT).grid(row = 4, column = 2)
        self.subtotal = StringVar()
        Label(otherFrame, textvariable = self.subtotal, justify = RIGHT).grid(row = 5, column = 2)

        #set up the output area for the calculator below the input area, using two labels and a button; the button calls the function computePayment when it's clicked
        self.salestax = StringVar()
        Label(otherFrame, textvariable = self.salestax).grid(row = 6, column = 2, sticky = E)
        self.grandtotal = StringVar()
        Label(otherFrame, textvariable = self.grandtotal).grid(row = 8, column = 2, sticky = E)
        Button(otherFrame, text = "Compute Payment", command = self.computePayment).grid(row = 10, column = 2, sticky = E)
        next_btn = Tk.Button(otherFrame, text = 'Next', pady = 5, padx = 25, command = self.productPage).pack(side = 'right')
              

    def computePayment(self):
        subtotal = self.getsubtotal(float(self.price.get()), int(self.quantity.get()))
        discount = self.getdiscount(float(subtotal), float(self.discount.get()))
        grandtotal = self.gettaxes(float(discount), float(self.salestax.get()))
        self.grandtotal.set(format(grandtotal, '10.2f'))   #output totalPayment formatted to two decimal places in the totalPaymentVar
        
    #calculate subtotal using  the formula provided    
    def getsubtotal(self, price, quantity):
        subtotal_amt = price * quantity
        self.subtotal.set(format(subtotal_amt, '10.2f'))
        return subtotal_amt

    def getdiscount(self, subtotal, discount):
        discount /= 100
        return (subtotal + (subtotal * discount))

    def gettaxes(self, discountedprice, taxes):
        tax = subtotal * taxes
        self.salestax.set(format(tax), '10.2f') 
        return (discountedprice + (discountedprice * taxes))
    
    #----------------------------------------------------------------------
    
    def confirm(self):
        self.hide()
        otherFrame = Tk.Tk()
        otherFrame.geometry('600x400')
        otherFrame.title('Glamping World Ordering App')
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        back_btn = Tk.Button(otherFrame, text="Back", command=handler, padx = 25, pady = 5).place(relx = 0.01, rely = 0.08)
        date_time = Tk.Label(otherFrame, text = 'Date 12/12/9999    Time 24:24').pack(anchor = 'e', padx = 5)
        title = Tk.Label(otherFrame, text = 'Order Confirmation', bd = 1, relief = 'solid', font = ('Arial Bold', 20), padx = 50, pady = 15, justify = 'center').place(relx = .2, rely = 0.2)

        item1 = Tk.Label(otherFrame, text = 'GET ITEM INFO').place(relx = 0.05, rely = 0.4)
        item1_entry = Tk.Label(otherFrame, text = '$99.99').place(relx = 0.3, rely = 0.4)
        item2 = Tk.Label(otherFrame, text = 'GET ITEM INFO').place(relx = 0.05, rely = 0.5)
        item2_entry = Tk.Label(otherFrame, text = '$99.99').place(relx = 0.3, rely = 0.5)
        item3 = Tk.Label(otherFrame, text = 'GET ITEM INFO').place(relx = 0.05, rely = 0.6)
        item3_entry = Tk.Label(otherFrame, text = '$99.99').place(relx = 0.3, rely = 0.6)

        promo = Tk.Label(otherFrame, text = 'Promo Code: ').place(relx = 0.6, rely = 0.4)
        promo_entry = Tk.Entry(otherFrame).place(relx = 0.73, rely = 0.4)
        apply = Tk.Button(otherFrame, text = 'Apply', pady = 2, padx = 5).place(relx = 0.85, rely = 0.45)

        subtotal = Tk.Label(otherFrame, text = 'Order Subtotal: ').place(relx = 0.6, rely = 0.55)
        subtotal_field = Tk.Label(otherFrame, text = '$99.99').place(relx = 0.77, rely = 0.55) 
        tax = Tk.Label(otherFrame, text = 'Sales Tax: ').place(relx = 0.6, rely = 0.6)
        tax_field = Tk.Label(otherFrame, text = '13%').place(relx = 0.77, rely = 0.6) 
        ship_cost = Tk.Label(otherFrame, text = 'Shipping: ').place(relx = 0.6, rely = 0.65)
        ship_cost_field = Tk.Label(otherFrame, text = '$9.99').place(relx = 0.77, rely = 0.65) 

        grand_total = Tk.Label(otherFrame, text = 'Grand Total: $99.99').place(relx = 0.6, rely = 0.77)
        submit_btn = Tk.Button(otherFrame, text = 'Submit', bg = 'light yellow', pady = 5, padx = 25, command = self.submission).place(relx = 0.82, rely = 0.9) #FIXME: Insert 'Exit' command
        help_btn = Tk.Button(otherFrame, text = "Help", pady = 5, padx = 25).place(relx = 0.01, rely = 0.9)

    #----------------------------------------------------------------------
    def submission(self):
        """"""
        self.hide()
        otherFrame = Tk.Tk()
        otherFrame.geometry("700x300")
        otherFrame.title("Glamping World Ordering App")
        handler = lambda: self.onCloseOtherFrame(otherFrame)
        title = Tk.Label(otherFrame, text = 'Order #999999\n Successfully Submitted', bd = 1, relief = 'solid', font = ('Arial Bold', 20), padx = 50, pady = 15, justify = 'center').pack(pady = 10) #FIXME: Change font & center on page
        new = Tk.Button(otherFrame, text = "Submit a New Order", activebackground = 'green', command = handler, padx = 5, pady = 3).pack(pady = 20)
        help_btn = Tk.Button(otherFrame, text="Help", pady = 5, padx = 25).place(relx = 0.0, rely = 0.85)

    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()

    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()