Задание :
Проектирование БД. Реализация с использованием фреймворка Django.
В компании имеется несколько складов с техникой. На каждый склад закреплен сотрудник, отвечающий за принятие и выдачу оборудования по поступающим накладным.

У каждой единицы техники есть инвентарный номер,производитель, страна производства, стоимость и модель.
Предложить структуру БД для инвентаризации оборудования на складах.

Написать скрипт для создания и заполнения 100 единиц техники с остатками на 5-ти складах. Остатки должны заполняться по нормальному закону распределения в диапазоне от 0 до 100.

Реализовать отображение отчета по остаткам на каждом складе и общем остатке по каждой единице техники. Вывести гистограмму частот для общих остатков по единицам техники.

Результат оформить в виде проекта на github/gitlab.



Для запуска проекта нама понадобятся команды.
1- sudo docker-compose build  

2- sudo docker-compose up  
Подняли контейнер.

3- sudo docker-compose exec -ti app python manage.py createsuperuser   
Создаем суперпользователя.

4- sudo docker-compose exec app python manage.py add_info  
Выполняем крипт по заполнению всех полей.

5- sudo docker-compose exec app python manage.py makemigrations   
6- sudo docker-compose exec app python manage.py migrate  

Создаем миграции

Проверка работы django 
- http://localhost:8080
Вход а вдминку
- http://localhost:8030/admin/


При возможной ошибке :
Error response from daemon: driver failed programming external connectivity on endpoint medical_work-app-1 (ced13881f118a9578f22ef4586888779cc42da7991b4615faf7f64e95cb210fe): Bind for 0.0.0.0:8080 failed: port is already allocated
1 - Поменять порт с 8080 на 8030 в строке 

    ports:
      - "8030:8000"

2 -  sudo fuser -k 8080/tcp   
