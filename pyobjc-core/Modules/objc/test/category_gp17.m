
/*
 *     *** GENERATED FILE ***
 *
 * This file is generated by Tools/generate-category-tests.py
 */
#include "Python.h"
#include "pyobjc-api.h"

#import <Foundation/Foundation.h>
__attribute__((__visibility__("default")))
@interface OC_Category_GP17 : NSObject {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_P17 : OC_Category_GP17 {
}
@end

__attribute__((__visibility__("default")))
@interface OC_Category_C17 : OC_Category_P17 {
}
@end

@implementation
OC_Category_GP17 (Cat)
- (id)gpMethod1
{
    return @"GP17 - gpMethod1 - GP17(Cat)";
}
- (id)gpMethod5
{
    return @"GP17 - gpMethod5 - GP17(Cat)";
}
- (id)pMethod1
{
    return @"GP17 - pMethod1 - GP17(Cat)";
}
- (id)pMethod3
{
    return @"GP17 - pMethod3 - GP17(Cat)";
}
- (id)method1
{
    return @"GP17 - method1 - GP17(Cat)";
}
- (id)method2
{
    return @"GP17 - method2 - GP17(Cat)";
}
@end

static PyMethodDef mod_methods[] = {{0, 0, 0, 0}};

static struct PyModuleDef mod_module = {
    PyModuleDef_HEAD_INIT, "category_gp17", NULL, 0, mod_methods, NULL, NULL, NULL, NULL};

PyObject* PyInit_category_gp17(void);

PyObject* __attribute__((__visibility__("default"))) PyInit_category_gp17(void)
{
    PyObject* m;

    m = PyModule_Create(&mod_module);
    if (!m) {
        return NULL;
    }

    PyObjC_ImportAPI(m);

    return m;
}