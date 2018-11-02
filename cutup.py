import random
import io

def CutUp(input1, input2):

    wordlist1 = []
    wordlist2 = []
    output = []

    # Make word lists
    words = (input1.split())
    for word in words:
        wordlist1.append(word)

    words = (input2.split())
    for word in words:
        wordlist2.append(word)

    for i in range(10):
        if i % 2 == 0:
            wordlist = wordlist1
        else:
            wordlist = wordlist2


        start = random.randint(0, len(wordlist))
        end = start + random.randint(0, 10)
        output.append(' '.join(wordlist[start:end]))
        del(wordlist[start:end])


    return ' '.join(output)
