class User():
    def __init__(self,user_name,user_email,user_job,user_pwd):
        self.name = user_name
        self.email = user_email
        self.title = user_job
        self.password = user_pwd

    def change_password(self,new_password):
        self.password= new_password

    def change_email(self,new_email):
        self.email=new_email

    def get_user_info(self):
        print(f"The user {self.name} job title is {self.title} and they can be reached on {self.email}")

app_user_one = User("mani","log@gmail.com","QA Lead","secretP")
app_user_one.get_user_info()

app_user_one.change_email("changedEmail@gmail.com")
app_user_one.get_user_info()


