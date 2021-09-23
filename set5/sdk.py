import features

print("1.Post \n2.Comment")
ch=input("Enter choice")
if(ch=='1'):
    print("1.Get posts\n2.Get post based on the user\n3.Get post detail")
    p=input("Enter choice")
    if(p=='1'):
        features.get_posts()
    elif(p=='2'):
        id=int(input("Enter id"))
        print(features.get_user(id))
    elif(p=='3'):
        id=int(input("Enter id"))
        print(features.get_detail(id))

elif(ch=='2'):
    print("1.Get comments\n2.Get comments based on the post")
    c=input("Enter choice")
    if(c=='1'):
        features.get_comments()
    elif(c=='2'):
        id=int(input("Enter post_id"))
        features.get_comment(id)
