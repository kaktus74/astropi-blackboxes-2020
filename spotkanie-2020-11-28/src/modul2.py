print("Moduł 2, __file__: {0}".format(__file__))
print("Moduł 2, __name__: {0}".format(__name__))


def egg():
    return 1

if __name__ == '__main__':
    print('Jestem modułem 2, zostałem odpalony jako główny')
