# Simulated in-memory "database"
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Doe", "email": "jane@example.com"},
]

# Repository functions
def get_all_users():
    return users

def get_user_by_id(user_id: int):
    return next((user for user in users if user["id"] == user_id), None)

def create_user(user_data: dict):
    new_id = len(users) + 1
    user_data["id"] = new_id
    users.append(user_data)
    return user_data

def update_user(user_id: int, updated_data: dict):
    for user in users:
        if user["id"] == user_id:
            user.update(updated_data)
            return user
    return None

def delete_user(user_id: int):
    global users
    users = [user for user in users if user["id"] != user_id]
    return True
