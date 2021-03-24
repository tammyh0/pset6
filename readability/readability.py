# Computes the grade level comprehension for inputted text

from cs50 import get_string


def main():
    
    # Get input text from user
    text = get_string("Text: ")
    
    # Calculate and print reading level
    L = (100.0 * get_letter_count(text)) / get_word_count(text) 
    S = (100.0 * get_sentence_count(text)) / get_word_count(text)
    
    index = round((0.0588 * L) - (0.296 * S) - 15.8)
    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")
    
    
# Returns the number of letters in the given text
def get_letter_count(text):
    letterCount = 0
    for i in range(len(text)):
        if text[i].isalpha():
            letterCount += 1
            
    return letterCount
    
    
# Returns the number of words in the given text
def get_word_count(text):
    wordCount = 0
    for i in range(len(text)):
        if text[i] == " ":
            wordCount += 1
    if wordCount > 0:
        wordCount += 1
        
    return wordCount
    
    
# Returns the number of sentences in the given text
def get_sentence_count(text):
    sentenceCount = 0
    for i in range(len(text)):
        if text[i] == "." or text[i] == "!" or text[i] == "?":
            sentenceCount += 1
            
    return sentenceCount
    
    
main()