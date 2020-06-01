import webbrowser as web
import PySimpleGUI as gui
import hashlib
import random
import sys
import socket

from Crypto import Random
from Crypto.Cipher import AES

"""
    Variables below are encrypted and require a hardware dependant key to extract meaningful data from. Art assets are held internally in a bytes structure to reduce dependence on extra folders.
    The links will not have any documentation as they are already very well documented in the amazon internal wiki.
"""

_C_FCRESEARCH_ = b'eb\x97b#"\xbc\x13#\xf5$\x1542v\x8a\x0e\xd2\x11\xdb\xdc\x08o\xbd\x86=\xa3\xdfpz\xd6\x19\'S\xb4\x90\xb8\xd6\x969\xf9#\x1f\x18\xbb]\xe5\xd6k\xe1\xb7\xcb\x98/\x9b#\xd4\xa7\x1a\xe1\x82.\xc9\x08'
_C_MOVEITEMS_ = b'\x87J5\x0c\xf4M\xcc\xff\xda\xc1\xf2\xb5\x90\xf5f\xab\xa3>\xa0)v\xbc\x05\x9c\xe1\xb4\x0e3\xaf\xf6\xcc\xad\x91\x07y5\xac\xaf\xdf\rI\xf0\x97\x19r\xec\x94\xb8\xcd\xd6\xf6\x9f*T\x86A\xf5>\x8f5\x18\x83h\x91\x96\x06\xe6\xa06K>\x8c+~(\x0e\x10\xd1\x92\xf9\x9c\xda\xc5\x0b\xe1\xeb\x1c\xc6T7;\xf5\xb0\xcd\x90z'
_C_PODCONSOLE_ = b':\x8e\xbe\x06\xfb\xb8S-\xdd7\xa6\xb3\xe97>I{\xb6\x0c\x86J\xa4\xa3\xe0\x8b\x9bY\xba6\x12\x17j\x02Q\xe9\xdb\x10RY\xfb\xbf\xf2\xf2K\x07\x8d\xa4rV\xcf<0\x88\x15\xbf\x17\x18\x08y\xabz\x84\xb5"'
_C_RODEO_ = b'\xe8\xfe\xc0y\xdfh\xbf\xf9\xe7J7\x19\x14\x1c\x0f\x04\xbf\x992\x1c\xaa^\xa4\x17\xab\x19Sv\xc2iE(\xa3_\x81\xfb\xa3\xb5P\xfd\xff\x84\xabc\xd6\x17\x04q\x8f\x9b\x99\x05\xaf9\xf0\xbc*6\x1cs\xae\xa8td'
_C_PRINTMON_ = b'\xbb\x93r,\xf4\x19\xd2\x0e\xbe\xb7\xb5S\xddW\x13t\x99\x18D*\xe8\xa2,O\xa7p\xd2\x02\xceh\x94HM{6\xe7\xfbQ\xeb@hF;\xb3\xc2\xe6\xe8\xc5\xd0\xb9&\xe7\xb7\x90\xd9\xd1\xfd\xad\x889\xbe4\xd1\xdb'
_C_FCART_ = b'\xceWUq\xb7\xdb\xd9l\xb4\\\x05Hr\x16\xaaWQ\xda\xe0+\xa9\xe6\x98\n\x87bXg>\xd1\xeeE\x99\x06\x120\xce\x98 pY\x84`-\x02\xc5H\xc9'
_C_MOTHER_ = b'{8\x99\xd4\x97\x02\xdb\x15-\x9848\x1fH\xf1\x14C\xfarS\xdf\xee\xa4\xec\x0e\xc62\x98u\xe6\xcf\xee\xd6\xcduHY*"\xb0\xbdg0A\xc1\x8e^\xb5'
_C_LABORTRACK_ = b'\xbf\xc5v\xd2\xca\r\x1f\xd1\xef\x1a\xf5_3R\x80\x18\xb6\xc0\x815\x19\x18\xf5\xbf\x9d\x8e\xde\xed\xac\x08\x84~\t\x90\xd0\xa4\xc2k\xdbv\x91\x0eyg\xc9R\x80N\x1dw\xca\x8eb:\x1c9\xc7\x08s\x04\xe5&qR\x14\xbeiO\x9ede\t\xf6\xad\xb5\xe9WJ\x08\x82%O\xbf+\xcb\xff\xd2:\x9f\x91\xc3C\xfc\xa0d\xeb'
_C_ICQATT_ = b'^(\x88D\xe7\xff\xbb\xd2\xdb\xe4\x84]o\xc4\x9bpC\xf5\x00\xa6\r\n3\xaf\x94\x11\x02\xcb\xc7zC\xf8\xce^\xb1\\\xf5\x8b\xc8#"\x9bx\x88%IUG<\x9c\xc7+\x16\xf1\xad\xa3\x11\x9f\x80\xd1H\xd2v\x08~X]\xe4\xd5\x01\xc9q\xcd,p>\t\x98\x84\xb57kz\x06\xe8\x80z\xc1\xef5E\x81\x11\xd8\xc9a\x04\xbf\xed\x1d\x18\xb8.V\xa2\xf7\xd2m\xac.\xf1\xd5\x1dt\x8d\xc7E)\x1f\xadR\x12\xccc\xa7\xe5\x18>{m\xe3\xb3yo\xa0\xc4n\x05\xcb+?E\xfa\x90\xb9\xda6\x90\ny=\xee\x81o0\x87\xa7_\xf6\xf6\x85\xcc\x10\xf1\t\\10\x92\xf6\xab\x86\xd39\xddrZl\xbf\xee\xa4\xdap\xfd\xda\x1b\x91\x1aI-\x81\xd5\x8d\t\xd6\xf9\xc63P\\\xcd,2\x9aE\x055g\xa7\x06w\xc0\x03\xc4\x1b\x9d\x03\xc3F{\xa5\x06j^\x15\x0b\xa9\xff\xfb^\xab\xdd\xf9D\xf0\x12\x9c\x15\xf0\x1b\x9a\x0c\xff\x14\xc4r\xe4y\xf5\x00Zd\xcd\xa2z\x82\xd4\'\x15\x8e2_\xc0YD\xd9V\xa0\xcc\x14Q^\xca_!\x91\xbd\x1ex\xe7\xfeKo\xc5\xa9Hxap\xb2\xa6k\xe8\x17\x81\xc8Z\x9d\xbc\x19\xb9\x88d\xbaq\x01\x0cz\x9a\x8e\x19/9\xff\x93k\xd4\x1a\xc5\x12;\xa2\xd0^\x18\xef<\xc2\xad\xd7\x08-kMN\xaee \xd0A\x9f\x15\xc3\xc4A\x1b9S=\xd1\xc4e\x82\xa0\x049s\x80\xee\xcc\x91V\xaa\xfe\t\x93\x98,\xddf\xb9\xaa;\xb2FjI\xe9\xfa\xd0\xc1\xb9\x82\x99'
_C_TROUBLETICKET_ = b'\x91\xa38J\xfd4\x01B\x95\xe6\r\xd1\x89\xd4\xda\xa7\x179\x93L\xbd|r\xdb=A\xe0\x91\x91\xc8<^\x07\xde\xa8\xa19\x1f\x9aQ\x08\x97\x86\xc2 \xd4\x04#'
_C_ADDPACKAGE_ = b'\r*\xd6\x88\xcf\xc5\xec\xf3x\x17\xb8\x81\xdf&\x9b\xbfB\x01\x01\xc4X\x1d>\x8d\xa4\xde~\xdf\x83\x1c\xf1\x17\x8b*t;\x96P@B\xdf&,O\x81S.\xb3v\xfb\xbf\xc1"l\x82\xa3\x9b\\M\xe7u\xc98\xe8\x0685\x998\xa7CO4\x81\xb2\xd7\x1c8j\xe7z2\xf1pS\x19\xc8\xe4\xf6\xb2\x8d\xc5UdY\xe4'
_C_DOCKOB_ = b'\x86\x8b\xb5\xef\xe2\xd8\xec\x00\xed\xa3\x1e\xd1B\xc0U\x7f},+\x1bE};)\x10t\\\x8b\x80\x92\xa3+\xc9\xf0}S\xc7\xd5\xda\xe0e\x9f\xa9\x91\xc6\x07!\xaed(\xe9%G\xb4h\x86\x01\xf20\x97\xcfM\xe4\xaa[\xf8\xfd\xfb\xa8\xf7\xcd\xb9\x88S\x15J\xcd\xd4\x1c\xe4'
_C_YARDMANAGER_ = b"\xd2\x14+\xb8{8\xeb\x00J\xcf\x9a\xde!\x04\x9f\xc0\xa5\xd6zk\xdf<'\xe9nhx\xe4\xb8\xa7.q\xd7+\xda\xe9\x91\x99\x19(\xfd\x15\x8aUe\xacE\xd5\x18\x88#8s'\xe18B\xb0\xc7\x97,%H\x01\xb9OeO\xc9\xc4\x8fNl\x92\x17\xd0\xceJ\\*"
_C_DOCKIB_ = b'\x05;\xcc+\xcc*\x1c\xd2\x13\xf7\x9d\xf2|\x82\xc2\xec\t\xd4\xb0\xb7\x89sE\x15\x81_\nR\x930o\\\x00\x8c\xc37D\x9b,Y\x89\xb4\xcf\xb7y\x88*H\xa0\xb0\r\xaf\xd2\x00\xe0\xaaO,\xb6\x19\xeaE\x7f\x03\xf0\x1c>%\x9f\x81\x85e<8\x9a\x12D_\xe8w'
_C_PODRESEARCH_ = b'\x01\xe5\xd8\xf7\xef\xd8\xa9\x19B\x96\xce\xda|@\xafT~-\xf26&\xb0\x936I\x8d\x9b)\xb9\xef\x06D\x1a/\xfce\xb6\xbe)>\x9b\xf8\xba\x1e[\xa8\x05l\x92\xb2\xe0\xdb|\x0e\xf8-\x0f\xa7\xa8\x85\xf8,\xbe\xf2p\x18\xd4\xf7)\xea"\xb8\x08\x12\xdd\xaa\x95D\x85\xe9'
_C_DOCKAUDITS_ = b'\xa2\x84F\xc2\x9b\x7f|>%\xc8\x1ek\x06\xc2)\x17@\xae\xc8\xec#\xb1a?U\xcb>n\x07B\xfd\xa8\xfe\xdc\xc8U\xc8\x1c\xb9]\xf6\xf2\x9fW\xe0\xf8we\xe7\xbdn#\x98UQC\xd3\xa99\xbe\xa5\xfc\x08\x9e3hnG\xe1ZK\xcf\x87\xc3\xf8\t\xab\xc2\x0e~'
_C_ADDBACK_ = b'\xaf\xbeAn\x8eP\x93\xd7\xc9t\n#\xd1\x8aQp\xe17\x0c\xda\x9bF\x94g\xfa89rb\x1fy\x8d\xc6T\xedx\t\xbd!6\xffI\x11\xa2\xb1\x19g8c\x0exh\xc2#\x8d\xd3\xd0\x02\xbc\xdf=\xfd\xc9Vr\xdf\xec\xe0\xb2-\xaa(\xf8x\xa5<G\xbd\x90\xc8\xa3\xf1\x1c\x9f\xd5\xbc\x14$\x06VEL\xb6,\xbc\x8b'
_C_TOTEROUTING_ = b"\x86\xdbDw=j\x92\xa0\x0fL P\xd0Jf\xb5\xe74:\xd2\xf3\x01\xe6L\x8b\x87\x9d\xbb&\x820\xbd\xb1\x86\xf0\xb4^\xf1\xd3\xbe_\xeb\x82\x94\x1f\xbb\x9c\xceMMB\xbb\x96\x98\x98\x91\xed\x84\x8a\xa8w\x12B\x01\xd3'i16\xc6\x93\xb6\x19\x11\xd1{t\xc5\xdf\xe7"
_C_IOPRINT_ = b"\x8a\\\x8a\xcf\xd4\x82\xf9cs\x82\xa4\x97\x94z\xe8\x0b\nH\xb3\xa5yD\xa7\xc1\xd9\xcd\x92y$X\xfd}\xea\xd5\xbe\xbe/\xa2\xd3_9\xb5\xa9\xeamR\x1e-\x89\xbfY\xf1R\x11\x1f\xd3J\x11b\xcaZ\x9fI\x93\x0e\x00e\xba\x06\x85E2\xf0'x\x1c'\x94\x10P"
_C_FCLM_ = b'\x9f\xa2\xff\x93+\xa1\xb4\x8f\xb00\xe7\xd1\xb0<\xf2c$~\xaa\xfe`\x16\xca\x13\x02\x86DC\xe5<\x87(\xc9Y$W=\xdbs\xb1\xc72\x18\x1d\xf7Z6\xd0\xd1X\xe3\x89\xbe\x9c\xc8\x11Xy ,\x8f\x94\xb5\xf1\xc4\xb9\xc2\xf1+_\x1fi8^\xbc\xfa2\x19eD\xdb\xcb\xbe\x03\x1e\xf8\xc7\xfb- ,\xf7z\xb4\x02-0?e\xf2\x0f\xd1\xbed\t\x1e\x95\xd0\xb0\x83\xe4\x8f#\x13\x0c\xdax\xe1\x91\xb1\xac\x0f\x048\x98b\xab1{\x92\x93C\x05\xf6\x16\x8b;\xdf\xa5\xf4\x0c\x98\xee\xff\xb3\x8a\xaa\xe0\xdc\r\xe3O\x12\x8f\xae\x8b\x18\x9e"~I\x81\xa5\x0e\xb8\xe0\xf8\xdc\xb6Z\xe0r\xd2\x19*\xc8x3\xb9\x1e\x14\xeb\xd8\x1e\xc1u\x0f*_\r3\xf4e\t\x9d.U,\xd1\x17\x00`Gz\xbd=\x05\xcb3e\xd1%\xa3 r\xac\x8d\xb3c\xc5\x16G\x85\x9f\x8f\xab \xdfIcF\x7f\x82J\xa2^\x9e\x99\x06\x1e\xe7\x91\xa1+,u)\x123\xb8\xb8\xc7\xb8\x8e:\x16\x91\xbc\xa7\xec\xc5\xac]\xb3\xec\xa4\xa2]\xfa\x0b:\x8a\x81\xfew\xc3\xbe>\xc3#\x01_\xee\x91\xe1\xd7\xa1\xe8\xa6\xed[\x97\x87\xab\xb5i\xb0\xed\xf5G\xaf\x8cq\xb1\x94\xb2N\x16\xc7\xa8\x02:\xe8\xa8>5\x19~\xe5\xb1'
_C_HISTORYMANAGER_ = b'\xa8\xe6W_\x13\xfd\xc6\x93\xcc\xbe\xef[7D\x1a\xcf\x18\xcfH=\xae\xfd4\x87\x8e\xd4\xc7\xd8`&\x823\x87\xc2\x87b\xd1\x8ar#\xca\xec|MO\xd7\x11\xd5g\xb8\xaf\xc4o\xe2\xe9\xcf\x16$Pi\xbe\x0b\xd8/'
_C_ARU_ = b'\x04\x01Z\x94\xf9\x95x\x90 r\xdb\xb2Zdi\xeba\xb9\x04\xbcZ\t\xa6\xda\xa6\xe1\x93\x8d#\x1e\xc0\xb6\xca\xb6b \x8d\x11>%\x04\x1d\xb8\x05\xdd-\x05\xff0=\xcc\x85\x19\x0b\xa7\xbe\x00LNX\xe7`N\x8a\x9b\xd1;:0z\xca<\xfc\xaa\x9f\xb6E(\xdc\xcd'
_C_DAMAGECARDGEN_ = b'\xa7oh\x15\x98\x88\xe9\t7K3%@\xba,\xeb\xc7\x8a\xcd\x1b\x8c)Q\x05\xce\xe7\xa4\x1c\xdb\xb4\xbe\x9b\x92pA\x88\x13y\x16\xc2\xf3\x04_\xb9`\xa9\xf3-,\xf9\xddg\x04\xac\x06\xac\x9f!_\x94\x0e\xe4\x90\xde'
_C_EMPLOYEESEARCH_ = b'\x05C\x11\xb2^\xdb\x9d\xae\xcc\xa6I\xa7\xae\x90z\xd7\x1d\x93w\x02gl\xf9hg\xfeB\xa3/\x9b_\x08\xfd\x0b\x19\x1dR\xb7Z\xd0\xb2\xc1\x1ceS\x88\xf3u|[sg)\x84\x8ab\x9b\t\xeaAQ\xb0\xbe7\x17>\xb3\x80z\xa4`\xff\x1a9C\xb8\xe5\xdd\xf2\xbc'
_C_FANS_ = b'\xcch\xb2=l(\x9cr=\xbd\x1d\x19\xdc\x85\x1b\x9dH!tl\xba\xd7\xf6\xcc\xa9\xdaa0\t\x0f\xd8\x16&Z\xf80Y\x13Wp\xb9e_\x86\xf1:\x16)'
_C_DAMAGETEMPLATE_ = b"e\x9b\x8fQWo\xad\x00{R4M\xf4\xf0\xe0\xa4x%r#\xa8?<DO\xf97\xb3'5C\xce\x15\xee\xf0\x8f\x9b\x13\xa35s\x1e\x05\xc6\x15\x81\xb9\tI\xf9&\xb8\x1c\xa7oL\xd0\x00\xed\x0c\x80\x93\x7f\xaaq\x94=\xca\x8f\x8b\xf1\x15\xa3\x17\xbc\xf0\x17'\x15\xc3\xb0D<c\xf5\x19\x1b\xcae\xaaU\x15\xf3\xe9@\xef\x19H\x98\x0b\xb0\x11\xab\xd4\xceQ\xa2f\xb1|\xc7\xac"
_C_FCCONSOLE_ = b"\x1a\x00\x05\x16[>\xd5Nv\xbfP\xe8C\x021\xb2\x83jF\xb5\xa0\xd3\xae\x94\x08QE\x8a\xed\x95\xd0+\xce\xd0.\xda\x86l\xf6\xb2\x99\xb6(\x1a\x90\xc6\xd5\xfb\r+n\x19\xf1b\xa1\xc0\xfd\xc6R\xa7\xc3\xb8Z \x1a-A'\x14\xca\xec\xe2\x9c\xfe\x05z&\x04\xdb0"
_C_KNET_ = b'\xbc\xf9\xc2D\x13;+i\x04\x8a\x1e\x83\xde\x18\xbbV\x19\x90\xa2\x8fr}\x0c\xb7\x16q\xe4\xee\x8a\x1d\xf8\xfb\xb3\x9d\xe0;\xb0&\xb5k\xc0~q\xcf\xbd\xc9\x04h'
_C_BUTTON_ = "iVBORw0KGgoAAAANSUhEUgAAAGQAAAAjCAYAAABiv6+AAAAACXBIWXMAAAOkAAADpAGRLZh1AAAC0UlEQVRoge2br24iURSHfyXBgJkaDIhBY4rB0kdAXtk+QeENtk/Q7hO0dVfyCJCgMGAwGEaAwTAGDGbzm5zLDgVaIMB0l/MlhKYJDHO+nHvunzM3OABrrQegBqAKwAdwB8A75DuugBBAH0AAoA2gaYwJ973tvYRYa+8BPIkM5HK56JXJZJDNZq9dwBrz+RyLxQLT6TR6CU0Av40xre8+/6UQay2z4IUiKMD3fRSLxdPfxX/MaDRCEARODsU0jDHBrjveKcRa+0AZ2WzWq1QqUUYox0Mh3W6XGRSKlPe9hVhr65TBbCiXy0in06riBCyXS/R6vShrRMrr52/dEOJkMCt0eDoPFMJs2SZlTYgMU28q4/zEpDzGh6+U+8MVcIpQGecnFucXiX1EKnblqICzZiiXgbFmzGUm+1eIrDNqHKq0gF8OxpoxZ+zFwSpDntxiT7kssbhz4Y0b2Q6ZaSFPjliBv0257RCVkRyFQsFdu0YhVR2qkoW1RBxUKcRXIckjDnwKueOurZIs4uCOQjzdQk8eceClfvjvvDoiIdyFVJLFOaCQVhjufcKonAlx0KKQcDabaZwTRhyEFNKOnf0qCSEO2hTS5Pg1mUzURUIw9lJDmik5cG+pkOSQI90WXbhp7wf/qcX98jDmkgwfcNNeOULs8wBeuSwS8747xo0vDBssLMPhUJVcCMZainnDXXElRLrqnmlMZ13nhzGW7HiOdzSubZ0YY34BeO90OlpPzghjyxgz1hLzFbsa5d4APOgp4umJnQ5SxuPnC3zVSspOiHo+n3fdEf/Ujf802ITNIUpmVK/GmMa2n/hdszU7IZgtPjOlVCqpmAOhiMFg4NYagTTG7eyC3/dxhLp0Rfie50VnwHyPHT0qAos1V92sE+Px2NXiQB5H2OjlPUpITIx7WOdeHtZRdsOHdpgJbWNMc984HSRkiyBPxWzARd5xU1QAfwDvPzbqRGQg7QAAAABJRU5ErkJggg=="
_C_LOGO_ = b'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'
_C_AA_LOGO_ = b'iVBORw0KGgoAAAANSUhEUgAAAGQAAAAqCAIAAADK0mkfAAAACXBIWXMAAABYAAAAWAF42ktiAAAHHUlEQVRoge1aX0hbVxj/NoZ7yc1keUmTgYG6ijBImMEwFtAMZYFVXTUPnbYzsHa6TV3/CGZV6lJqUbDSVrsuc2wJdNaH1lZtIUWLOizFEEtkgyySQgoa8zDB5t6X+tJxcuLJyU1i7o1x28P9IeHk3HvP/c7v+31/rrmvvXr1CiQIw+sST8IhkSUCElkiIJElAhJZIiCRJQISWSIgkSUCbwg5dcnrm5h2z84tRlkOz1SZjNZGi0Gvw1/Xw5Gu3n48HrDbJqbdd6bc6+FIaUlxR4u1ymT0B4LXHM7ZuUU5IyvX63o629QqJVk/ynLDDufM3OJ6OIJnSkuKrY2W+lozOadvcOSvQDCtec2NliqTkZjqHLvt8fqiLKdWKatNxvYWq5yR4aP+QLBvcAQAGEZ2Y+jisMPJs3N3HrJ38BNTbkIEDwN2G97Pktd37OQpsk9/8q5uDF3s6u0nRAOAnJHNPRjHe/AHgsdOnqKPEtTXmgfsNvzt+MlTS15fWjPaW63tLdZMpsoZ2c3RK6UlxQAw7HBe+9GJ5ztarWRM7NydryxhGGU57ApCBPESAFxzOFMv8af4/6szPTwuoiw3MeXG477BEXJUzshoxU1MuVNXS4VcJsMOI0yVlhQfqTFjU6Msl9bZPKYAwDl2e/cbZSGLDr3uzrap8Z/nHoyT/ZCo4cHaZOG5SK1SdrRasXsxWC6+LNFLlcm4/Pv9+Qfj9LWErH677eboFfxHn6BWKY/E1D2847lyve7erdF+e9e9W6NkEeIbGtampEjPpFyCLDnLoNd1tFrXwpEoy1mbLNj51Saj87eMTqivNXd3tgFA5SdHCZsDdptBr6uqNNYePcE7v6PVGmU5fyDYE7sK7aHRMju3iMfrGxFCCnaSPxAkR/HKckYWZbkE6ZUfkktITpiZX6R5oe30B4JC9JudLLVKidPBejgyMeVe34ishSO0B5a8PpLmMQxl8a/vqJSELHwOrSwCvH6U5TyxMkJvOxVRlvv6TA+Zbm6ylMdWpndL34XZSRqelDWrK+PypBPL7sheDXGlyypRAjrpCAEuhbtIlcaww0lXzO4dMWaShqFMh2lKLSCMYI4IspAVZbnaoyfwneSMrLmxobxM5w8EL12+LvZOmdDV20/C6kjNx1WVRjkjO/7l6dTTPV6fi+K0f6dQ7hEGvU6gFLKQNexwEp/cG/tJrGqyYsnrI0ydO/tNc2NDpit4Adjd2UaHW9oAB4C1DCUoN2SphkTe5WU6whSteeEBnxae5YRLCVNpi6yN6tRQRudQ8BKiaTNo80h9yMSmKAjq4FGlp2J+dv4xbVle7MAcYX/cvf+QTC55fe0t/AqI0txOlyRnZOc62+przeqdeuIPPCOnkaY/XmEO7clUoc+G/tWga+yOZ3nF9v0ALQe6pcwBjCyhiEuXr3uWV+5OP3SN3SGTOE7ZzLeIstzdadRDNex0Bnen3SMOl2fZ913vAMm21kZLbkmdRhZl1deYSfIjSZ10xjnUPh6qTUaSFmfnHxPNEpngnp6lApAIeS0coQO2vcU6M7eIYxA1qI7EnbqTH0VzRjayas3+1SBd1w16XXdnmz8Q7OrtN+h1PwxdzJS2iBt3yWtqlXLAbqOfHNUqZU8seeP2FT/W+QPBKpOxvsbMezBA3d90ojW/OXqlb3CEbtbxalmfkAVC0E9huMPGfSb9rJPH4oj1SwuHRFDiJPY5bCwAF4KXW/BmIZp5txmYIt5S6+HIWnIznC/s+XfDVRdwz+G9DigozKNZfGxvwZOz6F48HKiAw4/Q1MYCGtODVRe66lBzkmHbW7C5Ej+BgA0BoxFixZ7/+afQwR9X4dZBeHoBmbJPePkCKajsPKLm8COo+AUU2mQKfEkDgJgLv4XQJGJncwWRGJpExMmK4mNM6MYCspwNofHmyn6TpYXPnqGdLNsRZU/OoBvnHUwRvH8e/QEgOg59Dpo6NMbBGJqE7RfokwwQv1uICE0dskehRVepKmJRHItlLDFGg1TGaOLrpER0vskCQO6qf4rcuL0Ff16F8YNw/6N4FOQLbAj5H6+8fAFw/sJhiA3APJIB5vFABZrBRMg0iERZjI63tYgghRYtu7kCBW+h1RhNnOXMyOu7DhsL8OR0kpgVWtB8iozmpQkh2N6C8AJa8/lkQq0KLVT8ij7Hi9Fk89/iciUbQsrKwZgY9uHFkFUXCsZUWSmwP3XIk4oMRWrTh+IoPI+2xAvngkL4YAglbBx3Mw0ohREdCYTgXJ4W+/YWzaornjj3DkaDSNHUJUS08AWi9fCj/S3BKdjnV442V1AW21jIhTVGA0V1SEp04cMITaJs/e8ytf9kEaDiPY8+2RDiLi0KChEvCh36xEXqf4b/7mU2XLwxFNp/XyY5QHrzTwSkn+9FQCJLBCSyREAiSwQkskRAIksEJLKEAgD+Ab0ShUDln1yWAAAAAElFTkSuQmCC'

def key_gen():
    """
    :var host_list: Get the host name from current network, expects ASIN282 access
    :var _HOST_NAME_: Join host parts without front face unique tag, this allows use of all internal computers
    :var _Hash_Master_: Hashes the host name into a unique key using modern sha512
    :var random_key: A 16 bytes key pulled from seed-random addition, is a bytes like string for AES encryption
    :var lib2: a library of letters and digits in byte form
    :return: "Random" key to be ejected and used in encryption steps
    """
    host_list = (str(socket.getfqdn()).split('.'))  # The real thing you should use
    host_list.pop(0)  # Remove the initial identifier, it causes problems over cross facility
    _HOST_NAME_ = "".join(host_list)
    _Hash_Master_ = hashlib.sha512(_HOST_NAME_.encode('UTF-8')).hexdigest()
    random.seed(abs(sum(char_to_num(_Hash_Master_))))  # Set seed to be a constant in the right facility, requires Amazon internal access
    random_key = b""
    for i in range(16):  # Iterate to create the 16 byte key
        lib2 = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q',
                b'r', b's', b't', b'u', b'v', b'w', b'x', b'y', b'z', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8',
                b'9', b'0']
        random_key += random.choice(lib2)
    return random_key


def char_to_num(arg=None):
    """
    :param arg: takes input list and converts to float value
    :var new_list: New list containing only digits, no alpha characters
    :return: New list of only numbers
    """
    new_list = []
    for item in arg:  # Cycle through characters and identify numbers vs digits, must exit with all numbers
        try:
            valueless = item / 1.0  # Attempt to use char as number, if fail, then convert to num
            new_list.append(float(item))
        except:
            new_list.append((ord(item.lower()) - 96))  # numberfy the letters
    return new_list


def decrypt(encrypted_data, key):
    """
    :param encrypted_data: Data that is encrypted and in need of decryption before use
    :param key: The key taken from external parameters to decrypt data
    :var iv: Randomized initialization vector stored in block
    :var cipher: The assembly blueprint of the encryption phase, rebuilding it to the original
    :var plaintext_data: The data decrypted using the rebuilt cipher
    :return: Plaintext data to be turned into a URL
    """
    iv = encrypted_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext_data = cipher.decrypt(encrypted_data[AES.block_size:])
    return plaintext_data.rstrip(b"\0")


def get_link(enc_data):
    """
    :param enc_data: The encrypted data to be turned into the original URL
    :var key: Generates the key to be used in data decryption
    :var link: The decrypted and restructured link
    :return: Returns a string link
    """
    key = key_gen()
    link = decrypt(enc_data, key).decode('UTF-8')
    return link


def template_window(warning_message="", labor_tracking="", link_list=None):
    """
    :param warning_message: The message to be relayed to associate of actions needing to be taken to complete task or start task safely; Text will appear in red to user.
    :param labor_tracking: The labor tracking codes accepted for the certain path, this can vary by department so all possible codes should be given.
    :param link_list: List of encrypted links that will be actively decrypted upon call, preventing some leakage.
    :var lay_3: The basic layout of ll windows, final design after 2 prior iterations.
    :var win2: The final base design of window template, lacks a title bar as it does not need nor should it have, any critical features as of 5/31/2020
    :var window_input: Reads input from the window by user action
    :return: None
    """
    web.open_new_tab(get_link(_C_LABORTRACK_))  # Open labor track window, may require secure login

    lay_3 = [[gui.Text(text="Please login\n\n",  # Generic text
                       background_color="white",  # Background must be white
                       text_color="orange")],  # Basic orange
             [gui.Text(warning_message,  # The warning message that is path specific
                       text_color='red',  # Alert red
                       background_color="white")],  # Background must be white
             [gui.Text(labor_tracking,  # Labor tracking that is path specific
                       background_color="white",  # Background must be white
                       text_color="orange")],  # Basic orange
             [gui.Button(button_text="Continue",  # Generic text
                         image_data=_C_BUTTON_,  # Custom Button
                         border_width=0,  # Remove default ugly button outline
                         button_color=("orange", "white"))]]  # Basic orange with white matching background

    win2 = gui.Window(no_titlebar=True,  # Removes title bar from window
                      title="",  # Window title
                      layout=lay_3,  # layout to use
                      auto_size_buttons=True,  # Automatically resize buttons if possible
                      auto_size_text=True,  # Aut-resize text if possible
                      keep_on_top=True,  # Keep window on top of others
                      grab_anywhere=True,  # Grab window anywhere to move it
                      element_justification="center",  # Centers all items
                      icon=_C_LOGO_,  # The custom icon for windows
                      background_color="white"  # Must be white
                      )
    window_input = win2.read()
    if window_input:  # Any input will close the window
        win2.close()
    else:
        pass
    for url in link_list:  # Cycle through links in list, links are decrypted
        web.open_new_tab(url)  # open url in new tab of default browser


def fc_menu():
    """
    :var layout: The main window layout, has a drop box to select items and paths
    :var window: The actual window component, using a base white theme
    :var button: Receives and holds button input
    :var list_box: Holds input from the listbox element
    :var mode: The selection mode from listbox
    :var lay2: Second layout for a warning message if no options are selected
    :var win: The active window of the lay2
    :var window_input: Any input the receives
    :return:
    """
    layout = [[gui.Image(data=_C_AA_LOGO_,  # Customized logo
                         background_color="white")],  # Must be white
              [gui.Listbox(values=sorted(["ICQA Problem Solve",
                                          "AFM Problem Solve",
                                          "Find Item",
                                          "Pod Transfer",
                                          "Induction",
                                          "AFM Trainer"]),
                           size=(30, 10),  # Ensures the listbox element is visible on nearly all displays
                           default_values="AFM Problem Solve",  # defaults to what should be the top value
                           background_color="white",  # Must be white
                           text_color="orange",  # Basic orange
                           enable_events=True)],  # Any interaction with listbox element forces a window read
              [gui.Button(button_text="LAUNCH!",  # Launch button text
                          image_data=_C_BUTTON_,  # Custom button logo
                          button_color=("orange", "white"),  # Orange text with white background
                          key="launch",  # Callable key
                          border_width=0),  # Removes ugly button border
               gui.Button(button_text="EXIT",  # Exit button text
                          image_data=_C_BUTTON_,  # Custom button
                          button_color=('grey', 'white'),  # Inactive grey and white background
                          border_width=0)]]  # Removes ugly button border

    window = gui.Window(title="Launcher",  # Window titlebar text
                        layout=layout,  # uses predefined layout
                        icon=_C_LOGO_,  # Custom icon for window
                        background_color="white")  # Must be white
    while True:  # Keep reading window until something happens
        button, list_box = window.Read()
        try:  # Keep launch button disabled until a selection is made
            mode = str(list_box[1][0])
            window.find_element("launch").Update(disabled=False)
        except:
            mode = ""
            window.find_element("launch").Update(disabled=True)
        if button == "launch":  # When launch is chosen a path will called and it's subsequent window layout
            if mode == "ICQA Problem Solve":
                template_window("Click the button when you have logged in and labor tracked",
                                "LABOR TRACK CODES: ICQAPS",
                                [get_link(_C_FCRESEARCH_),
                                 get_link(_C_MOVEITEMS_),
                                 get_link(_C_PODCONSOLE_),
                                 get_link(_C_RODEO_),
                                 get_link(_C_IOPRINT_),
                                 get_link(_C_FCART_),
                                 get_link(_C_PRINTMON_),
                                 get_link(_C_ICQATT_)])
            elif mode == "AFM Problem Solve":
                template_window("Make sure to grab a kindle with MMA if you have not done so!",
                                "LABOR TRACK CODES: ICQAPS, ICQAAD, ICQAAM",
                                [get_link(_C_PODCONSOLE_),
                                 get_link(_C_FCRESEARCH_),
                                 get_link(_C_MOVEITEMS_),
                                 get_link(_C_ADDBACK_),
                                 get_link(_C_TOTEROUTING_),
                                 get_link(_C_FCART_),
                                 get_link(_C_TROUBLETICKET_),
                                 get_link(_C_PRINTMON_)])
            elif mode == "Find Item":
                template_window("Make sure you have bags, gloves and minor severity cleaning supplies",
                                "LABOR TRACK CODES: ICQAPS",
                                [get_link(_C_FCRESEARCH_),
                                 get_link(_C_MOVEITEMS_),
                                 get_link(_C_FCART_),
                                 get_link(_C_PRINTMON_),
                                 get_link(_C_ICQATT_)])
            elif mode == "Pod Transfer":
                template_window("Have a kindle available if AFM or TDR trained; Make sure all audits match up!",
                                "LABOR TRACK CODES: OPSREG",
                                [get_link(_C_ADDPACKAGE_),
                                 get_link(_C_DOCKOB_),
                                 get_link(_C_YARDMANAGER_),
                                 get_link(_C_DOCKIB_),
                                 get_link(_C_PODRESEARCH_),
                                 get_link(_C_DOCKAUDITS_)])
            elif mode == "Induction":
                template_window("A kindle with MMA is required! Make sure you have pallet jacks with H-frames! Have everyone sign off on an escort sheet!",
                                "LABOR TRACK CODES: OPSREG, ICQAAD",
                                [get_link(_C_MOTHER_),
                                 get_link(_C_PODCONSOLE_),
                                 get_link(_C_PODRESEARCH_)])
            elif mode == "AFM Trainer":
                template_window("Labor track yourself and all students. Make sure you have a laptop, kindles, and your portfolio!\n",
                                "LABOR TRACK CODES: LNPITC",
                                [get_link(_C_KNET_),
                                 get_link(_C_ARU_),
                                 get_link(_C_HISTORYMANAGER_),
                                 get_link(_C_EMPLOYEESEARCH_),
                                 get_link(_C_FANS_),
                                 get_link(_C_FCCONSOLE_)])
            else:
                lay_2 = [[gui.Text(text="PLEASE ENTER A SELECTION!", text_color="red", background_color="white")],
                         [gui.Button(button_text="ERROR", image_data=_C_BUTTON_, button_color=("red", "white"))]]
                win = gui.Window(no_titlebar=True, title="", layout=lay_2, auto_size_buttons=True, auto_size_text=True, keep_on_top=True)
                window_input = win.read()
                if window_input:  # Any input will close this window
                    win.close()
                else:
                    pass
        elif button == "EXIT":  # The exit button closes the window and kills the running instance
            window.close()
            sys.exit()
        else:
            pass


fc_menu()
