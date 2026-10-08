#LAB 3 Object Collaboration & Direct Dependency Injection

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def introduce(self) -> None:
        print(f"HI, my name is {self.name} this is my email:({self.email}).")

class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author: User = author

    def show_post(self) -> None:
        print(f" TITLE:  {self.title}")
        print(f" AUTHOR: {self.author.name} <{self.author.email}>")
        print(f" CONTENT:\n {self.content}")

#TESTING GROUNDS
if __name__ == "__main__":
    #User Creation
    
    user1 = User(
        name="Aldo Fabian",
        email="aldocarrillo2002@hotmail.com"
    )
    user1.introduce()

    #Associated Post Creation
    post1 = Post(
        title="Informatio about goats",
        content=(
            "The goats are animals that live in montains or are preserved in barns"
        ),
        author=user1
    )

    #Information Retieval
    post1.show_post()