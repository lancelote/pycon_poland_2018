from types import CodeType


class Challenge:
    # noinspection PyMethodMayBeStatic
    def second_level(self):
        raise Exception()
        # noinspection PyUnreachableCode
        print('hello world')


def patch_function(func, payload):
    """Replace function byte code."""
    fn_code = func.__code__
    func.__code__ = CodeType(
        fn_code.co_argcount,
        fn_code.co_kwonlyargcount,
        fn_code.co_nlocals,
        fn_code.co_stacksize,
        fn_code.co_flags,
        payload,
        fn_code.co_consts,
        fn_code.co_names,
        fn_code.co_varnames,
        fn_code.co_filename,
        fn_code.co_name,
        fn_code.co_firstlineno,
        fn_code.co_lnotab,
        fn_code.co_freevars,
        fn_code.co_cellvars,
    )


def main():
    ch = Challenge.second_level
    # Original byte code:
    #   t\x00\x83\x00\x82\x01t\x01d\x01\x83\x01\x01\x00d\x00S\x00
    #
    # Raise part:
    #   \x01t\x01d\x01\x83
    #
    # Without raise:
    #   t\x01t\x01d\x01\x83\x01\x01\x00d\x00S\x00
    payload = b't\x01t\x01d\x01\x83\x01\x01\x00d\x00S\x00'
    patch_function(ch, payload)
    ch(Challenge())


if __name__ == '__main__':
    main()
