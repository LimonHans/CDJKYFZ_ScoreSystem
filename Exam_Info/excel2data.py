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

#'G' names for 'Goal'
#Gscore_Overall = []# 总成绩分段，每一个段占两个空
# 这个功能合并至具体的展示界面

Gstudent_Numall = len(Rank_Overall)# 参考的所有人数
Gstudent_NumActual = Gstudent_Numall# 有效参考人数(任何一个科目都不为零)
while (not(Score_YW[Gstudent_NumActual - 1] != 0 and Score_SX[Gstudent_NumActual - 1] != 0 and Score_WY[Gstudent_NumActual - 1] != 0 and Score_WL[Gstudent_NumActual - 1] != 0 and Score_HX[Gstudent_NumActual - 1] != 0 and Score_SW[Gstudent_NumActual - 1] != 0)):
    Gstudent_NumActual -= 1
print(Gstudent_Numall)
print(Gstudent_NumActual)

GQ1 = []
GQ2 = [sum(Score_Overall)/2, sum(Score_YW)/2, sum(Score_SX)/2, sum(Score_WY)/2, sum(Score_WL)/2, sum(Score_HX)/2, sum(Score_SW)/2]
GQ3 = []
for i in range(0, 7):
    GQ1.append(GQ2[i]/2)
    GQ3.append(GQ1[i]*3)
print(GQ1)
print(GQ2)
print(GQ3)