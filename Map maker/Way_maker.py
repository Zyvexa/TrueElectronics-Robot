# принимает данные вида: от до
# наиример: M11 P21
arr_from =[]
arr_to =[]
while 1:
    fromm, to = input().split()
    if fromm == '-1': break
    arr_from.append(fromm)
    arr_to.append(to)
    
for i in range(len(arr_from)):
    print(f'edges[{i}].from = {arr_from[i]};')
    print(f'edges[{i}].to = {arr_to[i]};')
    print(f'edges[{i}].cost = 0;')
