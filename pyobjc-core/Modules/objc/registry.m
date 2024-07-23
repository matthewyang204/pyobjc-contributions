/*
 * registry.m -- Storing and finding exception data.
 *
 * This file defines generic functionality to store exception data for
 * a class/method.
 */
#include "pyobjc.h"

NS_ASSUME_NONNULL_BEGIN

BOOL PyObjC_UpdatingMetaData = NO;

PyObject* _Nullable PyObjC_NewRegistry(void) { return PyDict_New(); }

int
PyObjC_AddToRegistry(PyObject* registry, PyObject* class_name, PyObject* selector,
                     PyObject* value)
{
    int       result;
    PyObject* sublist;

    PyObjC_Assert(PyBytes_Check(class_name), -1);
    PyObjC_Assert(PyBytes_Check(selector), -1);

    switch(PyDict_GetItemRef(registry, selector, &sublist)) {
    case  -1:
        return -1;
    case 0:
        sublist = PyList_New(0);
        if (sublist == NULL) { // LCOV_BR_EXCL_LINE
            return -1;         // LCOV_EXCL_LINE
        }
        result = PyDict_SetItem(registry, selector, sublist);
        if (result == -1) { // LCOV_BR_EXCL_LINE
            return -1;      // LCOV_EXCL_LINE
        }
    /* default: fallthrough */
    }

    if (!PyObjC_UpdatingMetaData) {
        PyObjC_MappingCount += 1;
    }

    /*
     * Check if there is a registration for *class_name* in
     * *sublist*, if so replace that registration.
     */
    Py_ssize_t len = PyList_Size(sublist);
    for (Py_ssize_t i = 0; i < len; i++) {
        PyObject* item = PyList_GetItemRef(sublist, i);
        if (item == NULL) {
            Py_DECREF(sublist);
            return -1;
        }

        PyObjC_Assert(PyTuple_CheckExact(item), -1);
        PyObjC_Assert(PyTuple_GET_SIZE(item) == 2, -1);

        int r = PyObject_RichCompareBool(PyTuple_GET_ITEM(item, 0), class_name, Py_EQ);
        if (r == -1) {  // LCOV_BR_EXCL_LINE
            Py_DECREF(item); // LCOV_EXCL_LINE
            Py_DECREF(sublist); // LCOV_EXCL_LINE
            return -1; // LCOV_EXCL_LINE
        }
        if (r) {
            Py_DECREF(PyTuple_GET_ITEM(item, 1));
            PyTuple_SET_ITEM(item, 1, value);
            Py_INCREF(value);
            Py_DECREF(item);
            Py_DECREF(sublist);
            return 0;
        }
    }

    PyObject* item = Py_BuildValue("(OO)", class_name, value);
    if (item == NULL) { // LCOV_BR_EXCL_LINE
        Py_DECREF(sublist); // LCOV_EXCL_LINE
        return -1;      // LCOV_EXCL_LINE
    }
    result = PyList_Append(sublist, item);
    Py_DECREF(item);
    Py_DECREF(sublist);
    return result;
}

PyObject* _Nullable PyObjC_FindInRegistry(PyObject* registry, Class cls, SEL selector)
{
    Py_ssize_t i;
    Py_ssize_t len;
    PyObject*  cur;
    Class      found_class = nil;
    PyObject*  found_value = NULL;
    PyObject*  sublist;

    if (registry == NULL) {
        return NULL;
    }

    PyObject* k = PyBytes_FromString(sel_getName(selector));

    switch (PyDict_GetItemRef(registry, k, &sublist)) {
    case -1:
        Py_DECREF(k);
        return NULL;
    case 0: // XXX: differentiate from error case.
        Py_DECREF(k);
        return NULL;

    /* default: fallthrough */
    }

    len = PyList_Size(sublist);
    for (i = 0; i < len; i++) {
        Class cur_class;

        cur = PyList_GetItemRef(sublist, i);
        PyObjC_Assert(cur != NULL, NULL);
        PyObjC_Assert(PyTuple_CheckExact(cur), NULL);

        PyObject* nm = PyTuple_GET_ITEM(cur, 0);
        PyObjC_Assert(PyBytes_Check(nm), NULL);

        cur_class = objc_lookUpClass(PyBytes_AsString(nm));

        if (cur_class == nil) {
            Py_DECREF(cur);
            continue;
        }

        if (!PyObjC_class_isSubclassOf(cls, cur_class)
            && !PyObjC_class_isSubclassOf(cls,
                                          (Class _Nonnull)object_getClass(cur_class))) {
            Py_DECREF(cur);
            continue;
        }

        if (found_class != NULL && found_class != cur_class) {
            if (PyObjC_class_isSubclassOf(found_class, cur_class)) {
                Py_DECREF(cur);
                continue;
            }
        }

        found_class = cur_class;
        Py_INCREF(PyTuple_GET_ITEM(cur, 1));
        Py_XDECREF(found_value);
        found_value = PyTuple_GET_ITEM(cur, 1);
        Py_DECREF(cur);
    }
    Py_DECREF(sublist);
    return found_value;
}

PyObject* _Nullable PyObjC_CopyRegistry(PyObject*            registry,
                                        PyObjC_ItemTransform value_transform)
{
    PyObject* result = PyDict_New();
    if (result == NULL) { // LCOV_BR_EXCL_LINE
        return NULL;      // LCOV_EXCL_LINE
    }
    PyObject*  key;
    PyObject*  sublist;
    Py_ssize_t pos = 0;

    while (PyDict_Next(registry, &pos, &key, &sublist)) {
        Py_ssize_t i, len;
        PyObject*  sl_new;

#ifdef PyObjC_DEBUG
        if (!PyList_CheckExact(sublist)) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            PyErr_SetString(PyObjCExc_InternalError, "sublist of registry is not a list");
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
#endif

        len    = PyList_Size(sublist);
        sl_new = PyList_New(0);
        if (sl_new == NULL) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        if (PyDict_SetItem(result, key, sl_new) == -1) { // LCOV_BR_EXCL_LINE
            // LCOV_EXCL_START
            Py_DECREF(sl_new);
            Py_DECREF(result);
            return NULL;
            // LCOV_EXCL_STOP
        }
        Py_DECREF(sl_new);

        for (i = 0; i < len; i++) {
            PyObject* item;
            PyObject* new_item;

            item     = PyList_GetItemRef(sublist, i);
            if (item == NULL) {
                Py_DECREF(result);
                return NULL;
            }
            new_item = Py_BuildValue("(ON)", PyTuple_GET_ITEM(item, 0),
                                     value_transform(PyTuple_GET_ITEM(item, 1)));
            Py_DECREF(item);
            if (new_item == NULL) { // LCOV_BR_EXCL_LINE
                // LCOV_EXCL_START
                Py_DECREF(result);
                return NULL;
                // LCOV_EXCL_STOP
            }

            if (PyList_Append(sl_new, new_item) < 0) {
                Py_DECREF(new_item);
                Py_DECREF(result);
                return NULL;
            }
            Py_DECREF(new_item);
        }
    }

    return result;
}

NS_ASSUME_NONNULL_END
