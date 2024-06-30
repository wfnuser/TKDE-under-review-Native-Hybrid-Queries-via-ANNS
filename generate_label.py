import random
import numpy as np
import os

def generate_label_sift_txt(num_lines, filename, dimensions):
    dir_path = os.path.expanduser("~/datasets/sift-161m/sift_label")
    file_path = os.path.join(dir_path, filename)

    with open(file_path, "w") as file:
        file.write(f"{num_lines} {len(dimensions)}\n")
        for _ in range(num_lines):
            line_elements = []
            for dim in dimensions:
                if isinstance(dim, int):
                    element = random.randint(1, dim)
                else:
                    element = random.choice(dim)
                line_elements.append(str(element))
            line = " ".join(line_elements) + "\n"
            file.write(line)

####################################################################

def read_fvecs(file_path):
    with open(file_path, 'rb') as f:
        while True:
            dim_bytes = f.read(4)
            if not dim_bytes:
                break
            dim = np.frombuffer(dim_bytes, dtype=np.int32)[0]
            vector = np.frombuffer(f.read(4 * dim), dtype=np.float32)
            yield vector

def write_ivecs(file_path, data):
    with open(file_path, "wb") as f:
        for vec in data:
            f.write(np.array([len(vec)], dtype=np.int32).tobytes())
            f.write(np.array(vec, dtype=np.int32).tobytes())

def load_labels(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]  # Skip the first line containing number of lines and dimensions
        labels = [line.strip().split() for line in lines]
    return labels

def generate_ground_truth(base_vectors, query_vectors, base_labels, query_labels, k=20):
    ground_truth = []
    i = 0
    for query_vector, query_label in zip(query_vectors, query_labels):
        i = i + 1
        print (i / query_number)
        
        distances = []
        for base_vector, base_label in zip(base_vectors, base_labels):
            if query_label == base_label:  # Check if labels match
                dist = np.linalg.norm(base_vector - query_vector)
                distances.append((dist, base_vector))
        distances.sort(key=lambda x: x[0])
        nearest_indices = [idx for _, idx in distances[:k]]  # Get the indices of the k nearest neighbors
        ground_truth.append(nearest_indices)
    return ground_truth

####################################################################

cardinalities = [3]

# we need to generate three files: 
# label_sift_base.txt / label_sift_query.txt
# label_sift_groundtruth.ivecs

for cardinality in cardinalities:
    dimensions = [cardinality, ["indoor", "outdoor"], ["night", "daytime"]]

    base_number = 1000000
    base_file_name = f"label_sift_base{cardinality}.txt"

    query_number = 10000
    query_file_name = f"label_sift_query{cardinality}.txt"
 
    # generate_label_sift_txt(base_number, base_file_name, dimensions)
    # generate_label_sift_txt(query_number, query_file_name, dimensions)

####################################################################

    ground_file_name = f"label_sift_groundtruth{cardinality}.ivecs"
    vector_base_file = "/home/qinghao/datasets/sift-161m/sift/sift_base.fvecs"
    vector_query_file = "/home/qinghao/datasets/sift-161m/sift/sift_query.fvecs"
 
    # Read vectors
    base_vectors = np.array(list(read_fvecs(vector_base_file)))
    query_vectors = np.array(list(read_fvecs(vector_query_file)))
    # Load labels
    base_labels = load_labels(os.path.expanduser(f"~/datasets/sift-161m/sift_label/{base_file_name}"))
    query_labels = load_labels(os.path.expanduser(f"~/datasets/sift-161m/sift_label/{query_file_name}"))
    # Calculate ground truth
    ground_truth = generate_ground_truth(base_vectors, query_vectors, base_labels, query_labels)
    # Write ground truth to file
    write_ivecs(os.path.expanduser(f"~/datasets/sift-161m/sift_label/{ground_file_name}"), ground_truth)