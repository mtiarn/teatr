import admin_m
import actor_m
import data as n
ac=actor_m.actor()
ad=admin_m.administrator()
actors={'user1': '123', 'user2': '1234'}
admins={'volik':'2018','gladkov':'8978','milovanov':'4534'}
k=0
access=-1
action=0
act=True
def enter():
    k=False
    global access
    while k==False:
        log = input("Введите логин: ")
        pas = input("Введите пароль: ")
        for i,j in actors.items():
            if log==i and pas==j:
                print('Вы вошли как "Актер"')
                access=0
                k=True
                actions()
                    
        for i,j in admins.items():
            if log==i and pas==j:
                print('Вы вошли как "Администратор"')
                access=1
                k=True
                actions()
        
        if k==False:
            print('Неверный логин или пароль, попробуйте снова')

def actions():
    global action
    global act
    if access==0:
        while act==True:
            print('Выберете действите: посмотреть даты спектаклей - 1, Оставить пожелания на даты репетиций - 2, Оставить заявку на костюмы - 3, Посмотреть список костюмов - 4, Зарезервировать билеты - 5, Сменить пользователя - 6')
            action=input()
            if action=='1':
                ac.date()
                n.write()
            if action=='2':
                ac.rep()
                n.write()
            if action=='3':
                ac.suit()
                n.write()
            if action=='4':
                ac.w_suit()
                n.write()
            if action=='5':
                ac.res_tik()
                n.write()
            if action=='6':
                enter()                
            new=input('Хотите выполнить другое действие? (Да/Нет) ')
            if new=='Да' or new=='да':
                pass
            if new=='Нет' or new=='нет':
                act=False

    if access==1:
        while act==True:
            print('Выберете действите: Назначить дату спектакля - 1, Управление репетициями - 2, Управление заявками на костюмы и их списками - 3, Одобрить зарезервированные билеты - 4, Сменить пользователя - 5')
            action=input()
            if action=='1':
                ad.a_date()
                n.write()
            if action=='2':
                ad.a_rep()
                n.write()
            if action=='3':
                ad.a_suit()
                n.write()
            if action=='4':
                ad.true_res_tik()
                n.write()
            if action=='5':
                enter()                
            new=input('Хотите выполнить другое действие? (Да/Нет) ')
            if new=='Да' or new=='да':
                pass
            if new=='Нет' or new=='нет':
                act=False
    
enter()