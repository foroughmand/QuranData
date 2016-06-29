import re, sys, codecs

t = {}
for l in codecs.open('corpus-chars-data', encoding='utf-8'):
	if l.find('|') != 3: continue

	j = l.find('|')+2
	for i in range(l.find('|')):
		print >>sys.stderr, l[0:3], i, j
		t[l[i]] = l[j+2*i]

f = codecs.open('corpus-chars', 'w', encoding='utf-8')
for k, v in t.iteritems():
	print >> f, u'%s\t%s' % (k, v)
f.close()
print len(t.keys())
