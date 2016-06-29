import re, sys
r = re.compile("\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]+)\t(.+)")

def print_aye(s, a, w, words, a_abs, w_abs):
	print '(%s, %s, %s, %s, %s, %s, %s),' % (s, a, w, 
			'"'+words['ROOT']+'"' if 'ROOT' in words else 'NULL', 
			'"'+words['LEM']+'"' if 'LEM' in words else 'NULL',
			a_abs, w_abs)

ps, pa, pw = -1, -1, -1
word_abs, aye_abs = 0, 0
words = {}

print "INSERT INTO WORD(sure, aye, word, root, lem, aye_abs, word_abs) VALUES";

for l in sys.stdin:
	l = l.strip()
	if len(l) == 0 or l[0] == '#':
		continue
	m = r.match(l)
	if not m:
		print >>sys.stderr, 'NM ', l
		continue
	s, a, w, p, form, tag, feat = m.groups()
	feats = dict(s.split(':') for s in feat.split('|') if s.find(':') != -1)
	if ps == s and pa == a and pw == w:
		pass
	else:
		if ps != -1:
			print_aye(ps, pa, pw, words, aye_abs, word_abs)
		word_abs += 1
		if (pa != a):
			aye_abs += 1
		ps, pa, pw = s, a, w
		words = {}

	words.update(feats)
	
print_aye(s, a, w, words, aye_abs, word_abs)

print ";"
