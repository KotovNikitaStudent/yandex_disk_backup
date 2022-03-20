import os

import yadisk
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TOKEN")
NAME_FOLDER = "/научная_стипендия_2022"


class DiskData:
    def __init__(self, token=""):
        self.__token = token
        self.__yandex_object = yadisk.YaDisk(token=self.__token)
        self.__all_link = []

    def get_list_files(self, root="/"):
        self.__walk(root)
        return self.__all_link

    def __walk(self, top):
        for lnk in self.__yandex_object.listdir(top):
            if lnk["file"] is None:
                self.__walk(lnk['path'].split(":")[-1])
            else:
                self.__all_link.append(lnk['path'].split(':')[-1])


if __name__ == '__main__':
    d = DiskData(TOKEN)
    list_folders = d.get_list_files(NAME_FOLDER)
    print(list_folders)

    y = yadisk.YaDisk(token=TOKEN)
    print(list(y.listdir("/научная_стипендия_2022/Котов Н.В./Награды с конференций/5.2.1")))
