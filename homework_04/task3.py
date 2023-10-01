n = 0
print(n)

while n < 101:
    choice = input('Should we break ')
    if choice == 'yes':
        break
    if choice == 'no':
        n += 1
        print(f'{n}')
    else:
        print("Don't understand you")
