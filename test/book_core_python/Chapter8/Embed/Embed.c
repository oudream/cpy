#include <Python.h>
int main()
{
	Py_Initialize();				/* Python��������ʼ�� */
	PyRun_SimpleString("print 'hi,python!'");	/* �����ַ��� */
	Py_Finalize();					/* ����Python���������ͷ���Դ */
	return 0;
}

