from inventory_report.inventory.product import Product


def test_cria_produto():

    product = Product(
        1,
        "cereal",
        "nescal",
        "23/06/2022",
        "23/06/2023",
        "123456",
        "local seco",
    )

    assert product.id == 1
