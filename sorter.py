import os

def sort_partitions():

    for file in os.listdir("partitions"):

        path = os.path.join("partitions", file)

        with open(path, "r") as f:
            lines = f.readlines()

        lines.sort()

        with open(path, "w") as f:
            f.writelines(lines)