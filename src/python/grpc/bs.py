# Importing the `BusinessService` class from the `grongier.pex` module.
from grongier.pex import BusinessService

# > The gRPCService class is a BusinessService that sends a request to the CrudPerson service and
# returns the response
class gRPCService(BusinessService):

    def on_init(self):
        
        if not hasattr(self,'target'):
            self.target = "Python.CrudUser"
        
        return 

    def on_process_input(self,request):
        return self.send_request_sync(self.target,request)

 