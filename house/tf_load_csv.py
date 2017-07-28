def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def _floats_feature(value):
  return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))


def convert_to_record(name, image, label, map):
    """Create a data record."""


    filename = os.path.join(params.TRAINING_RECORDS_DATA_DIR, name + '.' + params.DATA_EXT)
    print('Writing', filename)

    writer = tf.python_io.TFRecordWriter(filename)

    image_raw = image.tostring()
    map_raw = map.tostring()
    label_raw = label.tostring()

    example = tf.train.Example(features=tf.train.Features(feature={

        'image_raw': _bytes_feature(image_raw),
        'map_raw': _bytes_feature(map_raw),
        'label_raw': _bytes_feature(label_raw)

        }))        
    writer.write(example.SerializeToString())
    writer.close()
