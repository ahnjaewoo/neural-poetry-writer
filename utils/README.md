# Utility Codes

1. code_book
- manage character:number mapping, vector creation based on number code dictionary
- major functions are below:
	1. gather character mapping of unseen character
	2. save to file
	3. load from file
	4. get numpy vectors that correspond to given text
	5. get expected size of a vector
- TODO : upper case letter should be same value as lower case letter

2. data_loader
- manage poem input data
- major functions are below:
	1. data_preprocess
		- make char, vocab, tensor vector
		- code_book module used
	2. load from file
	3. save to file
	4. make batch
- TODO : make 2 batch method

3. data_gatherer
- gather separated poem data, save to one file
- major functions:
	1. clean target file
	2. gather all files, save to target file

4. data_parser
- process raw poem file, return set of title and set of poem_data in the file