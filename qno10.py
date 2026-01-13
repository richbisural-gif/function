# Accept input from the user
user_input = input("Enter a string: ")

cleaned_string = ""

# Replace non-alphanumeric characters with #
for ch in user_input:
    if ch.isalnum():
        cleaned_string += ch
    else:
        cleaned_string += "#"

# Print the cleaned string
print("Cleaned string:", cleaned_string)