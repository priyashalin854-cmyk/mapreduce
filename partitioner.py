import os

def partition(pairs, reducers):

    os.makedirs("partitions", exist_ok=True)

    files = []

    for i in range(reducers):
        files.append(open(f"partitions/partition{i}.txt", "a"))

    for key, value in pairs:
        index = hash(key) % reducers
        files[index].write(f"{key} {value}\n")

    for f in files:
        f.close()