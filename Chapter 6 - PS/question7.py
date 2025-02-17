# Write a program to find out whether a given post is talking about "Ankit" or not.

post = input("Enter the post: ")

if ("Ankit".lower() in post.lower()):
    print("This post is talking about Ankit")
else:
    print("This post is not talking about Ankit")

