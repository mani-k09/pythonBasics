class Post():
    def __init__(self,custom_message,author_name):
        self.message= custom_message
        self.author = author_name

    def publish_message(self):
        print(f"The message : {self.message} was published by the {self.author}")

