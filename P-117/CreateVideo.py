import os 
import cv2

path="C:/Users/HP/OneDrive/Desktop/P-C-110/P-117/Images"

Images=[]

# Use a for loop to check each file in the folder
for file in os.listdir(path):
    # Separate the name and extension from a file name
    name, extension = os.path.splitext(file)

    if extension in ['.jpg', '.jpeg', '.png', '.gif']:
            # Create a variable file_name by concatenating the path and filename
            file_name = path + "/" + file

            print(file_name)
            Images.append(file_name)

count = len(Images)

frame = cv2.imread(Images[0])

height, width, channels = frame.shape

size = (width, height)

print(size)

video_name = "Project.avi"
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
fps = 0.8
Size = size

out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count-1):
      frame = cv2.imread(Images[i])
      out.write(frame)

print("Done")
