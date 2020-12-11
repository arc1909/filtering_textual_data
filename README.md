# filtering_textual_data

1.) vrt_parser_custom.py: this python script extracts the
web data coming from suomi24 finnish forum and
groups the text segments by argument keyword –
groupby

2.) select_vocab.py: it builds a vocabulary out of the raw
counts of unigrams of a given corpus. More precisely,
given a threshold, it adds in the vocabulary words that
appear at least threshold+1 times.

3.) add_id.py: this python script reconstruct the web sentences in the right format requested by Senarvi algorithm as input. The format is initially correct when
output by the parser, but it’s then modified due to the
preprocessing phase that removes symbols such as underscores and hashtags.
