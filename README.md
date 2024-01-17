# FundBackTesting

该代码基于给定的历史数据进行基金数据回测，并在提供了每月定投、手续费计算、再平衡等功能。



**回测是基于历史数据，不能代表预测！！**


### 说明

1. 不支持货币类基金
1. 第一个月初始化后，不再定投资金，而是到第二月才开始定投。
1. 定投和再平衡可能会在同一天发生。
1. 再平衡的资金将不会视为新增资金。


### 使用

1. Python运行：
   1. `pip install -r requirements.txt`安装依赖文件。
   2. 修改需要回测的基金基础数据py文件`fundsParam.py`，其中为作者测试的基金样本，按照格式修改为你要测试的基金。
   3. 在文件`fundbacktesting.py`设定`loseStatusAssignFundCode`值，用于当发现缺失数据基金的时候，将比例添加至`loseStatusAssignFundCode`指定的基金，如基金数据是从2018年开始，但部分基金是从2019或者2020年开始，这部分基金将被视为后期增加的基金，当新基金出现数据后，将马上进行再平衡。
   4. 在文件`fundbacktesting.py`设定`startDate`和`endDate`值，按照给定样本设定，该部分会影响到手动复制数据做回测，也会影响到设置好了爬虫后，自动进行数据的获取。
   5. 获取数据：第一种使用爬虫，需要对`FundBT.py`的`getFundData`方法中设定`headers`请求头和`url_Template`请求URL字符串模版。
   6. 获取数据：第二种则是通过手动复制，需要保持数据至少有两列数据，列名必须为`FSRQ`（基金日期）和`DWJZ`（基金日期对应的净值），然后数据保存为`csv`或者`xlsx`文件格式存放至代码目录下的`data`目录，同时文件名字需要按照格式为“基金编码-开始日期-结束日期.csv/xlsx”保存，这里的开始时间和结束时间需要与数据的时间和第4步骤设定对应。
   7. `python fundbacktesting.py`。
2. Jupyter运行：
   1. 通过`fundbacktesting.ipynb`文件设定上面的值
   2. Jupyter运行会多输出图表，对于表格类输出更友好。





