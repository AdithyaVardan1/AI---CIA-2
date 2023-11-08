# AI---CIA-2

Sequence Generator

This Python program, generate_sequence, is designed to create a sequence of words by piecing together a list of words based on specific rules.
How to Use

To use this program, you need to have a list of words in the format of strings. This list is passed as an argument to the generate_sequence function along with the starting sequence, initial index, and a count parameter.

For instance:

python

word_list = ['SNU_', 'U_CH', 'CHEN' , 'ENNA' , 'NAI.']
result_sequence = generate_sequence('', word_list, 0, 0)
for index, word in enumerate(result_sequence):
    print("Sequence", index + 1, ":", word)

The above code snippet demonstrates how to generate a sequence from a list of words and print each word sequence obtained.
Sequence Generation Rules

The program operates with the following rules:

    It tries to concatenate words together to form a sequence by matching the last two characters of one word to the first two characters of the next word.
    If a match is found, the words are combined in a sequence. For example:
        If the last two characters of a word match the first two characters of the next word, the sequence continues by appending the rest of the next word.
        If the first two characters of the last word in the sequence match the last two characters of the next word, the next word is appended to the beginning of the sequence.

Implementation Details

The generate_sequence function is recursive and follows these steps:

    It traverses through the word list and checks for matching criteria to create a sequence.
    If a sequence is found or if all words have been used, it returns the final sequence.
    If some words remain unused, it attempts to generate additional sequences until all words have been included.

Notes

    The generated sequence(s) might vary based on the order of words in the initial list and the fulfillment of the matching criteria.
    The code ensures that it utilizes all available words in the list before concluding the sequence generation.

This code offers a simple yet intriguing approach to create sequences based on word associations. Users can experiment with different word lists to observe the variations in the generated sequences.
