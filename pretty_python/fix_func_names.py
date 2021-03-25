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
            while current_pointer < len(func_name[1:]):  # this needs to refactor once it changes something rip
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