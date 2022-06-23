from inventory_report.inventory.product import Product


def test_cria_produto():

    product = Product(
        1,
        "cereal",
        "nescal",
        "23/06/2022",
        "23/12/2022",
        "123456",
        "local seco",
    )

    assert product.id == 1
    assert product.nome_do_produto == 'cereal'
    assert product.nome_da_empresa == 'nescal'
    assert product.data_de_fabricacao == '23/06/2022'
    assert product.data_de_validade == '23/12/2022'
    assert product.numero_de_serie == '123456'
    assert product.instrucoes_de_armazenamento == 'local seco'
