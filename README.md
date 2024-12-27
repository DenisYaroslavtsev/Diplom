# Дипломная работа по курсу Python-разработчик
## Тема: Анализ и сравнение написания web-приложений с использованием разных фреймворков

<details><summary><b>Содержание:</b></summary>
1. Введение
  
2. Общие сведения о web-фреймворках
   * 2.1 Что такое web-фреймворки
   * 2.2 Для чего нужны web-фреймворки
  
3. Обзор популярных инструментов для разработки разработки веб-приложений на Python
   * 3.1 Django
   * 3.2 FastApi
   * 3.3 Flask
  
  
4. Сравнение фреймворков
5. Заключение
6. Список используемой литературы

## 1. Введение:
Современные веб-приложения требуют высокой производительности, удобства в разработке и гибкости в использовании. В последние годы на рынке разработаны множество фреймворков, каждый из которых имеет свои преимущества и недостатки. В данной работе будет проведен анализ и сравнение трех популярных фреймерков для создания веб-приложений на Python: Django, FastAPI и Flask.

## 2. Общие сведения о web-фреймворках
2.1 Фреймворк (с англ. framework — «каркас, структура») — заготовка, готовая модель в программировании для быстрой разработки, на основе которой можно дописать собственный код. Он задает структуру, определяет правила и предоставляет необходимый набор инструментов для создания проекта. 
  Существует 2 типа web-фреймворков:
  * Фронтенд фреймворки
    Эти фреймворки используются для разработки внешнего(прльзовательского) интерфейса. Чаще всего в данных фреймворках используются такие языки, как JavaScript, CSS и HTML.
    Среди решаемых задач — разработка дизайна UX/UI, SEO-оптимизация, фрагменты кода, шаблоны, управление взаимодействием с пользователем и многое другое. А среди самых известных фронтенд фреймворков — React, Vue.js, Ember, Bootstrap и Angular.
    
  * Бэкэнд фреймворки
    Эти фреймворки используются для разработки серверной части, которая отвечает за функционирование ИТ-продукта. Они основаны на таких языках программирования, как Python, .NET, Ruby, Java и PHP.
    Среди решаемых задач — функционирование сервера и базы данных, протоколы маршрутизации, логика и архитектура сервиса, параметры авторизации, безопасность и многие другие. Среди наиболее популярных фреймворков — Django, Laravel, Ruby On Rails, Spring, Express, ASP.NET Core.
    
2.2 Для чего нужны web-фреймворки?

  Любой фреймворк на различных языках упрощает жизнь программиста при создании архитектуры, разработке и поддержке проекта. В фреймворках на архитектурном уровне заложено множество принципов оптимизации. Рассмотрим основные преимущества ниже.

  * <b>Более высокая производительность.</b> 
    Фреймворки разработаны с использованием готовых функций для обеспечения высокой эффективности и производительности при создании ИТ-решений. Скорость загрузки веб-сайтов и программ, разработанных с их использованием, значительно возрастает.
    
  * <b>Сокращение количества ошибок.</b>
    Большинство фреймворков включают в себя лучшие практики разработки программного обеспечения. Многие из них имеют встроенный механизм тестирования, который проверяет код сразу, уменьшая количество ошибок в конечном коде.
  * <b>Быстрое развитие проекта или продукта.</b> 
     У фреймворков есть заранее написанные шаблоны, которые можно использовать для выполнения избыточных задач программирования. Эти инструменты экономят время разработчиков и позволяют им сосредоточиться на более приоритетных для команды действиях, обеспечивая более быстрые результаты.
  * <b>Надежность и безопасность.</b>
      Фреймворки включают в себя сотни готовых компонентов, созданных и регулярно обновляемых сообществом разработчиков. Это своего рода гарантия, что ваш проект — актуальное и одно из лучших решений бизнеса.

## 3. Обзор фреймворков:
3.1 Django
  * Django — это высокоуровневый Python веб-фреймворк, который позволяет быстро создавать безопасные и поддерживаемые веб-сайты. Созданный опытными разработчиками, Django берёт на себя большую часть хлопот веб-разработки, поэтому вы можете сосредоточиться на написании своего веб-приложения. Django включает в себя множество встроенных средств для решения распространенных задач.
    
    <b>Преймущества:</b>
    * Принцип "Всё включено"(«Batteries included»)
      Фраза «всё включено» означает, что большинство инструментов для создания приложения — часть фреймворка, а не поставляются в виде отдельных библиотек.

      Django содержит огромное количество функциональности для решения большинства задач веб-разработки. Вот некоторые из высокоуровневых возможностей Django:
        * ORM
        * Миграции базы данных
        * Аутентификация пользователя
        * Панель администратора
        * Формы
     
    * Стандартизированная структура
   
      Django как фреймворк задаёт структуру проекта. Она помогает разработчикам понимать, где и как добавлять новую функциональность.

      Благодаря одинаковой для всех проектов структуре гораздо проще найти уже готовые решения или получить помощь от сообщества.

    * Приложения Django
   
      Приложения в Django позволяют разделить проект на несколько частей. Приложения устанавливаются путём добавления в <b>settings.INSTALLED_APPS</b>. Этот подход позволяет легко интегрировать готовые решения.

    * Безопасность
   
      Django безопасен и включает механизмы предотвращения распространенных атак вроде SQL-инъекций (XSS) и подделки межсайтовых запросов (CSRF).

    * REST Framework для создания API

      Django REST Framework(DRF), является библиотекой для построения API. Он имеет модульную и настраиваемую архитектуру, которая хорошо работает для создания как простых, так и сложных API.

      В DRF политики аутентификации и разрешений доступны из коробки. Он поставляется с базовыми классами для CRUD операций и встроенной утилитой для тестирования разрабатываемого API.

    * GraphQL фреймворк для создания API
   
      Большие REST API часто требуют большого количества запросов для получения всех необходимых данных. GraphQL — это язык запросов, который позволяет обмениваться связанными данными гораздо проще.

      Graphene-Django позволит легко добавить соответствующую функциональность в ваш проект. Модели, формы, аутентификация, политики разрешений и другие функциональные возможности Django можно использовать для создания GraphQL API. Библиотека так же поставляется с утилитой для тестирования результата.

    <b>Недостатки:</b>
      * Избыточность

        У Django есть все инструменты для создания высоконагруженных приложений. А вот для небольших сайтов их, зачастую, слишком много. За счет этого, не всегда есть смысл применять фреймворк для таких проектов. Тем более, что у него есть более простые альтернативы.

     * Функции ORM
   
       На сегодня этот компонент Django устарел и не дотягивает до современных стандартов. Ключевой минус ORM — отсутствие поддержки SQLAlchemy. Сейчас это основной инструмент для работы с базами данных у Python.
 
3.2 FastApi
  * FastAPI - является легковесным асинхронным фреймворком для Python, который используют преимущественно для разработки API-сервисов. Фреймворк довольно молодой и существует всего лишь 6 лет.

    <b>Преймущества:</b>

    * Скорость работы
   
      FastAPI обходит все Python-фреймворки по производительности

    * Гибкость на уровне Flask
   
      У вас нет какой-либо утвержденной архитектуры, что дает волю вашей фантазии и различным подходам разработки

    * Ассинхронность
   
      FastAPI использует ASGI-сервера по умолчанию.  Благодаря асинхронному коду запросы выполняются независимо друг от друга и могут запускаться параллельно, а это значит, что время выполнения значительно сокращается по сравнению с выполнением при последовательном запуске.

    * Автоматическая документаци
   
       FastAPI использует аннотации типов Python для определения входных и выходных данных API и поддерживает дополнительные метаданные Swagger для более полной документации.

    <b>Недостатки:</b>

    * Отсутствие подробной документации
   
      Это может создавать проблемы при поиске ответов на вопросы или получении помощи в решении проблем.

    * Недостаток плагинов и модулей
   
      У FastAPI ограниченное количество плагинов и модулей, доступных для использования. Это может ограничить функциональность и возможности разработчиков при создании веб-приложений.

3.3 Flask
  * Flask — это легковесный веб-фреймворк для языка Python, который предоставляет минимальный набор инструментов для создания веб-приложений.

    <b>Преймущества:</b>

    * Считается лучшим веб-фреймворком для создания небольших статических сайтов и легковесных веб-приложений.
    * Гибкость и модульность
   
      Flask предусматривает модульное программирование, что помогает избежать путаницы и сохранить порядок «на рабочем месте». При этом фреймворк позволяет разработчику брать контроль над структурой проекта и самостоятельно выбирать инструменты.

    * Много подробной документации на русском языке.
   
    <b>Недостатки:</b>

    * Однопоточная система
   
       Каждый запрос разрабатывается поочередно. Это увеличивает время обработки.

    * Нет поддержки многостраничных приложений.
   
      В Flask отсутствует встроенный механизм маршрутизации для многостраничных приложений. Из коробки фреймворк предоставляет механизм для обработки запросов и возвращения ответов, но не дает удобных инструментов для организации навигации между различными страницами приложения.

## 4. Сравнение фреймворков:
Django следует архитектуре Model-View-Template (MVT), FastAPI основывается на принципах асинхронного программирования, а Flask позволяет использовать любую архитектуру на усмотрение разработчика.

* Простота в использовании:

  Django требует более глубокого изучения из-за своего объёма и конфигурации, тогда как Flask и FastAPI легче осваиваются, особенно для небольших проектов.

* Производительность:

  FastAPI продемонстрировал наилучшие результаты в производительности благодаря асинхронной обработке запросов. Flask и Django, будучи синхронными, работают медленнее в сценариях с высокой нагрузкой
  ![8abd3c976a2047e6d6975c5241882dee](https://github.com/user-attachments/assets/8379a307-ce44-4e95-bc3f-4d42f24d1976)
  (Данные взяты с сайта https://www.techempower.com)

* Гибкость и расширяйомсть:

  Flask предлагает максимальную гибкость, так как предоставляет разработчику возможность выбирать компоненты и библиотеки. Django более строг в подходе, но предлагает мощный набор встроенных средств. FastAPI сочетает в себе гибкость и производительность, что делает его идеальным для разработки API.

* Сообщества и документации:

  Django обладает самым большим сообществом и обширной документацией. Flask также имеет активное сообщество, но меньше ресурсов по сравнению с Django. FastAPI является относительно новым фреймворком, но его популярность быстро растет, и документация постоянно обновляется

* Безопасность:

  Django имеет встроенные инструменты безопасности, которые делают его предпочтительным для создания крупных и безопасных приложений. Flask требует большего внимания к безопасности, так как многие функции безопасности необходимо реализовывать самостоятельно. FastAPI также предлагает хорошие меры безопасности, но разработчики должны быть внимательны к настройкам.

## 5. Заключение:
В данной работе был проведен анализ фреймворков Django, FastAPI и Flask. Каждый из них имеет свои сильные и слабые стороны. Django подходит для крупных проектов с высокими требованиями к безопасности. Flask идеален для небольших приложений и прототипов. FastAPI демонстрирует высочайшую производительность и является предпочтительным выбором для создания API.

## 6. Список литературы:
* [django-project.com](https://www.djangoproject.com/)
* [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
* [flask.palletsprojects.com](https://flask.palletsprojects.com/en/stable/)
* [https://www.kevsrobots.com/learn/fastapi/06_implementing_registration_and_login.html](https://fastapi-users.github.io/fastapi-users/10.2/)
* [flask-paginate](https://flask-paginate.readthedocs.io/en/master/index.html)
* https://docs.djangoproject.com/en/5.1/topics/auth/default/
</details>

<details><summary><b>Структура проекта</b></summary>
  
## Django:

![django](https://github.com/user-attachments/assets/d8d08c8b-d635-4b78-a42e-fc4fa4ffa1b2)

## FastApi

![FastApi](https://github.com/user-attachments/assets/606a0251-251a-4b23-8441-6a45ba3ea4b8)
![Fastapi2](https://github.com/user-attachments/assets/c567ca27-33c8-46b4-b362-96b5e5024934)

## Flask

![flask](https://github.com/user-attachments/assets/9912d2d2-a91c-43c6-a10e-6b9004208e63)
</details>

<details><summary><b>Запуск проекта</b></summary>

## Запуска проекта Django

Откройте териминал и введите в нём команду: 

` cd myapp `

После ввода данной команды, вы попадёте в рабочую директорию проекта "myapp"

Для запуска проекта так же в терминале прописываем команду:

`python manage.py runserver`

После чего переходим по запущенному локальному серверу(http://127.0.0.1:8000/):

![runserver](https://github.com/user-attachments/assets/06474ff3-1e4f-4c71-96e0-c7f077301cb3)

Для остановки работы сервера в терминале нажмите сочетание клавишь `Ctrl + C`

## Запуск проекта FastApi

Для начало нужно вернуться в исходный каталок(если изначально запускали проект на Django), для этого в терминале прописывает команду:

`cd ..`

Чтобы запустить приложение в терминале прописываем следующую команду:

`python -m uvicorn FastApi.main:app`

![run fastapi](https://github.com/user-attachments/assets/a389d463-0a39-44bc-9761-ded03071ea98)

Для остановки работы сервера в терминале нажмите сочетание клавишь `Ctrl + C`

## Запуск проекта Flask

Перейдите в проект Flask. Далее найдите файл `main.py` и откройте его. Для запуска приложение, если вы используете Pycharm можете нажать сочетание клавишь `Shift + F10` или воспользоваться значком запуска, который находится на верху в правой области:

![значок запуска](https://github.com/user-attachments/assets/00d4a6be-99c8-44f9-912c-65ce4e7fc7dd)

Для остановки работы сервера можно использовать комбинацию клавишь `Ctrl + F2` или же воспользоваться значком остановки работы приложения:

![стоп](https://github.com/user-attachments/assets/58df43f7-07c0-4ee2-8f7e-2a9bd260c541)

</details>
      
