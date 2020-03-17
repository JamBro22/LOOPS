for var1 in range(20,0,-2): #decrementing in twos from 20 to 2/countdown loop
    print(var1) #displaying number pattern
else:
    print("Enough with loops") #signaling the end of the programme

cars=["VW","BMW","Ford","Mazda","Tata"] #declaring list of items
for mycars in cars:
    print(mycars) #printing the previously declared list
    if mycars=="Ford": #indicating Ford as a break point for the programme
        break

cars=["VW","BMW","Ford","Mazda","Tata"]
for mycars in cars:
    if mycars=="Ford": #telling programme to continue without including Ford
        continue
    print(mycars)

for class2 in "lifechoices": #declaring a string of characters
    print(class2) #printing the characters

cars1=["VW","BMW","Ford","Mazda","Tata"] #declaring list
bikes=["Suzuki","Kawasaki","Honda","Ducatti","Vuka"] #declaring second list
for mycars1 in cars1: #showcasing outer loop
    for mybikes in bikes: #showcasing inner loop
        print(mycars1,mybikes) #displaying list adjacently

for i in range(1,6,+1): #introducing a range and increment
    print("* "*i) #printing stars
for j in range(6,0,-1): #introducing a range and decrement
        print("* "*j) #printing stars