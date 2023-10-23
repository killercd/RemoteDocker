import xmlrpc.server
import fire
from subprocess import Popen, PIPE
import docker

class DockerServer:

    def docker_list(self):
        client = docker.from_env()
        container_list = client.containers.list()
        docker_list = []
         
        
        for container in container_list:
            docker_obj = {"id": container.id,
                          "name": container.name,
                          "image": container.image.id,
                          "status": container.status
                          
                          }
            docker_list.append(docker_obj)

        return docker_list



        
        



def start(interface, port):

    server = xmlrpc.server.SimpleXMLRPCServer((interface, port))
    server.register_instance(DockerServer())
    server.serve_forever()



if __name__ == '__main__':
    fire.Fire({
        'start': start,
    })
