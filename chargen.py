#!/bin/python
import random
import sys
adj = []
cul = []
job = []
cre = []

if __name__ == '__main__':
	for line in open('adjectives.txt','r'):
		adj.append(line.strip())
	for line in open('cultures.txt','r'):
		cul.append(line.strip())
	for line in open('jobs.txt','r'):
		job.append(line.strip())
	for line in open('creatures.txt','r'):
		cre.append(line.strip())	
	if len(sys.argv) == 1:
		print random.choice(adj).strip().title() + ' ' + random.choice(cul).strip() + " " + random.choice(job).strip() + " (maybe " + random.choice(cre).strip() + ")"
	elif sys.argv[1] == "-b" or sys.argv[1] == "--build":
		adj = ['"'+x.title()+'"' for x in adj]
		cul = ['"'+x+'"' for x in cul]
		job = ['"'+x+'"' for x in job]
		cre = ['"'+x+'"' for x in cre]
		fout = open("index.html","w")
		fout.write("<!DOCTYPE html>\n")
		fout.write("<html>\n")
		fout.write("<head>\n")
		fout.write("	<title>Chargen character generator</title>\n")
		fout.write("<script>\n")
		fout.write("function generate(){\n")
		fout.write("adjwords = ["+",".join(adj)+"];\n")
		fout.write("culwords = ["+",".join(cul)+"];\n")
		fout.write("jobwords = ["+",".join(job)+"];\n")
		fout.write("crewords = ["+",".join(cre)+"];\n")
		fout.write("""var adj = adjwords[Math.floor(Math.random()*adjwords.length)]\n""")
		fout.write("""var cul = culwords[Math.floor(Math.random()*culwords.length)]\n""")
		fout.write("""var job = jobwords[Math.floor(Math.random()*jobwords.length)]\n""")
		fout.write("""var cre = crewords[Math.floor(Math.random()*crewords.length)]\n""")
		fout.write("""document.getElementById('character-description').innerHTML = adj + " <a href='http://en.wikipedia.org/wiki/" + cul + "'>" + cul + "</a> <a href='http://en.wikipedia.org/wiki/" + job + "'>" + job + "</a> (maybe <a href='http://en.wikipedia.org/wiki/" + cre + "'>" + cre + "</a>)";\n""")
		fout.write("}\n")
		fout.write("</script>\n")
		fout.write("</head>\n")
		fout.write("<body onLoad='generate();'>\n")
		fout.write("<div id='character-description'></div>\n")
		fout.write("<button id='regen-button' onclick='generate()''>Regenerate</button>\n")
		fout.write("</body>\n")
		fout.write("</html>")