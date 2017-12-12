#CTI-110
#M5HW1 - Age Classifier
#Guillermo Ayerbe
#11-20-2017

def main():
    age = int(input('How old are you? '))

    if age <= 1:
        print('You are an infant. ')

    elif age > 1 and age <= 12:
        print('You are a child. ')

    elif age >= 13 and age <=19:
        print('You are a teenager. ')
        
    elif age >= 20:
        print('You are an adult. ')

main()
    
        

    
