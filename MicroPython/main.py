"""
Created by: Bain Liao
Created on: Sep 2024
This module does basic math
"""

from microbit import *
from time import sleep

display.clear()
sleep(1)

# Perimeter
display.scroll(
    "A rectangle has dimensions 5 cm & 3 cm. The perimeter would be: "
    + str(2 * (5 + 3)),
    display.scroll("cm"),
)
display.show(Image.HAPPY)
sleep(0.5)
display.clear()

# Area
display.scroll("The area would be: " + str(5 * 3))
display.scroll("cm^2")
display.show(Image.HAPPY)
sleep(0.5)
display.clear()
