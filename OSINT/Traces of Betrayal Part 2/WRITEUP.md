# Следы предательства Часть 2 | medium | osint

## Информация

> Мы подозреваем, что в слитой базе данных находятся персональные данные предателя, скрывающегося под псвевдоднимом 5h4d0wL33ch. 
> 
> Миссия №2: Найдите корпоративную почту предателя, мы должны знать его в лицо! 
> 
> Формат флага: PolyCTF{email@company.fi}

## Выдать участникам
-

## Описание
Гитхаб **5h4d0wL33ch** -> подозрительный коммит -> личная gmail почта -> получение ФИ через Ghunt или вручную -> получение email из бд в тг канале
## Решение
 гитхаб аккаунте **[5h4d0wL33ch](https://github.com/5h4d0wL33ch)** в репозитории my_contacts, в [коммитах](https://github.com/5h4d0wL33ch/my_contacts/commits/main/) можно заметить что один коммит верифицирован и с аватаркой 5h4d0wL33ch, а другой нет. Также до этого можно дойти через то, что в профиле 5h4d0wL33ch этот коммит не отображается. 
Зайдя в его [.patch](https://github.com/5h4d0wL33ch/my_contacts/commit/6519951fa2c84a2d83e4608f32e5957c2b1263b8.patch) 

```
From 6519951fa2c84a2d83e4608f32e5957c2b1263b8 Mon Sep 17 00:00:00 2001
From: 5h4d0wL33ch <kksuomi1985@gmail.com>
Date: Fri, 10 Jan 2025 19:02:58 +0300
Subject: [PATCH] wallet

---
 wallet.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 wallet.txt

diff --git a/wallet.txt b/wallet.txt
new file mode 100644
index 0000000..3d0b757
--- /dev/null
+++ b/wallet.txt
@@ -0,0 +1 @@
+bc1p3aqse9wggd24qqwg2fysnyy07pm9mmleksk7z2lq6kvf60zkw40qj3jgtm
\ No newline at end of file
```

или выполнив `git clone git log` мы можем узнать почту из первого коммита 
kksuomi1985@gmail.com

По лору он создал коммит, забыв поменять свою личную почту.

Пробив эту почту через GHunt или [узнав google id вручную](https://www.securitylab.ru/blog/company/CABIS/348481.php) можно получить его профиль в гугл картах, где будут написаны имя, фамилия и ник.

![gmaps.png](solve/gmaps.png)

По нику можно найти [лорный tumblr ](https://kaapokyyr.tumblr.com/) а по имени и фамилии в тг канале из первой части задания в базе данных компании N найти корпоративную почту.
 
```sql
SELECT * FROM employees WHERE first_name = 'Kaapo' AND last_name = 'Kyyrönen';
```
```json
[{"employee_id":"326698","first_name":"Kaapo","last_name":"Kyyrönen","hire_date":"2024-12-24","department_id":2}]
```
```sql
SELECT * from email_addresses WHERE employee_id = 326698;
```
```json
[{"email_id":4512,"employee_id":"326698","email_address":"kaapo-326698@company.fi"}]
```

## Флаг
`PolyCTF{kaapo-326698@company.fi}`
