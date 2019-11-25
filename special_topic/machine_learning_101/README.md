## What
### 1. Machine learning model

是机器学习算法产出的结果，可以将其看作是在给定输入情况下、输出一定结果的函数 (function) F

机器学习模型不是预先定义好的固定函数，而是从历史数据中推导出来的。因此，当输入不同的数据时，机器学习算法的输出会发生变化，即机器学习模型发生改变

***机器学习的任务，就是从广阔的映射空间中学习函数***

### 2. Supervised vs Unsupervised
* supervised learning
* unsupervised learning
  * clustering
  * association: 发现样本属性之间隐藏的关联模式，例如频繁项集挖掘算法：
    * Apriori
    * [FPGrowth](https://www.ibm.com/developerworks/cn/analytics/library/machine-learning-hands-on2-fp-growth/index.html)
    * TODO: 算法待实现
* semi-supervised learning

    通过将有监督和无监督的学习结合在一个只有少量标记的数据集中，人们可以更好地利用数据集，并获得比单独应用它们更好的结果

### 3. Classification vs Regression
* classification
* regression
    
    一些机器学习模型（例如决策树）可以直接处理非数字特征，而更多时候人们必须以某种方式将这些非数字特征转换（transform）为数字特征
* 问题转化
    
    人们经常应用一种称为逻辑回归（Logistic Regression）的机器学习模型，这种模型将连续概率值作为输出，但用于解决分类问题

## How
### 1. Workflow
***构建机器学习模型的工作流是以数据为中心的***

row data -> feature engineering (split, normalize, clean) -> train/test data -> model -> hyper-parameter tuning
### 2. Data
模型所能达到的性能上限是由数据决定的

现实世界中，在有利的情况下，我们得到的数据可能反映了现实的一部分，而在不利的情况下就可能是一些干扰判断的噪音，在最糟糕的情况下，甚至会与现实相矛盾。不管机器学习算法如何，人们都无法从包含太多噪音或与现实不符的数据中学到任何东西
### 3. Underfitting vs Overfitting
泛化: 它衡量从训练数据导出的模型对不可见数据的期望属性的预测能力
* underfitting
    
    不能很好地拟合训练数据的模型，即显著偏离真实值的模型。原因可能是：
    
    * 模型对于数据而言过于简化，因此**无法捕捉数据中隐藏的关系**

    措施： 需要选择一种能够从训练数据集生成更复杂模型的替代算法
* overfitting

    过拟合模型是与训练数据拟合较好的模型，即误差很小或没有误差，但不能很好地推广到不可见数据

    与欠拟合相反，过拟合往往是一个能够适应每一位数据的超复杂模型，但却可能会陷入噪音和误差的陷阱

    措施： 
    1. 可以尝试另一种从训练数据集生成更简单的模型的算法 
    2. 添加正则化（regularization）项，即对过于复杂的模型进行附加处理，从而引导算法在拟合数据的同时生成一个不太复杂的模型

## Why
### 1. Why important？
***“在 Facebook 上，机器学习提供了驱动用户体验几乎所有方面的关键功能……机器学习广泛应用于几乎所有的服务。”***

以下是关于 ML 如何在 Facebook 中应用的几个示例：

* 新闻提要中的事件排序是通过 ML 进行的
* 显示广告的时间、地点和对象由 ML 确定
* 各种搜索引擎（如照片、视频、人物）都是由ML支持的
### 2. Can ML do everything?
***需要一种整体的方法来改进模型，而不是逐例修补模型***
在偏重模型可解释性的场景中，应该仔细考量应用基于神经网络的 ML 模型的决定

概括地说，ML不是灵丹妙药，因为它常常无法达到100% 精确，而且我们不能逐例更正 ML 模型，在某些情况下，我们甚至无法对 ML 模型进行推理