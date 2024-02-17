# Python version of coding exercise
# ---------------------------------
import requests
import pytest


# This class holds two data values that get sent out on a web request to a payment processing API, and
# writes two returning values when processing the web response.
class CreditCardTransaction:

    # Outgoing values in a web request sent to a payment processing API.
    _amount = None               # Numeric x.xx between 0.00 and 1000.00 ???
    _credit_card_number = None   # String of 16 numeric digits.

    # Incoming values in a web request received from a payment processing API.
    _status = None               # Expected to be a string of "processed" or "rejected".
    _processed_amount = None     # Expected to be the same as amount if status is "processed",
    # or None if status is rejected.

    # TODO: 1. Fill in missing getter and setter code.
    def set_amount(self, amount):
        a = "{:.2f}".format(amount)
        if (float(a) < 0.00) or (float(a) > 1000.00):
            #self._status = 'rejected'
            #self._processed_amount = None
            raise ValueError("Sorry, check the amount")
        else:
            #self._status = 'processed'
            #self._processed_amount = float(a)
            self._amount = float(a)

    def get_amount(self):
        return self._amount

    # TODO: 2. Fill in missing getter and setter code.
    def set_credit_card_number(self, credit_card_number):
        if isinstance(credit_card_number, int):
            credit_card_number = str(credit_card_number)
            if len(credit_card_number) != 16:
                #self._status = 'rejected'
                #self._processed_amount = None
                raise ValueError("Invalid credit card number.")
        elif isinstance(credit_card_number, str):
            if not (len(credit_card_number) == 16 and credit_card_number.isdigit()):
                #self._status = 'rejected'
                #self._processed_amount = None
                raise ValueError("Invalid credit card number.")
        else:
            #self._status = 'rejected'
            #self._processed_amount = None
            raise ValueError("Invalid credit card number")

        self._credit_card_number = credit_card_number

    def get_credit_card_number(self):
        return self._credit_card_number

    # TODO: 3. Write a getter for each of _status and _processedAmount.
    # Getter code goes here.

    def get_status(self):
        return self._status

    def get_processed_amount(self):
        return self._processed_amount

    def send_transaction(self):
        # r = requests.post(
        #     'http://localhost', data={'credit_card_number': self._credit_card_number,
        #                               'amount': self._amount})
        # if r.status_code == 200:
        #     self._status = r.status
        #     self._processed_amount = r.processed_amount
        # else:
        #     self._status = 'rejected'
        #     self._processed_amount = None

        # Assume code exists in send_transaction() to send the _amount and _credit_card_number out in
        # a web request and returns two values, which are then set in _status and _processed_amount.
        # If the payment processing API is reached, then its returning values will be expected to be
        # present.  If the payment processing API cannot be reached due to a networking or other
        # problem, then _status and _processed_amount are not set to any value.

        # dummy method for testing
        # set _status
        self._status = "processed"
        # set _processed_value
        self._processed_amount = self._amount


def test_send_credit_card_transaction():
    # TODO: 4. Create a credit card transaction instance, set the amount and credit card number, and send it.
    transaction_amount = 100.05
    credit_card_number = "4263982640269299"
    expected_status = "processed"
    rejected_status = "rejected"

    cc_transaction = CreditCardTransaction()
    cc_transaction.set_amount(transaction_amount)
    cc_transaction.set_credit_card_number(credit_card_number)
    cc_transaction.send_transaction()

    # TODO: 5. Write asserts to check that the amount and status are valid and acceptable values.
    #  Use as many asserts as you like.

    actual_status = cc_transaction.get_status()
    actual_processed_amount = cc_transaction.get_processed_amount()

    assert not (actual_status is None and actual_processed_amount is None), \
        "send_transaction() failed: payment processing API cannot be reached due to a networking or other problem."

    assert actual_status is not None, "send_transaction() failed to set _status."
    assert isinstance(actual_status, str), f"Unexpected type of _status: {type(actual_status)}, expected: 'str'."
    assert rejected_status != actual_status, "send_transaction() failed: credit card transaction rejected."
    assert expected_status == actual_status, \
        f"Unexpected value of _status: '{actual_status}', expected: '{expected_status}'."

    assert actual_processed_amount is not None, "send_transaction() failed to set _processed_amount."
    assert isinstance(actual_processed_amount, float), \
        f"Unexpected type of _processed_amount: {type(actual_processed_amount)}, expected: 'float'."
    assert transaction_amount == actual_processed_amount, \
        f"Unexpected value of _processed_amount: '{actual_processed_amount}', expected: '{transaction_amount}'."


if __name__ == '__main__':
    test_send_credit_card_transaction()