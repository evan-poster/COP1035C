# Tower of hanoi game
# Move all disks from first stack to last stack
# First index in a stack is the lowest position

# Our three stacks
stacks = [[] for _ in range(3)]

# The number of disks
num_disks = 3

# Move the topmost disk from stack a to stack b
def move(stack_a, stack_b):
    # If there are disks in stack_a
    if len(stacks[stack_a]) > 0:
        # If there are no disks in stack b, just move it
        if len(stacks[stack_b]) == 0:
            stacks[stack_b].append(stacks[stack_a].pop())
        # Check if the topmost disk on stack a is smaller than the topmost disk on stack b
        elif stacks[stack_a][-1] < stacks[stack_b][-1]:
            # Move the topmost disk from stack a to stack b
            stacks[stack_b].append(stacks[stack_a].pop())


if __name__ == "__main__":
    # Add disks to the first stack
    for i in range(num_disks, 0, -1):
        stacks[0].append(i)

    print(stacks)

    # Loop until stack 3 is full
    while len(stacks[2]) < num_disks:
        # Ask user for a first stack
        stack_a = int(input("Which stack do you want to move from? ")) - 1
        # Ask user for a second stack
        stack_b = int(input("Which stack do you want to move to? ")) - 1
        # Attempt to move the topmost disk from stack a to stack b
        move(stack_a, stack_b)
        print(f"Stack: {stacks}")
    
    print("Congrats! You won!")
