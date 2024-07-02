from flask_restful import Resource, Api
import logging as logger

# from modules.Hello import routes as hello_routes
from Modules.mod1 import routes as mod1_route
from Modules.mod2 import routes as mod2_route
# from modules.Business import routes as add_busines_route

class Routes(object):
    def __init__(self,app,base_path=None):
         self.api=Api(app)
         self.base_path=''.join(base_path)
         logger.basicConfig(level=logger.DEBUG)  
         logger.info(f"Base path {self.base_path}")
      
    #   here i have added imported route from init.py
     #     hello_routes(self.api,self.base_path)
         mod1_route(self.api,self.base_path)
         mod2_route(self.api,self.base_path)
         
         
      