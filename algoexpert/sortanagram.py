def sortanagram(array):
    sortedWords = ["".join(sorted(w)) for w in array]
    print(sortedWords)
    indices = [i for i in range(len(array))]
    print(indices)
    indices.sort(key=lambda x:sortedWords[x])
    print(indices)

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = array[index]
        sortedword = sortedWords[index]

        if sortedword == currentAnagram:
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedword

    result.append(currentAnagramGroup)
    print(result)


sortanagram(["yo","act","flop","tac","foo","cat","oy","olfp"])