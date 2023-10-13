
class User:
    def __init__(self,name,username,email) -> None:
        self.username = username
        self.name = name
        self.email = email
        print(f"User {self.username} created.")

    def introduce_yourself(self):
        print(f"My name is {self.username}. Plis contact me")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"{self.username}, {self.name}, {self.email}"
        
peter = User('Peter','petes','mugwepeter0@gmail.com')
# print(peter)

class usersDB():
    def __init__(self) -> None:
        self.users = []

    def insert(self,user):
        i = 0
        for i in range(len(self.users)):
            if self.users.username[i] > user.username:
                break
            i + 1
        self.users.insert(i,user)

        # print(self.users)

    def find(self,username):
        for us in self.users:
            if us.username == username:
                return us
            else:
                print(f"{username} doesnt exist")

    def update(self,user):
        user = self.find(user)
        user.email = "another@gmail.com"
        return user.email

    def list_all(self):
        return self.users
    
    def delete(self,user):
        user = self.find(user)



    


# db = usersDB()
# db.insert(peter)
# print(db.find("petes"))
# print(db.update("petes"))
# print(db.list_all())


## second tree
class tree:
    def __init__(self,key):
        self.data = key
        self.right = None
        self.left = None
    
def insert(root,data):
    if root is None:
        return tree(data)

    else:
        if root.data == data:
            return

        elif root.data > data:
            root.left = insert(root.left,data)

        else:
            root.right = insert(root.right,data)

    return root


def inorder(root,results = []): #from bottom left => root => right
    if root is None:
        return
    
    inorder(root.left)
    results.append(root.data)
    inorder(root.right)

    return results

def preorder(root,results = []):  #root => left => right
    if root is None:
        return
    
    results.append(root.data)
    preorder(root.left)
    preorder(root.right)

    return results


def postorder(root,results = []): #left => right => root
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    results.append(root.data)

    return results



root = tree(50)

insert(root,20)
insert(root,89)
insert(root,10)
insert(root,1)
insert(root,15)
insert(root,101)
insert(root,30)
insert(root,61)

print(f"Inorder : {inorder(root)}")
print(f"Postorder : {postorder(root)}")
print(f"Preorder : {preorder(root)}")


