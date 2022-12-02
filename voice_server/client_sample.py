#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from srvmsgs.srv import SpeechToText
#from srvmsgs.srv import TTS
from rclpy.node import Node

class MyClient(Node):
    def __init__(self):
        super().__init__("my_client")
        self.cli = self.create_client(SpeechToText,"stt_server")
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.req = SpeechToText.Request()

    def send_request(self):
        self.req.short_str = True
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()

def main(args=None):
    rclpy.init(args=args)
    client = MyClient()
    response = client.send_request()
    client.get_logger().info(response.result_str)
    client.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

