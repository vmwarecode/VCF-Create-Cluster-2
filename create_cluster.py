#Create Cluster
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint


class CreateCluster:
    def __init__(self):
        print('Create Clusterr')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]

    def create_cluster(self):
        data = self.utils.read_input(os.path.abspath(__file__ +'/../')+'/create_cluster_spec.json')
        validations_url =  'https://'+self.hostname+'/v1/clusters/validations/creations'
        print ('Validating the input....')
        response = self.utils.post_request(data,validations_url)
        if(response['resultStatus'] != 'SUCCEEDED'):
            print ('Validation Failed.')
            exit(1)
        create_cluster_url = 'https://'+ self.hostname + '/v1/clusters'
        response = self.utils.post_request(data,create_cluster_url)
        print ('Creating Cluster...')
        task_url = 'https://'+self.hostname+'/v1/tasks/' + response['id']
        print('Create cluster eneded with status: ' + self.utils.poll_on_id(task_url,True))

if __name__== "__main__":
    CreateCluster().create_cluster()

