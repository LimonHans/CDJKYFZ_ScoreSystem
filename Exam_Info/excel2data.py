import pandas as pd

####################################################
# The following parts(to "END") are not completed. #
####################################################

input_file = pd.read_excel("2019级高二上期期末模拟（理科）-总分-成绩榜.xls")

#######
# END #
#######

data = input_file.iloc[1:].values
print(data)

Rank_Overall = data[:, 0]# 年级排名 -- 0
Name = data[:, 1]# 姓名 -- 1
Id = data[:, 2]# 考号 -- 2
Number = data[:, 3]# 学籍号 -- 3
Class = data[:, 4]# 班级 -- 4
Rank_Class = data[:, 5]# 班级排名 -- 5
Score_Overall = data[:, 6]# 总分 -- 6
Score_YW = data[:, 7]# 语文得分 -- 7
Score_SX = data[:, 8]# 数学得分 -- 8
Score_WY = data[:, 9]# 外语得分 -- 9
Score_WL = data[:, 10]# 物理得分 -- 10
Score_HX = data[:, 11]# 化学得分 -- 11
Score_SW = data[:, 12]# 生物得分 -- 12
#Finder = dict()# map