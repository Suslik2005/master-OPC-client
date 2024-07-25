#from opcua import Client
#
#class HelloClient:
#    def __init__(self, endpoint):
#        self.client = Client(endpoint)
#
#    def __enter__(self):
#        self.client.connect()
#        return self.client
#
#    def __exit__(self, exc_type, exc_val, exc_tb):
#        self.client.disconnect()
#
#
#if __name__ == '__main__':
#    with HelloClient("opc.tcp://localhost:54000/freeopcua/server/") as client:
#        root = client.get_root_node()
#        print("Root node is: ", root)
#        objects = client.get_objects_node()
#        print("Objects node is: ", objects)
#

'''
   Show 3 different examples for creating an object:
   1) create a basic object
   2) create a new object type and a instance of the new object type
   3) import a new object from xml address space and create a instance of the new object type
'''


from opcua import Client
from opcua import ua


if __name__ == "__main__":

    client = Client("opc.tcp://localhost:54000/freeopcua/server/")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()
        client.load_type_definitions()  # load definition of server specific structures/extension objects

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()
        print("Root node is: ", root)
        objects = client.get_objects_node()
        print("Objects node is: ", objects)
        # Node objects have methods to read and write node attributes as well as browse or populate address space
        print("Children of root are: ", root.get_children())

        # get a specific node knowing its node id
        var = client.get_node("ns=1;s=DCONEXAMPLE.МВ110-8АС (I-7017).Вход1")
        var.set_value(0)
        b = var.get_value()
        c = var.get_data_value()
        print(var.get_browse_name(), var.get_data_type_as_variant_type())
        print(c)
        print(b)
        print(str(c).split(':')[3].split(')')[0])
        #var.set_value(3.9)
        #var = client.get_node("ns=2;g=1be5ba38-d004-46bd-aa3a-b5b87940c698")
        #print(var)
        #var.get_data_value() # get value of node as a DataValue object
        #var.get_value() # get value of node as a python builtin
        #var.set_value(ua.Variant([23], ua.VariantType.Int64)) #set node value using explicit data type
        #var.set_value(3.9) # set node value using implicit data type
    finally:
        client.disconnect()