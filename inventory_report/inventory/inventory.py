from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory():

    def read_file(path):

        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')

            return list(data)

    @classmethod
    def import_data(cls, path, type):

        data = cls.read_file(path)

        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
