import contextlib


if __name__ == '__main__':
    
    num = 3

    with contextlib.ExitStack() as s:
        names = [f"file{i}.txt" for i in range(num)]
        files = [s.enter_context(open(name, "w")) for name in names]
        for file in files:
            file.write("Hello World")
            