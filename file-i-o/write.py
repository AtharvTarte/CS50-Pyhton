name = input("whats your name ?")

#write the file
with open("names.txt","a") as file: # opens the file if not present creats the one , w-writes the file only one time. use append to keep adding.
    file.write(f"{name}\n") # write in the file , f string so every data will be on next line 

