# mid_data directory

- place for preprocessed data
- loaded as already preprocessed

- file list
	1. code_set.txt : character array of code_book, each character's position represent each vector location to be set.
	2. poem_set.txt : poem data in one text file, not separated each other.
	3. title_set.txt : consist of titles of each poem, and length of each peom data
	4. np_batchs.npy : numpy array representation of batches, based on code_set.txt and poem_set.txt