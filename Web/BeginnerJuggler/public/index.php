<?php
  session_start();
  $err = "";

  if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if(isset($_POST['code'])) {
      $code = $_POST['code'];

      if (md5($code) == "0e974114726967211511915142978119") {
        $err =  "PolyCTF{MD5_AnD_tyPE_jUG9L!n6_IN_PHP_@R3_7r!Cky}";
      } else {
        $err = "Вы ввели неверный код!";
      }
    }
  }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Добро пожаловать в цирк!</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="dis-tickets-2">
        <div class="container">
            <h1>Наш удивительный цирк</h1>
            <nav>
                <ul>
                    <li><a href="#about">О Нас</a></li>
                    <li><a href="#shows">Мероприятия</a></li>
                    <li><a href="#tickets">Билеты</a></li>
                    <li><a href="#tickets">Бесплатный билет</a></li>
                    <li><a href="#contact">Контакты</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="about" class="dis-tickets-1">
            <h2>О Нас</h2>
            <p>Добро пожаловать в самый волшебный цирк в мире! Мы приносим радость, удивление и острые ощущения зрителям всех возрастов.</p>
        </section>

        <section id="shows" class="dis-tickets-4">
            <h2>Предстоящие Шоу</h2>
            <ul>
                <li><strong>Acrobat Extravaganza:</strong> January 15, 2024</li>
                <li><strong>Magical Animal Parade:</strong> February 5, 2024</li>
                <li><strong>Clown Comedy Night:</strong> March 20, 2024</li>
                <li><strong>Jangler show:</strong> March 26, 2024</li>

            </ul>
        </section>

        <section id="tickets">
            <h2>Покупайте Билеты</h2>
            <form action="" method="POST">
                <label for="name">Имя:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="show">Выберите Шоу:</label>
                <select id="show" name="show" required>
                    <option value="Acrobat Extravaganza">Acrobat Extravaganza</option>
                    <option value="Magical Animal Parade">Magical Animal Parade</option>
                    <option value="Clown Comedy Night">Clown Comedy Night</option>
                    <option value="Clown Comedy Night">Jangler show</option>
                </select>

                <label for="tickets">Кол-во Билетов:</label>
                <input type="number" id="tickets" name="tickets" min="1" max="10" required>

                <button disable type="submit">Купить билеты</button>
            </form>
        </section>

        <section id="tickets">
            <h2>Получить Билет Бесплатно</h2>
            <form method="POST" action="">

                <label for="tickets">Код-ключ-сертификат:</label>
                <input type="text" id="code" name="code" required>

                <div class="error"><?php echo $err; ?></div>

                <button type="submit">Применить</button>
            </form>
        </section>

        <section id="contact" class="dis-tickets-3">
            <h2>Наши Контакты</h2>
            <p>Email: info@amazingcircus.com</p>
            <p>Phone: +123 456 789</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 The Amazing Circus. All rights reserved.</p>
    </footer>
</body>
</html>