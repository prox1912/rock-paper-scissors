import random
x=eval(input("Hi,this is a rock,paper,scissors game. Choose 1 for rock, 2 for paper and 3 for scissors"))
y=random.randint(1,3)
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Your choice is: ")
if(x==1):
    print("Rock\n")
    print(rock)
elif(x==2):
    print("Paper\n")
    print(paper)
elif(x==3):
    print("SCissors\n")
    print(scissors)
else:
    print("Invalid choice!")
print("Computer choice is: ")
if(y==1):
    print("Rock\n")
    print(rock)
elif(y==2):
    print("Paper\n")
    print(paper)
elif(y==3):
    print("SCissors\n")
    print(scissors)
if(x==y):
    print("\nThere is a tie!")
elif(x==1 and y==3)or(x==2 and y==1) or (x==3 and y==2):
    print("\nYou won!")
else:
    print("You lost!!")
