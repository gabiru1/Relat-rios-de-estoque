from inventory_report.inventory.product import Product


def test_relatorio_produto():

    expect = Product(
        1,
        "Cereal",
        "Nescal",
        "23/06/2022",
        "23/12/2022",
        "CE-9E45",
        "local seco",
    )

    assert expect.__repr__() == (
            f"O produto {expect.nome_do_produto}"
            f" fabricado em {expect.data_de_fabricacao}"
            f" por {expect.nome_da_empresa} com validade"
            f" até {expect.data_de_validade}"
            f" precisa ser armazenado {expect.instrucoes_de_armazenamento}."
        )
