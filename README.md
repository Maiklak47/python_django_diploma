# MEGANO — это проект торговой площадки, созданный с использованием Django и инфраструктуры Django REST.
Это позволяет пользователям просматривать и покупать товары в различных категориях.

<h2 align="center">Проект сайта интернет-магазина MEGANO</h2>

> <h2> Структура сайта: </h2>
> <p> Главная страница</p>
> <p> Каталог (сам каталог, детальная страница товара)</p>
> <p> Скидки </p>
> <p> Страница оформления заказа (корзина, оформление заказа, оплата)</p>
> <p> Личный кабинет (личный кабинет, профиль, история заказов)</p>
> <p>


> <h2> Пошаговый запуск проекта локально: </h2>
>
> <h3> Активируем виртуальное окружение </h3> 
>
>> <p><i> source venv/bin/activate </i></p> 
> <h3> Устанавливаем пакеты </h3>  
>
>> <p><i> pip install -r requirements.txt </i></p> 
> <h3> Запускаем базу данных </h3> 
> 
>> <p><i> python manage.py makemigrations </i></p> 
>> <p><i> python manage.py migrate </i></p> 
> <h3> Запускаем фикстуры </h3> 
> 
>> <p><i> python manage.py loaddata accounts/fixtures/users_data.json </i></p>
>> <p><i> python manage.py loaddata catalog/fixtures/catalog_data.json </i></p>
>> <p><i> python manage.py loaddata orders/fixtures/orders_data.json </i></p>
>> <p><i> python manage.py loaddata products/fixtures/products_data.json </i></p>

>
> <h3> Запускаем проект </h3>
>
>> <p><i> python manage.py runserver </i></p>
>
> <h2> Пошаговый запуск проекта в Docker: </h2>
>

>> <p><i> docker-compose up --build </i></p>
>>> <p> или </p>
>>> <p><i> docker-compose up --build -d (с возможностью закрывать терминал) </i></p>
