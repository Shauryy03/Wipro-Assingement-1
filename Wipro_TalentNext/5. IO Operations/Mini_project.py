# Project 1: Decode secret message from text file

from collections import Counter

# Read the file
with open("Sample1.txt", "r") as file:
    lines = file.readlines()

# 1. Determine meeting time
line_count = len(lines)
if line_count <= 12:
    meeting_time = f"{line_count} AM"
else:
    hour = line_count % 12
    hour = 12 if hour == 0 else hour
    meeting_time = f"{hour} PM"

# 2. Determine meeting place
# Combine all lines into one string and split into words
words = ' '.join(lines).replace(',', '').replace('.', '').split()
word_freq = Counter(words)

# Find the most common word
most_common_word, _ = word_freq.most_common(1)[0]
meeting_place = f"{most_common_word} Street"

# Output the result
print("Meeting time:", meeting_time)
print("Meeting place:", meeting_place)
