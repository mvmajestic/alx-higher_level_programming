#!/usr/bin/python3
"""Define Rectangle Class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Module Representation of Square
"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a Square
        """
        super().__init__(size, size, x, y, id)

