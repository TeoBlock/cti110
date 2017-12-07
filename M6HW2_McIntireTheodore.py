# Generate a random number between 1-100 and user guesses the number
# 22 November 2017
# CTI-110 M6HW2 - Random Number Guessing Game
# Theodore McIntire
 

def main():
    
    play_again = input('Do you want to play a guessing game? (Enter y for yes or n for no): ')
    print('')

    import random
    
    while play_again == 'y':
        x = random.randint(0, 100)
        play_game(x)

        print('')
        play_again = input('Play again? (Enter y for yes or n for no): ')
        print('')

    print('Thanks for running my program, I hope you liked it!')

# This finishes the code for the main method


def play_game(ran_num):

    print('This program generates a random number and you guess the number.')
    print('You have up to 8 chances to guess the number.')
    print('')
    user_guess = int(input('Enter an integer between 1-100 as your first guess: '))
    num_guesses = 1

    while user_guess != ran_num and num_guesses <= 7: #Gives the user 8 guesses

        num_guesses = num_guesses + 1

        if user_guess > ran_num:
            print(user_guess, 'is too high, try again.')
            user_guess = int(input('Enter a new guess: '))

        elif user_guess < ran_num:
            print(user_guess, 'is too low, try again.')
            user_guess = int(input('Enter a new guess: '))

    if user_guess == ran_num: #Only prints congrats if number is guessed
            print('Well done, you guessed the correct number!')

    print('The number of guesses you used was', num_guesses)
    print('Your last guess:', user_guess)
    print('The random number:', ran_num)
    
# This finishes the code for this method

    
# program start 
main()

