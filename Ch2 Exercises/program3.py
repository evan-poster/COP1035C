# Week1/Ch2 Exercises/program3.py
# Prompt the user for the number of each type of video and output the total cost.

# Define a function to calculate the total cost
def calculate_total_cost(new_videos, old_videos):
    return new_videos * 3.00 + old_videos * 2.00

# Get number of new and old videos from the user
new_videos = int(input("Enter the number of new videos: "))
old_videos = int(input("Enter the number of old videos: "))

# Output the total cost
print(f"The total cost is ${calculate_total_cost(new_videos, old_videos):.2f}")
