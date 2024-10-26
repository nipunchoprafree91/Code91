import json


def test_basic_loops():
    # output expected is
    for i in range(2):
        for j in range(i+1,4):
            for k in range(j,4):
                print("j: ", j, "k: ",k)

def test_dict_loops():
    test_dir= []

    mylist1 = [
        {
            "hostname": "172.16.27.105",
            "username": "root",
            "password": "root",
            "mount_paths": ["/mnt/1_1", "/mnt/1_2"]
        },
        {
            "hostname": "172.16.27.106",
            "username": "root",
            "password": "root",
            "mount_paths": ["/mnt/2_1", "/mnt/2_2"]
        }
    ]

    """
    change this code so that expected output is
    mylist1 = [
        {
            "hostname": "172.16.27.105",
            "username": "root",
            "password": "root",
            "mount_paths": ["/mnt/1_1/dir1", "/mnt/1_2/dir2", "/mnt/1_1/dir3", "/mnt/1_2/dir4"]
        },
        {
            "hostname": "172.16.27.106",
            "username": "root",
            "password": "root",
            "mount_paths": ["/mnt/2_1/dir1", "/mnt/2_2/dir2", "/mnt/2_1/dir3", "/mnt/2_2/dir4"]
        }
    ]
    """

    for client in mylist1:
        newpaths=[]
        for path in client['mount_paths']:

            for dir in range(1,3):
                newpath = path + "/" + str(dir)
                newpaths.append(newpath)
        newclient = [
            {
                "hostname": client["hostname"],
                "username": client["username"],
                "password": client["password"],
                "mount_paths": newpaths
            }
        ]
        test_dir.append(newclient)


    print(json.dumps(test_dir, indent=4))


test_dict_loops()