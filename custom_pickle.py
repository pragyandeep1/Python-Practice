import pickle


class foobar:
    def __init__(self):
        self.p = 25
        self.q = " testing "
        self.r = lambda x: x * x

    def __getstate__(self):
        attribute = self.__dict__.copy()
        del attribute['r']
        return attribute


user_foobar_instance = foobar()
user_pickle_string = pickle.dumps(user_foobar_instance)
user_new_instance = pickle.loads(user_pickle_string)

print(user_new_instance.__dict__)  