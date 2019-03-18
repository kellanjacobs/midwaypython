import os

USER = os.getenv('HELLO_NAME', 'world')
print("Hello %s" % USER)