import subprocess


for i in range(1000):
    j=35000+i
    image_file = '/home/alexandreabela/Desktop/stylegan3-projector/out/'+f'{j}'+'.npy'

    command = [
        'cp' , image_file,
        '/home/alexandreabela/Desktop/stylegan3-projector/subdataset'
    ]

    subprocess.run(command)