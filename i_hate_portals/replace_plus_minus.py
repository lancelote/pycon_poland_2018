from types import CodeType
import dis


def wadd(x, y=1):
    pow_n = 3
    result = (x + y) ** pow_n
    return abs(result)


def patch_function(func, payload):
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
    payload = wadd.__code__.co_code
    minus_opcode = dis.opmap['BINARY_SUBTRACT'].to_bytes(1, byteorder='little')
    payload = payload[0:12] + minus_opcode + payload[13:]

    print(wadd(3, 1))
    patch_function(wadd, payload)
    print(wadd(3, 1))


if __name__ == '__main__':
    main()
