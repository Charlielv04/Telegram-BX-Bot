from utils import config

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

def subs_of_committee(committee_name):
    """
    Takes a committee name and returns a list of the keys of the db of all users subscribed to it
    """
    keys_of_subs = []
    cursor = '0'

    while cursor != 0:
        cursor, keys = r.scan(cursor=cursor, match="user*")
        for key in keys:
            subs = r.hget(key, "subs")
            sub_list = sub_db_list(subs)
            if committee_name in sub_list:
                keys_of_subs.append(key)
    return keys_of_subs

def get_pass_committee(committee_name):
    """
    Takes a committee name and returns the password associated to that committee
    """
    key = 'pass:' + str(committee_name)
    password = r.get(key)
    return password

def get_users_info(keys):
    """
    Takes a list of keys and returns the dictionaries associated to them
    """
    users_info = []
    for key in keys:
        info = r.hgetall(key)
        users_info.append(info)
    return users_info

def user_wrong_password(user):
    """
    Registers the users that put passwords wrong when logging to committees to give a wake-up call to any people playing
    """
    key = user_to_key(user)
    info = r.hgetall(key)
    try:
        info["errors"] = int(info["errors"]) + 1
    except KeyError:
        info["errors"] = 1
    r.hset(key, mapping=info)

def record_logging(user, committee_name):
    """
    Registers the last fifty loggings to a committee
    """
    key = 'log:' + committee_name
    length = r.llen(key)
    print(length)
    if r.llen(key) >= 50:
        r.rpop(key)
    r.lpush(key, user.full_name)

