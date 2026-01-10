"""
Chill Coffee Cashier - кассовая система для кофейни.
"""

__version__ = "0.1.0"
__author__ = "quozaru"
__email__ = "zHIjsBlKlHF7oCZ@proton.me"

from chillcoffee.main import run_app, main_window
from chillcoffee.models import Product, CartItem

__all__ = ['run_app', 'main_window', 'Product', 'CartItem']