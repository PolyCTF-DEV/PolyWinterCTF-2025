# Смешной мем, ситуация страшная | easy | steganography

## Информация
> Почему это так жизненно

## Выдать участникам
файл [funny_mem_scary_situation.zip](public/funny_mem_scary_situation.zip)

## Описание
Для решения необходимо подобрать кодовое слово для утилиты `steghide`

## Решение
Существует 2 способа решения:

  - Подобрать кодовое слово в ручную, основываясь на идее мема.
  - Найти кодовое слово через брутфорс с помощью утилиты stegbrute:
    
    `stegbrute -x -f task.jpg wordlist.txt`

## Флаг
`PolyCTF{w1nt3r_p0ly_ctf_but_n0_sn0w}`
