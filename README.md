# Смешной телеграм

Это телеграм бот который отправляет фото комиксов и комментарии к нему в telegram.

### Установка

Скачайте необходимые файлы, затем используйте pip (или pip3, если есть конфликт с Python 2) для установки зависимостей и установить зависимости.
Зависимости можно установить командой, предоставленной ниже.
Создайте бота у отца ботов. Создайте новый канал в Telegram.

```
pip install -r requirements.txt
```

### Пример запуска скрипта

Для запуска скрипта у вас уже должен быть установлен Python3.
Для публикации необходимых изображений в телеграм необходимо: 
Просто запустить скрипт.
Или же написать в командную строку(консоль):
```
python main.py
```

### Переменные окружения
Часть проекта построена на переменных окружения. Переменные окружения похожи на переменные в языках программирования. Они существуют в рамках запущенной сессии командного интерпретатора, то есть, переменные пропадут, когда терминал закроется. Они подгружаются туда во время его инициализации, хотя это не единственный путь их появления.
Посмотреть установленные переменные можно командой env (environment).

Пример содержания файла `.env`:


```
TG_CHAT_ID = "dasdsadjsandsamdnsajdhsaj123mdsandmsan"
TOKEN_TG = "sakdsmakqwheudsajkdjakdasj@mdnsamdnaj"
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).