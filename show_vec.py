import numpy as np

def read_ivecs(file_path):
    with open(file_path, 'rb') as f:
        data = []
        i = 0
        while True:
            dim_bytes = f.read(4)
            if not dim_bytes:
                break
            i = i + 1
            if i > 10:
                break
            dim = np.frombuffer(dim_bytes, dtype=np.int32)[0]
            vector = np.frombuffer(f.read(dim * 4), dtype=np.int32)
            print(len(vector))
            print(vector)
            data.append(vector)
        return np.array(data)

# label_sift_groundtruth = '/home/qinghao/datasets/sift-161m/sift_label/label_sift_groundtruth3.ivecs'
# data = read_ivecs(label_sift_groundtruth)
# print("ground_truth", data)


# sift_base = '/home/qinghao/datasets/sift-161m/sift/sift_base.fvecs'
# data = read_ivecs(sift_base)
# print("sift_base", data)

sift_query = '/home/qinghao/datasets/sift-161m/sift/sift_query.fvecs'
data = read_ivecs(sift_query)

