import pickle


class forexample_class:
    the_number = 25
    the_string = " hello"
    the_list = [1, 2, 3]
    the_dict = {" first ": " a ", " second ": 2, " third ": [1, 2, 3]}
    the_tuple = (22, 23)


user_object = forexample_class()

user_pickled_object = pickle.dumps(user_object)  # here, user is Pickling the object
print(f" This is user's pickled object: \n {user_pickled_object} \n ")

user_object.the_dict = None

user_unpickled_object = pickle.loads(user_pickled_object)  # here, user is Unpickling the object
print(
    f" This is the_dict of the unpickled object: \n {user_unpickled_object.the_dict} \n ")  