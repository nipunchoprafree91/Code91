from collections import OrderedDict

original_dict = {"best": 5, "is": 2, "of": 9}

for key, val in original_dict.items():
    print(key, val)

# Dict domprehensions
original_dict = {"best": 5, "is": 2, "of": 9}

new_dict = {key: value for key, value in original_dict.
            items() if value % 2 == 0}
print(new_dict)

pairs = [('a', 1), ('b', 2), ('c', 3)]
new_dict2 = {key: value for key,
             value in pairs if value % 2 == 0}
print(new_dict2)

clientdict = {
    "client_config" : {

        "multiple_subnets" : [
            {
                "prefix": "172.0.0",
                "start": "1",
                "end": "10"
                },
            {
                "prefix": "172.0.0",
                "start": "1",
                "end": "10"
                },
            {
                "prefix": "172.0.0",
                "start": "1",
                "end": "10"
            }
        ]
    }
}

if len(clientdict["client_config"]["multiple_subnets"]) == 0:
    print("Length is Zero")
else:
    print("lenght of siubnets is: ",len(clientdict["client_config"]["multiple_subnets"]))
    print("IO Client subnets to be used are: ", clientdict["client_config"]["multiple_subnets"])

subnetlist = clientdict["client_config"]["multiple_subnets"]

for subnets in subnetlist:
    print(subnets)


