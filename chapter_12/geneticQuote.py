import random

target = "I never go back on my word, because that is my Ninja way."


characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"


def makeList():
    charList = []
    for i in range(len(target)):
        charList.append(random.choice(characters))
    return charList


def score(mylist):
    matches = 0
    for i in range(len(target)):
        if mylist[i] == target[i]:
            matches += 1
    return matches


def mutate(mylist):
    newList = list(mylist)
    new_letter = random.choice(characters)
    index = random.randint(0, len(target) - 1)
    newList[index] = new_letter
    return newList


random.seed()
bestList = makeList()
bestScore = score(bestList)

guesses = 0

while True:
    guess = mutate(bestList)
    guessScore = score(guess)
    guesses += 1
    if guessScore <= bestScore:
        continue
    print(''.join(guess), guessScore, guesses)
    if guessScore == len(target):
        break
    bestList = list(guess)
    bestScore = guessScore
