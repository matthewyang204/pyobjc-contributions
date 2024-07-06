#ifndef PyObjC_GIL_DISABLED
#define Py_LIMITED_API 0x03090000
#endif
#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include "pyobjc-api.h"

#import <CoreBluetooth/CoreBluetooth.h>

/* We include the source code here instead of
 * using the linker due to limitations in pyobjc-api.h
 */
#include "_CoreBluetooth_protocols.m"

static PyMethodDef mod_methods[] = {
    {0, 0, 0, 0} /* sentinel */
};

/* Python glue */
static struct PyModuleDef mod_module = {PyModuleDef_HEAD_INIT,
                                        "_CoreBluetooth",
                                        NULL,
                                        0,
                                        mod_methods,
                                        NULL,
                                        NULL,
                                        NULL,
                                        NULL};

PyObject* PyInit__CoreBluetooth(void);

PyObject* __attribute__((__visibility__("default"))) PyInit__CoreBluetooth(void)
{
    PyObject* m;
    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    if (PyObjC_ImportAPI(m) == -1)
        return NULL;

    return m;
}
