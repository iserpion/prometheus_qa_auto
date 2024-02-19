import pytest


# Required part of project:

@pytest.mark.database
def test_database_connection(db):
    """Test checks database connection"""

    db.test_connection()
    expected_output = "Connected successfully. SQLite Database Version is:"

    # check connection output
    assert expected_output in db.connection_output


@pytest.mark.database
def test_check_all_users(db):
    """Test checks retrieving all users"""

    users = db.get_all_users()

    # check that select users query result is not empty
    assert len(users) > 0


@pytest.mark.database
def test_check_user_sergii(db):
    """Test checks retrieving address of specific user"""

    user = db.get_user_address_by_name("Sergii")

    # check that user address is valid
    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(db):
    """Test checks updating product qty by id"""

    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    # check that product qty is updated
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert_replace(db):
    """Test checks product inserting/replacing"""

    db.insert_or_replace_product(4, "печиво", "солодке", 30)
    cookies_qnt = db.select_product_qnt_by_id(4)

    # check that product is inserted
    assert cookies_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(db):
    """Test checks product deleting"""

    db.insert_or_replace_product(99, "тестові", "дані", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    # check that product is deleted
    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(db):
    """Test checks order details by user"""

    orders = db.get_detailed_orders()
    
    # Step 1: Check quantity of orders is equal to 1
    assert len(orders) == 1

    # Step 2: Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"


# Individual part of project:

@pytest.mark.database
@pytest.mark.parametrize(
    "id, name, description, quantity",
    [
        (5, "meat", "chicken", 9), 
        (6, "beer", "lager", 24), 
        (7, "juice", "banana", 14)
    ],
)
def test_insert_products_multiple_times(db, id, name, description, quantity):
    """Test that inserts data into products table multiple times"""

    db.insert_or_replace_product(id, name, description, quantity)
    qnt = db.select_product_qnt_by_id(id)

    # check that data inserted
    assert qnt[0][0] == quantity

    
@pytest.mark.database
def test_insert_duplicated_key(db):
    """
    Test verifies that it's not possible to insert data
    with a duplicated primary key to products table
    """

    db.insert_product(4, "cookie", "sweet", 30)
    product_count = db.select_count_product_by_id(4)

    # check that product is not duplicated
    assert product_count[0][0] == 1


@pytest.mark.database
def test_create_table_and_manipulate_with_it(db):
    """
    Test verifies that a table can be created,
    some data can be stored/read to/from it and table can be dropped from DB
    """

    db.create_table_order_details()
    table_names = db.select_name_from_sqlite_schema()

    # Step 1: check that table is created
    assert table_names[3][0] == "order_details"

    db.insert_order_details(1, 1, 5)
    order_detail = db.select_order_details()

    # Step 2: check structure of data
    assert order_detail[0][0] == 1
    assert order_detail[0][1] == 1
    assert order_detail[0][2] == 5

    db.drop_order_details_table()
    table_names = db.select_name_from_sqlite_schema()

    # Step 3: check that table is deleted
    assert len(table_names) == 3


@pytest.mark.database
def test_min_product_qty(db):
    """Test checks minimum quantity of products"""

    minimum_qty = db.select_min_product_qty()

    # check that minimum quantity is valid
    assert minimum_qty[0][0] == 9


@pytest.mark.database
def test_max_product_qty(db):
    """Test checks maximum quantity of products"""

    maximum_qty = db.select_max_product_qty()

    # check that maximum quantity is valid
    assert maximum_qty[0][0] == 30


@pytest.mark.database
def test_avg_product_qty(db):
    """Test checks average quantity of products"""

    average_qty = db.select_avg_product_qty()

    # check that average quantity is valid
    assert average_qty[0][0] == 17


@pytest.mark.database
def test_max_product_description(db):
    """Test checks product description with maximum length"""

    max_desc = db.select_product_with_max_description()

    # check that product description with maximum length is valid
    assert max_desc[0][0] == "натуральне незбиране"


@pytest.mark.database
def test_max_city_count_in_customers(db):
    """Test checks which city most appears in customers table"""

    max_city = db.select_customers_city_max_count()

    # check the city is valid
    assert max_city[0][0] == "Odesa"


@pytest.mark.database
def test_best_selling_product(insert_delete_orders):
    """Test checks the best selling product"""

    bestseller = insert_delete_orders.select_bestseller()

    # check that bestseller product is valid
    assert bestseller[0][0] == "beer"
