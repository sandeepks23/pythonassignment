import requests

def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    users=response.json()
    # print(data)
    for user in users:
        print(user)


def get_user(id):
    response=requests.get("https://jsonplaceholder.typicode.com/posts/%d"%(id))
    user=response.json()
    # print(user)
    return user

def get_detail(id):
    response = requests.get("https://jsonplaceholder.typicode.com/posts/%d" % (id))
    user = response.json()
    return user['body']
    # print(user['body'])


def get_comments():
    response=requests.get("https://jsonplaceholder.typicode.com/comments")
    comments=response.json()
    for comment in comments:
        print(comment)

def get_comment(id):
    response=requests.get("https://jsonplaceholder.typicode.com/posts/%d/comments" %(id))
    comments=response.json()
    for comment in comments:
        print(comment)




