#Write the definition of a Python function named long_lines( )
# which reads the contents of a text file named 'lines.txt' and
# displays those lines from the file which have at least 8 words in it
def long_lines():
    with open('filehandling1.txt', 'r') as readfiles:
        content = readfiles.readlines()
        # while content == 8:
        # print(content)
        for lines in content:
            words = lines.split()
            if len(words) >= 8:
                print(lines)
long_lines()