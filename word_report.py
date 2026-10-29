with open("text.txt", "r") as file:
    text = file.read()

text = text.lower()

for char in ".,!?":
    text = text.replace(char, "")

words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

with open("report.txt", "w") as file:
    file.write(f"Words: {len(words)}\n")
    file.write(f"Unique words: {len(counts)}\n")

    for word in sorted(counts):
        file.write(f"{word:<12} {counts[word]}\n")

print("Report saved to report.txt")