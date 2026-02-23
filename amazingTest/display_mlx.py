from mlx import Mlx


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


class CellData:
    size: int = 0

    def __init__(self, pos: int, value: int):
        self.pos = pos
        self.value = value

    @classmethod
    def init_size(cls, maze_h: int, n_cell: int):
        cls.size = int(maze_h / n_cell)


class XVar:
    """Structure for main vars"""

    def __init__(self):
        self.mlx: Mlx = None
        self.mlx_ptr = None
        self.screen_w = 0
        self.screen_h = 0
        self.win_1 = None
        self.win_2 = None
        self.img_1: ImgData = ImgData()
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
        # xvar.mlx.mlx_put_image_to_window(
        #     xvar.mlx_ptr, win, xvar.img_1.img, 100, 100)
        return 0

    if button == 3:  # right click
        # if xvar.imgidx % 2:
        #     xvar.mlx.mlx_put_image_to_window(
        #         xvar.mlx_ptr, win, xvar.img_png.img, x, y)
        # else:
        #     xvar.mlx.mlx_put_image_to_window(
        #         xvar.mlx_ptr, win, xvar.img_xpm.img, x, y)
        # xvar.imgidx += 1
        gere_close_1(xvar)


def gere_mouse_1(button, x, y, xvar):
    gere_mouse(button, x, y, xvar, xvar.win_1)


def put_pixel(x: int, y: int, img: ImgData, color: int):
    pos = y * img.sl + x * (img.bpp / 8)
    img.data[pos: pos + 4] = color.to_bytes(4, 'little')


def draw_all(cell_x, cell_y, value, img):
    size = CellData.size
    color = 0xFFFFFFFF  # blanc

    start_x = cell_x
    start_y = cell_y

    end_x = start_x + size
    end_y = start_y + size

    # north
    if value & (1 << 0):
        for x in range(start_x, end_x):
            put_pixel(img, x, start_y, color)

    # east
    if value & (1 << 1):
        for y in range(start_y, end_y):
            put_pixel(img, end_x - 1, y, color)

    # south
    if value & (1 << 2):
        for x in range(start_x, end_x):
            put_pixel(img, x, end_y - 1, color)

    # west
    if value & (1 << 3):
        for y in range(start_y, end_y):
            put_pixel(img, start_x, y, color)


if __name__ == "__main__":

    try:
        xvar = XVar()
        xvar.mlx = Mlx()
        xvar.mlx_ptr = xvar.mlx.mlx_init()
        xvar.win_1 = xvar.mlx.mlx_new_window(xvar.mlx_ptr, 1400, 1400, "Main")
        xvar.img_maze.width = 1200
        xvar.img_maze.height = 1200
        xvar.img_maze.img = xvar.mlx.mlx_new_image(
            xvar.mlx_ptr, xvar.img_maze.width, xvar.img_maze.height)
        for i in range(0, xvar.img_1.sl * 1200, 1):
            xvar.img_1.data[i] = 0x80
        xvar.img_maze.data, xvar.img_maze.bpp, xvar.img_maze.sl, xvar.img_maze.iformat = xvar.mlx.mlx_get_data_addr(
            xvar.img_maze.img)
        for j, line in enumerate(maze_test):
            for i, value in enumerate(line):
                x = i * CellData.size
                y = j * CellData.size
                pos = y * xvar.img_maze.sl + x * (xvar.img_maze.bpp / 8)
                case: CellData = CellData(pos, value)
                # draw_all(case, xvar.img_maze)
                # Draw def draw_all(cell_x, cell_y, value, img):

        origin_x = 100
        origin_y = 10
        xvar.mlx.mlx_put_image_to_window(
            xvar.mlx_ptr,
            xvar.win_1,
            xvar.img_maze.img,
            origin_x,
            origin_y)
    except Exception as e:
        print(f"{e}")
