from utils import config

r = config.r

def db_to_list(db_string):
    """
    Takes a comma separated (string), as stored in the redis db, and returns a normal python list
    """
    if db_string == '': return []
    db_list = db_string.split(', ')
    return db_list

def list_to_db(db_list):
    """
    Takes a python list and returns it as a comma separated list (string) to be stored in the redis db
    """
    if db_list == []: return ''
    db_string = ', '.join(db_list)
    return db_string

def list_to_telegram(db_list):
    """
    Takes a python list and returns a list to be inserted into a telegram message and portrayed as such
    """
    if db_list == []: return ''
    string_list = ' - ' + '\n - '.join(db_list)
    return string_list

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
        'subs': '', #comma separated list as redis has to store everything as strings
        'rights': ''
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
            sub_list = db_to_list(subs)
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

def get_user_info(user):
    """
    Takes a user and returns its info
    """
    info = r.hgetall(user_to_key(user))
    return info

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

def get_committee_access(committee_name):
    """
    Takes a committee name and returns its settings for the hub
    """
    key = 'access:' + committee_name
    access = r.hgetall(key)
    return access

def add_one_time_pass(password, committee_name):
    """
    Takes a generated password and committee name and uploads it on the database for future use
    """
    key = 'pass:' + committee_name
    r.set(key, password)

def use_one_time_pass(password, committee_name):
    """
    Takes a password and a committee name and uses the password if valid, then deletes the database instance
    """
    key = 'pass:' + committee_name
    if r.exists(key) and password == r.get(key):
        r.delete(key)
        return True
    return False

def add_access_rights(user, committee_name, committee_command):
    """
    Adds access rights to a user
    """
    access_string = r.hget(user_to_key(user), key="rights")
    access_list = db_to_list(access_string)
    access_list.append(committee_command)
    updated_access = list_to_db(access_list)
    committee_key = 'access:' + committee_name
    p = r.pipeline()
    p.hset(user_to_key(user), key="rights", value=updated_access)
    p.hset(committee_key, key=user.id, value="admin")
    p.execute()

def eliminate_access_rights(id, committee_name, committee_command):
    """
    Eliminates access rights to a given id
    """
    user_key = 'user:' + id
    access_string = r.hget(user_key, key="rights")
    access_list = db_to_list(access_string)
    access_list.remove(committee_command)
    updated_access = list_to_db(access_list)
    committee_key = 'access:' + committee_name
    p = r.pipeline()
    p.hset(user_key, key="rights", value=updated_access)
    p.hdel(committee_key, id)
    return p.execute()

def change_committee_access(committee_name, new_rights):
    """
    Updates the committee access to a new set of rights
    """
    commmittee_key = 'access:' + committee_name
    r.hset(commmittee_key, mapping=new_rights)
