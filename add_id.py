def change_page(vrtpath, key):
	j=0
	data=[]
	with open(vrtpath) as fi:
		for line in fi:
			if line.startswith(" "+key):
				j+=1
				line="###### "+str(key)+": "+str(j)+"\n"
			data.append(line)
	return data
if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser("reformat the perl preprocessed file in order to make it compatible with input for senarvi-speech/filter-text/")
	parser.add_argument("file")
	parser.add_argument('--key', default='threadid', type=str)
	args = parser.parse_args()
	data=change_page(args.file, args.key)
	for i in data:
		print(i, end='')
