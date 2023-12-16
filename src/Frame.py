class Frame(object):
    """
    The frame is a collection of attributes with no methods. 
    One frame object exists for each active function call.
    A frame includes a code object; the local, global, and built-in namespaces;
    a reference to the previous frame (if any); and a data stack; a block stack; and 
    the last instruction executed by the frame.
    """
    def __init__(self, code_obj, global_names, local_names, prev_frame) -> None:
        self.code_obj = code_obj
        self.global_names = global_names
        self.local_names = local_names
        self.prev_frame = prev_frame
        self.stack = []
        if prev_frame:
            self.builtin_names = prev_frame.builtin_names
        else:
            self.builtin_names = local_names['__builtins__']
            if hasattr(self.builtin_names, '__dict__'):
                self.builtin_names = self.builtin_names.__dict__
        
        self.last_instruction = 0
        self.block_stack = []

class Function(object):
    __slots__ = [
        'func_code', 'func_name', 'func_defaults', 'func_globals',
        'func_locals', 'func_dict', 'func_closure',
        '__name__', '__dict__', '__doc__',
        '_vm', '_func',
    ]

    def __init__(self) -> None:
        pass