number = str(input("Enter an integer: "))
reps = int(input("How many times should the program run? "))
count = 0
digit = 0


for x in range(0,reps):
    new_number = ""
    for i in range(0,len(number)):
        
        if i == 0:
            count = 1
            digit = number[i]
            
        elif number[i] == number[i-1]:
            count += 1
            
        else:
            new_number += str(count)
            new_number += str(digit)
            count = 1
            digit = number[i]
            

    new_number += str(count)
    new_number += str(digit)
    print(new_number)
    number = new_number

