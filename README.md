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

Перед запуском проекта необходимо установить зависимости, для этого в терминале прописываем команду:

`pip install -r requirements.txt`

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

<details><summary><b>Список используемых библиотек</b></summary>
  
* annotated-types==0.7.0
  
* anyio==4.7.0
 
* asgiref==3.8.1
 
* bcrypt==4.2.1
 
* blinker==1.9.0

* charset-normalizer==3.4.0
 
* click==8.1.7
 
* cloudpickle==3.1.0
 
* colorama==0.4.6
 
* dask-expr==1.1.21
 
* Django==5.1.4
 
* dnspython==2.7.0
 
* email_validator==2.2.0
 
* exceptiongroup==1.2.2
 
* fastapi==0.115.6
 
* fastapi-pagination==0.12.34
 
* filelock==3.16.1
 
* Flask==3.1.0
 
* flask-paginate==2024.4.12
 
* Flask-SQLAlchemy==3.1.1
 
* Flask-WTF==1.2.2
 
* greenlet==3.1.1
 
* h11==0.14.0
 
* huggingface-hub==0.27.0
 
* idna==3.10
 
* importlib_metadata==8.5.0
 
* itsdangerous==2.2.0
 
* Jinja2==3.1.4
 
* joblib==1.4.2
 
* locket==1.0.0
 
* MarkupSafe==3.0.2
 
* mpmath==1.3.0
 
* networkx==3.4.2
 
* numpy==2.2.1
 
* packaging==24.2
 
* pandas==2.2.3
 
* partd==1.4.2
 
* passlib==1.7.4
 
* pillow==11.0.0
 
* psutil==6.1.1
 
* pyarrow==18.1.0
 
* pydantic==2.10.4
 
* pydantic_core==2.27.2
 
* python-multipart==0.0.20
 
* PyYAML==6.0.2
 
* requests==2.32.3
 
* safetensors==0.4.5
 
* scikit-learn==1.6.0
 
* scipy==1.14.1
 
* sentence-transformers==3.3.1
 
* six==1.17.0
 
* sniffio==1.3.1
 
* SQLAlchemy==2.0.36
 
* sqlparse==0.5.3
 
* starlette==0.41.3
 
* swifter==1.4.0
 
* sympy==1.13.1
 
* threadpoolctl==3.5.0
 
* tokenizers==0.21.0
 
* toolz==1.0.0
 
* torch==2.5.1
 
* tqdm==4.67.1
 
* transformers==4.47.1
 
* typing_extensions==4.12.2
 
* tzdata==2024.2
 
* urllib3==2.3.0
 
* uvicorn==0.34.0
 
* Werkzeug==3.1.3
 
* WTForms==3.2.1
 
* zipp==3.21.0

</details>
      
