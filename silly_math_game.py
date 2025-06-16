import random
import sys

def main():
   #count games
   count=0
   list=[]
   print("Press any key to start (or press I for instructions): ", end="")
   if input().strip().upper()=="I":
         instructions("I")
   score=0
   while True:
      count+=1
      try:
         #prompt user if they only want to solve equations with positive numbers or both positive and negative 
         pos_neg=get_positive_negative()
         #get the level of difficulty
         level=get_level()
         score=0
         #set to 10 rounds
         while True:
            #get random integers
            int1=generate_integer(level, pos_neg)
            int2=generate_integer(level, pos_neg)

            #for any zero integers add by a random number
            if int1==0:
               int1=int1+random.randint(1,9)
            elif int2==0:
               int2=int2+random.randint(1,9)
            
            #prevent negative answers when positive is selected
            if pos_neg==1:
               if int1<int2:
                  num1=int2
                  num2=int1
               else:
                  num1=int1
                  num2=int2
            else:
               num1=int1
               num2=int2

            #select operation
            operation_list=["+", "-", "/", "*"] 
            if score==0:
               while True:
                  operation_input=input("Operation (+, -, *, /): ").strip()
                  if operation_input not in operation_list:
                     continue
                  break
            
            match operation_input:
               case "+":
                  sign= " " + operation_input + " "
                  answer=num1+num2
               case "-":
                  sign=" " + operation_input + " "
                  answer=num1-num2
               case "*":
                  sign=" " + operation_input + " "
                  answer=num1*num2
               case "/":
                  if num2>num1:
                     temp=num1
                     num1=num2
                     num2=temp
                  sign=" " + operation_input + " "
                  answer=round(num1/num2)
                                       
            #set to strings for prompt
            num1=str(num1)
            num2=str(num2)
            equation=num1 + sign + num2 + " ="
      
            j=0
            while j>=0:
               j+=1
               if j<=3:
                  try:
                     input_answer=round(int(input(equation + " ")))
                  except ValueError:
                     continue
               #loop again if answer is wrong
                  if answer!=input_answer:
                     print("EEE")
                     continue
               #if user gets it right, increment by 1
                  if answer==input_answer:
                     score+=1 
                     break
               #print equation and answer if user gets it wrong three times
               print(equation, answer)
               break
            if j==4:
               break
         print()
         print("Score:", score)

         previous_scores=add_to_list(score, level, operation_input)
         list.append(previous_scores)

         print()
         see_scores=input("To see previous scores from session press S: ").strip().upper()
         print()
         if "S" in see_scores:
            print("Games:", count)
            for l in list:
               print(l)

         print()
         stop_game=play_again()
         if stop_game=="N":
            continue
         else:
            break
      except EOFError:
         sys.exit("Game Exited")

def get_level():
    while True:
        try:
            level_input=int(input("Level of difficulty (1-4): "))
            if level_input>=0 and level_input<=4:
               return level_input   
        except ValueError:
            continue
        
def get_positive_negative():
   while True:
      prompt=input("Press P for just positive numbers. Press N for positive/negative numbers: ").strip().upper()
      if "P" in prompt:
         return int(1)
      elif "N" in prompt:
         return int(-1)
      else:
         continue

def play_again():
   while True:
      play_again=input("Do you want to play again? Y/N: ").strip().upper()
      if "N" in play_again:
         return "Y"
      elif "Y" in play_again:
         return "N"
      else:
         continue

def instructions(prompt):
   if prompt=="I":
      print()
      print("How to play Silly Math Game: ")
      print()
      print("Game Setup")
      print("1. Select if you want only positive numbers or a combo of negative and positive numbers")
      print("2. Select the level of difficulty (1-4). Higher level means more digits, for example, level 1 will only produce equations composed of numbers within 1-9")
      print("Each level adds more digits (level 2: 1-99, level 3: 1-999, level 4: 1-9999)")
      print("3. Select what type of operation you want to do (+, -, *, /)")
      print()
      print("How to Play")
      print("Each question right gives you a point, while a wrong one ends the game.")
      print("If you get a question wrong, 'EEE' will be produced along with the question being asked again.")
      print("You have three chances to answer correctly before the answer is produced and the game ends")
      print("Your score is how many questions you can answer correctly in a row")
      print()
      print("Note: for division, answers are rounded to the nearest whole (no decimals)")
      print()

def add_to_list(sc, lv, op_in):

   lv=str(lv)
   sc=str(sc)

   if op_in=="+":
      op_in="addition"
   elif op_in=="-":
      op_in="subtraction"
   elif op_in=="*":
      op_in="multiplication"
   else:
      op_in="division"

   to_list="--Score " + sc + " --Level: " + lv + " --Operation: " + op_in
   
   return to_list

def generate_integer(level, pn):
   if pn==int(1):
      if level==1:
         num=random.randint(0, 9)
      elif level==2:
         num=random.randint(0, 99)
      elif level==3:
         num=random.randint(0, 999)
      else:
         num=random.randint(0, 9999)
   elif pn==-1:
      if level==1:
         num=random.randint(-9, 9)
      elif level==2:
         num=random.randint(-99, 99)
      elif level==3:
         num=random.randint(-999, 999)
      else:
         num=random.randint(-9999, 9999)

   return num

main()