temp_list = {}

while True:
    try:
        user = input().strip().title()
        if user not in temp_list:
            
            temp_list[user] = 1
            continue
        
        temp_list[user] += 1

    
    except EOFError:
        for key,value in sorted(temp_list.items()):
            print(f"{value} {key.upper()}")
        break