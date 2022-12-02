#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from srvmsgs.srv import TTS
#from srvmsgs.srv import TTS
from rclpy.node import Node

class MyClient(Node):
    def __init__(self):
        super().__init__("my_client")
        self.cli = self.create_client(TTS,"tts")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = TTS.Request()

    def send_request(self):
        self.req.data = "hello world"
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    client = MyClient()
    response = client.send_request()
    res = str(response.result)
    client.get_logger().info(res)
    client.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

