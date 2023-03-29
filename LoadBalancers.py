# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import sys

from typing import List

from alibabacloud_slb20140515.client import Client as Slb20140515Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_slb20140515 import models as slb_20140515_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


class LoadBalancers:

    def __init__(self):
        self.access_key_id = ""
        self.access_key_secret = ""
        self.region_id = ""

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Slb20140515Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 必填，您的 AccessKey ID,
            access_key_id=access_key_id,
            # 必填，您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'slb.aliyuncs.com'
        return Slb20140515Client(config)

    #根据RegionId查询已创建的负载均衡实例
    @staticmethod
    def findByRegion(
        access_key_id: str,
        access_key_secret: str,
        region_id:str,
    ) -> None:
        # 初始化 Client，采用 AK&SK 鉴权访问的方式，此方式可能会存在泄漏风险，建议使用 STS 方式。更多鉴权访问方式请参考：https://help.aliyun.com/document_detail/378659.html
        client = LoadBalancers.create_client(access_key_id, access_key_secret)
        describe_load_balancers_request = slb_20140515_models.DescribeLoadBalancersRequest(
            region_id=region_id
        )
        runtime = util_models.RuntimeOptions()
        resp = client.describe_load_balancers_with_options(describe_load_balancers_request, runtime)
        return UtilClient.to_jsonstring(resp) 

    #根据RegionId查询指定负载均衡实例的详细信息
    @staticmethod
    def findByIBid(
        access_key_id: str,
        access_key_secret: str,
        region_id:str,
        load_balancer_id:str,
    ) -> None:
        # 初始化 Client，采用 AK&SK 鉴权访问的方式，此方式可能会存在泄漏风险，建议使用 STS 方式。鉴权访问方式请参考：https://help.aliyun.com/document_detail/378659.html
        # 获取 AK 链接：https://usercenter.console.aliyun.com
        client = LoadBalancers.create_client(access_key_id, access_key_secret)
        describe_load_balancer_attribute_request = slb_20140515_models.DescribeLoadBalancerAttributeRequest(
            region_id= region_id ,
            load_balancer_id = load_balancer_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            resp = client.describe_load_balancer_attribute_with_options(describe_load_balancer_attribute_request, runtime)
            data = UtilClient.to_jsonstring(resp) 
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)
            data = ''
        return data

    @staticmethod
    def findServerPort(
        access_key_id: str,
        access_key_secret: str,
        region_id:str,
        load_balancer_id:str,
        listener_protocol:str,
    ) -> None:
        # 初始化 Client，采用 AK&SK 鉴权访问的方式，此方式可能会存在泄漏风险，建议使用 STS 方式。鉴权访问方式请参考：https://help.aliyun.com/document_detail/378659.html
        # 获取 AK 链接：https://usercenter.console.aliyun.com
        client = LoadBalancers.create_client(access_key_id, access_key_secret)
        describe_load_balancer_listeners_request = slb_20140515_models.DescribeLoadBalancerListenersRequest(
            region_id = region_id,
            listener_protocol= listener_protocol,
            load_balancer_id= load_balancer_id
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            resp = client.describe_load_balancer_listeners_with_options(describe_load_balancer_listeners_request, runtime)
            data = UtilClient.to_jsonstring(resp) 
        except Exception as error:
            # 如有需要，请打印 error
            UtilClient.assert_as_string(error.message)
            data = ''
        return data