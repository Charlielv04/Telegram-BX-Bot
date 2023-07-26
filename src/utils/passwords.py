from passlib.context import CryptContext

def hash_password(password):
    HASH_SCHEME = "bcrypt_sha256"
    password_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")
    return password_context.hash(password)

def verify_password(stored_hash, password):
    HASH_SCHEME = "bcrypt_sha256"
    password_context = CryptContext(schemes=[HASH_SCHEME], deprecated="auto")
    return password_context.verify(password, stored_hash)

