#! /usr/bin/env python3

import rospy
from remap_node import TakeInput

if __name__ == '__main__':
    rospy.init_node('remap_node')
    input_topic_left = '/camera/depth/image_rect_raw'
    output_topic_left = '/camera/depth_registered/image_raw'
    
    input_topic_right = '/camera/color/image_raw'
    output_topic_right = '/camera/rgb/image_raw'

    remap_left = TakeInput(input_topic_left, output_topic_left, False)
    remap_right = TakeInput(input_topic_right, output_topic_right, False)
    while not rospy.is_shutdown():
        remap_left.publish_remapped_image_data()
        remap_right.publish_remapped_image_data()