import random

def generate_list_length():
    first_number = random.randint(2,5 )
    second_number = random.randint(2, 5)
    list_length = first_number + second_number
    return list_length

def listnums_Generator(listlength):
    testlist = [random.randint(1, listlength) for i in range(listlength)]
    return testlist

def generate_difficulty():
    difficulty_factor = int(input("Enter difficulty number from 1-3 (1-Hard, 2-Med, 3-Easy): "))        
    return difficulty_factor

def determine_win(guesses: int):
    if guesses == 0:
        print (f"You have lost!")
    else:
        print(f'You have won!')
    
def run_game():
    current_index = 0
    difficulty_factor = generate_difficulty()
    list_length = generate_list_length()
    guesses_allowed = list_length * difficulty_factor
    current_list = listnums_Generator(list_length)

    print(f'Current list: {current_list} \n')

    while guesses_allowed != 0 and current_index < len(current_list):

        try:
            user_guess = int(input("Try a number: "))
            print(f'Current list: {current_list} \n')

            if user_guess < current_list[current_index]:
                print(f'Your number {user_guess} is less than the current: {current_list[current_index]}')
                guesses_allowed -= 1
                print(f'Guesses remaining: {guesses_allowed}')
            elif user_guess > current_list[current_index]:
                print(f'Your number {user_guess} is higher than current: {current_list[current_index]}')
                guesses_allowed -= 1
                print(f'Guesses remaining: {guesses_allowed}')
            else: 
                print(f'Your guess matched! Move on to the next number!')
                current_index +=1 
                print(f'Guesses remaining: {guesses_allowed}')
            
        except ValueError:
            print(f'Your input was NOT an integer! ')
    
    determine_win(guesses_allowed)

if __name__ == '__main__':
    run_game()
