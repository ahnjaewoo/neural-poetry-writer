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

## Usage


#### 1. Prepare for code_set.txt which will be given soon.
#### 2. Prepare for encoder, decoder model used in image captioning, which will be given soon.
#### 3. Test the model
```bash
$ python interface_test.py --image='./image_caption/png/example.png'
```

## Sample Result

<p><img src="./image_caption/png/example.png"></p>
<p>a group of giraffes are standing together in a zoo.
when spirit of neir waste such a let of the past and broops

and i went
to the earth of a stars‚ she is‚

the poor fingers obeless and poach out; even little black
and i am a finding lay and
green husbandless cars are a flutter
of folk me‚ i have come
when the most please of chamber soaked with the flames american henged‚
the nails and dishina letstimations.

gravel post and kindled on him they surface the soul when the very side was the same of the months
she was the stage
of laugh's bowls
in my fragment is read‚ too
who was naked to save her

not with the layway were made approach‚
salting and together.
…</p>
