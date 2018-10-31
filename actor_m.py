import data as d
import datetime
import random
class actor:
    
    def date(self):
        k1=0
        self.name=input("Введите название спектакля: ")
        for i in d.theatre:
            if self.name==i:
                print("Дата проведения спектакля: ",d.theatre[i])
                k1+=1
                break
        if k1==0:
            print('Спектакль отсутствует')
    
    def rep(self):
        self.date=input("Введите дату (ДД.ММ.ГГГГ): ")
        d.training.append(self.date)
        d.write()
        print('Желаемые даты репетиций: ', sorted(d.training, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y')))
    
    def suit(self):
        self.app=input('Введите данные костюма (Название, размер, вид): ')
        d.app_suit.append(self.app.split(','))
        print('Заявки на костюмы: ', d.app_suit)
    
    def w_suit(self):
        print('Утвержденные костюмы: ', d.suits)
    
    def res_tik(self):
        k2=0
        n=0
        while n<=5:
            ans=input('Вы хотите заказать билет? (Да/Нет): ')
            if ans=='Да' or ans=='да':
                if n<5:
                    res_tik={'Спектакль':'','Дата':'','Цена':'','Ряд':'','Место':''}
                    self.name=input('Введите желаемый спектакль: ')
                    for i in d.theatre:
                        if self.name==i:
                            self.price=input('Введите желаемую цену: ')
                            res_tik['Спектакль']=self.name
                            res_tik['Дата']=d.theatre[i]
                            res_tik['Цена']=self.price
                            res_tik['Ряд']=random.randint(1,10)
                            res_tik['Место']=random.randint(1,30)
                            for i in res_tik:
                                if res_tik['Спектакль'] in res_tik and res_tik['Дата'] in res_tik and res_tik['Ряд'] in res_tik and res_tik['Место'] in res_tik:
                                    res_tik['Ряд']=random.randint(1,10)
                                    res_tik['Место']=random.randint(1,30)
                            d.res_tik_point.append(res_tik)
                            n+=1
                            print('\nЗапрос резервации билетов: ', d.res_tik_point)
                            print('Желаемых билетов: ', n)
                            print('')
                            k2+=1
                            break
                    if k2==0:
                        print('Спектакль не найден!\n')
                        break
                else:
                    print('Вы уже заказали 5 билетов!\n')
                    break
            if ans=='Нет' or ans=='нет':
                break