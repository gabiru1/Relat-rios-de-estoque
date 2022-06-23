from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    @staticmethod
    def generate(products):

        company_tuple_products = Counter(
            product["nome_da_empresa"] for product in products
        ).most_common()

        company_products_string = "".join(
            f"- {company}: {amount}\n"
            for company, amount in company_tuple_products
        )

        return (
            SimpleReport.generate(products)
            + "\nProdutos estocados por empresa:\n"
            + company_products_string
        )
