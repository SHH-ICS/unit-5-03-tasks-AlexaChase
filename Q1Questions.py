# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer.
# This will be six lines, and then store the questions in the file questions.txt.
Question= input("The multiple choice question is:")
Option1= input("1. ")
Option2= input("2. ")
Option3= input("3. ")
Option4= input("4. ")
Answer= input("The answer is: ")
filehandle= open("questions.txt", 'w')
filehandle.writelines(["The multiple choice question is: ", Question, "\n1. ", Option1,"\n2. ",
                       Option2, "\n3. ", Option3, "\n4. ", Option4, #Continuation of the code above
                       "\nPlease type your answer here: \n", "\nThe answer is: ", Answer]) #Continuation of the code above
filehandle.close()
