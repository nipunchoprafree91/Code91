
def test_dict():
    mylistdict1 = ({
    "client" : "172.27.149.53",

    "username": "root",
    "password": 'root',
    "mount_paths": ["/mnt/1", "/mnt/2"],
    "fileshares_mounted" : True
    },
    {
    "client" : "172.27.149.53",
    "username": "root",
    "password": 'root',
    "mount_paths": ["/mnt/1", "/mnt/2"],
    "fileshares_mounted" : True
    })

    # Contruct mydict2 such that client key is relaced by hostname takes value of
    # corresponding client keys from mydict1  and all values of mount_dir are in test_dir
    # of mylistdict2 for coreesponding keys and remove key fileshares_mounted

    mydict2 = []
    for item in mylistdict1:
        new_item = {
            "hostname": item["client"],
            "username": item["username"],
            "password": item["password"],
            "test_dir": item["mount_paths"],
        }

    # Accessing nested dictionary
    for item in mydict2:
        print(item["hostname"])
        print(item["username"])
        print(item["password"])
        print(item["test_dir"])


    # Printing the keys of a dictionary
    for item in mydict2:
        print(item.keys())

    mylistdict2 = [
               {
                "a": 1,
                "b": 1,
                "c": [8, 9]
               },
               {
                "a": 1,
                "b": 1,
               }
            ]

    for i in mylistdict2:
        if "c" in i:
            print(i["c"])
        else:
            print(f"Key not found at index {mylistdict2.index(i)}")

dict2 = {
    "share1": "Z",
    "share2": "Y"
}

for share  in dict2.keys():
    print(share,dict2[share])

dict_evs = {
    "passthruone": {
        "type": "passthru",
        "label": "passthruone",
        "virtualServerId": "1",
    },
    "passthrutwo": {
        "type": "passthru",
        "label": "passthruone",
        "virtualServerId": "1",
    },
    "passthruthree": {
        "type": "passthru",
        "label": "passthruone",
        "virtualServerId": "1",
    },

}

for passthru in dict_evs:
    print(passthru)

test_dict()

users = [
               {
                "username": 1,
                "password": 1
               },
             {
                "username": 1,
                "password": 1
               }
            ]

for user in users:
    print(user["username"])

users = {
        "user1": {
            "username": "nipunuser1",
            "password": "password"
            },
        "user2":{
            "username": "nipunuser2",
            "password": "password"
            }
        }

print(users["user1"]["username"])
print(users["user2"]["username"])

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)

