#output_file = open("hello.txt", "w")
#print(type(output_file)
#)
#lines=["Hello world.\n", "Welcome to TutorialsTeacher.\n", "Some Text. \n","Some Text. \n", "Some Text. \n", "Some Text. \n"]
#output_file.writelines(lines)
#output_file.close()
hello = "hello"

output_file = open("hello.txt", "r")
#firstLine = output_file.readline()
#print(firstLine)


#line = output_file.readline()
#while line!='':
    #print(line)
    #line=output_file.readline()

def grepLines(seekContent, lines):
    matchingContent = []
    for line in lines:
        if(seekContent(line)):
            matchingContent.append(line)
    return matchingContent

matchingContent = grepLines(lambda line: "Some Text." in line, output_file.readlines())
print(len(matchingContent))  
output_file.close()         