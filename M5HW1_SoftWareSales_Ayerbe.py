#CTI-110
#M5HW1 - Software Sales
#Guillermo Ayerbe
#11-20-2017

def main():

    packagePrice = 99
    

    quantity = float(input('How many packages would you like to purchase? '))

    if quantity >= 10 and quantity <= 19:
        print('Your discount is 10%. ')
        discountAmount1 = (quantity * 99) * .10
        print('Your discounted amount is',discountAmount1)
        print('Your total is',(quantity * 99) - discountAmount1)

    elif quantity >= 20 and quantity <= 49:
        print('Your discount is 20%. ')
        discountAmount2 = (quantity * 99) * .20
        print('Your discounted amount is',discountAmount2)
        print('Your total is',(quantity * 99) - discountAmount2)

    elif quantity >= 50 and quantity <= 99:
        print('Your discount is 30%. ')
        discountAmount3 = (quantity * 99) * .30
        print('Your discounted amount is',discountAmount3)
        print('Your total is',(quantity * 99) - discountAmount3)

    elif quantity >= 100:
        print('Your discount 40%. ')
        discountAmount4 = (quantity * 99) * .40
        print('Your discounted amount is',discountAmount4)
        print('Your total is',(quantity * 99) - discountAmount4)
    
        


main()

    
