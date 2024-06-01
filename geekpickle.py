import pickle
import io

class SimpleObject(object):
    def __init__(self, name):
        self.name = name
        l = list(name)
        l.reverse()
        self.name_backwards = ''.join(l)
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('cPickle'))
data.append(SimpleObject('last'))

out_s = io.BytesIO()  # Use BytesIO instead of StringIO

for o in data:
    print('WRITING: %s (%s)' % (o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

in_s = io.BytesIO(out_s.getvalue())  # Use BytesIO instead of StringIO

while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('READ: %s (%s)' % (o.name, o.name_backwards))
