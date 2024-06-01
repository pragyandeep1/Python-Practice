import animals


def patchFunc():
    print("patching on monkey")


# normal class method call
objMonkey = animals.monkey()
objMonkey.monkeyFunc()

# calling class method after monkey patch
objMonkey.monkeyFunc = patchFunc
objMonkey.monkeyFunc()