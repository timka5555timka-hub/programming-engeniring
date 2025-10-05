def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(x1=[2, 3], y3=[3, 2], z0=[2, 0], q=[3, 0], w=[3, 0])
    print()
    main(**{'x': [1, 2, 3], 'y': [3, 3, 0]})
