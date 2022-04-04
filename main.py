"""PIG Latin"""

CONSONANTS = ['b','c','d','f','j','k','m','n','p','q','s','t','v','x','z']
VOWELS = ['a','e','g','h','i','l','o','r','u','w','y']


def main():
    """Main Function """
    while True:
        input_sentence = input("Just feed me with one sentence:\n").split(' ')
        for index, word in enumerate(input_sentence):
            ending = word[-1] if not word[-1].isalpha() else ''
            word = word.lower().replace(ending, '')
            if word[0].lower() in CONSONANTS:
                input_sentence[index] = f"{word[1:]}{word[0]}ay{ending}"
            else:
                input_sentence[index] = f"{word}way{ending}"

        print(f"Te Pig-Latin is: {' '.join(input_sentence)}")
        again = input("Wanna play again? Press Enter, otherwise n:\n")

        if again.lower() == 'n':
            break

if __name__ == "__main__":
    main()
