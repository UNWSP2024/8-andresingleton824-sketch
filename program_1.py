# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.

# Add your logic starting on line 11

def initials_generator(personsName):

    personsInitials = ""

    parts = personsName.split()
    for part in parts:
        personsInitials += part[0].upper() + ". "

    return personsInitials.strip()


# Example usage
if __name__=="__main__":
    personsName = input('Enter the users first, middle, and last name')

    initials = initials_generator(personsName)

    print(initials)
