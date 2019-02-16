import re

path_text = './text_sakhasire.txt'

file = open(path_text)

sentence = open('sentence.txt', 'a')

for line in file:
	split_regex = re.compile(r'[.|!|?|…|—|–]') 
	sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(line)]) 
	for s in sentences:
		s_lengts = len(s.split())
		if(s_lengts > 20 and s_lengts < 25):
			s = s + '\n'
			sentence.write(s)

sentence.close()
file.close()