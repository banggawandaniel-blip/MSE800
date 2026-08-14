# Open and read the junk.txt file
with open("junk.txt", "r") as file:
    text = file.read()

# Count the total number of lines
line_count = len(text.splitlines())
print("Total number of lines:", line_count)

# Convert all text to lowercase
text = text.lower()

# Add the required line at the end
text = text.rstrip() + "\ntext file nanalyssis\n"

# Save the processed file
with open("junk_processed.txt", "w") as file:
    file.write(text)

print("Processed file saved successfully.")