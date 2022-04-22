import csv
import argparse
import pickle5 as pickle

list_keys = ['Sk', 'A', 'Se', 'C', 'P', 'B', 'Hc', 'D', 'Hs']

def main(args):
    dict = {}
    file = args.img_file
    file = file.replace('/home/alexandreabela/Desktop/stylegan3-projector/dataset/','')
    for i in range(len(list_keys)): 
        label = file[0]
        key = list_keys[i]
        dict[key] = label
        file = file[2:]
    
    filename = args.img_file.replace('/home/alexandreabela/Desktop/stylegan3-projector/dataset/','')
    filename = filename.replace('.png','')
    
    file = open(f'/home/alexandreabela/Desktop/stylegan3-projector/dictionnary_labels/{filename}.csv', 'w')
    writer = csv.writer(file)

    for key, val in dict.items():
        writer.writerow([key,val])
    

if __name__=='__main__': 
    parser = argparse.ArgumentParser()

    parser.add_argument('--img_file', 
                        type=str,
                        help='image file from which to convert labels')

    args = parser.parse_args()
    main(args)