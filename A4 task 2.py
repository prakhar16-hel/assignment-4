#Name = Prakhar
#mail = chprakhar1@gmail.com

file2 = open('output.txt','w')
writing_file = file2.write("hello python teacher \n ")
print(writing_file)
file2.close()

file2 = open('output.txt','r')
reading_file = file2.read()
print(reading_file)
file2.close()

file2 = open('output.txt','a')
appending_file = file2.write("python is gr8 ")
print(appending_file)
file2.close()

file2 = open('output.txt','r')
reading_file = file2.read()
print(reading_file)
file2.close()

