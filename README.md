<h1 align="center">Привет, я <a href="https://t.me/starboy_shpak/" target="_blank">Вадим</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Бэкэнд-разработчик, электроэнергетик, студент Яндекса</h3>

# Содержание
- [Автор](#автор)
- [Используемые технологии](#используемые-технологии)
- [Описание проекта](#описание-проекта)
- [Как запустить проект](#как-запустить-проект)



## Автор
*Вадим Шпак* 

## Используемые технологии

<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green" />
<img src="https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white" />
<img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white" />
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white" />

## Описание проекта

Добавление API для проекта Yatube.

## Как запустить проект
- #### Клонировать репозиторий и перейти в него в командной строке:

  ```
  git clone https://github.com/Starboy-Shpak/api_yatube.git
  ```

  ```
  cd API_Yatube
  ```
- #### Cоздать и активировать виртуальное окружение:

  ```
  python -m venv venv
  ```

  ```
  source venv/Scripts/activate
  ```

- #### Обновить pip и установить зависимости из файла requirements.txt:

  ```
  python -m pip install --upgrade pip
  ```

  ```
  pip install -r requirements.txt
  ```

- #### Выполнить миграции:

  ```
  python manage.py migrate
  ```

- #### Запустить проект:

  ```
  python manage.py runserver
  ```
  