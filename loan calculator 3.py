from tkinter import * # Import tkinter
    
class LoanCalculator:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Glamping World Application") # Set title of a window
        
        tkvar = StringVar(window)
        products = ('Excursion 1', 'Excursion 2', 'Excursion 3', 'T-Shirt', 'Bug Spray')
        tkvar.set('Excursion 1')

        #set up labels for the loan calculator in the left column of the window, align labels left (Sticky=W)
        Label(window, text = "Product Name").grid(row = 1, column = 1, sticky = W)                     
        Label(window, text = "Price").grid(row = 2, column = 1, sticky = W)
        Label(window, text = "Quantity").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Subtotal ($)").grid(row = 5, column = 1, sticky = W)
        Label(window, text = "Discount (%)").grid(row = 4, column = 1, sticky = W)
        Label(window, text = "Sales Tax").grid(row = 6, column = 1, sticky = W)
        Label(window, text = "Grand Total ($)").grid(row = 8, column = 1, sticky = W)
        
        # set up the input area for the calculator in the right column, using Entry for textboxes and assigning the values entered to variables
        OptionMenu(window, tkvar, *products).grid(row = 1, column = 2)
        self.price = StringVar()
        Entry(window, textvariable = self.price,justify = RIGHT).grid(row = 2, column = 2)
        self.quantity = StringVar()
        Entry(window, textvariable = self.quantity, justify = RIGHT).grid(row = 3, column = 2)
        self.discount = StringVar()
        Entry(window, textvariable = self.discount, justify = RIGHT).grid(row = 4, column = 2)
        self.subtotal = StringVar()
        Label(window, textvariable = self.subtotal, justify = RIGHT).grid(row = 5, column = 2)

        #set up the output area for the calculator below the input area, using two labels and a button; the button calls the function computePayment when it's clicked
        self.salestax = StringVar()
        Label(window, textvariable = self.salestax).grid(row = 6, column = 2, sticky = E)
        self.grandtotal = StringVar()
        Label(window, textvariable = self.grandtotal).grid(row = 8, column = 2, sticky = E)
        Button(window, text = "Compute Payment", command = self.computePayment).grid(row = 10, column = 2, sticky = E)
        
        window.mainloop() # Create an event loop to display the window

    # function computePayment calls the getMonthlyPayment function with arguments assigned the values from the user
    def computePayment(self):
        subtotal = self.getsubtotal(float(self.price.get()), int(self.quantity.get()), int(self.discount.get()))
        grandtotal = float(self.subtotal.get()) + float(self.salestax.get())
        self.grandtotal.set(format(grandtotal, '10.2f'))   #output totalPayment formatted to two decimal places in the totalPaymentVar
        
    #calculate subtotal using  the formula provided    
    def getsubtotal(self, price, quantity, discount):
        discount = discount / 100
        subtotal_amt = price * quantity * (1 - discount)
        tax_amt = subtotal_amt * .13
        self.salestax.set(format(tax_amt, '10.2f')) 
        self.subtotal.set(format(subtotal_amt, '10.2f'))
        return subtotal_amt

LoanCalculator()  # Create GUI 
