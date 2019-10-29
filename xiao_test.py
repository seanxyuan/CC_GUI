
def sumAdd(a):
    a=a+10
    return a



class animal():

    def __init__(self, n, h):
        self.name=n
        self.height=h

    def getName(self):
        return self.name


def main():
    dog = animal("pie", 10)
    print(dog.name)

if __name__ == "__main__":
    main()