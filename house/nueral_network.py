#coding=utf-8
import tensorflow as tf
import os
import math
import numpy as np
filename_queue = tf.train.string_input_producer(["/home/zzq/kaggle/house/feartures/data_demo.csv",
 "/home/zzq/kaggle/house/feartures/demo_label.csv"])
reader = tf.TextLineReader()
key, value = reader.read(filename_queue)
print key
print value

# col= tf.decode_csv(value, record_defaults=[ ['int32']*6], field_delim=',', name=None) 
# print type(col)
record_defaults = [[1], [1], [1], [1], [1]]
record_defaults = [[1.0], [1.0], [1.0], [1.0], [1.0],[1.0], [1.0], [1.0], [1.0], [1.0],[1.0], [1.0], [1.0], [1.0], [1.0],
[1.0], [1.0], [1.0], [1.0], [1.0],[1.0], [1.0], [1.0], [1.0], [1.0],[1.0], [1.0], [1.0]]
# record_defaults =[['int32']*5]
col1,col2, col3, col4, col5 ,col6,col7,col8,col9,col10,col11, col12, col13, col14, col15 ,col16,col17,col18,col19,col20,col21, col22, col23, col24, col25 ,col26,col27,col28= tf.decode_csv(
    value, record_defaults=record_defaults)
# features = tf.concat(0, [col1, col2, col3, col4])
# print features
print col1
print col7
