import random
def rule(a,b):
  if(a==b):
    print("Draw")
  elif(a==0 and b==1):
    print("computer winns")
  elif(a==0 and b==2):
    print("player wins")
  elif(a==1 and b==0):
    print("player wins")
  elif(a==1 and b==2):
    print("computer wins")
  elif(a==2 and b==0):
    print("player wins")
  elif(a==2 and b==1):
    print("player wins")
  else:
    print("wronng choice")
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

choice=input("enter your choice of rock paper scissors\t")
if choice=="rock":
   choice_val=0
   print(rock)
elif choice=="paper":
  choice_val=1
  print(paper)
else:
  print(scissors)
  choice_val=2
randit=random.randint(0,2)
if randit==0:
  computer=rock
  print(rock)
elif randit==1:
  computer=paper
  print(paper)
else:
  computer=scissors
  print(scissors)
rule(choice_val,randit)
