import matplotlib.pyplot as plt

# 数据
ef_search = [25, 50, 75, 100, 125, 150, 200, 250, 300, 350, 400, 500]

# cardinality 10
qps_10 = [1.60724, 0.824726, 0.570456, 0.439386, 0.367856, 0.313108, 0.246652, 0.206176, 0.177654, 0.156954, 0.141209, 0.118183]
accuracy_10 = [0.21614, 0.63954, 0.82754, 0.91134, 0.94606, 0.96429, 0.98022, 0.98673, 0.99001, 0.99161, 0.99266, 0.99388]


# cardinality 100
qps_100 = [2.61616, 1.39779, 0.951334, 0.716366, 0.585524, 0.491544, 0.378348, 0.309154, 0.261881, 0.227747, 0.202873, 0.166715]
accuracy_100 = [0.03788, 0.14524, 0.24799, 0.33896, 0.40464, 0.45996, 0.53346, 0.58046, 0.61194, 0.63444, 0.65172, 0.67737]

# cardinality 1000
qps_1000 = [2.876, 1.8098, 1.29375, 1.00848, 0.825564, 0.708464, 0.545857, 0.449267, 0.378908, 0.330632, 0.29256, 0.239332]
accuracy_1000 = [0.00796002, 0.02411, 0.03748, 0.0514, 0.06226, 0.0733, 0.09195, 0.10878, 0.12307, 0.13495, 0.14583, 0.16505]

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制图形
plt.plot(accuracy_10, qps_10, marker='o', linestyle='-', color='b', label='Cardinality 10')
plt.plot(accuracy_100, qps_100, marker='o', linestyle='-', color='g', label='Cardinality 100')
plt.plot(accuracy_1000, qps_1000, marker='o', linestyle='-', color='r', label='Cardinality 1000')

# 添加标签和标题
plt.xlabel('Recall (10NN accuracy)')
plt.ylabel('QPS')
plt.title('Recall vs QPS for Different Cardinalities')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 保存图形为 PNG 文件
plt.savefig('./results/recall_vs_qps_cardinalities.png')

# 显示图形
plt.show()