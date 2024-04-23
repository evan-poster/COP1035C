

def main():
    # Open the file and read its contents
    with open("lorem.txt") as file:
        contents = file.read().split()

    # Count the number of occurances of each word
    word_count = {}
    for word in contents:
        word_count[word] = word_count.get(word, 0) + 1

    # Print the unique words in alphabetical order
    unique_words = sorted({word for word, count in word_count.items() if count == 1})
    for word in unique_words:
        print(word)


if __name__ == "__main__":
    main()
