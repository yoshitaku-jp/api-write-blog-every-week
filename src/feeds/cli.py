import csv
import feedparser

def get_authors_data(file):
    authors = []
    with open(file) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            authors.append(row)
    return authors

def get_blog_data(author):

    d = feedparser.parse(author[0])
    blog = {
        "name" : "",
        "url" : "",
        "user_name" : "",
        "icon" : "",
        "entry" : [{
            "title" : "",
            "link" : "",
            "published" : ""
        },
        {
            "title" : "",
            "link" : "",
            "published" : ""
        },
        {
            "title" : "",
            "link" : "",
            "published" : ""
        }],
        "last_published" : ""
    }

    blog["name"] = d['feed']['title']
    blog["url"] = d['feed']['title']
    blog["user_name"] = author[1]
    blog["icon"] = ""
    blog["last_published"] = d['items'][0]['published']
    blog["entry"][0]["title"] = d['items'][0]['title']
    blog["entry"][0]["link"] = d['items'][0]['link']
    blog["entry"][0]["published"] = d['items'][0]['published']
    blog["entry"][1]["title"] = d['items'][1]['title']
    blog["entry"][1]["link"] = d['items'][1]['link']
    blog["entry"][1]["published"] = d['items'][1]['published']
    blog["entry"][2]["title"] = d['items'][2]['title']
    blog["entry"][2]["link"] = d['items'][2]['link']
    blog["entry"][2]["published"] = d['items'][2]['published']
    return blog

def sort_blogs(blogs):
    return sorted(blogs,key=lambda x: x['last_published'])

if __name__ == "__main__":

    authors = get_authors_data('data/authors.csv')

    blogs = []
    for author in authors:
        blogs.append(get_blog_data(author))

    print(sort_blogs(blogs))
    