#Lab 2: Object Association & Multi-Class Systems
from __future__ import annotations
from typing import Union

class User:
    def __init__(self, name: str, email: str, age: int, password: str):
        self.name = name
        self.email = email
        self.age = age
        self.__password = password 

    def login(self, entered_password: str) -> bool:
        if entered_password == self.__password:
            print(f"Login succesfull, Welcome back {self.name}!")
            return True
        else:
            print(f"Incorrect password for this user.")
            return False

    def create_post(self, title: str, content: str) -> Post:
        new_post = Post(title=title, content=content, author=self, likes=0)
        print(f"[{self.name}] Created a new post: '{title}'")
        return new_post

class Post:
    def __init__(self, title: str, content: str, author: User, likes: int = 0):
        self.title = title
        self.content = content
        self.author: User = author
        self.likes = likes

    def show(self) -> None:
        print(f" POST: {self.title.upper()}")
        print(f" Author: {self.author.name} ({self.author.email})")
        print(f" Likes:  {self.likes}")
        print(f" {self.content}")

class Comment:
    def __init__(self, text: str, author: User, receiver: Union[Post, User]):
        self.text = text
        self.author: User = author
        self.receiver = receiver

    def show(self) -> None:
        if isinstance(self.receiver, Post):
            target_info = f"Post '{self.receiver.title}' by {self.receiver.author.name}"
        elif isinstance(self.receiver, User):
            target_info = f"User profile of {self.receiver.name}"
        else:
            target_info = str(self.receiver)

        print(f"\n{self.author.name} commented on {target_info}:")

class Message:
    def __init__(self, text: str, sender: User, receiver: User):
        self.text = text
        self.sender: User = sender
        self.receiver: User = receiver

    def show(self) -> None:
        print(f" From: {self.sender.name} ({self.sender.email})")
        print(f" To:   {self.receiver.name} ({self.receiver.email})")
        print(f"\"{self.text}\"")

#TESTING GROUNDS
if __name__ == "__main__":
    print("LOGIN")
    user1 = User(
        name="Aldo Fabian",
        email="aldocarrillo2002@hotmail.com",
        age=23,
        password="aldo123"
    )
    user2 = User(
        name="Fernando Manuel",
        email="Fernandocarrillo95@hotmail.com",
        age=25,
        password="carrascuas123"
    )

    user1.login("WrongPass")
    user1.login("aldo123")

    print("\nCreate Post USER 1")
    post1 = user1.create_post(
        title="hotdog a sandwich or another creation",
        content="in the beggining of the time sandwich it's a meat between two breads, so what exactly it's a hotdog?"
    )

    print("\nDisplay Output")
    post1.show()

    print("\nInteraction Verification (Optional/Extension)")
    comment1 = Comment(
        text="Thanks now i have more doubts than answers",
        author=user2,
        receiver=post1
    )
    comment1.show()

    dm1 = Message(
        text="oh do you?",
        sender=user1,
        receiver=user2
    )
    dm1.show()