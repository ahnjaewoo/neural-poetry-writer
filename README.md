# neural-poet-writer

- Objective
1. image -> caption creation
2. caption -> text (poem / title) creation

- Method
1. Image->Caption

2. Caption->Text
	1. use lstm, feed batch for train batch
	2. make text from caption feed. remove caption on poem.
	3. tile creation method not decided yet.

- Issue
1. title creation : how? (learn double lstm?)
2. batch division : per poem (drop per poem) / whole data basis (drop lack of sequence per data)
3. generation cutting : user define (user set generation length) / learning (learn length on vectors)
4. memory issue : can memory hold all data during learning?
5. vectors ready : set all vectors for whole data before training? / set only used vectors on each batches?