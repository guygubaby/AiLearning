import numpy as np


if __name__ == '__main__':
    rand_arr=np.random.rand(4,4)
    # print(rand_arr,type(rand_arr))

    rand_matrics=np.mat(rand_arr) # np.mat(np.array()) 将numpy.array转matrix
    print(rand_matrics,type(rand_matrics))

    '''
    .I 表示对矩阵求逆(可以利用矩阵的初等变换)
       意义：逆矩阵是一个判断相似性的工具。逆矩阵A与列向量p相乘后，将得到列向量q，q的第i个分量表示p与A的第i个列向量的相似度。
       参考案例链接：
       https://www.zhihu.com/question/33258489
       http://blog.csdn.net/vernice/article/details/48506027
    .T 表示对矩阵转置(行列颠倒)
        * 等同于: .transpose()
    .A 返回矩阵基于的数组
        参考案例链接：
        http://blog.csdn.net/qq403977698/article/details/47254539
    '''

    print(np.mat(np.array([[1,2],[3,4]])).A)

    print(np.eye(4))