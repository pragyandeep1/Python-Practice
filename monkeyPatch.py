class monkey:
    def monkeyFunc(self):
        print("my function")


def patchFunc():
    print("patching on monkey")


# normal class method call
objMonkey = monkey()
objMonkey.monkeyFunc()

# calling class method after monkey patch
objMonkey.monkeyFunc = patchFunc
objMonkey.monkeyFunc()