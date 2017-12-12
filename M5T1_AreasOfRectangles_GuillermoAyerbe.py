#CTI-110
#M5T1
#Guillermo Ayerbe
#11-20-2017

def main():
    #Rectangle 1
    length1 = int(input('What is the length of your shape? '))
    width1 = int(input('What is the width of your shape? '))

    #Rectangle 2
    length2 = int(input('What is the lenth of your shape? '))
    width2 = int(input('What is the width of your shape? '))

    area1 = length1 * width1
    area2 = length2 * width2


    if area1 < area2:
        print('The area of Rectangle 2 is bigger. ')
        
    elif area2 < area1:
        print('The area of Rectangle 1 is bigger. ')
        
    elif area1 == area2:
        print('The area of the rectangles is the same. ')
        
main()
