import os
import re
from datetime import datetime
from pythondb import DataBase

class ParseFile():
    def __init__(self):
        pass

    def transfer(self, parsed_date):
        day = parsed_date.split()[0]
        month = parsed_date.split()[1]
        year = parsed_date.split()[2]
        month_dict = {"January": "01" , "February": "02", "March": "03", "April": "04",
                    "May": "05", "June": "06", "July": "07", "August": "08", 
                    "September": "09", "October": "10", "November": "11", "December": "12"} 
        month = month_dict[month]
        issue_date = year + "/" + month + "/" + day
        return issue_date

    def read_article(self, dir_name):
        name_list = os.listdir(path = dir_name)
        DataBase().create_article_table()
        for file_name in name_list:
            file_path = dir_name + file_name
            file = open(file_path, "r", encoding="ISO-8859-1")
            lines = file.readlines()
            file.close()
            content = []
            for line in lines:
                if(len(line.strip()) > 0):
                    content.append(line)
            report_media = content[0]
            report_title = content[1]
            file_content = ''.join(content)
            issue_date = re.findall(r"[\d]{4}/[\d]{2}/[\d]{2}", file_content)
            if len(issue_date) == 0 : 
                issue_date = re.findall(r'''(\d{1,2}\s+(December|January|February|March|April|
                            |May|June|July|August|September|October|November)\s+\d{4})''', file_content)
                if len(issue_date) == 0 : 
                    # only in case of wrong match
                    issue_date = "3000/12/12"
                else:
                    issue_date = ParseFile().transfer(issue_date[0][0])
            else:
                issue_date = issue_date[0]
            # preserve information in database
            DataBase().insert_article(file_name, issue_date, report_media, report_title, file_content)
            # generate new file for analysis
            issue_date = issue_date.replace("/", "-")
            report_media = report_media.replace("\n", "-")
            report_media = report_media.replace(" ", "-")
            if os.path.isdir("./A1_analysis/sorted_media_article/") == False: 
                os.mkdir("./A1_analysis/sorted_media_article/")
            if os.path.isdir("./A1_analysis/sorted_number_article/") == False: 
                os.mkdir("./A1_analysis/sorted_number_article/")
            # for same media
            new_name1 = issue_date + "-" + report_media + file_name
            newfile = open("./A1_analysis/sorted_media_article/" + new_name1, "w+")
            newfile.write(file_content)
            # for convenience to read in mysql
            new_name2 = issue_date + "-" + file_name.strip(".txt") + "-" + report_media + ".txt"
            newfile = open("./A1_analysis/sorted_number_article/" + new_name2, "w+")
            newfile.write(file_content)
            newfile.close()

    def filter_email(self):
        email_abstract = DataBase().select_email()
        DataBase().create_email_table()
        for email in email_abstract:
            email_from = email[1]
            email_time = email[3]
            email_subject = email[4]
            # filter name in email_from and email_to
            email_from = re.findall(r"(([\S]+)@\S+)", email_from)[0]
            email_from = email_from[1]
            # split every email_to_users in email_to_list and construct network edge
            email_to_content = email[2]
            email_to_list = re.findall(r"(([\S]+)@\S+)", email_to_content)
            email_to_list = [person[1] for person in email_to_list]
            for email_to in email_to_list:
                DataBase().insert_email(email_from, email_to, email_time, email_subject)