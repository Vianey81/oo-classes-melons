from random import randint

"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """A melon order."""

    def __init__(self, species, qty, country_code = "US"):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        # self.base_price = 5
        # self.base_price = self.get_base_price()
        self.base_price = randint(5, 9)

    def get_base_price(self):
        # base_price = randint(5, 9)
        # return base_price
        return self.base_price

    def get_total(self):
        """Calculate total order price."""

        base_price = self.get_base_price()

        print base_price

        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        # if self.qty < 10 and self.country_code != 'US':
        #     total = total + 3

        return total

    def mark_shipped(self):
        """Set initialized attribute shipped to true."""
        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code




class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    # def __init__(self, species, qty):
    #     """Initialize melon order attributes"""

    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
    order_type = "domestic"
    tax = 0.08

    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes"""

    #     self.species = species
    #     self.qty = qty
    #     self.country_code = country_code
    #     self.shipped = False
    order_type = "international"
    tax = 0.17

    def get_total(self):
        """Calculate price and only add $3 USD International Flat Fee if qty < 10."""

    #     base_price = 5
        total = super(InternationalMelonOrder, self).get_total()
        
        if self.qty < 10:
            total = total + 3
        
        return total
    #     return total

    # def mark_shipped(self):
    #     """Set shipped to true."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """An domestic (US) government melon order."""

    order_type = "government"
    tax = 0.00
    passed_inspection = False

    def inspect_melons(self, passed):
        """Inspect US government order and update inspection status."""

        self.passed_inspection = passed