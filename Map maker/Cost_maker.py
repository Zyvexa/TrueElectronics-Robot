# принимает данные вида: место цена
# наиример: M11 0
arr_place =[]
arr_cost =[]
while 1:
    fromm, to = input().split()
    if fromm == '-1': break
    arr_from.append(fromm)
    arr_to.append(to)
    
for i in range(len(arr_place)):
    print(f'nodes[{arr_place[i]}].cost = {arr_cost[i]};')
    