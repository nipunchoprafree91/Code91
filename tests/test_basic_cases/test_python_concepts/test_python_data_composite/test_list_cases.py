clustervms = ["1.1.1.1","1.1.1.2","1.1.1.3"]
evsconfig  = [
    {
        "name": "evs1",
        "networkInfo" : [
            {
                "IP": "1.1.1.1",
                "nodeId": "1"
            },
            {
                "IP": "1.1.1.2",
                "nodeId": "2"
            },
            {
                "IP": "1.1.1.3",
                "nodeId": "3"
            }
        ]
    }
]
passthru = ["A"]


for vm in clustervms:
    for evs, psss in zip(evsconfig, passthru):
        cifs_name = evs["name"] + vm.split(".")[-1]
        print(f"Create cifs name {cifs_name} command for vm {vm}")


list1 = [1,2,3]
list1.append(4)
list1.extend([5])

print(list1)