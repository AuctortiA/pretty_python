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