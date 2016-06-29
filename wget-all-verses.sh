cat quranic-corpus-morphology-0.4.txt | grep '^(' | grep ':1)' | sed 's/\t.*//' | while read a; do
	echo $a | grep ':1:1)'
	wget -qc "http://corpus.quran.com/wordmorphology.jsp?location=$a" -O a/$a
done


for ((i=1; i<77430; i++)); do
	echo $i
	wget -cq http://corpus.quran.com/wordimage?id=$i -O images/$i.png
done
