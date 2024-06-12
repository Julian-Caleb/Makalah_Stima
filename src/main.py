import image_converter as image_converter
import kmp as kmp
import bm as bm
import bf as bf
import time
import os

# Main function
if __name__ == "__main__":
    # Introduction
    print("----- Let me help you find Waldo! -----\n")
    print("Put the image you want to find in the tc folder!\n")
    
    # Input image from the 'tc' folder
    print("Which image do you want to use?")
    while True:
        filename = input(">>> ")
        filepath = os.path.join('tc', filename)
        
        if os.path.isfile(filepath):
            break
        else:
            print(f"File '{filename}' not found in the 'tc' folder. Please try again.")
    print()
    
    # Input the algorithm to be used
    print("Which algorithm do you want to use?")
    print("1. Brute Force")
    print("2. Knuth-Morris-Pratt")
    print("3. Boyer Moore")
    algorithm = int(input(">> "))
    while algorithm not in [1, 2, 3]:
        algorithm = int(input(">> "))
    print()
        
    # Start the timer
    start_time = time.time()
    
    # Update filepath
    filepath = os.path.join("./tc", filename)
    
    # Convert the image to BMP format
    image_converter.image_to_bmp(filepath, "./temp/converted_image.bmp")
    
    # Convert the image to binary format
    file_binary = image_converter.image_to_binary("./temp/converted_image.bmp")
    
    # Check each image in the database to see if there is a match
    for dataname in os.listdir("./db"):
        datapath = os.path.join("./db", dataname) 
        
        # Crop the middle row
        image_converter.crop_middle_row(datapath, "./temp/converted_db.bmp")
        
        # Convert the cropped image to binary as well
        data_binary = image_converter.image_to_binary("./temp/converted_db.bmp")
        
        # Get the length of the binary data
        data_binary_length = len(data_binary)
        
        # Perform string matching based on the selected algorithm
        if algorithm == 1:
            idx = bf.brute_force_search(data_binary, file_binary)
        elif algorithm == 2:
            idx = kmp.KMP_search(data_binary, file_binary)
        else:
            idx = bm.BM_search(data_binary, file_binary)
            
        if idx != -1: 
            break
    
    # Stop the timer
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Elapsed time:", elapsed_time, "seconds")
    
    if idx != -1:
        print("Waldo found!")
        image_converter.draw_square_around_index(filepath, idx)
    else:
        print("Waldo not found!")
