def change_page(vrtpath, threshold):
	data=[]
	with open(vrtpath) as fi:
		for line in fi:
			if int(line.strip().split()[1]) <= threshold:
				continue
			data.append(line.strip().split()[0])
	return data

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser("Create a vocabulary based on a raw counts file by filtering words appearing less than or equal to threshold.")
	parser.add_argument("file")
	parser.add_argument('--threshold', default=1, type=int)
	args = parser.parse_args()
	data=change_page(args.file, args.threshold)
	for i in data:
		print(i)
