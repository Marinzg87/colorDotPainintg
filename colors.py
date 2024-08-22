import colorgram
#
colors = colorgram.extract("image.jpeg", 10)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

"""
Color set has been produced based on the Hirst spot image, the background 
colors have been deleted from the set.
"""

color_set = [
    (12, 24, 232), (40, 29, 235), (230, 238, 233), (228, 233, 238),
    (235, 38, 116), (215, 164, 59), (142, 27, 69), (237, 71, 36),
    (12, 142, 89), (179, 160, 47)
]
