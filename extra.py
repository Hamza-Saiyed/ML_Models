import random 

computer = random.choice([0,1,2])
yourstr = input("Enter rock, paper, or scissors: ")
yourdict = {'r':0,'p':1,'s':2}
revdict = {0:'rock',1:'paper',2:'scissors'}

you =yourdict[yourstr]

w = "You Win!"
l = "Computer Win!"
d = "It's a Draw!"

print(f"you chose {revdict[you]}, computer chose {revdict[computer]}")

# if(computer == you):
#     print(d)
# else:
#     if(computer == 0 and you == 1):
#         print(w)
#     elif(computer == 0 and you == 2):
#         print(l)
#     elif(computer == 1 and you == 0):
#         print(l)
#     elif(computer == 1 and you == 2):
#         print(w)
#     elif(computer == 2 and you == 0):
#         print(w)
#     elif(computer == 2 and you == 1):
#         print(l)
a = int(input("Enter Your Choice: "))
case in a:
    
    
    