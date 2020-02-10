"""
MDST Workshop 1 - Python Basics Starter Code
"""
import random
import base64
# Add any imports you need here:


def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    in_num = raw_input("Please input an interger ")
    num = int(in_num)
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd!")




def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    random_num = random.randrange(1,10)
    guess_input = input("Choose a random number from 1 to 9 ")
    while guess_input != "exit":
        if (guess_input == random_num):
            print("Exactly right!")
            break
        elif(guess_input > random_num):
            print("Too high!")
        else:
            print("Too low!")
        guess_input = input("Continue guessing...")



def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    if string == "":
        in_word = raw_input("Please enter a word:")
        string = in_word
    count = 0
    for i in range(int(len(string))/2):
        if string[i] != string[len(string) - i - 1]:
            print("Not a palindrome")
            break
        count += 1
    if count == int(len(string))/2:
        print("This is a palindrome.")
           

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    encryp_username = base64.standard_b64encode(username)
    encryp_password = base64.standard_b64encode(password)
    file = open(filename, "a")
    file.write(str(encryp_username))
    file.write("\n")
    file.write(str(encryp_password))
    file.write("\n")
    file.close()



def part4b(filename, password = None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    file = open(filename)
    file_in_line = file.readlines()
    username = base64.standard_b64decode(file_in_line[0])
    orig_password = base64.standard_b64decode(file_in_line[1])
    print(username)
    print(orig_password)
    if(password != None):
        file_in_line[1] = base64.standard_b64encode(password)





if __name__ == "__main__":
    #part1(3)  # odd!
    #part1(4)  # even!
    #part2()
    #part3("ratrace")  # False
    #part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
