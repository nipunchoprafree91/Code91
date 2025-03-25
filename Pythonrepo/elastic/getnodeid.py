import requests
import json

response1 = requests.get('http://10.2.46.238:9200/_nodes')
nodes_data1 = response1.json()['nodes']
node_ids1 = list(nodes_data1.keys())

response2 = requests.get('http://10.2.46.231:9200/_nodes')
nodes_data2 = response2.json()['nodes']
node_ids2 = list(nodes_data2.keys())

response3 = requests.get('http://10.2.41.147:9200/_nodes')
nodes_data3 = response3.json()['nodes']
node_ids3 = list(nodes_data3.keys())

response1 = requests.get('http://10.2.46.238:9200/_cluster/state')
nodes_data1 = response1.json()

response2 = requests.get('http://10.2.46.231:9200/_cluster/state')
nodes_data2 = response2.json()

response3 = requests.get('http://10.2.41.147:9200/_cluster/state')
nodes_data3 = response3.json()

response1 = requests.get('http://10.2.46.238:9200/_cluster/health?pretty')
nodes_data4 = response1.json()

response2 = requests.get('http://10.2.46.231:9200/_cluster/health?pretty')
nodes_data5 = response2.json()

response3 = requests.get('http://10.2.41.147:9200/_cluster/health?pretty')
nodes_data6 = response3.json()



print(node_ids1)
print(node_ids2)
print(node_ids3)

print(nodes_data1)
print(nodes_data2)
print(nodes_data3)

print(nodes_data4)
print(nodes_data5)
print(nodes_data6)
