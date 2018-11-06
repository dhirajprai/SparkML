def trimr(new_p1,lb,ub):
    col=new_p1.columns.values
    for i in range(len(p1)):
        for j in range(len(col)):
            if new_p1.loc[i][j]>ub[j]:
                new_p1.loc[i][j]=ub[j]
            elif new_p1.loc[i][j]<lb[j]:
                new_p1.loc[i][j]=lb[j]
    return new_p1