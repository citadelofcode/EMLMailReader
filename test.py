lines = list()
EmlFile = open("./Sample-Emails/Sample-Email-1.eml", "r")
lines = EmlFile.readlines()
EmlFile.close()
LineNumber = 0
MimeReached = False
for line in lines:
    LineNumber += 1
    if MimeReached:
        print(f"Line {LineNumber} in question is:'" + line + "'")
        print(f"Length of line is: {len(line)}")
        print(f"Length of line after strip is: {len(line.strip())}")
        if line[0] == " ":
            print("Line contains nothing but on whitespace character")
        break
    if line.startswith("MIME-Version"):
        MimeReached = True
