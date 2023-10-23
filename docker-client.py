import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://192.168.178.51:8000")
docker_list = server.docker_list()

for docker in docker_list:
    print("ID:{} NAME: {} STATUS: {}".format(docker["id"], docker["name"], docker["status"]))