# Global dictionary to store user information
users_db = { }

def register_user(username, password, email):
    if username in users_db:
        return "Username already exists"
    users_db[username] = {
        "password": password,
        "email": email
    }
    return f"Registration successful for {username}"

def login_user(username, password):
    if username not in users_db:
        return "User not found"
    if users_db[username]["password"] != password:
        return "Incorrect password"
    return f"Welcome back, {username}"

# Testing the program by registering users
print(register_user("ram", "ram123", "ram@email.com"))
print(register_user("shyam", "shyam456", "shyam@email.com"))
print(register_user("hari", "hari231", "hari@email.com"))

# Optional login tests
print(login_user("ram", "ram123"))
print(login_user("shyam", "wrongpass"))
print(login_user("unknown", "123"))