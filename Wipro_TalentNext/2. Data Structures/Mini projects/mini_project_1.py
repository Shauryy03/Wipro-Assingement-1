# Project: Data Structure - Dictionary of People and Facts

# Create a dictionary that contains a list of people and one interesting fact about each of them.
# Display each person and his or her interesting fact to the screen.
# Next, change a fact about one of the people.
# Also add an additional person and corresponding fact.
# Display the new list of people and facts.
# Run the program multiple times and notice if the order changes.
# Sample Output:
# Jeff: Is afraid of Dogs.
# David: Plays the piano.
# Jason: Can fly an airplane.
# Jeff: Is afraid of heights.
# David: Plays the piano.
# Jason: Can fly an airplane.
# Jill: Can hula dance

def display_facts(facts_dict):
    for person, fact in facts_dict.items():
        print(f"{person}: {fact}")

# Initial dictionary
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

print("=== Original Facts ===")
display_facts(people_facts)

# Modify a fact
people_facts["Jeff"] = "Is afraid of heights."

# Add a new person
people_facts["Jill"] = "Can hula dance."

print("\n=== Updated Facts ===")
display_facts(people_facts)
