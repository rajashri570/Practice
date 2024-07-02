from .controller import Hello
from .controller import Square,TodoSimple

def routes(api,base_path):
    pth = base_path + '/mod1'

    api.add_resource(Hello,pth + '/greet')
    api.add_resource(Square,pth + '/getsqaure/<int:num>')
    api.add_resource(TodoSimple,pth + '/')
   