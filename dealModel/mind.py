# coding=utf-8
"""
逻辑回归
"""
from common import Common
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
import sys 


def main():
    """
    主函数
    :return:
    """
    # 日志文件清空
    conf=Common.readconf()
    sampleDir=conf['sampleDir']
    mindresdir=conf['mindResDir']
    sample=sampleDir + '/feature11.txt'
    fp_model = open(mindresdir+"/logistic-regression.model", "w")
    fp_para = open(mindresdir+"/logistic-regression.para", "w")

    print "load dataset"
    # 加载数据
    dataset = np.loadtxt(sample, delimiter=",")
    np.set_printoptions(suppress=True)
    len = np.shape(dataset)  # 获取数据集大小（row_len,col_len）
    len_col = len[1]
    # x = dataset[:, 0:len_col-1]     #特征矩阵：x
    x = dataset[:, 1:len_col - 1]  # 特征矩阵：x
    y = dataset[:, len_col - 1]  # 目标变量：y
    fp_model.write("shape of dataset, x, y: " + str(dataset.shape) + "\t" +
                   str(x.shape) + "\t" + str(y.shape) + "\n")
   
    # 数据切分：
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    
    # 数据预处理：归一化
    min_max_scaler = preprocessing.MinMaxScaler()
    x_train_minMax = min_max_scaler.fit_transform(x_train)  # 训练并转换特征矩阵： (x-min)/(max-min)
    fp_model.write("\nx_train_min(parameters):\n" + str(x_train.min(axis=0)) + "\n")
    fp_model.write("\nx_train_max(parameters):\n" + str(x_train.max(axis=0)) + "\n")
    fp_para.write(str(x_train.min(axis=0).tolist()) + "\n")
    fp_para.write(str(x_train.max(axis=0).tolist()) + "\n")
    print "train logistic-regression"
    # LR模型
    # print  x_train.
    clf = LogisticRegression(C=3)
    clf.fit(x_train_minMax, y_train)
    fp_model.write("\ncoefficient(parameters):\n" + str(clf.coef_) + "\n")  # 系数矩阵
    fp_model.write("intercept(parameters):" + str(clf.intercept_) + "\n")  # 截距
    fp_para.write(str(clf.coef_[0].tolist()) + "\n")
    fp_para.write(str(clf.intercept_.tolist()) + "\n")
    print "logistic-regression  OK"
    # 指标计算: precision, recall, auc
    print "print zhibiao"
    x_test_minMax = min_max_scaler.transform(x_test)
    predict = clf.predict(x_test_minMax)
    predict_pro = clf.predict_proba(x_test_minMax)[:, 1]
    # clf模型给出预估的概率,predict_proba返回的是一个两列的矩阵，第一列代表该事件不会发生的概率，第二列代表的是该事件会发生的概率
    # report = predict_pro > 0.5
    report = predict_pro > 0.7
    fp_model.write("\ny_test: " + str(y_test) + "\n")
    fp_model.write("report: " + str(report) + "\n")
    neg_pos_zhibiao = classification_report(y_test, report, target_names=['neg', 'pos'])  # 正确率和召回率
    fp_model.write("\n" + str(neg_pos_zhibiao) + "\n")

    r = clf.score(x_test_minMax, y_test)
    rtrain = clf.score(x_train_minMax, y_train)
    print "模型拟合度：" +str(rtrain)+"\n"
    print "模型准确率: " + str(r) + "\n"
    auc = roc_auc_score(y_test, predict_pro)  # auc计算
    print "AUC: " + str(auc) + "\n"

    fp_model.close()
    fp_para.close()
    return 0
    # LR模型，交叉验证
    # t_min_max_scaler = preprocessing.MinMaxScaler()
    # x_minMax = t_min_max_scaler.fit_transform(x)       #训练并转换特征矩阵： (x-min)/(max-min)
    # scores = cross_val_score(LogisticRegression(), x_minMax, y, cv=10)
    # log_data = str(scores) + "\n"
    # log_data += "Accuracy: %0.2f (+/- %0.2f): " + str(scores.mean()) + "\t" + str(scores.std()*2) + "\n"
    # #平均精度，及模型稳定性
    # fprint(log_data)
    # return 0


if __name__ == "__main__":
    main()
