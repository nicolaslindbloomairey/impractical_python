"""Generate funny names from 2 lists of names."""
import random

def main():
    """Choose names at random from 2 lists, then print to console."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
             "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cockentoasten', 'Endicott', 'Fewhairs', 'Gooberdapple')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name))
        print("\n\n")

        try_again = input("\n\nTry Again? (Press enter else n to quit)\n ")
        if try_again.lower() == 'n':
            break

if __name__ == '__main__':
    main()
