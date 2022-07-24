<h1 align="center"> :zap: Ongrid Task :zap:</h1>

![](https://img.shields.io/badge/Python-3.9.7-brightgreen) 
![](https://img.shields.io/badge/Django-4.0.6-brightgreen)
![](https://img.shields.io/badge/yarn-1.22.19-blue)
![](https://img.shields.io/badge/Node-v16.15.1-blue)

![](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)


## *Task description link*
> https://docs.google.com/document/d/1NuPLHv-7XN9YjVXFLNDDqhbOvH_eIhhxZ8TX_qtuT9g/edit#
## *Installation*
### ***Run With Docker Container***
`docker-compose up --build -d`
___
### *Run from terminal*
#### *To run Django Backend App*
```commandline
python3 -m venv venv
venv/bin/pip install -r requirements.txt 
source venv/bin/activate
cd app && python3 manage.py runserver
```

#### *Open new terminal to run React Frontend App*
```commandline
cd app/frontend && yarn install
yarn start
```
#### *Django REST API Roots*

> + Create user     
>   + http://localhost:8000/register/users/
> + Get user tokens      
>   + http://localhost:8000/api/token/
> + Refresh user tokens     
>   + http://localhost:8000/api/token/refresh/


