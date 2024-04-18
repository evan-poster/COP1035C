
hexbin_table = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

binhex_table = {value: key for key, value in hexbin_table.items()}


def hex_to_bin(hex):
    output = ""
    for char in hex:
        output += hexbin_table[char]
    return output


def bin_to_hex(bin):
    output = ""
    if len(bin) % 4 != 0:
        bin = "0" * (4 - len(bin) % 4) + bin
    for i in range(0, len(bin), 4):
        output += binhex_table[bin[i:i+4]]
    return output


if __name__ == "__main__":
    running = True
    while running:
        user_prompt = input("Do you want to enter a hex number or binary number? (h/b/q)")
        if user_prompt == "h":
            hex = input("Enter a hex number: ")
            print(hex_to_bin(hex))
        elif user_prompt == "b":
            bin = input("Enter a binary number: ")
            print(bin_to_hex(bin))
        elif user_prompt == "q":
            running = False
