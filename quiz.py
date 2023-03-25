print("welcome to my computer quiz!")

playing = input("Do you want to play? ") 
if playing.lower() != "yes":
    quit()
print("okay! Let's play :)")
score = 0
answer = input(" Who invented Java Programming?")
if answer .lower() == "james gosling":
    print('correct!')
    score = score + 1
else: 
    print('wrong :( ')
answer = input("What is the extension of java code files?")
if answer.lower() == ".java":
    print('correct!')
    score = score + 1
else: 
    print('wrong :( ')
answer = input(" Which environment variable is used to set the java path?")
if answer.upper() == "JAVA_HOME":
    print('correct!')
    score = score + 1
else: 
    print('wrong :( ')
print(" What is Truncation in Java?")
print("a) Floating-point value assigned to a Floating type     b) Floating-point value assigned to an integer type      c) Integer value assigned to floating type   d) Integer value assigned to floating type     ")
answer = input()
if answer.lower() == "floating-point value assigned to an integer type":
    print('correct!')
    score = score + 1
else: 
    print('wrong :( ')
print("Which of these are selection statements in Java?")
print("a) break    b) continue       c) for()       d) if() ")
answer = input()
if answer.lower() == "if()":
    print('correct!')
    score = score + 1
else: 
    print('wrong :( ')
print('your Total score is = ' +str(score) )
print('your persentage is '+str((score/5)*100) +'%')


    