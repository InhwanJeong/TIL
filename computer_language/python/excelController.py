import os
from openpyxl import load_workbook
from tempfile import NamedTemporaryFile
from openpyxl.drawing.image import Image
from django.conf import settings
import requests
import PIL


class ExcelController:
    def __init__(self):
        filename = os.path.join(settings.BASE_DIR, 'resources', 'template.xlsx')

        self.work_book = load_workbook(filename)
        self.work_sheet = self.work_book['Sheet1']

        self.logo_img = Image(os.path.join(settings.BASE_DIR, 'resources', 'logo.png'))
        self.logo_img.width = 122.456692913544
        self.logo_img.height = 38.503937007916

        self.work_sheet.add_image(self.logo_img, 'AF44')

        self.before_image_cell = "W10"
        self.after_image_cell = "AH10"

        self.base_url = "https://kr.object.gov-ncloudstorage.com/"

    def __set_excel_image(self, url: str, cell: str):
        image = PIL.Image.open(requests.get(url, stream=True).raw)

        with NamedTemporaryFile(delete=False) as tmp:
            image.save(tmp, image.format)
            tmp.seek(0)
            sheet_image = Image(tmp.name)

            sheet_image.width = 322.393700787818
            sheet_image.height = 202.20472440971

            self.work_sheet.add_image(sheet_image, cell)

    def set_excel_stream(self, data: list):
        before_url = self.base_url + str(data["befor_photo_path"])
        after_url = self.base_url + str(data["photo_path"])
        self.__set_excel_image(before_url, self.before_image_cell)
        self.__set_excel_image(after_url, self.after_image_cell)

        sheet_id = str(data["construction_done_id"])
        create_time = str(data["createtime"]).split(' ')[0]
        object_name = str(data["object_name"])
        address = str(data["address"])
        category = "차도" if data["construction_div"] else "인도"
        coverage = str(data["damage_area_ratio"])
        vibration = str(data["vib"])
        request_description = str(data["details"])
        complete_description = str(data["done_details"])

        self.work_sheet["AC5"] = ' NO. ' + sheet_id
        self.work_sheet["AC6"] = ' ' + create_time
        self.work_sheet["AD21"] = ' ' + object_name
        self.work_sheet["AD23"] = ' ' + address
        self.work_sheet["AD25"] = ' ' + category
        self.work_sheet["AD27"] = ' ' + coverage + '%'
        self.work_sheet["AD29"] = ' ' + vibration
        self.work_sheet["AD31"] = ' ' + request_description
        self.work_sheet["W35"] = ' ' + complete_description

    def get_excel_stream(self):
        with NamedTemporaryFile(delete=False) as tmp:
            self.work_book.save(tmp.name)
            tmp.seek(0)
            stream = tmp.read()
            return stream
