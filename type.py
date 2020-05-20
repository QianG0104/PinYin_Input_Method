import time
import math
import copy

p=[]
pyhz={}

def load_pyhz():
    file=open('pyhz')
    for l in file.readlines():
        line=l.split()
        k=line.pop(0)
        pyhz[k]=line

def veterbi_level(py):
    lvl={'all':0.0}
    for hz in pyhz[py]:
        lvl[hz]={'p':0.0,'str':hz}
        f=open(hz+'.txt')
        temp=eval(f.read())
        lvl['all']=lvl['all']+temp['num']
        f.close()
    # print(lvl)
    return lvl

def P_x1x2(x1,x2,all1,all2):
    f1=open(x1+'.txt')
    x1_dict=eval(f1.read())
    f2=open(x2+'.txt')
    x2_dict=eval(f2.read())

    if x2 in x1_dict:
        p1=x1_dict[x2]/x1_dict['num']
        p2=x2_dict['num']/all2
        P=(20*p1+p2)/2
    else:
        P=0
    P=-math.log(P+0.0000001)

    f1.close()
    f2.close()

    return P

def P_x2(x2,all2):
    f2=open(x2+'.txt')
    x2_dict=eval(f2.read())
    P=x2_dict['num']/all2
    P=-math.log(P+0.0000001)
    f2.close()
    return P

def level_link_to_hz(vl,hz,all2):
    tempvl1 = copy.deepcopy(vl)
    # print('tempvl1: ',tempvl1)
    for key1 in tempvl1:
        if key1!='all':
            tempvl1[key1]['p']=P_x1x2(key1,hz,tempvl1['all'],all2)+tempvl1[key1]['p']
    return tempvl1

def link(vl1,vl2):
    for key2 in vl2:
        if key2!='all':
            tempvl1=copy.deepcopy(level_link_to_hz(vl1,key2,vl2['all']))
            del tempvl1['all']
            # tempvl1=vl1
            # print(key2,tempvl1)
            # for key1 in tempvl1:
            #     if key1!='all':
            #         all1=tempvl1['all']
            #         all2=vl2['all']
            #         tempvl1[key1]['p']=P_x1x2(key1,key2,all1,all2)+vl1[key1]['p']
            # del tempvl1['all']

            k=min(tempvl1,key=lambda x:tempvl1[x]['p'])

            vl2[key2]['p']=tempvl1[k]['p']
            vl2[key2]['str']=tempvl1[k]['str']+vl2[key2]['str']

def listen():
    global p
    p.clear()
    l=input()
    p=l.split()

    head=veterbi_level(p.pop(0))
    for key in head:
        if key!='all':
            head[key]['p']=P_x2(key,head['all'])
    # print(head)

    for temp in p:
        next=veterbi_level(temp)
        link(head,next)
        head=next
    # print(head)
    return head

    # for temp in p:
    #     veterbi_level(temp)
    # print(p)

if __name__ == '__main__':
    load_pyhz()
    while 1:
        print('>>>')
        resultdic=copy.deepcopy(listen())
        del resultdic['all']
        k = min(resultdic, key=lambda x: resultdic[x]['p'])
        print(resultdic[k]['str'])
    # print(pyhz)