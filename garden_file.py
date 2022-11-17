# we import the spacy module
import spacy

# I took a few garden path sentences from the links below
# https://www.reddit.com/r/linguistics/comments/12bqpr/rlinguistics_give_me_your_best_garden_path/
# https://www.apartmenttherapy.com/garden-sentences-262915

# We load the English model and store under variable nlp
nlp = spacy.load('en_core_web_sm')

# We create a list variable gardenpathSentences which contains 5
# garden path sentences
gardenpathSentences = [["While Tom was washing the dishes fell on the floor."],
                       ["While I was surfing Reddit went down."],
                        ["The cotton clothing is made of grows in Mississippi."],
                        ["The cotton clothing is usually made of grows in the southern U. S."],
                        ["The man who hunts ducks out on weekends."]]

# We use a for loop to get each item(sentence) from the list
# We use another nested for loop to take the sentence out of the list and pass it
# to our english model, we use .text.split() method and use
# a list comprehension to tokenize the sentences. We print the result.
for sentence in gardenpathSentences:
    for words in sentence:
        new_line = nlp(words)
        new_line.text.split()
        new_list = [(token, token.orth_, token.orth) for token in new_line]
        print(new_list)


# We made a separate for loop to show the slightly different process
# We cast the sentence onto a string and then pass it to the english model as
# it only accepts a string and not list.
# We preform a list comprehension to print the labels/entities
for sentence in gardenpathSentences:
    new_sentence = str(sentence)
    new_sentence = nlp(new_sentence)
    entity_sentence = [(i, i.label_, i.label)for i in new_sentence.ents]
    print(entity_sentence)

# The two unusual entities I have found was that it classified Reddit as a NORP (nationalities or religious
# or political group when it is a website based on free speech wherein anything goes.
# The other unusual thing is that in 4th sentence it classifies US as a person rather than a country
