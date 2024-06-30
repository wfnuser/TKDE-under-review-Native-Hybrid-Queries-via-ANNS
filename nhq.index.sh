cardinality=$1

echo "./NHQ-NPG_nsw/examples/cpp/index ~/datasets/sift-161m/sift/sift_base.fvecs ~/datasets/sift-161m/sift_label/label_sift_base${cardinality}.txt ~/datasets/sift-161m/graph${cardinality} ~/datasets/sift-161m/attrtable${cardinality} 40 100"

./NHQ-NPG_nsw/examples/cpp/index ~/datasets/sift-161m/sift/sift_base.fvecs ~/datasets/sift-161m/sift_label/label_sift_base${cardinality}.txt ~/datasets/sift-161m/graph${cardinality} ~/datasets/sift-161m/attrtable${cardinality} 40 100
