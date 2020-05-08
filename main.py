import re


# indentation
def fix_indentation(_code):
    """
    Fixes indentation by converting each change in indentation in the code to pep8 standard of 4 spaces. Works out what
    is a postive or negative indentation by comparing the indentation to the previous line (but ignoring blank lines
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


def fix_comments(_code):
    pass


def fix_blanklines(_code):
    """

    :param _code:
    :return:
    """

    # first limit all blanklines to 1
    current_pointer = 0
    remove_line = False
    while current_pointer < len(_code):
        line = _code[current_pointer]
        if line == '':
            if remove_line:
                _code.pop(current_pointer)
                current_pointer -= 1
            else:
                remove_line = True
        else:
            remove_line = False

        current_pointer += 1

    current_pointer = 0
    while current_pointer < len(_code):  # make this ignore comments (probably in a similar way to how we did it with the indentation.
        line = _code[current_pointer]

        if current_pointer != 0:
            if line.lstrip().startswith(('class', 'def')):
                # Only adds double spacing to first level
                if _code[current_pointer-1] != '':
                    _code.insert(current_pointer, '')
                    current_pointer += 1
                if len(line) == len(line.lstrip()):
                    _code.insert(current_pointer, '')
                    current_pointer += 1

        current_pointer += 1
    return _code


def fix_func_names(_code):
    """

    :param _code:
    :return:
    """

    for index, line in enumerate(_code):
        if line.strip().startswith('def'):
            indentation, func_name = line.split('def ')

            func_name = list(func_name)
            func_name[0] = func_name[0].lower()

            current_pointer = 1
            while current_pointer < len(func_name[1:]):
                letter = func_name[current_pointer]
                if letter.isupper():
                    func_name.pop(current_pointer)

                    if func_name[current_pointer-1] == '_':
                        new_func_name = f'{letter.lower()}'
                    else:
                        new_func_name = f'_{letter.lower()}'

                    func_name.insert(current_pointer, new_func_name)

                current_pointer += 1

            _code[index] = f'{indentation}def {"".join(func_name)}'

    return _code


if __name__ == '__main__':
    # mainloop
    with open("func_names_test.txt", 'r') as f:
        code = f.read().splitlines()

    with open("result.txt", 'w') as f:
        f.write('\n'.join(fix_func_names(code)))
