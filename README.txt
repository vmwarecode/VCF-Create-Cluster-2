INTRODUCTION
------------:

This module contains script files to create a cluster.
After you add the primary cluster, you can add more clusters to expand the domain.


REQUIREMENTS:
------------

This module requires the following modules:

 * Python 3
   Libraries
 	* requests
 	* sys
 	* json
 	* time

 * The scripts must be run outside sddc-manager environment.

 * DNS resolution must be done for sddc-manager.



PREREQUSITES:
--------------

The following data is required

ID of the domain in which the cluster is to be created

Cluster details

	->Name of the cluster

Hosts details

	->ID of the host (UUID)

	->License key for the host

	->List of VDS names to associate with host

	->ID of the vmNic host to be associated with VDS, once added to cluster

Datastore details

NOTE:
Only one of "vsanDatastoreSpec" (For VSAN) or NFS "nfsDatastoreSpecs" (For NFS) must be specified.

For VSAN

	->Number of host failures to tolerate (can be 0, 1, or 2)

	->License key for the vSAN datastore

	->Unresolved directive in usecases/create_cluster.adoc - include::../vimanager/create-domain-v1-subsections/request-body-vSANDatastoreSpec.adoc[]

For NFS

	->List of NFS server names

	->Shared directory path

	->User tag used to annotate NFS share

	->Boolean to identify if the mount directory should be read-only

	{
	"nfsDatastoreSpecs" : [{
	"nasVolume" : {
		"serverName" : [ "10.0.0.250" ],
		"path" : "/nfs_mount/my_read_write_folder",
		"readOnly" : false
		},
		"datastoreName" : "NFSShare"
	}]
	}

Network Details

	->List of VDS details

	->For each VDS

	->Port group names and the corresponding transport type. Note that EDGE_INFRA_OVERLAY_UPLINK, VREALIZE should not be specified in the input spec.

	->DVS host Infrastructure traffic resource type

	->Maximum allowed usage for a traffic class

	->Amount of bandwidth to be reserved for the host infrastructure traffic class

NSX cluster Details

NOTE:
Only one of "nsxVClusterSpec" (For NSX-V) or "nsxTClusterSpec" (For NSX-T) must be specified.

For NSX-V

	->VLAN ID of the VXLAN

	->License key for NSX

VDS to be used for VXLAN traffic/port group. This should belong to one of the VDS being created for the cluster

{
  "nsxVClusterSpec" : {
    "vlanId" : 3,
    "vdsNameForVxlanConfig" : "SDDC-Dswitch-Private1"
  }
}
For NSX-T

VLAN ID of Geneve

{
  "nsxTClusterSpec" : {
    "geneveVlanId" : 2
  }
}
Network pool must be configured.

Logical VMware Cloud Foundation container (Workload Domain) must be provisioned.

NOTE
NSX manager and controller is configured when domain is created.
Prerequisites for vSAN/ NFS must be met.

License key details may be provisioned in vCenter.

Host configuration must have minimum two active vmNics.

There must be at least three hosts available in the VMware Cloud Foundation inventory.

Ensure that the hosts you want to add to the cluster are in UNASSIGNED_USEABLE state.

You must have valid host and vSAN (if using vSAN storage) license key specified with adequate sockets available for the host to be added.

A DHCP server must be configured on the VXLAN VLAN of the management domain. When NSX creates VXLAN VTEPs for the domain, they are assigned IP addresses from the DHCP server.


USAGE:
-----

Sample specification file "create_cluster_spec.json" will be used for creating cluster operation. So fill the required details and validate before executing the script.
For more information on the provided sample file, please refer to API reference documentation.

Usage:	python create_cluster.py <hostname> <username> <password>

