# MapReduce Engine in Python

## Overview

This project is a simple implementation of the **MapReduce Engine** using Python. It demonstrates the complete MapReduce workflow by splitting an input file, mapping data into key-value pairs, partitioning intermediate data, sorting partitions, and reducing them to produce the final output.

## Features

- Splits a large input file into smaller chunks
- Maps each record into (key, value) pairs
- Partitions data using hash partitioning
- Sorts intermediate data
- Reduces grouped values to generate the final result
- Produces output in a separate folder

## Project Structure

```
MapReduce/
│
├── chunks/
├── partitions/
├── output/
│
├── input.txt
├── master.py
├── splitter.py
├── mapper.py
├── partitioner.py
├── sorter.py
├── reducer.py
└── README.md
```

## Technologies Used

- Python 3
- File Handling
- Hashing
- Sorting
- MapReduce Programming Model

## Workflow

1. Read input data from `input.txt`
2. Split the input into multiple chunks
3. Convert each record into `(key, 1)` pairs using the Mapper
4. Partition the intermediate data based on hash values
5. Sort each partition
6. Reduce the grouped values
7. Generate the final output in `output/result.txt`

## Sample Input

```
Apple
Orange
Apple
Banana
Apple
Orange
Banana
Apple
Mango
Banana
```

## Sample Output

```
Apple 4
Banana 3
Mango 1
Orange 2
```

## How to Run

Open the project folder in the terminal and run:

```bash
python master.py
```

or

```bash
py master.py
```

## Learning Outcomes

- Understanding the MapReduce programming model
- Working with file handling in Python
- Data partitioning and sorting
- Aggregating data using reducers
- Building a simplified distributed processing engine

## Author

**Priya Shalin**

BCA Student  
Kamaraj College, Thoothukudi
