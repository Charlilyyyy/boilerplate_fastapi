from repositories.userRepository import get_all_users, get_user_by_id, create_user, update_user, delete_user

# Service to fetch all users
def fetch_all_users():
    return get_all_users()

# Service to get a single user
def fetch_user(user_id: int):
    return get_user_by_id(user_id)

# Service to create a new user
def add_user(user_data):
    return create_user(user_data)

# Service to update a user
def modify_user(user_id: int, updated_data):
    return update_user(user_id, updated_data)

# Service to delete a user
def remove_user(user_id: int):
    return delete_user(user_id)
