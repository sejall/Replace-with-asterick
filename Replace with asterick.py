
# Replace a word withasterick 


def replaceWithAsterisk(sent, word):
    # Use the replace function to find and replace the word with 
    # same number of asterisks as the length of the word.
    return sent.replace(word, "*" * len(word))

sent = "Go feed all the ducks in the lake"
censored_sent = replaceWithAsterisk(sent, "ducks")

print(censored_sent)

