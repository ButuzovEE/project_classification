# Final Project (Butuzov Evgenii)
Анализ настроений (Sentiment Analysis) — это процесс анализа цифрового текста, чтобы определить является ли эмоциональный тон сообщения положительным или  отрицательным.

Задача проекта - создать рабочую модель для получения эмоционального тона документа (отзыва о ресторанах на сайте tripadvisor.com)

Результатом является модель Roberta, которая с помощью файнтюнинга и различных способов оптимизации доведена по метерике 'f1_macro' до 0.96.   
Полученная модель упакована в контейнер и развернута с помощью Docker, Streamlit и FastAPI.





Для запуска модели локально запускаем терминал на Вашем компьютере, далее необходимо последовательно выполнить следующие команды:

1. С помощью команды ```cd```
переходим в папку, в которую нужно скопировать репозиторий.

2. Вводим следующую команду в териминал для клонирования репозитория:
```bash
git clone https://github.com/ButuzovEE/project_classification.git .
```
3. Вводим следующую команду для запуска модели на localhost:

```bash
docker-compose up --build -d
```

Модель запущена на localhost.
Для доступа необходимо перейти в любой браузер и ввести следующий адрес:
```bash
localhost:8501
```

Вводим текст от которого необходимо получить эмоциональный тон и кликаем на "classify".


Для остановки модели используем команду:
```bash
docker-compose down 
```
