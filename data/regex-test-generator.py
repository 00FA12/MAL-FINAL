if __name__ == '__main__':
    import os

    # Generate a list of all the files in a folder
    # This will be used to test a regex pattern to filter out the images
    target_folder = '/media/ieris19/development-drive/Development/Data/PokeAPI/sprites/sprites/pokemon/other/official-artwork'
    f = open('regex_test.txt', 'w')
    for file in os.listdir(target_folder):
        f.write(file + '\n')
    f.close()
