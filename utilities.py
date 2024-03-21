BAR_NUMBER = 50
CHAR = "-"

def title(text):
    side_bar = (BAR_NUMBER // 2) - (len(text) // 2)
    print((CHAR * side_bar) + text + (CHAR * side_bar))


def simple_bar():
    print(CHAR * BAR_NUMBER)


def sort_list(list):
    sorted_list = sorted(list)

    return sorted_list