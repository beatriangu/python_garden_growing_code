def ft_count_harvest_recursive(n):
    if n <= 0:
        return
    ft_count_harvest_recursive(n - 1)
    print(n)
