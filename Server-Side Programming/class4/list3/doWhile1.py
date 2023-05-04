acceptance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    isAccepted = float(input('Insert a grade: '))
    if isAccepted not in acceptance:
        print("The grade must be between 0 and 10")
    else:
        break
