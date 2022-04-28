import json
import os
from collections import defaultdict


class CheckCoco:
    """
    check coco json
    1. get each annotation count
    2. get each image count

    e.g.
        dir--
            - train/train.json
            - val/val.json
            - test/test.json

        Input: train
        result:
            image: defaultdict(<class 'set'>, {1: 2169, 2: 587, 3: 421, 4: 268, 5: 73, 6: 3845})
            All images: 7363
            Annotation: defaultdict(<class 'int'>, {1: 2842, 2: 679, 3: 645, 4: 276, 5: 82, 6: 4874})
            All annotations: 9398
    """
    def __init__(self, directory: str):
        self.directory = directory
        self.file_list = self.__get_file_list()
        self.annotation_count = defaultdict(int)
        self.image_count = defaultdict(set)

    def __get_file_list(self):
        file_list = [file for file in os.listdir(self.directory)]
        return file_list

    def get_annotation_count(self):
        """
        1. get each annotation count
        """
        for file in self.file_list:
            with open(os.path.join(self.directory, file), 'r') as f:
                data = json.load(f)
                [self.annotation_count[category["name"]] for category in data["categories"]]
                for category in data["annotations"]:
                    self.annotation_count[category["category_id"]] += 1

        print("Annotation:", self.annotation_count)
        print("All annotations:", sum(annotation for annotation in self.annotation_count.values()))
        self.annotation_count = defaultdict(int)

    def get_image_count(self):
        """
        2. get each image count
        """
        for file in self.file_list:
            with open(os.path.join(self.directory, file), 'r') as f:
                data = json.load(f)
                [self.image_count[category["name"]] for category in data["categories"]]
                for category in data["annotations"]:
                    self.image_count[category["category_id"]].add(category["image_id"])

        for key, values in self.image_count.items():
            self.image_count[key] = len(values)

        print("image:", self.image_count)
        print("All images:", sum(image for image in self.image_count.values()))
        self.image_count = defaultdict(set)


if __name__ == '__main__':
    input_data = input("Please Enter 'json' directory.\nInput: ")

    if not os.path.isdir(input_data):
        raise NotADirectoryError

    check_coco_object = CheckCoco(input_data)
    check_coco_object.get_image_count()
    check_coco_object.get_annotation_count()

