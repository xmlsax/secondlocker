#include <signal.h>
#include "Python.h"
typedef PyObject* object;
static object *pyabort (object self, object args)
{
    abort();
}
static PyMethodDef methods[]=
{
    {"abort", pyabort, METH_VARARGS, ""}, 
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef mod=
{
    PyModuleDef_HEAD_INIT, 
    "abort", 
    "", 
    -1, 
    methods
};
PyMODINIT_FUNC PyInit_abort(void)
{
    return PyModule_Create(&mod);
}
