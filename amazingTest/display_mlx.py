import mlx

if __name__ == "__main__":
    ptrmlx = mlx.Mlx().mlx_get_data_addr()
    ptrwin = mlx.Mlx().mlx_new_window(ptrmlx, 600, 300, "test")
    test = input()
    ptrmlx.mlx_destroy_window(ptrmlx, ptrwin)