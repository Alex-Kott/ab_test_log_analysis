import pandas as pd


'''Вы проводите сплит-тестирование на странице покупки услуг. Эксперимент проводится в трех группах (experimentValue = a || b || c). Каждой из групп показывается разный вариант страницы. Цель нововведения – повысить количество покупок определенной услуги. Необходимо проанализировать сессии пользователей и решить, какой из вариантов a, b или с выкатывать на 100% аудитории. В качестве ответа пришлите Jupyter Notebook с решением задачи и комментариями (в публичный репозиторий файл выкладывать не надо).
В файле по ссылке представлен access.log (сессии пользователей): https://cloud.hh.ru/f/828096d97ff84565a1d2/?dl=1
Пароль: test2019
goal – критерий сессий, которые участвуют в эксперименте (goal = gbb_price_experiment – id вашего эксперимента)
experimentValue – id сплита (experimentValue = a || b || c)
action – дейсвие пользователя (publications_visit – просмотр страницы покупки услуг, publications_checkout – покупка услуги)
hasRenewalVP – какую именно услугу купил пользователь (hasRenewalVP = true – покупка услуги, количество которых нужно увеличить)
cartID – id корзины пользователя
screenSize – размер экрана пользователя'''


def main(file_name: str):
    df = pd.read_csv(file_name, index_col=0)

    # print(df.head(20))

    for i, row in df.iterrows():
        print(row['cookies'].get('experimentValue'))
        
        print('----------')

        if i > 20:
            break


if __name__ == "__main__":
    main('log.csv')
