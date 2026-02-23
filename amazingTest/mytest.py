from mlx import Mlx
from typing import Generator


class ImgData:
    """Structure for image data"""

    def __init__(self):
        self.img = None
        self.width = 0
        self.height = 0
        self.data = None
        self.sl = 0  # size line
        self.bpp = 0  # bits per pixel
        self.iformat = 0


class MazeData:
    def __init__(
            self,
            grid: list[int],
            width: int,
            height: int,
            img_maze: ImgData):
        self.grid = grid
        self.width = width  # nb cell per line
        self.height = height  # nb cell per collumn
        # nb octet in width or height per cell
        self.cell_size = self.init_size(width, height, img_maze)
        # print(self.cell_size)
        self.set_color()

    @staticmethod
    def init_size(maze_w: int, maze_h: int, img_maze: ImgData):
         #print(maze_w, maze_h)
        if maze_w < maze_h:
            return (int(img_maze.width / maze_h))
        else:
            return (int(img_maze.width / maze_w))

    def set_color(self) -> None:
        self.color = self.new_color()

    @staticmethod
    def new_color() -> Generator[str, None, None]:
        while 1:
            yield "0xFFFFFFFF"
            yield "0xFFFFFF00"
            yield "0xFFFF00FF"


class XVar:
    """Structure for main vars"""

    def __init__(self):
        self.mlx: Mlx = None
        self.mlx_ptr = None
        self.screen_w = 0
        self.screen_h = 0
        self.win_1 = None
        self.img_maze: ImgData = ImgData()
        self.img_png: ImgData = ImgData()
        self.img_xpm: ImgData = ImgData()
        self.imgidx = 0


def gere_close_1(xvar):
    xvar.mlx.mlx_loop_exit(xvar.mlx_ptr)


def gere_close_2(xvar):
    xvar.mlx.mlx_destroy_window(xvar.mlx_ptr, xvar.win_2)
    xvar.win_2 = None


def gere_mouse(button, x, y, xvar, win):
    print(f"Got mouse : {button} at {x}x{y}")

    if button == 1:
        return 0

    if button == 3:  # right click
        gere_close_1(xvar)


def gere_mouse_1(button, x, y, xvar):
    gere_mouse(button, x, y, xvar, xvar.win_1)

# All draw


def draw_cell(
        start: int,
        value: int,
        size_cell: int,
        color: int,
        img_maze: ImgData):
    if value & 1 << 0:
        # 4 octets per pixel and img_maze.sl seems to be in octet per line
        # print(size_cell)
        for i in range(0, size_cell * 4, 4):
            pos = int(start + i)
            # print(pos)
            # img_maze.data[pos: pos + 4] = (color).to_bytes(4, 'little')
            # img_maze.data[pos: pos + 4] = (0xFFFFFF00).to_bytes(4, 'little')
            for k in range(4):
                img_maze.data[pos + k] = (0xFFFFFF00 >> 8 * k) & 0xFF
    if value & 1 << 1:
        new_start = start + (size_cell * 4)
        for i in range(size_cell):
            pos = new_start + (i * img_maze.sl)
            # img_maze.data[pos: pos + 4] = (color).to_bytes(4, 'little')
            # img_maze.data[pos: pos + 4] = (0xFFFFFF00).to_bytes(4, 'little')
            for k in range(4):
                img_maze.data[pos + k] = (0xFFFFFF00 >> 8 * k) & 0xFF
    if value & 1 << 2:
        new_start = start + (size_cell * img_maze.sl)
        for i in range(0, size_cell * 4, 4):
            pos = new_start + i
            # img_maze.data[pos: pos + 4] = (color).to_bytes(4, 'little')
            # img_maze.data[pos: pos + 4] = (0xFFFFFF00).to_bytes(4, 'little')
            for k in range(4):
                img_maze.data[pos + k] = (0xFFFFFF00 >> 8 * k) & 0xFF
    if value & 1 << 3:
        for i in range(size_cell * 4, 4):
            pos = start + (i * img_maze.sl)
            # img_maze.data[pos: pos + 4] = (0xFFFFFF00).to_bytes(4, 'little')
            for k in range(4):
                img_maze.data[pos + k] = (0xFFFFFF00 >> 8 * k) & 0xFF


def draw_all(maze_data: MazeData, img_maze: ImgData):
    for i, value in enumerate(maze_data.grid):
        # print(i)
        x = int(i % maze_data.width)
        y = int(i / maze_data.width)
        print(x, y)
        # print(xvar.img_maze.sl)
        # print(xvar.img_maze.sl)
        start = y * maze_data.cell_size * xvar.img_maze.sl + \
            ((x * maze_data.cell_size * xvar.img_maze.bpp) // 8)
        draw_cell(start, value, maze_data.cell_size, maze_data.color, img_maze)


if __name__ == "__main__":

    # try:
    xvar = XVar()
    xvar.mlx = Mlx()
    xvar.mlx_ptr = xvar.mlx.mlx_init()
    xvar.win_1 = xvar.mlx.mlx_new_window(
        xvar.mlx_ptr, 1200, 1200, "A-maze-ing")
    xvar.img_maze.img = xvar.mlx.mlx_new_image(xvar.mlx_ptr, 1200, 1200)
    xvar.img_maze.data, xvar.img_maze.bpp, xvar.img_maze.sl, xvar.img_maze.iformat = xvar.mlx.mlx_get_data_addr(
        xvar.img_maze.img)
    xvar.img_maze.width = 1200
    xvar.img_maze.height = 1200
    test = [
        13,
        5,
        3,
        9,
        5,
        5,
        3,
        9,
        5,
        5,
        5,
        5,
        3,
        13,
        5,
        1,
        7,
        9,
        1,
        3,
        9,
        7,
        12,
        6,
        9,
        7,
        12,
        6,
        9,
        3,
        9,
        3,
        12,
        5,
        3,
        12,
        5,
        6,
        10,
        10,
        10,
        9,
        5,
        5,
        4,
        1,
        7,
        9,
        6,
        12,
        6,
        8,
        1,
        7,
        10,
        9,
        5,
        5,
        6,
        10,
        8,
        6,
        9,
        3,
        11,
        12,
        5,
        6,
        15,
        15,
        15,
        14,
        8,
        3,
        12,
        6,
        9,
        5,
        7,
        10,
        12,
        5,
        6,
        12,
        2,
        13,
        3,
        15,
        15,
        15,
        15,
        15,
        14,
        10,
        9,
        3,
        8,
        5,
        5,
        6,
        11,
        9,
        3,
        9,
        6,
        9,
        2,
        11,
        15,
        15,
        15,
        9,
        5,
        2,
        10,
        12,
        6,
        13,
        1,
        3,
        10,
        10,
        12,
        6,
        13,
        2,
        10,
        10,
        15,
        15,
        15,
        8,
        3,
        14,
        10,
        9,
        3,
        9,
        6,
        14,
        10,
        12,
        5,
        5,
        5,
        6,
        12,
        2,
        15,
        15,
        15,
        10,
        12,
        3,
        12,
        6,
        10,
        10,
        9,
        3,
        8,
        7,
        9,
        1,
        3,
        9,
        5,
        6,
        15,
        15,
        15,
        12,
        3,
        8,
        5,
        7,
        10,
        8,
        6,
        10,
        8,
        5,
        6,
        10,
        14,
        8,
        7,
        15,
        15,
        15,
        15,
        15,
        14,
        12,
        3,
        9,
        6,
        10,
        11,
        10,
        8,
        7,
        9,
        2,
        9,
        6,
        15,
        15,
        15,
        15,
        15,
        15,
        15,
        9,
        2,
        12,
        3,
        8,
        6,
        10,
        10,
        9,
        6,
        10,
        10,
        13,
        3,
        15,
        15,
        11,
        15,
        15,
        9,
        6,
        12,
        3,
        10,
        14,
        9,
        2,
        14,
        10,
        9,
        6,
        10,
        9,
        2,
        9,
        3,
        12,
        1,
        3,
        10,
        9,
        3,
        10,
        12,
        3,
        10,
        10,
        9,
        6,
        12,
        7,
        10,
        10,
        10,
        10,
        12,
        5,
        6,
        10,
        10,
        10,
        10,
        12,
        7,
        10,
        10,
        10,
        12,
        5,
        5,
        5,
        4,
        6,
        12,
        6,
        13,
        5,
        5,
        6,
        12,
        6,
        12,
        5,
        5,
        4,
        6,
        14]
    truc = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15,15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15 ,15 ,15 ,15 ,15 ,15 ,15]
    width = 20
    height = 15
    maze_data = MazeData(test, width, height, xvar.img_maze)
    # print("test")
    draw_all(maze_data, xvar.img_maze)
    xvar.mlx.mlx_put_image_to_window(
        xvar.mlx_ptr, xvar.win_1, xvar.img_maze.img, 0, 0)

    # loop
    xvar.mlx.mlx_mouse_hook(xvar.win_1, gere_mouse_1, xvar)
    xvar.mlx.mlx_hook(xvar.win_1, 33, 0, gere_close_1, xvar)

    xvar.mlx.mlx_loop(xvar.mlx_ptr)
    # except Exception as e:
    #     print(f"{e}")
    # finally:
    #     xvar.mlx.mlx_destroy_window(xvar.mlx_ptr, xvar.win_1)
    #     xvar.mlx.mlx_release(xvar.mlx_ptr)
