import colored
from colored import stylize
print(stylize("This is green.", colored.fg("yellow")))
print("This is not.")
angry = colored.fg("red") + colored.attr("bold")
print(stylize("This is angry text.", angry))
print(stylize("This is VERY angry text.", angry, colored.attr("underlined")))
print("But this is not.")