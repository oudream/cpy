#include <string.h>
#include <iostream.h>
#include <boost/python.hpp>
#include <Python.h>
// ���߱��������ӵ�boost_python.lib��
#pragma comment(lib, "boost_python.lib")
using namespace std;	
using namespace boost::python;
int main(int argc, char* argv[])
{
	int size, i;
	list mylist, rel;
	handle<> module;
	char *funcname1 = "sum";
	char *funcname2 = "strsplit";
	cout << "-==ʹ��Boost.Python��C++��Ƕ��Python==-" << endl;
	// Python��������ʼ��
	Py_Initialize();
	if(!Py_IsInitialized())   
	{   
		cout <<"��ʼ��ʧ��!"<< endl;
		return -1;   
	}
	// ����Pythonģ��
	module = handle<> (PyImport_ImportModule("pytest"));
	cout << "ʹ��Python�е�sum�������������֮�ͣ�" << endl;
	for(i = 1; i < 6; i++ )
	{
		cout << i << "\t";
		mylist.append(i);
	}
	cout << endl;
	// ����Python�е�sum����
	call_method<void>(module.get(), funcname1, mylist);
	cout << "ʹ��Python�еĺ����ָ������ַ���:" << endl;
	cout << "this is an example" << endl;
	// ����Python�е�strsplit��������÷���ֵ
	rel = call_method<list>(module.get(), funcname2, "this is an example", " ");
	// �������ֵ
	size = call_method<int>(rel.ptr(),"__len__");
	cout << "���������ʾ:" << endl;
	for(i = 0; i < size; i ++)
	{
		cout << call_method<char *>(rel.ptr(),"__getitem__",i) << endl;
	}
	// ����Python�������ͷ���Դ
	Py_Finalize();
	return 0;
}


