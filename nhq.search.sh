cardinality=$1

echo "./NHQ-NPG_nsw/examples/cpp/search ~/datasets/sift-161m/graph${cardinality} ~/datasets/sift-161m/attrtable${cardinality} ~/datasets/sift-161m/sift/sift_query.fvecs ~/datasets/sift-161m/sift_label/label_sift_groundtruth${cardinality}.ivecs ~/datasets/sift-161m/sift_label/label_sift_query${cardinality}.txt"

./NHQ-NPG_nsw/examples/cpp/search ~/datasets/sift-161m/graph${cardinality} ~/datasets/sift-161m/attrtable${cardinality} ~/datasets/sift-161m/sift/sift_query.fvecs ~/datasets/sift-161m/sift_label/label_sift_groundtruth${cardinality}.ivecs ~/datasets/sift-161m/sift_label/label_sift_query${cardinality}.txt
