from xml.dom import minidom


class AnnotationsParser:

    @staticmethod
    def read(path):
        """
        Reads xml file and returns as a list of dictionaries
        :path: path to single xml file
        """
        file = minidom.parse(path)
        objects = file.getElementsByTagName('object')
        
        height = file.getElementsByTagName('height')
        width = file.getElementsByTagName('width')
        
        all_objects_in_frame = list()

        for i in objects:
            annotations = dict()
            annotations['name'] = i.getElementsByTagName('name')[0].firstChild.data
            annotations['xmin'] = i.getElementsByTagName('bndbox')[0].childNodes[1].firstChild.data
            annotations['xmax'] = i.getElementsByTagName('bndbox')[0].childNodes[3].firstChild.data
            annotations['ymin'] = i.getElementsByTagName('bndbox')[0].childNodes[5].firstChild.data
            annotations['ymax'] = i.getElementsByTagName('bndbox')[0].childNodes[7].firstChild.data
            
            annotations['height'] = height[0].firstChild.data
            annotations['width'] = width[0].firstChild.data
            
            all_objects_in_frame.append(annotations)
        return all_objects_in_frame

    @staticmethod
    def get_file_name(image_name):
        return image_name.split('.')[0].comcat("xml")


# Example run
# anns = AnnotationsParser().read("/home/s/singla/Documents/TensorFlow/workspace/training_demo/images/train/C02032-US_20181127_09495901130.xml")
# print(anns)
