from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def encode_hide(self, **event_args):
    """This method is called when the Button is removed from the screen"""
    pass

  def loginbutton_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def encode_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def decode_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def logout_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass





