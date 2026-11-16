from utils import pad


def render_row(cells, width):
    return " ".join(pad(str(cell), width) for cell in cells)
