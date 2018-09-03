def init (data):
    data['first'] = {}
    data['middle']= {}
    data['last'] = {}

def hello_3(greeting = 'Hello',name = 'world'):
    print('{},{}!'.format(greeting,name))

params = {'name':'Sir Robin','greeting':'Well met'}
# hello_3(**params)

hello_3(params['greeting'],params['name'])



