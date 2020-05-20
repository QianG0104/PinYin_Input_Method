import time


rec={}

#读取一二级汉字表，以每个汉字为key，以新建字典为value，建立字典rec

def load_single_chs_to_rec():
    file=open('chs')
    line=list(file.readlines()[0])
    for c in line:
        rec[c]={'num':0.0}
    # print(rec)

def init_rec_after_load():
    print('loading sinanews')
    #wiki_chs.split
    file=open('sinanews')
    for line in file.readlines():
        l=list(line)
        while ' ' in l:
            l.remove(' ')
        len=l.__len__()
        for i in range(0,len):
            if l[i] in rec:
                rec[l[i]]['num']=rec[l[i]]['num']+1
            if i+1<len:
                if l[i] in rec and l[i+1] in rec:
                    if l[i+1] not in rec[l[i]]:
                        rec[l[i]][l[i+1]]=1
                    else:
                        rec[l[i]][l[i + 1]]=rec[l[i]][l[i+1]]+1
    print('finished')

def save_rec():
    for key in rec:
        f=open(str(key)+'.txt','w')
        f.write(str(rec[key]))

# check_rec={}
#
# def check():
#     for key in rec:
#         f=open(str(key)+'.txt','r')
#         dict=eval(f.read())
#         for key in dict:
#             print(dict[key]+1)



if __name__ == '__main__':
    start=time.process_time()

    load_single_chs_to_rec()
    init_rec_after_load()
    save_rec()
    # print(rec)

    end=time.process_time()

    print('Running Time: ',end-start,' s')



# f=open('wiki_chs.split')
# print('loading wiki_chs.split')
#
# for line in f.readlines():
#     L=line.split()
#     for c in L:
#         print(c)
