import pytest
from modules.ui.page_objects.sign_in_page import SignInPage


# Required part of project:


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # Create page object
    sign_in_page = SignInPage()

    # Open https://github.com/login page
    sign_in_page.go_to()

    # Attempt to login in GitHub with wrong credentials
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Check that page title is as expected
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close browser
    sign_in_page.close()


# Individual part of project:


@pytest.mark.ui
def test_check_allo_product_is_added_to_cart(allo_page):
    """Test checks adding top product to cart from allo.ua main page"""

    allo_page.add_product_to_cart()

    expected_cart_popup_title = "Кошик"

    # Step 1: check that cart popup is opened
    assert allo_page.cart_data["popup_title"] == expected_cart_popup_title

    # Step 2: check that product title in cart popup is the same as on main page
    assert (
        allo_page.product_data["product_title"] == allo_page.cart_data["product_title"]
    )

    product_price = allo_page.get_nums_from_str(allo_page.product_data["product_price"])
    cart_price = allo_page.get_nums_from_str(allo_page.cart_data["product_price"])
    total_price = allo_page.get_nums_from_str(allo_page.cart_data["total_price"])

    # Step 3: check that product price in cart is the same as on main page
    assert cart_price == product_price

    # Step 4: check that cart total price is the same as product price on main page
    assert total_price == product_price


@pytest.mark.ui
def test_check_allo_product_is_removed_from_cart(allo_page):
    """Test checks removing product from cart on allo.ua"""

    allo_page.add_product_to_cart()
    allo_page.remove_product_from_cart()

    expected_empty_cart_text = "Ваш кошик порожній."

    # check that product is removed
    assert allo_page.empty_cart_msg == expected_empty_cart_text


@pytest.mark.ui
def test_check_allo_change_product_qty_in_cart(allo_page):
    """Test checks changing product quantity in cart popup"""

    allo_page.add_product_to_cart()
    allo_page.increase_product_qty_in_cart()
    # print(allo_page.increase_data)

    increase_result = allo_page.validate_increase_decrease("increase")

    # Step 1: check that qty of products is increased(product price x3)
    assert increase_result

    allo_page.decrease_product_qty_in_cart()
    decrease_result = allo_page.validate_increase_decrease("decrease")

    # Step 2: check that qty of products is decreased(product price x2)
    assert decrease_result


@pytest.mark.ui
def test_check_novaposhta_delivery_cost(nova_page):
    """Test checks NovaPoshta delivery calculation"""

    nova_page.fill_fields()
    nova_page.calculate_delivery()
    expected_text = "Вартість перевезення 205.00 ... 210.00грн"

    # check that calculated cost is shown
    assert nova_page.calculated_cost == expected_text


@pytest.mark.ui
@pytest.mark.parametrize("carid_page", ["login"], indirect=True)
def test_check_carid_login(carid_page):
    """Test checks login to carid.com"""

    carid_page.login()
    expected_url = "https://www.carid.com/my-account/"

    # check that new user is logged in
    assert carid_page.current_url == expected_url


@pytest.mark.ui
@pytest.mark.parametrize("carid_page", ["my_account"], indirect=True)
def test_check_carid_add_ship_address(carid_page):
    carid_page.add_shipping_address()

    # check that shipping address info is added to My Account page
    assert carid_page.validate_address_info("shipping")


@pytest.mark.ui
@pytest.mark.parametrize("carid_page", ["my_account"], indirect=True)
def test_check_carid_add_bill_address(carid_page):
    carid_page.add_billing_address()

    # check that billing address info is added to My Account page
    assert carid_page.validate_address_info("billing")
