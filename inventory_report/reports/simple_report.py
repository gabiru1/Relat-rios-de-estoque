from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products):

        oldest_manufactured = min(
            product["data_de_fabricacao"]
            for product in products
        )

        closer_to_spoiling = min(
            product["data_de_validade"]
            for product in products
        )

        biggest_company = Counter(
            product["nome_da_empresa"] for product in products
        ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufactured}\n"
            f"Data de validade mais próxima: {closer_to_spoiling}\n"
            f"Empresa com mais produtos: {biggest_company}"
        )
