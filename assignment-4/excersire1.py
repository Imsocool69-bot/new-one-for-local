import re
def validate_course_code(code: str) -> bool:
    pattern = r"^[A-Z]{3}\d{3}$"
    return bool(re.match(pattern, code))
code = input("Enter your course (EG: TEC001): ")
result = validate_course_code(code)
print("result: ", result)