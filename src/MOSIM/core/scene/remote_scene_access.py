## SPDX-License-Identifier: MIT
## The content of this file has been developed in the context of the MOSIM research project.
## Original author(s): Jannes Lehwald, Janis Sprenger


from MOSIM.core.utils.thrift_client import ThriftClient
from MMIStandard.services import MSceneAccess

def initialize(register_ip_address):
	# Get the service descriptions from the mmu register
	client = ThriftClient(register_ip_address.Address, 9000, MSceneAccess.Client) 
	client.__enter__() ## Todo: this appears dirty and we should probably clean this up in the future. 
	return client._access
