from modules.common.data.address import Address
from faker import Faker


faker_en = Faker('en-US')


def generated_shipping_address():
    return Address(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        company=faker_en.company(),
        address_line_1=faker_en.street_address(),
        address_line_2=faker_en.secondary_address(),
        city='Montgomery',
        state='Alabama',
        country='United States',
        zipcode='36107',
        phone=faker_en.phone_number()
    )

def generated_billing_address():
        return Address(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        company=faker_en.company(),
        address_line_1=faker_en.street_address(),
        address_line_2=faker_en.secondary_address(),
        city='Hanceville',
        state='Alabama',
        country='United States',
        zipcode='35077',
        phone=faker_en.phone_number()
    )
