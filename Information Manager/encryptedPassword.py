def encryptedPassword(len):
    import random
    list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result = ''.join((random.choice(list) for i in range(len)))
    return result

