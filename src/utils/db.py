import config

r = config.r

def sub_db_list(subs):
    """
    Takes a comma separated (string), as stored in the redis db, and returns a normal python list
    """
    if subs == '': return []
    sub_list = subs.split(', ')
    return sub_list

def sub_list_db(sub_list):
    """
    Takes a python list of subscriptions and returns it as a comma separated list (string) to be stored in the redis db
    """
    if sub_list == []: return ''
    subs = ', '.join(sub_list)
    return subs

def add_to_db(user):
    """
    Takes a user object from the telegram library and uploads its relevant information to the redis db using its id as hash
    """
    key = user_to_key(user)
    if r.exists(user_to_key(user)):
        return
    info = {
        'name': user.first_name,
        'fullname': user.full_name,
        'id': user.id,
        'subs': '' #comma separated list as redis has to store everything as strings
    }
    r.hset(key, mapping=info)

def user_to_key(user):
    """
    Formats the user id as a string to fit the name organization of the redis db
    """
    return 'user:' + str(user.id)