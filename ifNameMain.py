# 1. module can be run as a standalone program
# 2. module can be imported and used by other modules
# python interpreter sets "special variables", one of which is __name__
# then python will execute the code found within __main__

def hello():
    print("hello")

if __name__ == '__main__':
    hello()
