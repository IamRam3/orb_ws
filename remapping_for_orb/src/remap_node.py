#! /usr/bin/env python3

import time
import rospy
from sensor_msgs.msg import Image


class TakeInput:
    def __init__(self, input_topic, output_topic, is_remap_frame:bool):
        self.input_image_data = Image()
        # self.input_topic = input_topic
        self.output_topic = output_topic
        self.is_remap_frame = is_remap_frame
        self.remapped_image_pub = rospy.Publisher(output_topic, Image, queue_size=1)
        self.subscribe_to_input_topic(input_topic)

    def subscribe_to_input_topic(self, input_topic:str)->None:
        sub = rospy.Subscriber(input_topic, Image, self.input_callback)

    def input_callback(self, image_data)->None:
        self.input_image_data = image_data
        #self.publish_remapped_image_data()

    def remap_image_data(self):
        remapped_image_msg  = self.input_image_data
        if self.is_remap_frame:
            remapped_image_msg.header.frame_id = 'cam0'
        return remapped_image_msg
    
    def publish_remapped_image_data(self):
        self.remapped_image_pub.publish(self.remap_image_data())
        print(f"publishing remap on {self.output_topic}")


if __name__ == '__main__':
    print("remap module called. Call the approriate script, not the module")