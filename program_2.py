# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13
 
def word_separator(sentence):
 
    new_sentence = ""
 
    for char in sentence:
        # When we hit an uppercase letter (and it's not the very first character),
        # it signals the start of a new word — insert a space and lowercase the letter
        if char.isupper() and new_sentence != "":
            new_sentence += " " + char.lower()
        else:
            new_sentence += char
 
    return new_sentence.strip()
 
# Example usage
if __name__=="__main__":
    sentence = "StopAndSmellTheRoses"
 
    new_sentence = word_separator(sentence)
 
    print(new_sentence)
