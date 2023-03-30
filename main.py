from LoadBalancers import LoadBalancers 
import json

class LoadBalancersInfo:

     def __init__(self):
        self.Address = ""
        self.LoadBalancerId = ""
        self.LoadBalancerName = ""
        self.region_id = ""
        self.LoadBalancerStatus = ""
        self.ServerIds=[]
        self.Port = ""
        self.Protocal = ""
        self.ServerPort= ""
        self.ServerProtocal = ""


access_key_id = ''
access_key_secret = ''
region_id = 'cn-hangzhou'

myLoadBalancers = LoadBalancers()
myLoadBalancers.create_client(access_key_id,access_key_secret)
tempString1 = myLoadBalancers.findByRegion(access_key_id,access_key_secret,region_id)
tempString1 = json.loads(tempString1)
mylbs=tempString1['body']['LoadBalancers']['LoadBalancer']
mylbInfos = []
#根据RegionId查询已创建的负载均衡实例，解析json
for lb in mylbs:
    mylbInfo = LoadBalancersInfo()
    mylbInfo.Address = lb['Address']
    mylbInfo.LoadBalancerId = lb['LoadBalancerId']
    mylbInfo.LoadBalancerName = lb['LoadBalancerName']
    mylbInfo.region_id = region_id
    mylbInfo.LoadBalancerStatus = lb['LoadBalancerStatus']
    #根据RegionId查询指定负载均衡实例的详细信息
    tempString2= myLoadBalancers.findByIBid(access_key_id,access_key_secret,region_id,mylbInfo.LoadBalancerId)
    tempString2 = json.loads(tempString2)
    myServerIds = tempString2['body']['BackendServers']['BackendServer']
    for id in myServerIds:
        serverId = id['ServerId']
        mylbInfo.ServerIds.append(serverId)
    myPortProtocal = tempString2['body']['ListenerPortsAndProtocal']['ListenerPortAndProtocal']
    for j in myPortProtocal:
        mylbInfo.Port = j['ListenerPort']
        mylbInfo.Protocal = j['ListenerProtocal']
        #根据Protocal，lbid查询负载均衡后端服务器的端口
        if(mylbInfo.Protocal=='tcp'):
            tempString3= myLoadBalancers.findServerPort(
                 access_key_id,
                access_key_secret,
                region_id,
                load_balancer_id= mylbInfo.LoadBalancerId,
                listener_protocol=mylbInfo.Protocal)
            tempString3 = json.loads(tempString3)
            temp =tempString3['body']['Listeners']
            for j in temp:
                mylbInfo.ServerPort = j['BackendServerPort']
                mylbInfo.ServerProtocal = 'tcp'

    mylbInfos.append(mylbInfo)

print(mylbInfos[0].Address,
      mylbInfos[0].LoadBalancerId,
      mylbInfos[0].LoadBalancerName,
      mylbInfos[0].region_id,
      mylbInfos[0].LoadBalancerStatus,
      mylbInfos[0].ServerIds,
      mylbInfos[0].Port,
      mylbInfos[0].Protocal,
      mylbInfos[0].ServerPort,
      mylbInfos[0].ServerProtocal
      )
print(mylbInfos[1].Address,
      mylbInfos[1].LoadBalancerId,
      mylbInfos[1].LoadBalancerName,
      mylbInfos[1].region_id,
      mylbInfos[1].LoadBalancerStatus,
      mylbInfos[1].ServerIds,
      mylbInfos[1].Port,
      mylbInfos[1].Protocal,
      mylbInfos[1].ServerPort,
      mylbInfos[1].ServerProtocal
      )
