import argparse
import math
from PIL import Image, ImageDraw

WIDTH = 1000
HEIGHT = 1000
RADIUS = math.sqrt(WIDTH**2 + HEIGHT**2)/3

def plot_point(id, d):
    point = (WIDTH/2 + RADIUS*math.cos(angle_step*id),
              HEIGHT/2 - RADIUS*math.sin(angle_step*id))
    d.arc((point[0], point[1], point[0]+3, point[1]+3), 0, 360, 'black')

def id_to_cart(id):
    return (WIDTH/2 + RADIUS*math.cos(angle_step*id),
              HEIGHT/2 - RADIUS*math.sin(angle_step*id))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Image processing')
    parser.add_argument('--num', type=int)
    parser.add_argument('--inter', type=int)
    parser.add_argument('--name', type=str)
    args = parser.parse_args()
    blank = Image.new('RGBA', (WIDTH, HEIGHT), 'white')
    angle_step = 2*math.pi/args.num
    d = ImageDraw.Draw(blank)
    x = 2
    current_id = 0
    for i in range(args.num):
        d.line([id_to_cart(current_id), id_to_cart(current_id+args.inter)], 'black')
        plot_point(i, d)
        current_id += args.inter
    blank.show()
    blank.save(args.name+".png", "PNG")
