while True: 
    try:
        string1 = input()
        string2 = input()

        if string2 in string1:
            print("Resistente")
        else:
            print("Nao resistente")
            
    except EOFError:
        break
