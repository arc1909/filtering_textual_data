#!/usr/bin/env python3
import sys

def read_sentences(vrtpath, grouper='thread_id'):
	# sentence = []
	sentence_grouped = []

	current_grouper_value = None

	with open(vrtpath) as fi:
		for line in fi:
			if line.startswith("<text"):
				# If thread_id is different than before -> yield sentence_grouped
				if current_grouper_value == None:
					current_grouper_value = get_grouper_value(grouper, line)
				else:
					new_grouper_value = get_grouper_value(grouper, line)
					if new_grouper_value != current_grouper_value:
						yield (sentence_grouped, current_grouper_value)
						del sentence_grouped[:]
						current_grouper_value = new_grouper_value

			if line.startswith("<sentence"):
				if len(sentence_grouped) != 0:
					sentence_grouped += ['\n']

			# if line.startswith("</sentence"):
				# sentence_grouped.append(line.strip().split()[0])
				# sentence_grouped += sentence+['\n']
				# sentence_grouped += ['\n']
				# yield sentence
				# del sentence[:]
			if not line.startswith("<"):
				# sentence.append(line.strip().split()[0])
				sentence_grouped.append(line.strip().split()[0])

		yield (sentence_grouped, current_grouper_value) # Yield very last group

translation_table = {
		"&lt;": "<",
		"&gt;": ">",
		"&amp;": "&",
		"&quot;": '"',
		"&apos;": "'",
		}

def get_grouper_value(grouper, line):
	line = line.strip().split()
	for token in line: 
		if grouper in token:
			occurrence = token.find('"')
			return token[occurrence+1:-1]
	
	sys.exit('keyword for groupby NOT found. Use "thread_id" or "topic_name_leaf"')

def purify_sentence(sentence):
	as_text = ""
	previous_token = None
	for token in sentence:
		# This if clause handles spaces:
		if (not as_text #sentence start
			or token in ";:,.!?()[]\"'"): #punctuation
			as_text += token.lower()
		else:
			if previous_token != '\n':
				as_text += " " + token.lower()
			else:
				as_text += token.lower()
			
			previous_token = token
	# Get actual chars from HTML style tokens like "&amp;"
	for old, new in translation_table.items():
		as_text = as_text.replace(old,new)
	return as_text

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser("Parse a verticalized text (.vrt) file, print sentence by sentence")
	parser.add_argument("file")
	parser.add_argument('--groupby', default='thread_id', type=str)
	parser.add_argument('--debug', default=False, action='store_true')
	args = parser.parse_args()
	count = 0
	for sentence in read_sentences(args.file, args.groupby):
		print(f"###### {args.groupby}:{str(sentence[1])}")
		count += 1
		print(purify_sentence(sentence[0]))

		if args.debug:
			if count == 3:
				sys.exit()

