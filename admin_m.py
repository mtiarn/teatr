import data as m
import datetime
import random
class administrator:
    
    def a_date(self):

        print(m.theatre)
        ans=input('Вы хотите добавить или удалить спектакль?(Д/У): ')
        if ans=='Д' or ans=='д':
            self._name=input('Введите название спектакля: ')
            self._date=input('Введите дату спектакля (ДД.ММ.ГГГГ): ')
            m.theatre.update({self._name:self._date})
        if ans=='У' or ans=='у':
            d=input('Какой спектакль удалить? ')
            del m.theatre[d]
        print('Утвержденные спектакли: ', m.theatre)
    
    def a_rep(self):
        ans=input('Просмотреть утвержденые репетиции или предложения? (У/П): ')
        if ans=='У' or ans=='у':
            print('Утвержденные репетиции:', sorted(m.a_training, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y')))
            answ=input('Внести изменения в расписание? (Д/Н): ')
            if answ=='Д' or answ=='д':
                ans=input('Вы хотите добавить или удалить репетицию?(Д/У): ')
                if ans=='Д' or ans=='д':
                    self.a_date=input("Введите дату (ДД.ММ.ГГГГ): ")
                    m.a_training.append(self.a_date)
                    print('Даты репетиций: ', sorted(m.a_training, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y')))
                if ans=='У' or ans=='у':
                    d=input('Какую репетицию удалить? ')
                    m.a_training.remove(d)
                    print('Утвержденные репетиции: ', sorted(m.a_training, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y')))
            if answ=='Н' or answ=='н':
                return
        if ans=='П' or ans=='п':
            print('Утвержденные репетиции: ', m.a_training)
            print('Предложенные репетиции: ', m.training)
            answ=input('Утвердить репетиции? (Д/Н): ')
            if answ=='Д' or answ=='д':
                self.a_date=input("Введите дату (ДД.ММ.ГГГГ): ")
                m.a_training.append(self.a_date)
                m.training.remove(self.a_date)
                if len(m.training)==0:
                    m.training=None
                print('Даты репетиций: ', sorted(m.a_training, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y')))
            if answ=='Н' or answ=='н':
                return
    
    def a_suit(self):
        print('Утвержденные костюмы: ', m.suits)
        print('Заявки на костюмы: ', m.app_suit)
        ans=input('Утвердить костюмы? (Д/Н): ')
        if ans=='Д' or ans=='д':
            self.a_suit=input('Выберите костюм:')
            for i in range(len(m.app_suit)):
                for j in range(len(m.app_suit[i])):
                    if m.app_suit[i][j]==self.a_suit:
                        m.suits.append(m.app_suit[j])
                m.app_suit.remove(m.app_suit[i])
                if len(m.app_suit)==0:
                    m.app_suit=None
        print('Утвержденные костюмы: ', m.suits)
        print('Заявки на костюмы: ', m.app_suit)
        if ans=='Н' or ans=='н':
            return
    
    def true_res_tik(self):
        print('Запрос резервации билетов: ', m.res_tik_point)
        ans=input('Подтвердить резервацию? (Д/Н): ')
        if ans=='Д' or ans=='д':
            self.trt=input('Введите номер билета: ')
            m.true_res_tik.append(m.res_tik_point[int(self.trt)-1])
            print('Одобренные билеты: ', m.true_res_tik)
        if ans=='Н' or ans=='н':
            return