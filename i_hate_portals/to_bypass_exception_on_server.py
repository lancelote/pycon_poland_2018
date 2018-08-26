# Run line by line on the server
exec("import pdb; pdb.run('Challenge().second_level()')")
from types import CodeType
def fix_function(func, payload):fn_code = func.__code__;func.__code__ = CodeType(fn_code.co_argcount,fn_code.co_kwonlyargcount,fn_code.co_nlocals,fn_code.co_stacksize,fn_code.co_flags,payload,fn_code.co_consts,fn_code.co_names,fn_code.co_varnames,fn_code.co_filename,fn_code.co_name,fn_code.co_firstlineno,fn_code.co_lnotab,fn_code.co_freevars,fn_code.co_cellvars,)
ch = Challenge.second_level;fix_function(ch, b't\x00\x00t\x01\x00d\x01\x00d\x02\x00\x84\x00\x00}\x01\x00d\x03\x00d\x04\x00\x84\x00\x00}\x02\x00d\x05\x00d\x06\x00\x84\x00\x00}\x03\x00d\x07\x00d\x08\x00\x84\x00\x00}\x04\x00d\t\x00d\n\x00\x84\x00\x00}\x05\x00t\x02\x00S');ch(Challenge())