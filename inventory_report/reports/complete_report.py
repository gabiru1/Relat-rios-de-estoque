from collections import Counter


class CompleteReport:

    def gen(products):
        company_names = list()
        manufacture_dates = list()
        expiration_dates = list()

        for product in products:

            company_names.append(product["nome_da_empresa"])
            manufacture_dates.append(product["data_de_fabricacao"])
            expiration_dates.append(product["data_de_validade"])

        oldest_manufactured = min(manufacture_dates)
        closer_to_spoiling = min(expiration_dates)
        companies = Counter(company_names)
        biggest_company = companies.most_common(1)[0][0]

        companies = ""

        for company in companies.items():

            companies += f"- {company[0]}: {company[1]}\n"

        return (
            f"Data de fabricação mais antiga: {oldest_manufactured}\n"
            f"Data de validade mais próxima: {closer_to_spoiling}\n"
            f"Empresa com mais produtos: {biggest_company}\n"
            f"Produtos estocados por empresa:\n"
            f"{companies}"
        )
