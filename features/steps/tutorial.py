from behave import *

@given('we have behave installed')
def step_impl(context):
    """
    docstring
    """
    pass

@when('we implement a test')
def step_impl(context):
    """
    docstring
    """
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    """
    docstring
    """
    assert context.failed is False