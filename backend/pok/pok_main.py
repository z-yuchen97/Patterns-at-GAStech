from parse import ParseFile
from analysis import Analyze

def parse_article():
    dir_name = "./A1_Data/articles/"
    ParseFile().read_article(dir_name)

def parse_email():
    ParseFile().filter_email()

def analyze():
    Analyze().email_network()
    # Analyze().email_site_search()
    # Analyze().article_site_search()

if __name__ == "__main__":
    parse_article()
    parse_email()
    analyze()