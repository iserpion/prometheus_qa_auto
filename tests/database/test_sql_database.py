import pytest


# Required part of project:

@pytest.mark.sql_db
def test_database_connection(sql_db):
    """Test checks database connection"""

    sql_db.test_connection()
    connection_output_contains = (
        "Connected successfully. SQLite Database Version is:"
    )

    # check connection output
    assert connection_output_contains in sql_db.connection_output


@pytest.mark.sql_db
def test_check_all_users(sql_db):
    """Test checks retrieving all users"""

    users = sql_db.get_all_users()

    # check that select users query result is not empty
    assert len(users) > 0


@pytest.mark.sql_db
def test_check_user_sergii(sql_db):
    """Test checks retrieving address of specific user"""

    user = sql_db.get_user_address_by_name("Sergii")

    # check that user address is valid
    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.sql_db
def test_product_qnt_update(sql_db):
    """Test checks updating product qty by id"""

    sql_db.update_product_qnt_by_id(1, 25)
    water_qnt = sql_db.select_product_qnt_by_id(1)

    # check that product qty is updated
    assert water_qnt[0][0] == 25


@pytest.mark.sql_db
def test_product_insert_replace(sql_db):
    """Test checks product inserting/replacing"""

    sql_db.insert_or_replace_product(4, "печиво", "солодке", 30)
    cookies_qnt = sql_db.select_product_qnt_by_id(4)

    # check that product is inserted
    assert cookies_qnt[0][0] == 30


@pytest.mark.sql_db
def test_product_delete(sql_db):
    """Test checks product deleting"""

    sql_db.insert_or_replace_product(99, "тестові", "дані", 999)
    sql_db.delete_product_by_id(99)
    qnt = sql_db.select_product_qnt_by_id(99)

    # check that product is deleted
    assert len(qnt) == 0


@pytest.mark.sql_db
def test_detailed_orders(sql_db):
    """Test checks order details by user"""

    orders = sql_db.get_detailed_orders()
    
    # Step 1: Check quantity of orders is equal to 1
    assert len(orders) == 1

    # Step 2: Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# Individual part of project:

@pytest.mark.sql_db
@pytest.mark.parametrize(
    "id, name, description, quantity",
    [
        (5, "meat", "chicken", 9), 
        (6, "beer", "lager", 24), 
        (7, "juice", "banana", 14)
    ],
)
def test_insert_products_multiple_times(sql_db, id, name, description, quantity):
    """Test that inserts data into products table multiple times"""

    sql_db.insert_or_replace_product(id, name, description, quantity)
    qnt = sql_db.select_product_qnt_by_id(id)

    # check that data inserted
    assert qnt[0][0] == quantity

    
@pytest.mark.sql_db
def test_insert_duplicated_key(sql_db):
    """
    Test verifies that it's not possible to insert data
    with a duplicated primary key to products table
    """

    sql_db.insert_product(4, "cookie", "sweet", 30)
    product_count = sql_db.select_count_product_by_id(4)

    # check that product is not duplicated
    assert product_count[0][0] == 1


@pytest.mark.sql_db
def test_create_table_and_manipulate_with_it(sql_db):
    """
    Test verifies that a table can be created,
    some data can be stored/read to/from it and table can be dropped from DB
    """

    sql_db.create_table_order_details()
    table_names = sql_db.select_name_from_sqlite_schema()

    # Step 1: check that table is created
    assert table_names[3][0] == "order_details"

    sql_db.insert_order_details(1, 1, 5)
    order_detail = sql_db.select_order_details()

    # Step 2: check structure of data
    assert order_detail[0][0] == 1
    assert order_detail[0][1] == 1
    assert order_detail[0][2] == 5

    sql_db.drop_order_details_table()
    table_names = sql_db.select_name_from_sqlite_schema()

    # Step 3: check that table is deleted
    assert len(table_names) == 3


@pytest.mark.sql_db
def test_min_product_qty(sql_db):
    """Test checks minimum quantity of products"""

    minimum_qty = sql_db.select_min_product_qty()

    # check that minimum quantity is valid
    assert minimum_qty[0][0] == 9


@pytest.mark.sql_db
def test_max_product_qty(sql_db):
    """Test checks maximum quantity of products"""

    maximum_qty = sql_db.select_max_product_qty()

    # check that maximum quantity is valid
    assert maximum_qty[0][0] == 30


@pytest.mark.sql_db
def test_avg_product_qty(sql_db):
    """Test checks average quantity of products"""

    average_qty = sql_db.select_avg_product_qty()

    # check that average quantity is valid
    assert average_qty[0][0] == 17


@pytest.mark.sql_db
def test_max_product_description(sql_db):
    """Test checks product description with maximum length"""

    max_desc = sql_db.select_product_with_max_description()

    # check that product description with maximum length is valid
    assert max_desc[0][0] == "натуральне незбиране"


@pytest.mark.sql_db
def test_max_city_count_in_customers(sql_db):
    """Test checks which city most appears in customers table"""

    max_city = sql_db.select_customers_city_max_count()

    # check the city is valid
    assert max_city[0][0] == "Odesa"


@pytest.mark.sql_db
def test_best_selling_product(insert_delete_orders):
    """Test checks the best selling product"""

    bestseller = insert_delete_orders.select_bestseller()

    # check that bestseller product is valid
    assert bestseller[0][0] == "beer"
