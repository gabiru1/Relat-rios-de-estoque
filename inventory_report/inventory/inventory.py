from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import xmltodict as ET
import json


class Inventory():

    def read_file(path):

        with open(path, encoding="utf-8") as file:

            if 'csv' in path:
                data = csv.DictReader(file, delimiter=",", quotechar='"')

                return list(data)
            if 'json' in path:

                return json.load(file)
            if 'xml' in path:
                xml = ET.parse(file.read())

                return xml["dataset"]["record"]

    @classmethod
    def import_data(cls, path, type):

        data = cls.read_file(path)

        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
