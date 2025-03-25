import dataclasses

@dataclasses.dataclass
class Testmain:

    test_dirs = []
    client_obj = []


    def create_dir(self, client_info, num_dirs):

        clients = []
        for client in client_info:
            newpaths=[]
            for path in client['mount_paths']:
                for dir in range(1,num_dirs+1):
                    newpath = path + "/" + str(dir)
                    # print(f"Executing mkdir {newpaths}")
                    newpaths.append(newpath)

            client = [{
                "hostname": client["hostname"],
                "username": client["username"],
                "password": client["password"],
                "mount_paths": newpaths
            }]
            clients.append(client)

        return clients

class Testclass1:

    def test_testclass1(self) -> None:
        print("Running test_testclass1 function inside Testclass1.")

        client_info = [{
            "hostname": "nipun1",
            "username": "root",
            "password": "root",
            "mount_paths": ["mnt/1", "mnt/2"]
            },
            {
            "hostname": "nipun2",
            "username": "root",
            "password": "root",
            "mount_paths": ["mnt/3", "mnt/4"]
            }]

        clients = Testmain().create_dir(client_info, 4)

        print(clients)

    def test_return_somethiing(self, num):
        print(f"Number is {num}")
        return num

obj = Testclass1()
obj.test_testclass1()
obj.test_return_somethiing(5)




