#name : prakhar
#mail = chprakhar1@gmail.com
# Task 1 : Read a File and Handle Errors
file_1 = open('sample.txt','r')
reading_file = file_1.read()
print(reading_file)
file_1.close()
#we can see file dose not exist to remove this error we create a text file in system