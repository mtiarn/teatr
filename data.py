text_file = open("препы.txt", "r", encoding='utf-16')
training = text_file.read().split(',')
text_file2 = open("костюмы.txt", "r", encoding='utf-16')
suits = text_file2.read().split(',')
text_file3 = open("заявкост.txt", "r", encoding='utf-16')
app_suit = text_file3.read().split(',')
text_file4 = open("урепы.txt", "r", encoding='utf-16')
a_training = text_file4.read().split(',')
suits= [suits[i:i + 3] for i in range(0, len(suits), 3)]
app_suit= [app_suit[i:i + 3] for i in range(0, len(app_suit), 3)]
with open('даты.txt', encoding='utf-16') as f:
    theatre = dict(x.rstrip().split(',', 1) for x in f)
    
text_file5 = open("rezerv.txt", "r", encoding='utf-16')
z = text_file5.read().split(',')
res_tik={'Спектакль':'','Дата':'','Цена':'','Ряд':'','Место':''}
res_tik_point=[]
while len(z)>4:
    res_tik={'Спектакль':'','Дата':'','Цена':'','Ряд':'','Место':''}
    res_tik['Спектакль']=z[0]
    res_tik['Дата']=z[1]
    res_tik['Цена']=z[2]
    res_tik['Ряд']=z[3]
    res_tik['Место']=z[4]
    for i in range(0,5):
        del z[0]
    res_tik_point.append(res_tik)

text_file6 = open("rezervtrue.txt", "r", encoding='utf-16')
z = text_file6.read().split(',')
true_res_tik=[]
while len(z)>4:
    res_tik={'Спектакль':'','Дата':'','Цена':'','Ряд':'','Место':''}
    res_tik['Спектакль']=z[0]
    res_tik['Дата']=z[1]
    res_tik['Цена']=z[2]
    res_tik['Ряд']=z[3]
    res_tik['Место']=z[4]
    for i in range(0,5):
        del z[0]
    true_res_tik.append(res_tik)
    
def write():
    open("препы.txt","w", encoding='utf-16').close()
    f = open("препы.txt","w", encoding='utf-16')
    for i in range(len(training)):
        f.write(str(training[i]))
        f.write(',')
    f.close()
    open("урепы.txt","w", encoding='utf-16').close()
    g = open("урепы.txt","w", encoding='utf-16')
    for i in range(len(a_training)):
        g.write(str(a_training[i]))
        g.write(',')
    g.close()
    open("костюмы.txt","w", encoding='utf-16').close()
    q = open("костюмы.txt","w", encoding='utf-16')
    for i in range(len(suits)):
        q.write(str(suits[i]))
        q.write(',')
    q.close()   
    open("заявкост.txt","w", encoding='utf-16').close()
    e = open("заявкост.txt","w", encoding='utf-16')
    if len(app_suit)!=0:
        for i in range(len(app_suit)):
            e.write(str(app_suit[i]))
            e.write(',')
    e.close()
    open("rezerv.txt","w", encoding='utf-16').close()
    t = open("rezevr.txt","w", encoding='utf-16')
    for i in range(len(res_tik_point)):
        for j,k in res_tik_point[i].items():
            t.write(str(k))
            t.write(',')
    t.close()
    open("truerezerv.txt","w", encoding='utf-16').close()
    m = open("truerezevr.txt","w", encoding='utf-16')
    for i in range(len(true_res_tik)):
        for j,k in true_res_tik[i].items():
            m.write(str(k))
            m.write(',')
    t.close()    