import random

digits = ['1','2','3','4','5','6','7','8','9','0']
random.shuffle(digits)
secret_num = digits[0:4]

bulls = 0
cows = 0
tries = 0

def find_bulls(guessy, secret):
    bulls = 0
    for i, number in enumerate(secret):
        if number == guessy[i]:
            bulls += 1
    return bulls
    
while bulls < 4:
    
    guess = input('type number with 4 digits: ')
    tries += 1
    cows = 0

    for number in guess:
        cows += secret_num.count(number)
    bulls = find_bulls(guess, secret_num)
    cows -=  bulls
    print(f'there are {bulls} bulls \n There are {cows} cows \n')

print(f'You finished in {tries} tries.')