#include <python.h>
#include <windows.h>
/* ����C��չ�еĺ��� */
PyObject *show(PyObject *self, PyObject *args)
{
	char *message;
	const char *title = NULL;
	HWND hwnd = NULL;
	int r;
	/* ʹ��PyArg_ParseTuple������� */
	if (!PyArg_ParseTuple(args, "iss", &hwnd, &message, &title))
		return NULL;
	r = MessageBox(hwnd,message, title, MB_OK);
	return Py_BuildValue("i", r);
}
/* ģ��ķ����б� */
static PyMethodDef myextMethods[] = 
{
	{"show", show, METH_VARARGS,"show a messagebox"},
	{NULL,NULL}
};
/* ģ��ĳ�ʼ������ */
PyMODINIT_FUNC initmyext()
{
	PyObject *mod;
	/* ʹ��Py_InitModule��ʼ��ģ��*/
	mod = Py_InitModule("myext",myextMethods);
}
