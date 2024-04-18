
file = "thousand_words.txt"


def main():
    '''
        Given a file/text, identify the words with the highest frequency
    '''
    # Open file for reading
    with open(file, "r") as f:
        contents = f.read().split()
        # Count each word when it appears
        counts = {}
        for word in contents:
            counts[word] = counts.get(word, 0) + 1
            max_count = max(counts.values())
        # We have our counts and max_count; now we just need to pull all words
        modes = [word for word, count in counts.items() if count == max_count]
        for word in modes:
            print(word, counts[word])


if __name__ == "__main__":
    main()
