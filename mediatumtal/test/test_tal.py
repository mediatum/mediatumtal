# -*- coding: utf-8 -*-
'''
Created on 25.07.2013
@author: stenzel
'''
from __future__ import division, absolute_import
import os.path
from mock import MagicMock, call
import pytest

from mediatumtal.talextracted import runTAL

BASEDIR = os.path.join(os.path.dirname(__file__), "test_data")

Writer = MagicMock(name="writer")
Pizza = MagicMock(name="pizza")

def _path(filename):
    return os.path.join(BASEDIR, filename)


@pytest.fixture
def pizza():
    pizza = Pizza() 
    pizza.reset_mock()
    pizza.get_size.return_value = 13
    pizza.get_toppings.return_value = ["tomatoes", "mushrooms"]
    return pizza


@pytest.fixture
def writer():
    writer = Writer()
    writer.reset_mock()
    return writer


def test_tal_example_macro(writer, pizza):
    expected_pizza_toppings_write_calls = [
        call().write('\n\t'),
        call().write('<div>'),
        call().write('\n\t\t'),
        call().write('tomatoes'),
        call().write('\n\t</div>'),
        call().write('\n\t'),
        call().write('<div>'),
        call().write('\n\t\t'),
        call().write('mushrooms'),
        call().write('\n\t</div>'),
        call().write('\n'),
    ]
    runTAL(writer, {"pizza": pizza}, file=_path("pizza_macro.html"), macro="pizza_toppings")
    assert writer.write.call_args_list == expected_pizza_toppings_write_calls


def test_tal_example(writer, pizza):
    expected_pizza_write_calls = [
        call('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "DTD/xhtml1-transitional.dtd">\n'
             '<html>\n<head>\n<title>Pizza Details</title>\n</head>\n'),
        call('<body>'),
        call('\n\t<h1>Pizza:</h1>\n\t<b>Size:</b>\n\t'),
        call('<span>'),
        call('13'),
        call('</span>\n\t<br>\n\t<b>Topping(s):</b>\n\t<br>'),
        call('\n\t'),
        call('<div>'),
        call('\n\t\t'),
        call('tomatoes'),
        call('\n\t</div>'),
        call('\n\t'),
        call('<div>'),
        call('\n\t\t'),
        call('mushrooms'),
        call('\n\t</div>'),
        call('\n</body>\n</html>\n')
    ]
    runTAL(writer, {"pizza": pizza}, file=_path("pizza.html"))
    assert writer.write.call_args_list == expected_pizza_write_calls
    
    
if __name__ == "__main__":
    test_tal_example_macro(writer(), pizza())
