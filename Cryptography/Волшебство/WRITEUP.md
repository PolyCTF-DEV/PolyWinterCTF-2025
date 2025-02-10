# Волшебство | medium | crypto

## Информация
> В Хогвартсе были найдены два загадочных зашифрованных текста, которые, по слухам, связаны с древними тайнами волшебного мира. Разгадайте их и узнайте тайны волшебства!

## Выдать участникам
файлы [first.txt](public/first.txt) и [second.txt](public/second.txt)

## Описание
Нужно было понять, что это XOR, где ключ это флаг в длину текстов и им зашифрованы оба текста, дальше скучно и нудно расшифровываем

## Решение
Так как XOR обратимая функция, мы можем подставить начало флага `PolyCTF{` как ключ и первые буквы, которые складываются в слова.

Для первого текста [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'PolyCTF%7B'%7D,'Standard',false)&input=MzgwZTFlMGIzYTc0MjEwOTFkMTgxNTNhMDk0MTBmMDAxMDQxMWIzZTE5MGI1MjE4MGQzODA3MTIzMzExNDExMzAxNTkzNzE1NGYwNzAwMDAwMjNhMGQ1MzM2MDgxZDAzNGMxMTBjM2E1NzBkMWQwNTMzMGU0ZjAyMGQxMTUyM2MwOTA1MWIwNzBiMDY1NTFhMDAzZTEzMWE0NDJmMDYxYjBkMTYwYzBhMGU0MjA3MGIzMDA0MWQwMTE1NDkxMzFjMzMxMzBkMDgxZDE3MmIwNDQ5MTIwZTAwMDcwMTJhMWU0YzE1M2UxNjRlMzcwYjE2MGIwYTAzNTMwMzAwMTcwMzFhMzE0MTFhMGMzYTQzMDAxZDE3MzYxNTAxMDM0NTExMTMwNzFmM2ExNzUwMTcwOTAwMWExZQ&oeol=FF)

Для второго текста [cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'PolyCTF%7B'%7D,'Standard',false)&input=MjQwNzA5NTkzMDNiMzQwZjFkMDYwMjdmMDUwMDEzNDkxMzAwMTkyYzEyMGI1MjBkMTAzMDFmNDYzNzBkMTMxZjFiMTYzMTE1MWM1NDFjMDAxMzNiNDkwNDM3MGYxYTFjMDkxNzBkMzExMDQ5MWIwZTdmMWYwYTFjNDQwNjFlM2ExNzAxMDQwYjBiMDcwNjUyMDcyZDAwMTgwMTJkMTA0ZTAyMWMwMTQ0MDEwNzBkMTcyYjUzMTYwYTE0MDYxNzE2N2YxMTAxMGIxMzA5MzMwZTQ5MDkwOTFkMTEwNzM2MDgwYjU5MzgxZDE3MzkwNDFiMDEwYjAyMDE1NDFkMGM0YjA3MzcwNDRlMDczNzA2MDQwMTFkMzExNzRmMWYwNDFlMGE1NTAzMzk1MzE2MDQwMTAzMDYwZQ&oeol=FF)

Потихоньку угадывая буковки у нас будут открываться новые части слов в тексте и флаге.

Расшифровываем оба текста и флаг ваш.
```
first.txt: harry gripped his wand tightly as he steped into the dimly lit chamber heart pounding knowing voldemorts horcrux lay hidden within the ancient cursed relic 

second.txt: the sorting hat paused atop hermiones head whispering of her cleverness bravery and heart before finally shouting gryffindor to the cheering hall of famous

flag.txt: PolyCTF{the_magical_world_of_harry_potter_is_filled_with_wonder_adventure_and_incredible_stories_where_wizards_fly_on_broomsticks_and_cast_powerful_spells}
```

## Флаг
`PolyCTF{the_magical_world_of_harry_potter_is_filled_with_wonder_adventure_and_incredible_stories_where_wizards_fly_on_broomsticks_and_cast_powerful_spells}`