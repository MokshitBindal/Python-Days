# class UserName: #pascal case
    
#     def __init__(self): # executes everytime when we create a object using class
#         print("New object is created") 

# user_1 = UserName()
# user_1.name = "Mokshit"
# user_1.age = 18

# print(user_1.name)

# user_2 = UserName()
# user_2.names = "Wrong name entered"
# user_2.age = 21


class User:
    
    def __init__(self, user_id, username): 
        # these arguements are mandatory when creating a class
        # else error will be thrown
        self.id = user_id
        self.username = username
        self.followers = 0 #setting default value, no need to tell at function start 
        self.following = 0 #
        
    def follow(self, user):
        self.following += 1
        user.followers += 1
        
newuser_1 = User("001", "Mokshit")
newuser_2 = User("002", "Mohit")

newuser_2.follow(newuser_1)

print(newuser_1.followers)
print(newuser_1.following)
print(newuser_2.followers)
print(newuser_2.following)