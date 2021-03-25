def fix_indentation(_code):
    """
    Fixes indentation by converting each change in indentation in the code to pep8 standard of 4 spaces. Works out what
    is a positive or negative indentation by comparing the indentation to the previous line (but ignoring blank lines
    to preserve any separation the user has added).
    :param _code: List containing each line of the input code.
    :return: List containing each line of the resultant code (with correct indents)
    """

    result = []

    indentation_level = 0
    indent_pointer = 0
    current_pointer = 0

    while current_pointer < len(_code):
        line = _code[current_pointer]

        if line.strip() == '' or line.strip().startswith('#'):
            result.append(line)  # adds the blank line but ignores it in terms of indentation
        else:
            prev_indent_len = len(_code[indent_pointer]) - len(_code[indent_pointer].lstrip())
            curr_indent_len = len(_code[current_pointer]) - len(_code[current_pointer].lstrip())

            if prev_indent_len > curr_indent_len:
                indentation_level -= 1
            elif prev_indent_len < curr_indent_len:
                indentation_level += 1

            indent_pointer = current_pointer

            result.append(f'{" " * 4 * indentation_level}{line.strip()}')

        current_pointer += 1

    return result
