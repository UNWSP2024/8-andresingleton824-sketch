# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).


import random

def capital_quiz():

    state_capitals = {
        "Alabama": "Montgomery",       "Alaska": "Juneau",
        "Arizona": "Phoenix",          "Arkansas": "Little Rock",
        "California": "Sacramento",    "Colorado": "Denver",
        "Connecticut": "Hartford",     "Delaware": "Dover",
        "Florida": "Tallahassee",      "Georgia": "Atlanta",
        "Hawaii": "Honolulu",          "Idaho": "Boise",
        "Illinois": "Springfield",     "Indiana": "Indianapolis",
        "Iowa": "Des Moines",          "Kansas": "Topeka",
        "Kentucky": "Frankfort",       "Louisiana": "Baton Rouge",
        "Maine": "Augusta",            "Maryland": "Annapolis",
        "Massachusetts": "Boston",     "Michigan": "Lansing",
        "Minnesota": "Saint Paul",     "Mississippi": "Jackson",
        "Missouri": "Jefferson City",  "Montana": "Helena",
        "Nebraska": "Lincoln",         "Nevada": "Carson City",
        "New Hampshire": "Concord",    "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",      "New York": "Albany",
        "North Carolina": "Raleigh",   "North Dakota": "Bismarck",
        "Ohio": "Columbus",            "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",             "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",  "South Carolina": "Columbia",
        "South Dakota": "Pierre",      "Tennessee": "Nashville",
        "Texas": "Austin",             "Utah": "Salt Lake City",
        "Vermont": "Montpelier",       "Virginia": "Richmond",
        "Washington": "Olympia",       "West Virginia": "Charleston",
        "Wisconsin": "Madison",        "Wyoming": "Cheyenne"
    }

    correct = 0
    incorrect = 0

    # Pull the states into a list and shuffle for a random question order
    states = list(state_capitals.keys())
    random.shuffle(states)

    print("=== U.S. State Capitals Quiz ===")
    print("Type 'quit' at any time to stop.\n")

    for state in states:
        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == "quit":
            break

        if answer.lower() == state_capitals[state].lower():
            print("  Correct!\n")
            correct += 1
        else:
            print(f"  Incorrect. The capital of {state} is {state_capitals[state]}.\n")
            incorrect += 1

    total = correct + incorrect
    print("=" * 34)
    print(f"Quiz complete!")
    print(f"  Questions answered : {total}")
    print(f"  Correct            : {correct}")
    print(f"  Incorrect          : {incorrect}")
    if total > 0:
        print(f"  Score              : {round(correct / total * 100, 1)}%")

if __name__ == "__main__":
    capital_quiz()
