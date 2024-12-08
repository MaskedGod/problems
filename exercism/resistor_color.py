# def colors():
#     clrs = [
#         "black",
#         "brown",
#         "red",
#         "orange",
#         "yellow",
#         "green",
#         "blue",
#         "violet",
#         "grey",
#         "white",
#     ]
#     return clrs


def color_code(color):
    clrs = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    return clrs[color[0]] + clrs[color[1]]


def value(colors):
    clrs = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    res = int(str(clrs.index(colors[0])) + str(clrs.index(colors[1])))
    return res


def label(colors):
    """
    giga 1000000000
    mega 1000000
    kilo 1000
    """
    clrs = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    multiplier = clrs.index(colors[2])
    decoded = int(
        str(clrs.index(colors[0])) + str(clrs.index(colors[1])) + ("0" * multiplier)
    )
    if multiplier == 9:
        decoded = str(decoded // 10**9) + " gigaohms"
    elif multiplier >= 5:
        decoded = str(decoded // 10**6) + " megaohms"
    elif multiplier >= 2:
        decoded = str(decoded // 10**3) + " kiloohms"
    else:
        decoded = str(decoded) + " ohms"
    return decoded


# print(label(["orange", "orange", "black"]))  # "33 ohms"
# print(label(["blue", "grey", "brown"]))  # "680 ohms"
# print(label(["red", "black", "red"]))  # "2 kiloohms"
# print(label(["yellow", "violet", "yellow"]))  # "470 kiloohms"
# print(label(["yellow", "violet", "green"]))  # "4 megaoms"
# print(label(["blue", "violet", "blue"]))  # "67 megaohms"
# print(label(["white", "white", "white"]))  # "99 gigaohms"


# def resistor_label(colors):
#     if len(colors) == 1 and colors[0] == "black":
#         return "0 ohms"
#     clrs = [
#         "black",
#         "brown",
#         "red",
#         "orange",
#         "yellow",
#         "green",
#         "blue",
#         "violet",
#         "grey",
#         "white",
#     ]
#     tlrnc_colors = ["grey", "violet", "blue", "green", "brown", "red", "gold", "silver"]
#     tlrnc_percentage = [
#         "±0.05%",
#         "±0.1%",
#         "±0.25%",
#         "±0.5%",
#         "±1%",
#         "±2%",
#         "±5%",
#         "±10%",
#     ]

#     boundary = 3 if len(colors) == 5 else 2
#     tolerance = tlrnc_percentage[tlrnc_colors.index(colors[-1])]
#     multiplier = clrs.index(colors[-2])
#     decoded = int(
#         "".join([str(clrs.index(color)) for color in colors[:boundary]])
#         + ("0" * multiplier)
#     )

#     if multiplier >= 8:
#         decoded = str(decoded / 10**9) + " gigaohms" + f" {tolerance}"
#     elif multiplier >= 4:
#         decoded = str(decoded / 10**6) + " megaohms" + f" {tolerance}"
#     elif multiplier >= 1:
#         decoded = f"{decoded / 10**3}" + " kiloohms" + f" {tolerance}"
#     else:
#         decoded = str(decoded) + " ohms" + f" {tolerance}"


#     return decoded
def resistor_label(colors):
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    clrs = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]
    tlrnc_colors = ["grey", "violet", "blue", "green", "brown", "red", "gold", "silver"]
    tlrnc_percentage = [
        "±0.05%",
        "±0.1%",
        "±0.25%",
        "±0.5%",
        "±1%",
        "±2%",
        "±5%",
        "±10%",
    ]

    boundary = 3 if len(colors) == 5 else 2
    tolerance = tlrnc_percentage[tlrnc_colors.index(colors[-1])]
    multiplier = 10 ** clrs.index(colors[-2])
    decoded = int("".join([str(clrs.index(color)) for color in colors[:boundary]]))
    resistance_value = decoded * multiplier

    if resistance_value >= 10**9:
        result = f"{resistance_value / 10**9} gigaohms {tolerance}"
    elif resistance_value >= 10**6:
        result = f"{resistance_value / 10**6} megaohms {tolerance}"
    elif resistance_value >= 10**3:
        result = f"{resistance_value / 10**3} kiloohms {tolerance}"
    else:
        result = f"{resistance_value} ohms {tolerance}"
    result = result.replace(".0 ", " ")
    return result


print(resistor_label(["orange", "orange", "black", "green"]))  # "33 ohms ±0.5%"
print(resistor_label(["orange", "orange", "orange", "grey"]))  # "33 kiloohms ±0.05%"
print(resistor_label(["orange", "orange", "blue", "red"]))  # "33 megaohms ±2%"
print(
    resistor_label(["orange", "orange", "orange", "black", "green"])
)  # "333 ohms ±0.5%"
print(
    resistor_label(["orange", "red", "orange", "blue", "violet"])
)  # "323 megaohms ±0.1%"

print(resistor_label(["orange", "orange", "yellow", "black", "brown"]))  # 334 ohms ±1%
print(resistor_label(["blue", "grey", "brown", "violet"]))  # "680 ohms ±0.1%"
print(
    resistor_label(["blue", "grey", "white", "brown", "brown"])
)  # "6.89 kiloohms ±1%"
print(
    resistor_label(["red", "green", "yellow", "yellow", "brown"])
)  # , "2.54 megaohms ±1%"
print(resistor_label(["red", "black", "red", "green"]))  # "2 kiloohms ±0.5%"
print(resistor_label(["green", "brown", "orange", "grey"]))  # "51 kiloohms ±0.05%"
print(resistor_label(["violet", "orange", "red", "grey"]))  # "7.3 kiloohms ±0.05%"
print(
    resistor_label(["brown", "red", "orange", "green", "blue"])
)  # "12.3 megaohms ±0.25%"
