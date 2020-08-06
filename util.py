import os

    val = os.getenv(key)
    if val is None:
        raise Exception('environment variable %s is not defined' % key)
    return val
