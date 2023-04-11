![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
# WEBSCRAPPER CHALLENGE 🖥👾

![pika-2022-08-04T15_50_59 994Z](https://user-images.githubusercontent.com/27713965/182895990-8bee93b0-3cf7-400e-9b4e-9aa35cfb4686.png)

Esta es una pequeña aplicación web con un único objetivo: Obtener información de los libros listados en [esta página](http://books.toscrape.com)


## Comenzando 🚀
_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

-   Docker 19.03^
-   Docker Compose 1.25^
***
---

## Instalación 🔧

### 1. Clonar el repositorio
```
git clone https://github.com/raebeb/-webscraper-challenge.git
```
ó
```
git clone git@github.com:raebeb/-webscraper-challenge.git
```
---

### 2. Levantar el contenedor
```
docker-compose up
```
> Si es primera vez que se levanta el proyecto, este se _buildeara_ e instalara todas las dependencias necesarias

Si en la terminal aparece un mensaje como el siguiente, el proyecto se ha levantado con éxito
```
db_1   |
db_1   | PostgreSQL Database directory appears to contain a database; Skipping initialization
db_1   |
db_1   | 2022-08-04 16:38:07.899 UTC [1] LOG:  starting PostgreSQL 14.4 (Debian 14.4-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
db_1   | 2022-08-04 16:38:07.899 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1   | 2022-08-04 16:38:07.899 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1   | 2022-08-04 16:38:07.909 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1   | 2022-08-04 16:38:07.920 UTC [26] LOG:  database system was shut down at 2022-08-04 16:36:30 UTC
db_1   | 2022-08-04 16:38:07.927 UTC [1] LOG:  database system is ready to accept connections
web_1  | Watching for file changes with StatReloader
web_1  | Performing system checks...
web_1  |
web_1  | System check identified no issues (0 silenced).
web_1  | August 04, 2022 - 16:38:10
web_1  | Django version 3.2.14, using settings 'webscrapper_challenge.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.

```
> La primera vez que se levanta el proyecto es posible que falle, ya que se levanta web antes que db, si esto ocurre es necesario detener el contenedor con ```Ctrl + C``` y volver a levantarlo con ```docker-compose up```

---

### 3. Entrar al sitio

La aplicación cuenta con solo una vista, la cual puede ser accedida mediante ``` http://localhost:8000/core ```
> En caso de no poder ver el sitio detener el contenedor y levantarlo nuevamente

Una vez dentro seguir las instrucciones que se indican 
***
## Ejecutando las pruebas ⚙
_El proyecto cuenta con una serie de tests, para ejecutarlos el primer paso es tener contenedor levantado, luego seguir con los siguientes pasos_

1.  Ejecutar el siguiente comando en una terminal diferente:
	```
	docker-compose exec web sh -c "python manage.py test"
	```
   > En este paso se llevara a cabo la ejecución de los test unitarios desarrollados, al finalizar se visualizara un mensaje como el siguiente, indicando que todas las pruebas se ejecutaron con éxito
 ```
Ran 14 tests in 518.023s

OK
Destroying test database for alias 'default'...
 ```

***
## Construido con 🛠️
* [Python 3.10](https://www.python.org) - Lenguaje de programación
* [Django 3.2](https://www.djangoproject.com) - Framework web utilizado
* [PostgreSQL 14.4](https://www.postgresql.org) - Gestor de base de datos
* [Docker](https://www.docker.com) - Gestor de contenedores

***


## Autores ✒️
* [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) - Trabajo inicial

***

## ⌨️ con ❤️ por [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) 👩‍💻

```
          ／＞　 フ
         | 　_　_| 
       ／` ミ＿xノ 
      /　　　　 |
     /　 ヽ　　 ﾉ
    │　　|　|　|
／￣|　　 |　|　|
(￣ヽ＿_  ヽ_)__)
＼二)
```

