import mysql.connector
import mysql.connector
import sys
from tabulate import tabulate
try:
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'hoteldb')

except mysql.connector.Error as e:

    sys.exit('connection failure')
    mycursor = mydb.cursor()
l = []
while True:
    print('''
        Item contain in the hotel
        1 .coffee
        2 .Tea
        3 .Chips
        4 .Biscuit
        5 .Chocolate
        6 .Billing
        7 .view all transaction
        8 .Day wise transaction summary
        9 .transaction summary for a period
        10 .Exit
    ''')
    choice = int(input('Enter the item you need from the display part : '))
    
    if(choice == 1):
        print('You had selected coffee')
        price = 15
        qua = int(input('Enter the quantity you need : '))
        total_price = price * qua
        l.append(total_price)
    elif(choice==2):
        print("added coffee")
    elif(choice==3):
        print("added buger")
    elif(choice==4):
        print("added sandwich")
    elif(choice==5):
        print("added alpham")
    elif(choice==6):
        print("generating bill")
    elif(choice==7):
        exit