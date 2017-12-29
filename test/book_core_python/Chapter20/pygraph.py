# -*- coding:utf-8 -*-
# file: pygraph.py
#
def searchGraph(graph, start, end):				# ������
	results = []                
	generatePath(graph, [start], end, results)		# ����·��
	results.sort( lambda x, y:cmp(len(x), len(y)))		# ��·����������
	return results
def generatePath(graph, path, end, results):			# ����·��
	state = path[-1]
	if state == end:
		results.append(path)
	else:
		for arc in graph[state]:
			if arc not in path: 
				generatePath(graph, path + [arc], end, results)
if __name__ == '__main__':
	Graph = {'A':  ['B', 'C', 'D'],				# ������
	         'B':  ['E'],
	         'C':  ['D', 'F'],
	         'D':  ['B', 'E', 'G'],
	         'E':  [],
	         'F':  ['D', 'G'],
	         'G':  ['E']}
	r = searchGraph(Graph, 'A','D')				# ����A��D������·��
	print '************************'
	print '     path A to D'
	print '************************'
	for i in r:
		print i
	r = searchGraph(Graph, 'A','E')				# ����A��E������·��
	print '************************'
	print '     path A to E'
	print '************************'
	for i in r:
		print i
	r = searchGraph(Graph, 'C','E')				# ����C��E������·��
	print '************************'
	print '     path C to E'
	print '************************'
	for i in r:
		print i
