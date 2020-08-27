# Modular Scraper System

> Robust crawler framework for getting legal document from websites

[![Python Version][python-image]][python-url]
[![NPM Version][npm-image]][npm-url]
[![Flask Version][flask-image]][flask-url]
[![Scrapy Version][scrapy-image]][scrapy-url]
[![Vue Version][vue-image]][vue-url]
[![Mongo Version][mongo-image]][mongo-url]

### Backend: With Scrapy module running on Twisted Reactor. Wrapping with Flask.

### Frontend: Vue

### Database: MongoDB Atlas

![header-pic]

## Requirements

- [x] [Git CLI](https://git-scm.com/)
- [x] [NPM](https://www.npmjs.com/get-npm)
- [x] [PYTHON](https://www.python.org/)
- [x] [MONGO DB](https://www.mongodb.com/cloud/atlas)
- [x] [Pipenv]() `Not required but recommended`

## Installation & Setup

LINUX:

```bash
> mkdir '<create-a-folder>'

> cd '<create-a-folder>'

> sudo git clone https://github.com/PandorAstrum/reflect3746.git

> cd backend

> sudo pip install -r requirements.txt

> cd ..

> cd frontend

> sudo npm install
```

N.B: In `backend/db.py` file change `CONNECTION_STRING` to your own mongodb database

## RUN

1.  From `backend` directory start the server with:

    ```
    sudo python run_server.py
    ```

1.  From `frontend` directory start the dashboard with:

    ```
    sudo npm run serve
    ```

    Navigate to `localhost:5000` on your browser to use the Dashboard

_For api endpoint see below_

## Folder Structure

_project root_

    ├── backend
    |   ├── App
    |   |   ├── __init__.py
    |   |   ├── db.py                           # contains mongodb settings
    |   |   └── routes.py                       # API routes
    |   ├── scraper
    |   |   └── scraper
    |   |       ├── spiders                     # contains spiders
    |   |       ├── items.py
    |   |       ├── middleswares.py
    |   |       ├── pipelines.py
    |   |       └── settings.py                 # scrapy settings
    |   ├── static
    |   ├── template
    |   ├── config.py                           # flask config
    |   └── run_server.py                       # ENTRY POINT FOR FLASK
    |
    └── frontend
        ├── public
        └── src

## API Endpoints

`http://127.0.0.1:5000/api/v1` endpoints after this

---

### Server Status : `GET`

```
/server_status
```

returns: json (boolean if flask is running or not)

---

### Database Status : `GET`

```
/database_status
```

returns: json (try connecting to mongo db)

---

### List available spiders : `GET` , `POST`

```
/spider
```

returns: json (all spiders created by scrapy cli, e.g scrapy genspiders command)

---

### Run Spider : `POST`

```
/run
```

returns: json (start selected spiders with param provided)
requires: params as body payload

e.g:

{"spider_kwargs":{"baseurl":"https://www.example.com/","spider_name":"Example"},"spider_settings":{"sitemap":false,"delay":1}}

---

### Get Results by ID : `GET`

```
/results/<_id_here>
```

returns: json (from mongodb scraped collection matching documents with id number)

---

### Get All Results : `GET`

```
/all
```

returns: json (from mongodb scraped collections all documents)

---

### Get All Logs : `GET`

```
/logs
```

returns: json (from mongodb logs collection all documents)

---

Ashiquzzaman Khan – [@dreadlordn](https://twitter.com/dreadlordn)

[https://github.com/PandorAstrum/reflect3746.git](https://github.com/PandorAstrum/reflect3746.git)

## Contributing

1. Fork it (<https://github.com/PandorAstrum/reflect3746.git/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[python-image]: https://img.shields.io/badge/Python-3.7-yellowgreen.svg?style=flat-square
[python-url]: https://www.python.org/
[npm-image]: https://img.shields.io/badge/NPM-6.14-yellowgreen.svg?style=flat-square
[npm-url]: https://www.npmjs.com/
[flask-image]: https://img.shields.io/badge/flask-1.1-yellowgreen.svg?style=flat-square
[flask-url]: https://flask.palletsprojects.com/en/1.1.x/
[scrapy-image]: https://img.shields.io/badge/scrapy-2.3-yellowgreen.svg?style=flat-square
[scrapy-url]: https://scrapy.org/
[vue-image]: https://img.shields.io/badge/vue-2.6-yellowgreen.svg?style=flat-square
[vue-url]: https://vuejs.org/
[mongo-image]: https://img.shields.io/badge/mongo-Atlas-yellowgreen.svg?style=flat-square
[mongo-url]: https://www.mongodb.com/

<!-- Header Pictures and Other media-->

[header-pic]: header.png
