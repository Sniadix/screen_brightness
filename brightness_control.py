import screen_brightness_control as sbc
from PIL import Image
import pystray


print(sbc.get_brightness())


def on_quit():
    icon.visible = False
    icon.stop()


menu = [
    pystray.MenuItem('100%',lambda: sbc.set_brightness(100)),
    pystray.MenuItem('75%',lambda: sbc.set_brightness(75)),
    pystray.MenuItem('50%',lambda: sbc.set_brightness(50)),
    pystray.MenuItem('25%',lambda: sbc.set_brightness(25)),
    pystray.MenuItem('0%',lambda: sbc.set_brightness(0)),
    pystray.MenuItem('Quit',on_quit),
]

icon = pystray.Icon(
    name="Screen Brightness Control",
    icon=Image.open("icon1.png"),
    menu=menu,
    title="Screen Brightness"
)

icon.run()