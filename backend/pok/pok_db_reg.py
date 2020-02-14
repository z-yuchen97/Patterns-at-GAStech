from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT
from dateutil.parser import parse
from flask import Flask
import pymysql 
import config_pok

# connection with mysql database
app = Flask(__name__)
app.config.from_object(config_pok)
db = SQLAlchemy(app)

class Article(db.Model):
    __tablename__ = 'article'
    filename = db.Column(db.String(255), primary_key = True)
    issuedate = db.Column(db.String(255))
    media = db.Column(db.String(255))
    title = db.Column(db.String(255))
    filecontent = db.Column(db.Text)

class Email(db.Model):
    __tablename__ = 'email'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    emailfrom = db.Column(db.String(1255))
    emailto = db.Column(db.Text)
    date = db.Column(db.String(255))
    subject = db.Column(db.Text)

class Emaildegree(db.Model):
    __tablename__ = 'emaildegree'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    emaildegree = db.Column(db.String(255))
    emailname = db.Column(db.String(255))

class Emailparse(db.Model):
    __tablename__ = 'emailparse'
    autoid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    emailfrom = db.Column(db.String(1255))
    emailto = db.Column(db.String(2000))
    emaildate = db.Column(db.String(255))
    emailsubject = db.Column(db.Text)

db.create_all()

class PokInit():
    def __init__(self):
        pass

    def select_article(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from article"""
        cursor.execute(sql)
        article_list = cursor.fetchall()
        db.close()
        return article_list

    def select_email(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from email"""
        cursor.execute(sql)
        email_list = cursor.fetchall()
        db.close()
        return email_list

    def select_emaildegree(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from emaildegree"""
        cursor.execute(sql)
        emaildegree_list = cursor.fetchall()
        db.close()
        return emaildegree_list

    def select_emailparse(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from emailparse"""
        cursor.execute(sql)
        emailparse_list = cursor.fetchall()
        db.close()
        return emailparse_list


def init_article():
    article_list = PokInit().select_article()
    for article in article_list:
        filecontent = article[4].replace("\n", "; ")
        issuedate = article[1].replace("/", "-")
        print(issuedate)
        pok_article = Article(
                    filename = article[0],
                    issuedate = issuedate,
                    media = article[2],
                    title = article[3],
                    filecontent = article[4])
        db.session.add(pok_article)
        db.session.commit()

def init_email():
    email_list = PokInit().select_email()
    for email in email_list:
        pok_email = Email(
                    emailfrom = email[1],
                    emailto = email[2],
                    date = email[3],
                    subject = email[4])
        db.session.add(pok_email)
        db.session.commit()

def init_emaildegree():
    emaildegree_list = PokInit().select_emaildegree()
    for email_degree in emaildegree_list:
        pok_emaildegree = Emaildegree(
                    emaildegree = email_degree[1],
                    emailname = email_degree[2])
        db.session.add(pok_emaildegree)
        db.session.commit()

def init_emailparse():
    emailparse_list = PokInit().select_emailparse()
    for emailparse in emailparse_list:
        pok_emailparse = Emailparse(
                    emailfrom = emailparse[1],
                    emailto = emailparse[2],
                    emaildate = emailparse[3],
                    emailsubject = emailparse[4])
        db.session.add(pok_emailparse)
        db.session.commit()


if __name__ == "__main__":
    # initialize pok data
    # init_email()
    init_article()
    # init_emaildegree()
    # init_emailparse()
    