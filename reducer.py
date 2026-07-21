import os

def reduce_data():

    os.makedirs("output", exist_ok=True)

    output = open("output/result.txt", "w")

    for file in os.listdir("partitions"):

        counts = {}

        with open(os.path.join("partitions", file), "r") as f:

            for line in f:

                word, value = line.split()

                counts[word] = counts.get(word, 0) + int(value)

        for word in sorted(counts):
            output.write(f"{word} {counts[word]}\n")

    output.close()