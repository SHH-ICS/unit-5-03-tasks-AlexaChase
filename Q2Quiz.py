# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
filehandle=  open("questions.txt", 'r')
line = filehandle.readline()
if line != "The answer is: ":
    while line!= "The answer is: ":
        print(line)
        line = filehandle.readline()
filehandle.close()
