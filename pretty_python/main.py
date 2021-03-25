import re
import os

from .fix_blanklines import fix_blanklines
from .fix_comments import fix_comments
from .fix_func_names import fix_func_names
from .fix_indentation import fix_indentation


if __name__ == '__main__':
    # mainloop
    with open(os.path.join("data", "before_code.txt"), 'r') as f:
        code = f.read().splitlines()

    with open(os.path.join("data", "result.txt"), 'w') as f:
        code = fix_blanklines(code)
        code = fix_comments(code)
        code = fix_func_names(code)
        code = fix_indentation(code)

        f.write('\n'.join(code))
