class Man:
    def __init__(self, name):
        self.name = name
        print('hello world!')
    
    def hello(self):
        print('hello ' + self.name + '!')
    
    def goodbye(self):
        print('goodbye ' + self.name + '...')

m = Man('Inji')
m.hello()
m.goodbye()