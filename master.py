from splitter import split_file
from mapper import mapper
from partitioner import partition
from sorter import sort_partitions
from reducer import reduce_data

NUM_MAPPERS = 2
NUM_REDUCERS = 2

split_file("input.txt", NUM_MAPPERS)

for i in range(NUM_MAPPERS):
    pairs = mapper(f"chunks/chunk{i}.txt")
    partition(pairs, NUM_REDUCERS)

sort_partitions()

reduce_data()

print("MapReduce Completed!")
print("Output saved in output/result.txt")