
import os, sys, re

newdir = ""


# �ݹ���������
def search(rootdir, searchdirname):
    if os.path.isdir(rootdir):
        # print rootdir
        # ����·�����ļ���
        split1 = os.path.split(rootdir)
        # print split1[1]

        # �ж��Ƿ�Ϊָ�����ļ���
        if split1[1] == searchdirname:
            print
            "�ҵ��ļ��У�%s" % (rootdir)
            try:
                # ���ļ������Ƹ�Ϊ�µ��ļ�������
                os.rename(rootdir, split1[0] + "\\" + newdir)
                print
                "�ļ��� [%s] �Ѹ���Ϊ [%s]" % (rootdir, newdir)
            except:
                pass

                # ����ָ���ļ����µ����ݣ��ļ����ļ����б�
        listnew = os.listdir(rootdir)

        for l1 in listnew:
            path = rootdir + "\\" + l1
            # �ݹ����
            search(path, searchdirname)
    else:
        # print '�����ļ��У�%s' % (rootdir)
        return

        # ����ָ����ʽ���ļ�


def find_file_by_pattern(pattern, base):
    '''''���Ҹ����ļ����������� '''
    re_file = re.compile(pattern)
    if base == ".":
        base = os.getcwd()

    final_file_list = []
    # print base
    cur_list = os.listdir(base)
    for item in cur_list:
        print
        item
        full_path = os.path.join(base, item)
        if full_path.endswith(pattern):  # ����д�ɵ����ţ������Ŵﲻ��Ԥ�ڵ�Ч��
            # print full_path
            # bfile = os.path.isfile(item)
            if os.path.isfile(full_path):
                if re_file.search(full_path):
                    print
                    re_file.search(full_path).group()
                    final_file_list.append(full_path)
            else:
                final_file_list += find_file_by_pattern(pattern, full_path)
                # for filename in re_file.findall(final_file_list):
                # print filename
        else:
            continue
    return final_file_list


def serchDir(startdir, dirname):
    search(startdir, dirname)


if __name__ == '__main__':
    root = raw_input("��������Ŀ¼:")
    key = raw_input("������������ļ�������:")
    # newdir = raw_input("�ļ��и���Ϊ��")
    # serchDir(root,key)
    base = "".join([root, key])
    fileName = raw_input("������Ҫ���ҵ��ļ����ƻ��׺��:")
    for result in find_file_by_pattern(fileName, base):
        print
        result
���Ҫ����ָ�����ֵ��ļ�ֻ��Ҫ�����´�����Ļ����
if full_path.endswith(pattern):  # ����д�ɵ����ţ������Ŵﲻ��Ԥ�ڵ�Ч��
    ......
......
......
else:
continue