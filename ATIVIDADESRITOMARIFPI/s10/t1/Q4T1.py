def main():
    for i in range(10,1001,10):
        if i == 1000:
            print(f'{i}.')
        else:
            print(f'{i}', end=', ')

if __name__ == '__main__':
    main()