def mapper(chunk_file):
    pairs = []

    with open(chunk_file, "r") as f:
        for line in f:
            word = line.strip()
            pairs.append((word, 1))

    return pairs