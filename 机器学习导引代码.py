from numpy import *
import matplotlib.pyplot as plt

# 原始数据导入与处理
def loaddata(flName):
    dataset = []
    f = open(flName)
    for line in f.readlines():
        Line = line.strip().split('\t')
        flLine = []
        for i in Line:
            a = float(i)
            flLine.append(a)
        dataset.append(flLine)
    return mat(dataset)

# 随机生成类中心点
def random_center(dataset, k):
    n = shape(dataset)[1]
    center_spot = mat(zeros((k, n)))
    for j in range(n):
        min_j = min(dataset[:, j])
        rangej = float(max(dataset[:, j]) - min_j)
        center_spot[:, j] =  + rangej * random.rand(k, 1)
    return center_spot

# 欧氏距离计算
def dist_spot(A, B):
    return sqrt(sum(power(A - B, 2)))

# k-means
def k_means(dataset, k, distMeas=dist_spot, createCent=random_center):
    m = shape(dataset)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataset, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf;minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j, :], dataset[i, :])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        print(centroids)
        for cent in range(k):

            ptsInClust = dataset[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment

# 最终结果作图
def showCluster(dataSet, k, clusterAssment, centroids):
    fig_ori = plt.figure()
    plt.title("原始数据分布")
    ax1 = fig_ori.add_subplot(111)
    ax1.set_xlabel("消费/收入")
    ax1.set_ylabel('余额/百元')
    ax1.scatter(dataSet[:, 0].tolist(), dataSet[:, 1].tolist(), s=25, c='black', marker='o')

    fig_out = plt.figure()
    plt.title("K-means")
    plt.rcParams['font.sans-serif'] = ['SimHei']
    ax2 = fig_out.add_subplot(111)
    data = []
    for cent in range(k):
        ptsInClust = dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
        data.append(ptsInClust)
    for cent, marker in zip( range(k),  ['^', 'o', '*'] ):
         ax2.scatter(data[cent][:, 0].tolist(), data[cent][:, 1].tolist(), s=80, c='black', marker=marker)
    ax2.scatter(centroids[:, 0].tolist(), centroids[:, 1].tolist(), s=1000, c='black', marker='+', alpha=1)
    ax2.set_xlabel("消费/收入")
    ax2.set_ylabel('余额/百元')
    plt.show()


dataset = loaddata('test1.txt')
centroids, clusterAssment = k_means(dataset, 3)
showCluster(dataset, 3, clusterAssment,centroids)