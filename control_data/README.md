# control_data directory

- place for data_cutter rules
- loaded to setting replacing/removing rules

- file list
	1. accept.txt : odd lines are replace result, even lines are words to be replaced. each words to be replaced is separated by space.
	2. disallow.txt : each lines are unaccepted words, if words match, replace it by space character.
	3. one_accept.txt : odd lines are replace result, even lines are word to be replaced. whole even line is regarded as one word.
	4. unaccept.npy : each characters are unaccepted, if a character in this set is shown, replace it to space character.