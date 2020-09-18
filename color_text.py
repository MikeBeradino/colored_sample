from colored import fg, bg, attr
import colored
from colored import stylize

color = fg('#C0C0C0') + bg('#00005f')
res = attr('reset')
print (color + "Hello World !!!" + res)

print (color + "|\---/|" + res)
print (color + "| o_o |" + res)
print (color + " \_^_/" + res)





angry = colored.fg("red") + colored.attr("bold")
print(stylize("This is VERY angry text.", angry, colored.attr("underlined")))