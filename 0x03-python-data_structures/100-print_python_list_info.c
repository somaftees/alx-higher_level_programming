#include <Python.h>

/**
  * print_python_list_info- a function that prints
  * some basic info about Python lists.
  * @p: PyObject ptr.
  * Return: void.
  */

void print_python_list_info(PyObject *p)
{
	int i, s, a;
	PyObject *o;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (i = 0; i < s; i++)
	{
		printf("Element %d: ", i);

		o = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
