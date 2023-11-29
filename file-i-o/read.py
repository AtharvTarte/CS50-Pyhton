with open("names.txt","r") as file: #r-only load the file does not save it
    for line in file:
        print(line.rstrip()) #by default it prints with spaces inbetween lines so use method rstrip 
