def main():
    print('Hello world from Python!')

    import myapp.cython_module
    myapp.cython_module.do_something_in_cython()


if __name__ == '__main__':
    main()
