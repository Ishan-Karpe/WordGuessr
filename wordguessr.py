import random

common = [
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
        "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
        "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
        "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
        "people", "into", "year", "your", "good", "some", "could", "see", "other", "than",
        "then", "now", "look", "only", "come", "its", "over", "think", "also", "back",
        "after", "use", "two", "how", "our", "work", "first", "well", "way", "even",
        "new", "want", "because", "any", "these", "give", "day", "most", "us", "more",
    ],

uncommon = [
        "ubiquitous", "ephemeral", "cacophony", "serendipity", "mellifluous",
        "penumbra", "quixotic", "luminous", "esoteric", "gregarious",
        "nadir", "zenith", "obfuscate", "pulchritudinous", "languid",
        "ubermensch", "solipsism", "verisimilitude", "peregrinate", "quagmire",
        "juxtapose", "egregious", "iconoclast", "chicanery", "surreptitious",
        "parsimonious", "ignominious", "mendacious", "truculent", "recalcitrant",
        "perfunctory", "lugubrious", "salient", "sycophant", "plethora",
        "capricious", "vociferous", "sagacious", "nefarious", "ostentatious",
        "perspicacious", "ubiquity", "ephemeralness", "cacophonous", "serendipitous",
        "mellifluousness", "penumbral", "quixotically", "luminosity", "esotericism",
        "gregariously", "nadiral", "zenithal", "obfuscation", "pulchritude",
        "languidly", "ubermenschen", "solipsistic", "verisimilar", "peregrination",
        "quagmiry", "juxtaposition", "egregiously", "iconoclastic", "chicanerous",
        "surreptitiously", "parsimoniously", "ignominiously", "mendaciously", "truculently",
        "recalcitrantly", "perfunctorily", "lugubriously", "saliency", "sycophancy",
        "plethoric", "capriciously", "vociferously", "sagaciously", "nefariously",
        "ostentatiously", "perspicaciously", "zeitgeist", "phantasmagoria", "obsequious",
        "lachrymose", "ruminate", "erudite", "sanctimonious", "bilious", "contumacious"
]

def common_lvl():
    cword = random.choice(common)
    attempts = 7
    guessed_word = ["_"] * len(cword)

    while attempts > 0 and "_" in guessed_word:
        print("Current word: " + " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()
        if guess in cword:
            for i, letter in enumerate(cword):
                if letter == guess:
                    guessed_word[i] = guess
                else:
                    continue
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        
        if "_" not in guessed_word:
            print("Congratulations! You've guessed the word:", cword)
            break
        else:
            print(f'\nYou\'ve run out of attempts! The word was: {cword}')


def uncommon_lvl():
    uword = random.choice(uncommon)
    attempts = 15
    guessed_word_1 = ['_'] * len(uword):

    while attempts > 0 and "_" in guessed_word_1:
        print("Current word: " + " ".join(guessed_word_1))
        guess = input("Guess a letter: ").lower()
        if guess in uword:
            