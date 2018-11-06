def updatepopulation(p1,dim):
    best_x=np.array(p1.loc[p1['f'].idxmin][0:dim])
    worst_x=np.array(p1.loc[p1['f'].idxmax][0:dim])
    new_x=[]
    
    for i in range(len(p1)): 
        old_x=np.array(p1.loc[i][0:dim])
        r1=np.random.random(dim)
        r2=np.random.random(dim)
        new_x.append(old_x+r1*(best_x-abs(old_x))-r2*(worst_x-abs(old_x)))
    new_p1=pd.DataFrame(new_x)
    return new_p1