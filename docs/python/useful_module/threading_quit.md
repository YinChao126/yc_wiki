# SafetyThreadingQuit

说明：该模块用于安全结束子线程

```
# -*- coding: utf-8 -*-
"""
@copyright(c) 2019 Shenzhen Skycaster Microelectronic Co. Ltd.
@Created on Thu Feb 21 15:48:54 2019
@author: yinchao
@description: rabbit mq client, both of them are topic mode.
"""
import inspect
import ctypes


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    """
    safely stop thread
    """
    _async_raise(thread.ident, SystemExit)

```

