
from .controller import AddImage

def routes(api,base_path):
    pth = base_path + '/mod2'

    api.add_resource(AddImage,pth + '/add_image')
    # api.add_resource(Square,pth + '/getsqaure/<int:num>')
    # api.add_resource(TodoSimple,pth + '/')
   