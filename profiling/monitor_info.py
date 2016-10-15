from __future__ import print_function

from Xlib import display
from Xlib import X

d = display.Display()
s = d.screen()
res = s.root.xrandr_get_screen_resources()
edid = d.intern_atom("EDID")
for o in res.outputs:
    print("edid")
    prop = d.xrandr_get_output_property(o, edid, X.AnyPropertyType, 0, 100)
    for i, e in enumerate(prop.value):
        if i > 0 and i % 16 == 0:
            print()
        print("{:02x}".format(e), end="")
    print("\n-----")
