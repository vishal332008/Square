for i in range(1, 6):
    print("* ", end="")
    for j in range(1, 4):
        if i == 1 or i == 5:
            print("* ", end="")
        else:
            print("  ", end="")
    print("* ")
