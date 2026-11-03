import re
def validate_hex_color(color: str) -> bool:
    pattern = r"^#[0-9A-Fa-f]{6}$"
    return bool(re.match(pattern, color))
color = input("enter your HEX color code(eg: #FF5733): ")
result = validate_hex_color(color)
print(result)