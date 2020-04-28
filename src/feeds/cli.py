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
        "entry" : {
            "title" : "",
            "link" : "",
            "published" : ""
        },
        "last_published" : ""
    }

    blog["name"] = d['feed']['title']
    blog["url"] = d['feed']['title']
    blog["user_name"] = author[1]
    blog["icon"] = ""
    blog["last_published"] = d['items'][0]['published']
    blog["entry"]["title"] = d['items'][0]['title']
    blog["entry"]["link"] = d['items'][0]['link']
    blog["entry"]["published"] = d['items'][0]['published']
    return blog

def sort_blogs(blogs):
    return sorted(blogs,key=lambda x: x['last_published'])

if __name__ == "__main__":

    authors = get_authors_data('data/authors.csv')

    blogs = []
    for author in authors:
        blogs.append(get_blog_data(author))

    print(sort_blogs(blogs))
    