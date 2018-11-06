def jaya(*argv):
    pop_size, Gen, lb, ub = argv
    lb=np.array(mini)
    ub=np.array(maxi)
    p1=initialpopulation(lb,ub,pop_size)
    p1['f']=myobj(p1)
    dim=len(lb)
    gen=0
    best=[]
    while (gen<Gen):
        new_p1=updatepopulation(p1,dim)
        new_p1=trimr(new_p1,lb,ub)
        new_p1['f']=myobj(new_p1)
        p1=greedyselector(p1,new_p1)
        gen=gen+1
    #     print(gen)
        best=p1['f'].min()
        xbest=p1.loc[p1['f'].idxmin()][0:dim].tolist()
#     print('Best={}'.format(best))
#     print('xbest={}'.format(xbest))
    return best,xbest