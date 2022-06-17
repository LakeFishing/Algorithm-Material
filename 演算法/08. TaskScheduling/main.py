#Chap 16. Greedy Algorithms
#Page 16-12

import operator

n = 10 #工作數量
jobs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #工作編號
deadline = [3, 2, 5, 5, 4, 2, 2, 4, 3, 4]
profit = [100, 10, 15, 27, 36, 58, 62, 43, 52, 65]

result = [ None ] * max(deadline) #總工作天數不會超過 deadline 的最大值
schedule = []
sum = 0

#將三筆資料綁定
class Scheduling:
    def __init__(self, jobs, deadline, profit):
        self.jobs = jobs
        self.deadline = deadline
        self.profit = profit

#將綁定完的資料存入 schedule 清單中
for i in range(n):
    schedule.append(Scheduling(jobs[i], deadline[i], profit[i]))

#將 schedule 中的綁定資料以 profit 由大至小排序
schedule.sort(key = operator.attrgetter('profit'), reverse = True)

def insert(task):
    if (task.deadline == 0): #若 deadline 為 0 則跳出函式
        return
    if (result[task.deadline - 1] == None): #若該天的行程為 None 則插入工作
        result[task.deadline - 1] = task
    else: #若該天的行程不為 None 則繼續搜尋該工作在 deadline 前是否有行程為 None
        task.deadline -= 1 #往前一天搜尋
        insert(task)
        task.deadline += 1 #將 deadline 恢復成初始值

#將已排序過的 schedule 清單按條件依序插入 result 行程清單
for i in schedule:
    insert(i)
print('\n')
for i in result:
    print('第 %1d 天 | 工作編號：%2d | 利潤：%3d | 期限：%1d' %(result.index(i) + 1, i.jobs, i.profit, i.deadline))
    sum += i.profit
print('\n')
print('總利潤：%3d' %(sum))
print('\n')
