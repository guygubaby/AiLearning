import numpy as np
import matplotlib.pyplot as plt


'''
KNN 工作原理

    1. 假设有一个带有标签的样本数据集（训练样本集），其中包含每条数据与所属分类的对应关系。
    2. 输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应的特征进行比较。
        计算新数据与样本数据集中每条数据的距离。
        对求得的所有距离进行排序（从小到大，越小表示越相似）。
        取前 k （k 一般小于等于 20 ）个样本数据对应的分类标签。
    3.求 k 个数据中出现次数最多的分类标签作为新数据的分类。
'''

def file2matrix(file_path):
    """
       Desc:
           导入训练数据
       parameters:
           filename: 数据文件路径
       return:
           数据矩阵 returnMat 和对应的类别 classLabelVector
    """
    label_vector = []
    with open(file_path,'r') as f:
        fr=f.readlines()
        number_of_lines=len(fr)
        return_matrix=np.zeros((number_of_lines,3))
        i=0
        for line in fr:
            line=line.strip()
            list_from_line=line.split('\t')
            return_matrix[i,:]=list_from_line[0:3]
            label_vector.append(int(list_from_line[-1]))
            i+=1
    return return_matrix,label_vector


if __name__ == '__main__':
    ret,class_label=file2matrix('../../data/ml/knn/datingTestSet2.txt')
    ret=np.mat(ret)
    class_label=np.array(class_label)

    fig=plt.figure()
    ax=fig.add_subplot(111)
    # ax.scatter(np.array(ret[:,0])[:,0],15*class_label[:],label='111')

    scatters=ax.scatter(np.array(ret[:,0])[:,0],np.array(ret[:,1])[:,0],np.array(ret[:,2])[:,0],15*class_label[:],label=['11','22','33'])
    plt.legend()
    plt.show()