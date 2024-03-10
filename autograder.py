"""
MIT BWSI Autonomous RACECAR
MIT License
racecar-neo-autograder

File Name: autograder.py

Title: RACECAR Lab Autograder

Author: Christopher Lai (MITLL)

Purpose: Given a lab name, score, and Edly username, return an encrypted hash to
use as verification for student labs
"""

from aes import AES
import sys

if len(sys.argv) < 2:
    print("Usage: python3 autograder.py key")
    sys.exit(1)

KEY = sys.argv[1]

labs = [
    "Lab A - Printing Statements",
    "Lab B - Printing Statements Using Controller",
    "Lab C - RACECAR Controller",
    "Lab D - Driving in Mazes",
    "Lab E - Stoplight Challenge",
    "Lab F - Line Follower",
]

lab_id = [
    "laba",
    "labb",
    "labc",
    "labd",
    "labe",
    "labf",
]

def main():
    key = int(KEY, 16)
    aes = AES(key)

    username = ""
    lab = ""
    score = ""
    maxscore = 20

    print("\nWelcome to the RACECAR Neo Autograder!\n")

    username = input("Enter the username of the student that is requesting lab verification: ")
    
    print("\nEnter the ID # of the lab that you are grading:")
    print("==========================")
    for x in range(0, len(labs)):
        print(f"{x}: {labs[x]}")
    print("==========================")

    while True:
        try:
            ID = int(input())
            if ID >= 0 and ID < len(labs):
                break
            else:
                print("Input out of range. Try Again.")
        except:
            print("Invalid input detected. Please try again.")
    
    lab = lab_id[ID]

    print()
    while True:
        try:
            score = int(input("Enter the score that the student has earned from the lab grading sheet: "))
            if score >= 0:
                break
            else:
                print("Input out of range. Try Again.")
        except:
            print("Invalid input detected. Please try again.")

    message1 = f"{lab}|{score}|{maxscore}|"
    encoded_message = int(message1.encode('utf-8').hex(), 16)
    encrypted1 = hex(aes.encrypt(encoded_message))
    print(f"data: [{message1}], encoded_message: [{encoded_message}], encrypted: [{encrypted1}]")
    
    message2 = f"{username}"
    encoded_message = int(message2.encode('utf-8').hex(), 16)
    encrypted2 = hex(aes.encrypt(encoded_message))
    print(f"user: {message2}, encoded_message: {encoded_message}, encrypted: [{encrypted2}]")

    encrypted = encrypted1[2:] + encrypted2[2:]

    print("\n==========================")
    print("==========================\n")

    print(f"Provide the following hash to the student:")
    print("=================================================================")
    print(f"{encrypted}")
    print("=================================================================")

    print("Thank you for using the RACECAR Neo Autograder. Goodbye!\n")


if __name__ == "__main__":
    main()