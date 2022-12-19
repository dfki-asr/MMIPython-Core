## SPDX-License-Identifier: MIT
## The content of this file has been developed in the context of the MOSIM research project.
## Original author(s): Janis Sprenger


import argparse

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer
from MMIStandard.core.ttypes import MIPAddress
import threading

from MOSIM.core.utils.thrift_client import ThriftClient
from MMIStandard.register import MMIRegisterService
from MMIStandard.core.ttypes import MServiceDescription

import time

def __get_arguments(args):
    
    #Check command arguments
    address = None
    port = None
    address_int = None
    port_int = None
    r_address = None
    r_port = None
    
    ip_address = None
    int_ip_address = None
    r_ip_address = None
    
    executable = True
    
    try:
        r_address_port = args.raddress
        r_address_port = r_address_port.split(':')
        r_address = r_address_port[0]
        r_port = int(r_address_port[1])
        r_ip_address = MIPAddress(r_address, r_port)
    except:
        pass
    if r_ip_address is None:
        executable = False
        print('Register address not defined. Adapter is not executable!')
            
    try:
        address_port = args.address
        address_port = address_port.split(':')
        address = address_port[0]
        port = int(address_port[1])
        ip_address = MIPAddress(address, port)
        int_ip_address = ip_address
    except:
        pass
    if ip_address is None:
        executable = False
        print('Network adress not defined. Adapter is not executable!')

    if(args.addressInternal != ""):
        try:
            address_port = args.addressInternal
            address_port = address_port.split(':')
            address_int = address_port[0]
            port_int = int(address_port[1])
            int_ip_address = MIPAddress(address_int, port_int)
        except:
            pass
        if ip_address is None:
            executable = False
            print('Network adress not defined. Adapter is not executable!')
    return r_ip_address, ip_address, int_ip_address, executable


class ServiceController(object):
    """starts all adapter functions"""

    def __init__(self, a_address,a_int_address, r_address, processor, serviceImplementationInstance):
        """
            The basic constructor of the controller
        
            Parameters
            ----------
            r_ip_address : MIPAddress the Register MIPAddress
            r_ip_address : MIPAddress the Adapter MIPAddress
            mmuPath: string : the path where the MMUs are loaded
            serviceClass: tuples: (json description, Class)
        """
        assert (isinstance(a_address, MIPAddress)),"aAddress is no MIPAddress"#
        assert (isinstance(a_int_address, MIPAddress)),"aAddress is no MIPAddress"
        assert (isinstance(r_address, MIPAddress)),"rAddress is no MIPAddress"

        self.processor = processor
        self.serviceImplementation = serviceImplementationInstance
        self.a_address = a_address
        self.a_int_address = a_int_address
        self.r_address = r_address

       

    def start(self):
        thread2=threading.Thread(target=self.register_adapter,args=())
        thread2.start()
        thread3=threading.Thread(target=self.start_server,args=())
        thread3.start()

        thread2.join()
        thread3.join()
       

    def register_adapter(self):
        registered = False
        while registered!=True:
            try:
                with ThriftClient(self.r_address.Address, self.r_address.Port, MMIRegisterService.Client) as client:
                        response= client._access.RegisterService(self.serviceImplementation.GetDescription())
                        registered=response.Successful
                        if registered==True:
                            print("Sucessfully registered adapter at MMIRegister")
            except Exception as x:
                print("Failed to register at MMIRegister")
                time.sleep(1)
                          
       
    def start_server(self):
        print ("Starting adapter server" + self.r_address.Address + ":" + str(self.r_address.Port))
        processor = self.processor( self.serviceImplementation )
        transport = TSocket.TServerSocket(host=self.a_int_address.Address, port=self.a_int_address.Port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TCompactProtocol.TCompactProtocolFactory()

        #server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
        server = TServer.TThreadPoolServer(processor,transport,tfactory,pfactory)
        server.setNumThreads(4)
        server.serve()

      

      




def start_service(service_class, processor):
    parser = argparse.ArgumentParser(prog="GenericService")
    parser.add_argument("-a", "--address") # the address, on which this service should be reachable
    parser.add_argument("-aint", "--addressInternal") # optional the address, on which this service should be hosted
    parser.add_argument("-r", "--raddress") # the address of the registry.

    args = parser.parse_args()
    raddress, address, addressInternal, executable = __get_arguments(args)
    if not executable:
        print('Start of Adapter is aborted')
        exit()
    if __debug__:
        print("Service started in debug mode")
        print("Address = {0}".format(address.Address))
        print("Port = {0}".format(address.Port))
        print("Internal Address = {0}".format(addressInternal.Address))
        print("Internal Port = {0}".format(addressInternal.Port))
        print("Register Address = {0}".format(raddress.Address))
        print("Register Port = {0}".format(raddress.Port))
        print("-----------------------")


    service_instance = service_class(address, raddress)
    controller = ServiceController(address, addressInternal, raddress, processor, service_instance)
    controller.start()

