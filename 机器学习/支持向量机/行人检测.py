import os
import numpy as np
import cv2

#1.导入数据集
pwd = os.getcwd()
pos_dir = os.path.join(pwd, 'INRIAPerson','Train','pos')
pos = os.listdir(pos_dir)
neg_dir = os.path.join(pwd, 'INRIAPerson','Train','neg')
neg = os.listdir(neg_dir)
test_dir = os.path.join(pwd, 'INRIAPerson','Test','pos')
test = os.listdir(test_dir)

#2.创建训练数据
samples = []
labels = []
for f in pos:
    file_path = os.path.join(pos_dir, f)
    if os.path.exists(file_path):
        samples.append(file_path)
        labels.append(1.)
for f in neg:
    file_path = os.path.join(neg_dir, f)
    if os.path.exists(file_path):
        samples.append(file_path)
        labels.append(-1.)
labels = np.int32(labels)
labels_len = len(pos) + len(neg)
labels = np.resize(labels, (labels_len, 1))

train = []
num = 0.
total = len(samples)
for f in samples:
    num += 1.
    hog = cv2.HOGDescriptor((64, 128), (16, 16), (8, 8), (8, 8), 9)
    img = cv2.imread(f, 0)
    img = cv2.resize(img, (64, 128))
    descriptors = hog.compute(img)
    train.append(descriptors)

train = np.float32(train)
train = np.resize(train, (total, 3780))

svm = cv2.ml.SVM_create()
svm.setCoef0(0.0)
svm.setDegree(3)
criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 1000, 1e-3)
'''
—–cv2.TERM_CRITERIA_EPS :精确度（误差）满足epsilon停止。 
—- cv2.TERM_CRITERIA_MAX_ITER：迭代次数超过max_iter停止。 
—-cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER，两者合体，任意一个满足结束。 
'''
svm.setTermCriteria(criteria)
svm.setGamma(0.01)#把gamma设置成0.01，这样训练收敛速度会快很多
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setNu(0.5)
svm.setP(0.1)  # for EPSILON_SVR, epsilon in loss function?
svm.setC(0.01)  # From paper, soft classifier
svm.setType(cv2.ml.SVM_EPS_SVR)#设置svm的类型
svm.train(train, cv2.ml.ROW_SAMPLE, labels)#train是x变量，labels是y变量
model_path = os.path.join(pwd, 'svm.xml')
svm.save(model_path)

sv = svm.getSupportVectors()
rho, _, _ = svm.getDecisionFunction(0)#决策函数，rho是偏置
'''将alpha矩阵同support vector 相乘，得到一个行向量，将该向量前面乘以-1之后，在该
行向量的最后添加一个元素rho。如此得到一个分类器，利用该分类器替换opencv行人检测中
默认的分类器
'''
sv = np.transpose(sv)
s=np.append(sv, [[-rho]], 0)


hog = cv2.HOGDescriptor()
hog.setSVMDetector(s)
cv2.namedWindow('Detect')

for f in test:
    file_path = os.path.join(test_dir, f)
    img = cv2.imread(file_path)
    rects, _ = hog.detectMultiScale(img, winStride=(2,2), padding=(8, 8), scale=1.05)
    '''
    当我们用训练好的模型去检测测试图像时，我们会用到detectMultiScale() 这个函数来对图像进行多尺度检测
    winStride(可选):HoG检测窗口移动时的步长(水平及竖直)。winStride和scale都是比较重要的参数，需要合
    理的设置。一个合适参数能够大大提升检测精确度，同时也不会使检测时间太长。
    padding(可选):在原图外围添加像素，适当的pad可以提高检测的准确率（可能pad后能检测
    到边角的目标？）常见的pad size 有(8, 8), (16, 16), (24, 24), (32, 32).
    scale(可选):图像金字塔，也就是图像的多尺度表示。每层图像都被缩小尺寸并用gaussian平滑。
    scale参数可以具体控制金字塔的层数，参数越小，层数越多，检测时间也长.通常scale在1.01-1.5这个区间.
    '''
    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)  # 2是所画的线的宽度
        # x,y是矩行左上角的坐标，w,h是矩阵的宽和高
        #cv2.putText(img, 'face', (w / 2 + x, y - h / 5), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 255, 255), 2, 1)
        #cv2.putText(img, "face count", (20, 20), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 255, 255), 2, 1)
        cv2.putText(img, str(len(rects)), (230, 20), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 255, 255), 2, 1)
#各参数依次是：图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细
    cv2.imshow('Detect', img)
    c = cv2.waitKey(0) & 0xff
    if c == 27:
        break

cv2.destroyAllWindows()
