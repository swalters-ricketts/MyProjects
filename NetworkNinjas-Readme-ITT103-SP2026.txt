Best Buy Retail Pos System 

Authors:
Best Buy Point of Sale system
Authors
Samantha Walters Ricketts
Rashaun Barnett 

Date Created 
March 2026

Course:
ITT103 Programming Techniques

GitHub Public URL:

Purpose of the program:
This program is designed to create a simulates point of sale system used in a retail environment by a cashier. The system assists the cashier in processing customers’ transactions efficiently and reduces manual labor for stock-taking.
User Input Validation
The program requires the cashier to enter a customer name, this helps the cashier to keep track of customers' orders and adds a touch of personal care to the service been offered. This also allows the program to be versatile as it can be used in different environments. If invalid inputs are entered the cashier is prompted to try again, this allows a smaller margin for human errors.

Product Catalogue Display
The system stores the products in a dictionary ,where each product has;
•	A price
•	A stock quantity
The cashier will be able to see what products are low in stock, with the “Low Stock” warning if the stock quantity of items falls below 5.

Add Items to Cart
The cashier  can add items to the shopping cart by :
•	Entering the product name 
•	Choose the quantity of the selected items
The system performs the following validation:
•	Checks if the item selected exists in the dictionary 
•	Ensures the quantity is numeric
•	Verifies that stock is available to complete the order
If checks are valid, the item/s selected is added to the cart and stock is updated accordingly 

Remove Items from Cart 
The cashier can remove any item from the cart at any time. When an item is removed:
•	It is deleted from the cart
•	The stock is restored to the product catalogue
This ensures accurate inventory tracking
View Cart 
The system allows the cashier to view all items currently in the cart .It displays:
•	Item name
•	Quantity
•	Unit price
•	Total cost per item
This helps the cashier to review the order before completing a transaction for a customer

Checkout and Billing System
When the cashier selects checkout, the system calculates:
•	Subtotal (Total cost of items in cart)
•	Discount (5% applied if subtotal exceeds $5000)
•	Tax(10% applied after discount)
•	Final total
These calculations uses real world billing practices and provides transparency to the customer.

Payment Processing 
The system allows the cashier to enter the amount the customer pays. It :
•	Validates that the input is a float /numeric 
•	Ensures that payment covers the bill total generated
•	If the payment is adequate, the system calculates that change.

Receipt Generation
After successful payment, the system generated a receipt displaying:
•	Items purchased
•	Quantities and prices
•	Subtotal 
•	Tax
•	Total amount paid
•	Change 
This works like a real retail store receipt and enhances the realism of the program.

Multi-customer Processing
The program allows the cashier to process multiple customers to be processed in one session after completing a transaction, the system ask whether to process another customer. This allows the company to easily track how many persons the cashier severed within a shift and enhances checking off and accountability for each employee.

How to Run the Program
1.	Ensure that a Python IDE(an Integrated Development Environment)  is accessible to you.
2.	Open the program file using an Integrated Development Environment such as :
Pycharm or Visual Studio Code
      3. Run the program
      4. Enter the customer name when asked to do so 
      5. Select options from the menu (1-6) to perform different actions
      6Follow on screen instructions to complete a transactions 
Required Modifications
The program can be modified to improve functionality or adapt to different business models.
Suggested modifications include:
•	Updating product prices and quantities in the dictionary 
•	Changing tax rate or discount rate
•	Adding new products to the system
•	Connecting the system to a database for permanent storage 
•	Adding customer account management feature 
Assumptions
The program runs under the following assumptions:
•	The cashier will enter the customer's name and not theirs 
•	Product names will be entered correctly 
•	Payment values will be numeric 
•	Stock levels are accurate at the start of the program
Limitations
The program runs, despite this, it has several limitations:
•	No barcode scanning or advanced retail feature
•	Data is not stored permanently
•	It is not a graphical-based interface program
•	Product name input depends on the exact spelling in the catalogue 
Conclusion
This point-of-sale system successfully shows the application of fundamental programming concepts in solving real-world problems. This system is effective in carrying out transactions, handling cashier (user) input and performing calculations accurately.
Even though the program limitation was highlighted, it proves to be a strong foundation and has the potential to be a fully developed retail management system. Recommended improvements can improve on usability, security and scalability for any business model.

 








