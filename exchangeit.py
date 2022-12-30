"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
amount. It prints out the result of converting the first currency to the second.

Author: SCOTT R. HENZ
Date: 10/02/2022
"""
import currency


def main():
    """
    Requests input and displays a response.

    This function provides the code for the interactive currency exchange.
    """
    src = input('3-letter code for original currency: ')
    dst = input('3-letter code for the new currency: ')
    amt = float(input('Amount of the original currency: '))
    curr = str(round(currency.exchange(src, dst, amt), 3))
    result = 'You can exchange ' + str(amt) + ' ' + src + ' for ' + curr + \
             ' ' + dst + '.'

    print(result)


main()
