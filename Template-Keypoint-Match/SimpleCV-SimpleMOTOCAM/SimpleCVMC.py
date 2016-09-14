__author__ = "janez"


import time
from SimpleCV import * 


def my_program():

    tmp = None
    
    drinks = {'1': "pepsi_logo3.png",
              '2': "lasko.png",
              '3': "union_logo2.png",
              '4': "multisola_logo2.png",
              '5': "cocacola_logo2.png"}
    
    input = raw_input("""Menu:
                      \n 1 - Pepsi
                      \n 2 - Lasko
                      \n 3 - Union
                      \n 4 - Multi Sola
                      \n 5 - Coca Cola
                      \n
                      \n Select drink:""")
    
    for key,values in drinks.iteritems():
        if input in key:
            tmp = Image(values).grayscale()

    m = []
    f = 10
    
    for f in range(0,f):
        img = cam.getImage().grayscale()
        match = img.findKeypointMatch(tmp, quality=300.0, minDist=0.60, minMatch=0.28)
        if match:
            match.draw(color = (128,230,89), width=5, autocolor=False)
            match.show()
            values = match.coordinates()
            distv = match.center()
            print "Can positions: ", values
            m.append(values)
            if len(m) == 2:
            
                x1 = m.pop(0)
                x1 = x1.tolist()
                x1 = x1.pop()
                x_1 = x1.pop(0)
                x_1 = int(float(x_1))
            
                x2 = m.pop(0)
                x2 = x2.tolist()
                x2 = x2.pop()
                x_2 = x2.pop(0)
                x_2 = int(float(x_2))
                
                diff = x_2 - x_1
                if diff in range(-40,40,1):
                    
                    print "There's your drink."
                    m.append(x2)
                    break
                
                else:
                    if diff in range(-300,300,1):
                            print "There's no drink. Restart?"
                            stri = raw_input()
                        
                            print "\n"
                            if stri == "y":
                                my_program()
                            elif stri == "n":
                                print "Bye"
                                exit()
                    else:
                        continue
            else:
                continue
            
        else:
            print "No can for you.."

            

    
    print "Restart again?"

    stri = raw_input()
    print "n"
    if stri == "y":
        my_program()
    elif stri == "n":
        print "Bye."
        key = raw_input("Press enter to exit and go to the store.")
        exit()
my_program()

if __name__ == '__name__':
    my_program()
