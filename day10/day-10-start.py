# Functions with Outputs

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    format_f_name = f_name.title()
    format_l_name = l_name.title()
    return f'{format_f_name} {format_l_name}'


formated_name = format_name(input("What is your first name? "), input("What is your last name? "))

# Already used function with outputs.s
length = len(formated_name)
