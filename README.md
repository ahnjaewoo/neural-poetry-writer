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


#### 1. Prepare for code_set.txt in mid_data directory.
#### 2. Prepare for encoder, decoder model in image_caption/models directory.
#### 3. Train the image captioning model(description at image_caption directory).
#### 4. Train the poem generating model
```bash
$ python rnn_training.py
```
#### 5. Test the model
```bash
$ python interface_test.py --image='./image_caption/png/example.png'
```

## Sample Result

<p><img src="./image_caption/png/example.png"></p>
<p> a group of giraffes are standing together in a zoo . she wants
forgiven me to him in a lady light in a honey.
how they might want to his way into moloches and seemed many
over the inkform of his own melanchole who stood
for the brittle and the world of the horizon of white plunges

and the street was a late cloud of west step and straight alongside‚ how month
feels shoulder steam to your land. the woman i see
the other tree if i forget that i'd been held him
over the way to frown inside it‚ warned and drinking the bed.
the long living threatens the "angle?" like a name here mixed off the neck.

yes‚ i was a window and at sinfound men‚ these skies for a hundred
when it wouldn't go in the bugle‚ i want the other eyes...</p>
