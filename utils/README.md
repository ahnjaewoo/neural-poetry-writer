# Utility Codes

1. code_book
- manage character:number mapping, number:character mapping based on dictionary
- major functions are below:
	1. gather character mapping of observed character, count number for each character
	2. sort dictionary by order of most frequent character first, remake dictionary of character:index mapping on this order
	2. save to file
	3. load from file
	4. return mapping, reverse mapping on character, number
- upper case letters are regarded same as lower case letters

2. data_gatherer
- gather separated poem data, save to one file
- major functions:
	1. clean target file
		- 2 files : all poem connected file / poem separated file
	2. gather all files, save to target file
		- 2 files : all poem connected file / poem separated file
		- use data_parser
	3. parsing for poem files, before gather function
- data_cutter functions are used to transform some data

3. batch maker
- manage sequence and batch creation
- make sequences by following mode, and gather sequences iteratively.
- if enough sequences are gathered, make them as one batch, and start to gather next sequences.
- (drop/add), (normal/stride), (whole/one) mode
	1. (drop/add) : divided by seq_len, leftover part should be (dropped/padded)
	2. (normal/stride) : making sequence by striding seq_len filter
	3. (whole/one) : make sequence with (whole data text/separate each poem)

3. data_loader
- manage poem input data
- major functions are below:
	1. data_preprocess
		- make code_book, poem_set, title_set, batchs.npy for later use
	2. load from each file

4. data_cutter
- regulate character/word in poems
- replacing rule : replace words to anothoer word
- removing rule : replace words to space character