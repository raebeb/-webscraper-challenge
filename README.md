![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
# WEBSCRAPPER CHALLENGE 馃枼馃懢

![pika-2022-08-04T15_50_59 994Z](https://user-images.githubusercontent.com/27713965/182895990-8bee93b0-3cf7-400e-9b4e-9aa35cfb4686.png)

Esta es una peque帽a aplicaci贸n web con un 煤nico objetivo: Obtener informaci贸n de los libros listados en [esta p谩gina](http://books.toscrape.com)


## Comenzando 馃殌
_Estas instrucciones te permitir谩n obtener una copia del proyecto en funcionamiento en tu m谩quina local para prop贸sitos de desarrollo y pruebas._


### Pre-requisitos 馃搵

-   Docker 19.03^
-   Docker Compose 1.25^
***
---

## Instalaci贸n 馃敡

### 1. Clonar el repositorio
```
git clone https://github.com/raebeb/-webscraper-challenge.git
```
贸
```
git clone git@github.com:raebeb/-webscraper-challenge.git
```
---

### 2. Levantar el contenedor
```
docker-compose up
```
> Si es primera vez que se levanta el proyecto, este se _buildeara_ e instalara todas las dependencias necesarias

Si en la terminal aparece un mensaje como el siguiente, el proyecto se ha levantado con 茅xito
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

La aplicaci贸n cuenta con solo una vista, la cual puede ser accedida mediante ``` http://localhost:8000/core ```
> En caso de no poder ver el sitio detener el contenedor y levantarlo nuevamente

Una vez dentro seguir las instrucciones que se indican 
***
## Ejecutando las pruebas 鈿?
_El proyecto cuenta con una serie de tests, para ejecutarlos el primer paso es tener contenedor levantado, luego seguir con los siguientes pasos_

1.  Ejecutar el siguiente comando en una terminal diferente:
	```
	docker-compose exec web sh -c "python manage.py test"
	```
   > En este paso se llevara a cabo la ejecuci贸n de los test unitarios desarrollados, al finalizar se visualizara un mensaje como el siguiente, indicando que todas las pruebas se ejecutaron con 茅xito
 ```
Ran 14 tests in 518.023s

OK
Destroying test database for alias 'default'...
 ```

***
## Construido con 馃洜锔?
* [Python 3.10](https://www.python.org) - Lenguaje de programaci贸n
* [Django 3.2](https://www.djangoproject.com) - Framework web utilizado
* [PostgreSQL 14.4](https://www.postgresql.org) - Gestor de base de datos
* [Docker](https://www.docker.com) - Gestor de contenedores

***


## Autores 鉁掞笍
* [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) - Trabajo inicial

***
## Expresiones de Gratitud 馃巵
_Quiero utilizar este espacio para agradecer a la empresa Tech-k y a su equipo de reclutamiento por considerarme para participar en este proceso de selecci贸n y darme la oportunidad de demostrar mis conocimientos mediante este desaf铆o, espero poder cumplir con sus expectativas, por mi parte me divert铆 mucho desarrollando este proyecto y sin duda ha sido una oportunidad de profundizar mis conocimientos 喔佲倣飧嶁笇蹋史蹋太飧嵦ｂ笇鈧庎竸_
***
## 鈱笍 con 鉂わ笍 por [Francisca Osores](https://www.linkedin.com/in/francisca-osores-ortiz-152347149/) 馃懇鈥嶐煉?

```
          锛忥紴銆? 銉?
         | 銆?_銆?_| 
       锛廯 銉燂伎x銉? 
      /銆?銆?銆?銆? |
     /銆? 銉姐??銆? 锞?
    鈹傘??銆?|銆?|銆?|
锛忥浚|銆?銆? |銆?|銆?|
(锟ｃ兘锛縚  銉絖)__)
锛间簩)
```

