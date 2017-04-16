"""
Make a House
"""

import sys
import os
from hedron_3d import hedron
from prism_3d import prism
from truncated_hedron_3d import truncated_hedron
from half_cylinder_3d import half_cylinder
from cylinder_3d import cylinder
from cone_3d import cone
from rectangle_tr_hedron_3d import rectangle_tr_hedron

a = rectangle_tr_hedron()

result = a.get_points(10, 4, 4, 4)

print(result)