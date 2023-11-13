def calculate_code_effectiveness(num_bugs, num_lines):
    """
    Calculate code effectiveness based on number of bugs and lines of code.

    Effectiveness is defined as:
    Fewer bugs per line of code indicates more effective code.

    Args:
      num_bugs (int): Total number of bugs in the code.
      num_lines (int): Total number of lines of code.

    Returns:
      float: Code effectiveness score. Higher is better.
    """

    if num_lines == 0:
        return 0

    effectiveness = 1 - (num_bugs / num_lines)

    return effectiveness


num_bugs_str = int(input('Enter the bugs quantity: '))
num_bugs = int(num_bugs_str)

num_lines_str = int(input('Enter the code lines quantity: '))
num_lines = int(num_lines_str)

print(calculate_code_effectiveness(num_bugs, num_lines))