"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: SCOTT R. HENZ
Date: 10/02/2022
"""
import introcs

APIKEY = 'J4wUjS3omwGpfpiQFnYpzQnuAvnR4nBRIuETSNmzince'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, \
        'Precondition violation: ' + repr(s) + ' is not a string type.'
    assert introcs.count_str(s, ' ') >= 1, \
        'Precondition violation: ' + repr(s) + ' does not contain a space char.'

    space = introcs.find_str(s, ' ')
    result = s[0:space]

    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, \
        'Precondition violation: ' + repr(s) + ' is not a string type.'
    assert introcs.count_str(s, ' ') >= 1, \
        'Precondition violation: ' + repr(s) + ' does not contain a space char.'

    space_1 = introcs.find_str(s, ' ') + 1
    result = s[space_1:]

    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is
    a precondition violation, since there are no double quotes inside the
    string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it
    only picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters
    inside.
    """
    assert type(s) == str, \
        'Precondition violation: ' + repr(s) + ' is not a string type.'
    assert introcs.count_str(s, '"') >= 2, \
        'Precondition violation: ' + repr(s) + \
        ' does not contain two or more double quotes.'

    quot1 = introcs.find_str(s, '"') + 1
    quot2 = introcs.find_str(s, '"', quot1)
    result = s[quot1:quot2]

    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the
    string inside string quotes (") immediately following the substring '"src"'.
    For example, if the json is:

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814
        Euros", "error": ""}'

    Then this function returns '2 United States Dollars' (not '"2 United States
    Dollars"').
    On the other hand, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is
        invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The
    JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814
        Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the
    type)
    """
    assert type(json) == str, \
        'Precondition violation: ' + repr(json) + ' is not a JSON type.'

    src_jsn = introcs.split(json, ',')
    src_kv = introcs.split(src_jsn[1], ':')
    result = first_inside_quotes(src_kv[1])

    return result


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the
    string inside string quotes (") immediately following the substring '"dst"'.
    For example, if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814
        Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On
    the other hand, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is
        invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The
    JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814
        Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the
    type)
    """
    assert type(json) == str, \
        'Precondition violation: ' + repr(json) + ' is not a JSON type.'

    dst_jsn = introcs.split(json, ',')
    dst_kv = introcs.split(dst_jsn[2], ':')
    result = first_inside_quotes(dst_kv[1])

    return result


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True
    if the query failed and there is an error message. For example, if the json
    is

        '{"success":false,"src":"","dst":"","error":"Source currency code is
        invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814
        Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The
    JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814
        Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the
    type)
    """
    assert type(json) == str, \
        'Precondition violation: ' + repr(json) + ' is not a JSON type.'

    err_jsn = introcs.split(json, ',')
    err_kv = introcs.split(err_jsn[3], ':')
    err_val = first_inside_quotes(err_kv[1])
    err_true = err_val != ""
    result = err_true is True

    return result


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst.
    The response should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>",
        error: ""}'

    where the values src-amount and dst-amount contain the value and name for
    the src and dst currencies, respectively. If the query is invalid, both
    src-amount and dst-amount will be empty, and the error message will not be
    empty.

    There may or may not be spaces after the colon. To test this function, you
    should chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert type(src) == str and introcs.isalpha(src), \
        'Precondition violation: ' + repr(str) + \
        ' is not a string type containing one or more alpha characters.'
    assert type(dst) == str and introcs.isalpha(dst), \
        'Precondition violation: ' + repr(dst) + \
        ' is not a string type containing one or more alpha characters.'
    assert type(amt) == int or type(amt) == float, \
        'Precondition violation: ' + repr(amt) + ' is not an int or float type.'

    url_str = 'https://ecpyfac.ecornell.com/python/currency/fixed?src=' + \
              src + '&dst=' + dst + '&amt=' + str(amt) + '&key=' + APIKEY
    result = introcs.urlread(url_str)

    return result


def iscurrency(currency):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert type(currency) == str and introcs.isalpha(currency), \
        'Precondition violation: ' + repr(currency) + \
        ' is not a string type containing one or more alpha characters.'

    cur_call_svc = service_response(currency, 'USD', 1.0)
    cur_err = has_error(cur_call_svc)
    result = cur_err is not True

    return result


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the
    currency  dst. The value returned represents the amount in currency
    currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """
    assert iscurrency(src) is True, 'Precondition violation: ' + repr(src) + \
        ' is not a string for a valid currency code.'
    assert iscurrency(dst) is True, 'Precondition violation: ' + repr(dst) + \
        ' is not a string for a valid currency code.'
    assert type(amt) == int or type(amt) == float, '' + \
        'Precondition violation: ' + repr(amt) + ' is not an int or float type.'

    xch_call_svc = service_response(src, dst, amt)
    xch_dst = get_dst(xch_call_svc)
    xch_kv = before_space(xch_dst)
    result = float(xch_kv)

    return result
