```
📚 Дисциплина: Интеллектуальные системы управления данными
Курс: 4 курс 8 семестр
```

## Лабораторная работа. Рекомендуется выполнять 6-8 студентам.
1. Разработать упрощенную минималистичную базу данных интернет-магазина для поддержки каталога с товарами, корзин, заказов (набор атрибутов на усмотрение студента).
2. Специфицировать операции create/read/update/delete для товаров, корзин, заказов в виде HTTP-запросов (задание параметров и методов запросов на усмотрение студента).
3. Материализовать базу данных в PostgreSQL, а веб-сервис на любом языке программирования с применением любых средств на усмотрение студента. Никакого Frontend не предполагается. 
4. Настроить мультимастер-репликацию БД с помощью pgpool-II. Количество экземпляров backend не менее двух.
5. Продублируйте настроенный экземпляр pgpool-II. Запрограммируйте в веб-приложении круговую смену backend для балансировки нагрузки и переподключения в случае сбоя части экземпляров. В качестве backend настраивается не экземпляр PostgreSQL, а экземпляр pgpool-II.
6. Разверните еще один экземпляр веб-сервиса и настройте балансировку нагрузки с помощью nginx.
7. Продублируйте экземпляр nginx. 
8. Подготовьте клиент нагрузочного тестирования например, на python + requests, который будет имитировать поведение посетителя-шопоголика. Реализуйте круговую смену backend (nginx). Зафиксируйте среднее время выполнения различных запросов из специфицированного в п. 2 API. Сделайте замеры для различного количества экземпляров PostgreSQL, pgpool-II, веб-сервиса и nginx. Оцените влияние количества экземпляров компонентов на время выполнения операций чтения и записи. Постройте графики среднего времени выполнения каждого запроса для каждой конфигурации. Можно оформить в виде нескольких barchart.
9. Перенесите часть функциональности, например операции над корзиной, в redis. Предположение: модель пользователя-шопоголика подразумевает “муки выбора” и частое изменение корзины.
10. Настройте репликацию в redis. Сделайте доработки, аналогичные п. 5. По умолчанию реплики - read only, можете ограничиться балансировкой запросов чтения.
11. Вновь выполните нагрузочное тестирование и перестройте графики.
12. Перенесите часть функциональности, например, каталог товаров, в cassandra.
13. Настройте кластер cassandra из 3 узлов. Сделайте доработки, аналогичные п. 5. Вы можете поддерживать строгий уровень согласованности на операциях чтения и записи.
14. Вновь выполните нагрузочное тестирование и перестройте графики.