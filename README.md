# Patterns at Gastech
* Thanks to Heming, who helps me do the backend part of this project, and design the website with me.

## 1. Environment Setting(local machine / Remote Server)
* Local Machine: macOS Catalina 10.15.3
* Remote Server: AWS Ubuntu Server 18.04 LTS (HVM), SSD Volume Type 

## 2. Run up backend and frontend
```
$ cd backend
$ python3 app.py
$ cd ../frontend
$ npm run dev
```

## 3. Basic Function (implemented by present)
* Right now, we have implemented the backend with flask running on server, and we use the sqlalchemy as ORM to reflect those tables in MySQL database.
* Besides that, we use Vue.js as our front end and we have drew the basic GPS tracks on the Canvas. And we implemented the search function to search certain GPS track for certain person with certain time range.
* Thanks to the MySQL database and sqlalchemy on our backend, we process those data fluently.
* Next, we would like to map those points on the Kronos Tourist picture, and use other attributes like colors and lines to make it more clearly. 