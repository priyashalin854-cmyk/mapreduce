def split_file(input_file, num_chunks):
    with open(input_file, "r") as f:
        lines = f.readlines()

    chunk_size = len(lines) // num_chunks

    for i in range(num_chunks):
        start = i * chunk_size

        if i == num_chunks - 1:
            end = len(lines)
        else:
            end = start + chunk_size

        with open(f"chunks/chunk{i}.txt", "w") as out:
            out.writelines(lines[start:end])