""" Python script to sort files in a directory by their extension"""
import os
from shutil import move

DIRECTORY_PATH = "."
DESTINATION_DIRECTORY = ""

for filename in os.listdir(DIRECTORY_PATH):
    if os.path.isfile(
        os.path.join(DIRECTORY_PATH, filename)
    ) and filename != os.path.basename(__file__):
        file_extension = filename.split(".")[-1]
        DESTINATION_DIRECTORY = os.path.join(DIRECTORY_PATH, file_extension)
        if not os.path.exists(DESTINATION_DIRECTORY):
            os.makedirs(DESTINATION_DIRECTORY)
        move(
            os.path.join(DIRECTORY_PATH, filename),
            os.path.join(DESTINATION_DIRECTORY, filename),
        )
