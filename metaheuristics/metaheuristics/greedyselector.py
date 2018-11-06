def greedyselector(p1,new_p1):
    for i in range(len(p1)):
        if p1.loc[i]['f']>new_p1.loc[i]['f']:
            p1.loc[i]=new_p1.loc[i]
    return p1