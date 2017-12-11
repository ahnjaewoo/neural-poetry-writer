from image_caption.build_vocab import Vocabulary
from external import image_to_poem
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, required=True, help='input image for generating caption')
args = parser.parse_args()

#image_path='./image_caption/png/example.png'
poem = image_to_poem(args.image)
print(poem)
