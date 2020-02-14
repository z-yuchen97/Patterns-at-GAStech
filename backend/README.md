# Flask Instruction

## 1. Environment Setting(Local Machine / Remote Server)
* Local Machine: macOS Catalina 10.15.3
* Remote Server: AWS Ubuntu Server 18.04 LTS (HVM), SSD Volume Type 

### 1.0 Two approaches for running(Introduction for 1st method)
* venv -> (venv)flask -> dont need to install flask to run python3 app.py;
* pip3 install flask on machine -> python3 app.py


### 1.1 python3, pip3
``` bash
$ python3 --version
$ pip3 --version
```

### 1.2 virtual environment
```
$ sudo pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

### 1.3 flask installation
```
# if install flask, you dont need source activate
$ sudo pip3 install Flask
```

### 1.4 running flask
```
# on remote server
$ flask run --host=0.0.0.0
# a simple way 
$ python3 app.py
```

### 1.5 Connection with MySQL through flask_sqlalchemy
```
sudo pip3 install flask_sqlalchemy
```

## 2 Data Processing (On Local Machine)
### 2.0 Import .csv files into MySQL database (on Local Machine)
```
mysql> create database pok_origin;
mysql> create database pok; 
```
* Protectors of Kronos - ./pok/A1_data/email headers.csv
    * Add autoid mannually in .csv file
    * Using Import Wizard in Navicat to database 'pok_origin'
    * Encode with ISO-8859-1(latin)
    * Import it with text data type for 'to' and 'subject' field
    * Choose 'autoid' field as primary key with int type
    * **Modidy** the table name 'email headers' to 'email'

```
mysql> create database patterns_origin;
mysql> create database patterns;
```
* Patterns at GAStech - ./patterns/A2_data/*.csv
    * Add autoid for [car-assignemt/cc_data/gps/loyalty].csv files manually
    * Using Import Wizard in Navicat to database 'pok_origin'
    * Encode with ISO-8859-1(latin)
    * Choose 'autoid' as primary key
    * **Modidy** the table name 'car-assignments' to 'car_assignments'

### 2.1 Parse and Export Original Database (on Local Machine)
* Protectors of Kronos Data Wrangling
    * Following command lines will parse articles into structured data and store them in pok database and local directory.
    * It can also give you a static social network from the given data from email headers.csv
```
$ cd pok
$ mkdir A1_analysis
$ python3 pok_main.py
```

### 2.2 Convert sql tables into regularized ORM mode (Local Machine)
```
$ python3 pok_db_reg.py
$ python3 patterns_db_reg.py
```
* Above command lines will use original database 'pok_origin' 'patterns_origin' to generate two new structuralized databases 'pok' and 'patterns'.
* Export those tables to 'pok.sql' and 'patterns.sql'
* Change encode rules in .sql files for create table to 'utf8mb4_general_ci'

### 2.3 Use .sql sentence to generate tables in remote server (Local Machine / Remote Server)
```
$ mysql -u root -p pok < ./sql/pok.sql
$ mysql -u root -p patterns < ./sql/patterns.sql
```

## 3 Manipulate Data with ORM - sqlalchemy
### 3.1 Reflect tables in database with engine
Since we have used sqlalchemy to build orm, we just need reflect them back.