/*
 * This file is generated by objective.metadata
 *
 * Last update: Tue May 26 22:15:29 2015
 */

static void __attribute__((__used__)) use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1010
    p = PyObjC_IdToPython(@protocol(SKPhysicsContactDelegate)); Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(SKSceneDelegate)); Py_XDECREF(p);
#endif /* defined(__LP64__) && PyObjC_BUILD_RELEASE >= 1010 */
}