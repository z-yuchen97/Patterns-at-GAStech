import pymysql 
import time

class DataBase():
    def __init__(self):
        pass
    
    def create_article_table(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Drop table if it already exist using execute() method.
        cursor.execute("drop table if exists article")
        # Create table as per requirement
        sql = """create table article (
                filename varchar(20) primary key,
                issuedate varchar(100),
                media varchar(200),
                title varchar(200),
                filecontent text)"""
        cursor.execute(sql)
        # disconnect from server
        db.close()

    def insert_article(self, file_name, issue_date, report_media,
                report_title, file_content):
        articles = []
        articles.append((file_name, issue_date, report_media, report_title, file_content))
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """insert into article values(%s, %s, %s, %s, %s)"""
        cursor.executemany(sql, articles)
        db.commit()
        # disconnect from server
        db.close()

    def select_article_keyword(self, article_keyword):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # sql = """select * from emailparse where emailfrom = %s or emailto = %s"""
        # cursor.execute(sql, (email_doubtman, email_doubtman) )
        sql = """select * from article where filecontent like %s and
                issuedate = '2014/01/20' or issuedate = '2014/01/21' """
        article_keyword = "%" + article_keyword + "%"
        cursor.execute(sql, article_keyword)
        article_keyword_list = cursor.fetchall()
        db.close()
        return article_keyword_list
    
    def select_email(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select * from email"""
        cursor.execute(sql)
        email_abtract = cursor.fetchall()
        db.close()
        return email_abtract

    def create_email_table(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Drop table if it already exist using execute() method.
        cursor.execute("drop table if exists emailparse")
        # Create table as per requirement
        sql = """create table emailparse(
                autoid int  primary key  auto_increment,
                emailfrom varchar(2000),
                emailto varchar(2000),
                emailtime varchar(200),
                emailsubject text)"""
        cursor.execute(sql)
        # disconnect from server
        db.close()

    def insert_email(self, email_from, email_to, email_time, email_subject):
        emails = []
        emails.append((email_from, email_to, email_time, email_subject))
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """insert into emailparse(emailfrom, emailto, emailtime, emailsubject) 
                    values(%s, %s, %s, %s)"""
        cursor.executemany(sql, emails)
        db.commit()
        # disconnect from server
        db.close()

    def select_email_fromto(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """select emailfrom, emailto from emailparse"""
        cursor.execute(sql)
        email_fromto_list = cursor.fetchall()
        db.close()
        return email_fromto_list

    def select_email_doubtman(self, email_doubtman):
        # email_doubtman = self.email_doubtman
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # sql = """select * from emailparse where emailfrom = %s or emailto = %s"""
        # cursor.execute(sql, (email_doubtman, email_doubtman) )
        sql = """select * from emailparse where emailfrom = %s"""
        cursor.execute(sql, email_doubtman)
        email_doubtman_list = cursor.fetchall()
        db.close()
        return email_doubtman_list

    def create_emaildegree_table(self):
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        # Drop table if it already exist using execute() method.
        cursor.execute("drop table if exists emaildegree")
        # Create table as per requirement
        sql = """create table emaildegree(
                autoid int  primary key  auto_increment,
                emaildegree varchar(200),
                emailname varchar(200))"""
        cursor.execute(sql)
        # disconnect from server
        db.close()

    def insert_emaildegree(self, email_degree, email_name):
        degrees = []
        degrees.append((email_degree, email_name))
        # Open database connection
        db = pymysql.connect(user = "root", password = "Root2021@",
                            host = "127.0.0.1",
                            database = "pok_origin" )
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = """insert into emaildegree(emaildegree, emailname) values(%s, %s)"""
        cursor.executemany(sql, degrees)
        db.commit()
        # disconnect from server
        db.close()