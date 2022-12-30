"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: SCOTT R. HENZ
Date: 10/02/2022
"""
import introcs
import currency


def test_before_space():
    """
    Test procedure for before_space()
    """
    print("Testing before_space")
    # Test case 1
    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello', result)
    # Test case 2
    result = currency.before_space('Hello World !')
    introcs.assert_equals('Hello', result)
    # Test case 3
    result = currency.before_space('Hello  World')
    introcs.assert_equals('Hello', result)
    # Test case 4
    result = currency.before_space(' Hello')
    introcs.assert_equals('', result)


def test_after_space():
    """
    Test procedure for after_space()
    """
    print("Testing after_space")
    # Test case 1
    result = currency.after_space('Hello World')
    introcs.assert_equals('World', result)
    # Test case 2
    result = currency.after_space('Hello World !')
    introcs.assert_equals('World !', result)
    # Test case 3
    result = currency.after_space('Hello  World')
    introcs.assert_equals(' World', result)
    # Test case 4
    result = currency.after_space('Hello ')
    introcs.assert_equals('', result)


def test_first_inside_quotes():
    """
    Test procedure for first_inside_quotes()
    """
    print("Testing first_inside_quotes")
    # Test case 1
    result = currency.first_inside_quotes('A "B C" D')
    introcs.assert_equals('B C', result)
    # Test case 2
    result = currency.first_inside_quotes('A "B C" D "E F" G')
    introcs.assert_equals('B C', result)
    # Test case 3
    result = currency.first_inside_quotes('A "" C')
    introcs.assert_equals('', result)
    # Test case 4
    result = currency.first_inside_quotes('"B"')
    introcs.assert_equals('B', result)


def test_get_src():
    """
    Test procedure for get_src()
    """
    print("Testing get_src")
    # Test case 1
    result = currency.get_src('{"success": true, "src": ' +
        '"2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars',result)
    # Test case 2
    result = currency.get_src('{"success":true, ' +
        '"src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('2 United States Dollars',result)
    # Test case 3
    result = currency.get_src('{"success": false,' +
        '"src": "","dst": "","error": "Source currency code is invalid."}')
    introcs.assert_equals('',result)
    # Test case 4
    result = currency.get_src('{"success":false,' +
        '"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_get_dst():
    """
    Test procedure for get_dst()
    """
    print("Testing get_dst")
    # Test case 1
    result = currency.get_dst('{"success": true, "src": ' +
        '"2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros',result)
    # Test case 2
    result = currency.get_dst('{"success":true, ' +
        '"src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals('1.772814 Euros',result)
    # Test case 3
    result = currency.get_dst('{"success": false,' +
        '"src": "","dst": "","error": "Source currency code is invalid."}')
    introcs.assert_equals('',result)
    # Test case 4
    result = currency.get_dst('{"success":false,' +
        '"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('',result)


def test_has_error():
    """
    Test procedure for has_error()
    """
    print("Testing has_error")
    # Test case 1
    result = currency.has_error('{"success": false, ' +
        '"src": "", "dst": "", "error": "Source currency code is invalid."}')
    introcs.assert_true(result)
    # Test case 2
    result = currency.has_error('{"success":false,' +
        '"src":"","dst":"","error":"Source currency code is invalid."}')
    introcs.assert_true(result)
    # Test case 3
    result = currency.has_error('{"success": true, "src": ' +
        '"2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)
    # Test case 4
    result = currency.has_error('{"success":true,' +
        '"src":"2 United States Dollars","dst":"1.772814 Euros","error":""}')
    introcs.assert_false(result)


def test_service_response():
    """
    Test procedure for service_response()
    """
    print("Testing service_response")
    # Test case 1
    result = currency.service_response('USD', 'EUR', 2.5)
    introcs.assert_equals('{"success": true, ' +
        '"src": "2.5 United States Dollars", "dst": "2.2160175 Euros", ' +
        '"error": ""}',result)
    # Test case 2
    result = currency.service_response('USD', 'EUR', -2)
    introcs.assert_equals('{"success": true, ' +
        '"src": "-2.0 United States Dollars", "dst": "-1.772814 Euros", ' +
        '"error": ""}',result)
    # Test case 3
    result = currency.service_response('ABC', 'EUR', 1.0)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", ' +
        '"error": "The rate for currency ABC is not present."}',result)
    # Test case 4
    result = currency.service_response('USD', 'XYZ', 1.0)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", ' +
        '"error": "The rate for currency XYZ is not present."}',result)


def test_iscurrency():
    """
    Test procedure for iscurrency()
    """
    print("Testing iscurrency")
    # Test case 1
    result = currency.iscurrency('USD')
    introcs.assert_true(result)
    # Test case 2
    result = currency.iscurrency('XYZ')
    introcs.assert_false(result)


def test_exchange():
    """
    Test procedure for exchange()
    """
    # Test case 1
    print("Testing exchange")
    result = currency.exchange('USD', 'INR', 1.0)
    introcs.assert_floats_equal(1.0, 1.0)
    # Test case 2
    result = currency.exchange('USD', 'INR', -1.0)
    introcs.assert_floats_equal(-1.0, -1.0)


# Script code
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()
print("All tests completed successfully.")
