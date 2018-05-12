#include <Python/Python.h>

int fact(int n){
	if (n <= 1) return 1;
	else return n * fact(n - 1);
}

PyObject* wrap_fact(PyObject* self, PyObject* args){
	int n, reslut;
	if(!PyArg_Parse(args, "i:fact", &n)) return NULL;
	reslut = fact(n);
	return Py_BuildValue("i", reslut);
}

static PyMethodDef exampleMethods[] =
{
	{"fact", wrap_fact, METH_VARARGS, "Caculate N!"},
	{NULL, NULL}
};


void initexample()
{
	PyObject* m;
	m = Py_InitModule("example", exampleMethods);
}
