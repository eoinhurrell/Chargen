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
		fout.write("	<style type='text/css'>\n")
		fout.write("	body{background:#F9EA99;color:#4A4747;text-align:center;font-family:Arial, 'Helvetica Neue', Helvetica, sans-serif; padding:50px}\n")
		fout.write("	a:link{color:#3D4C53;}a:visited{color:#9D2E2C;}a:hover{color:#9D2E2C;}\n")
		fout.write("	.abutton{font-size:35px;font-family:Arial,sans-serif;font-weight:bold;background-color:#A9CF54;border-style:groove;border-color:#A9CF54;margin-top:100px;}\n")
		fout.write("	</style>\n")
		fout.write("<script>\n")
		fout.write("""function generate(){\n""")
		fout.write("""	adjwords = ["""+",".join(adj)+"""];\n""")
		fout.write("""	culwords = ["""+",".join(cul)+"""];\n""")
		fout.write("""	jobwords = ["""+",".join(job)+"""];\n""")
		fout.write("""	crewords = ["""+",".join(cre)+"""];\n""")
		fout.write("""	var adjnum = Math.floor(Math.random()*adjwords.length);\n""")
		fout.write("""	var culnum = Math.floor(Math.random()*culwords.length);\n""")
		fout.write("""	var jobnum = Math.floor(Math.random()*jobwords.length);\n""")
		fout.write("""	var crenum = Math.floor(Math.random()*crewords.length);\n""")
		fout.write("""	var adj = adjwords[adjnum]\n""")
		fout.write("""	var cul = culwords[culnum]\n""")
		fout.write("""	var job = jobwords[jobnum]\n""")
		fout.write("""	var cre = crewords[crenum]\n""")
		fout.write("""	location.hash = "!/"+adjnum+"/"+culnum+"/"+jobnum+"/"+crenum\n""")
		fout.write("""	document.getElementById('character-description').innerHTML = "<h1>" + adj + " <a href='http://en.wikipedia.org/wiki/" + cul + "' target='_blank'>" + cul + "</a> <a href='http://en.wikipedia.org/wiki/" + job + "' target='_blank'>" + job + "</a> (maybe <a href='http://en.wikipedia.org/wiki/" + cre + "' target='_blank'>" + cre + "</a>)</h1>";\n""")
		fout.write("""}\n""")
		fout.write("""function load(){\n""")
		fout.write("""	if(location.hash == ""){generate();}\n""")
		fout.write("""	else{\n""")
		fout.write("""		var nums = location.hash.split("/");\n""")
		fout.write("""		var adjnum = parseInt(nums[1]);\n""")
		fout.write("""		var culnum = parseInt(nums[2]);\n""")
		fout.write("""		var jobnum = parseInt(nums[3]);\n""")
		fout.write("""		var crenum = parseInt(nums[4]);\n""")
		fout.write("""		adjwords = ["""+",".join(adj)+"""];\n""")
		fout.write("""		culwords = ["""+",".join(cul)+"""];\n""")
		fout.write("""		jobwords = ["""+",".join(job)+"""];\n""")
		fout.write("""		crewords = ["""+",".join(cre)+"""];\n""")
		fout.write("""		var adj = adjwords[adjnum]\n""")
		fout.write("""		var cul = culwords[culnum]\n""")
		fout.write("""		var job = jobwords[jobnum]\n""")
		fout.write("""		var cre = crewords[crenum]\n""")
		fout.write("""		location.hash = "!/"+adjnum+"/"+culnum+"/"+jobnum+"/"+crenum\n""")
		fout.write("""		document.getElementById('character-description').innerHTML = "<h1>" + adj + " <a href='http://en.wikipedia.org/wiki/" + cul + "' target='_blank'>" + cul + "</a> <a href='http://en.wikipedia.org/wiki/" + job + "' target='_blank'>" + job + "</a> (maybe <a href='http://en.wikipedia.org/wiki/" + cre + "' target='_blank'>" + cre + "</a>)</h1>";\n""")
		fout.write("""	}\n""")
		fout.write("""}\n""")
		fout.write("</script>\n")
		fout.write("</head>\n")
		fout.write("<body onLoad='load();'>\n")
		fout.write("<div id='character-description'></div>\n")
		fout.write("<button id='regen-button' onclick='generate()' class='abutton'>Regenerate</button>\n")
		fout.write("</body>\n")
		fout.write("</html>")