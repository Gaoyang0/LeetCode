import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import pickle
import math


def auc_calculate(labels, preds, n_bins=100):
    postive_len = sum(labels)
    negative_len = len(labels) - postive_len

    if postive_len == 0:
        print("标签中正例个数为0")

    if negative_len == 0:
        print("neg0000000000000000000000000000000000000000")

    total_case = postive_len * negative_len
    pos_histogram = [0 for _ in range(n_bins)]
    neg_histogram = [0 for _ in range(n_bins)]
    bin_width = 1.0 / n_bins

    for i in range(len(labels)):
        nth_bin = int(preds[i]*0.99999999999/bin_width)
        if labels[i]==1:
            pos_histogram[nth_bin] += 1
        else:
            neg_histogram[nth_bin] += 1
    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(n_bins):
        satisfied_pair += (pos_histogram[i]*accumulated_neg + pos_histogram[i]*neg_histogram[i]*0.5)
        accumulated_neg += neg_histogram[i]

    return satisfied_pair / float(total_case)




def precision_recall_at_k(k, ranked_list, test_user_item):
    '''
    ranked_list:表示排好序的推荐列表
    test_user_item:表示test集里用户喜爱的物品
    '''
    hits = [val for val in ranked_list if val in test_user_item]
    count = len(hits)

    return float(count / k), float(count / len(test_user_item))


def map_mrr_ndcg_at_k(k, ranked_list, test_user_item):
    '''
    ranked_list:表示排好序的推荐列表
    test_user_item:表示test集里用户喜爱的物品
    '''
    ap = 0
    map = 0
    dcg = 0
    idcg = 0
    mrr = 0

    for i in range(min(len(test_user_item), k)):
        idcg += 1 / math.log(i + 2, 2)

    b1 = ranked_list
    b2 = test_user_item
    s2 = set(b2)
    hits = [(idx, val) for idx, val in enumerate(b1) if val in s2]
    count = len(hits)

    for c in range(count):
        ap += (c + 1) / (hits[c][0] + 1)
        # hits[c][0] + 2,其中+2是因为idx是从0开始取的, 公式是+1,但是idx是从1开始取的
        dcg += 1 / math.log(hits[c][0] + 2, 2)

    if count != 0:
        mrr = 1 / (hits[0][0] + 1)

    if count != 0:
        map = ap / count

    return map, mrr, float(dcg / idcg)


def AUC(label, pre):
    '''
    首先要明白ＡＵＣ的物理含义不仅是ＲＯＣ曲线下的面积，ＡＵＣ还有另外一个物理含义就是：
    给定正样本Ｍ个，负样本Ｎ个，以及他们的预测概率（０－１）之间，那么ＡＵＣ的含义就是所有穷举所有的正负样本对，
    如果正样本的预测概率大于负样本的预测概率，那么就＋１；如果如果正样本的预测概率等于负样本的预测概率，那么就＋0.5,　
    如果正样本的预测概率小于负样本的预测概率，那么就＋０；最后把统计处理的个数除以Ｍ×Ｎ就得到我们的ＡＵＣ
    '''
    # 计算正样本和负样本的索引，以便索引出之后的概率值
    pos = [i for i in range(len(label)) if label[i] == 1]
    neg = [i for i in range(len(label)) if label[i] == 0]

    auc = 0
    for i in pos:
        for j in neg:
            if pre[i] > pre[j]:
                auc += 1
            elif pre[i] == pre[j]:
                auc += 0.5

    return auc / (len(pos) * len(neg))

if __name__ == "__main__":
    label = [0, 0, 1, 1, 1, 1]
    score = [0.0, 0.8, 0.9, 0.2, 1, 0.9]

    auc = auc_calculate(label, score, 10)
    print(auc)

    auc = AUC(label, score)
    print(auc)
