import time


def spin():
    for _ in range(100):
        for ch in '-\\|/':
            print(ch, end='', flush=True)
            time.sleep(0.1)
            print('\b', end='', flush=True)


if __name__ == '__main__':
    spin()
