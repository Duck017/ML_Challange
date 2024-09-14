from utils import download_images
import pandas as pd
import os

# Load the CSV file
df = pd.read_csv('/Users/akshaypramodmalu/Downloads/student_resource 3/dataset/test.csv')

# Print columns to diagnose the issue
print("Columns in DataFrame:", df.columns)

# Strip any leading or trailing spaces from column names
df.columns = df.columns.str.strip()

# Check the first few rows of the DataFrame
print(df.head())

# Check the data types of the columns
print("Data types of columns:", df.dtypes)

# Define the download folder
download_folder = '/Users/akshaypramodmalu/Downloads/student_resource 3/src/Download_Images_Test'

# Extract image links and filter out invalid URLs
image_links = df['image_link'].tolist()
image_links = [link for link in image_links if isinstance(link, str) and link.strip()]

# Extract filenames from the 'index' column
filenames = df['index'].tolist()

# Print raw values from the 'index' column for debugging
print("Raw values in 'index' column:", filenames)

# Ensure all filenames are valid and strip whitespace
filenames = [f"{str(name).strip()}.jpg" for name in filenames if isinstance(name, (str, int)) and str(name).strip()]

# Print the number of valid links and filenames found
print(f"Found {len(image_links)} valid image links.")
print(f"Found {len(filenames)} valid filenames.")

# Check the contents of filenames for debugging
print("Filenames:", filenames)

# Ensure that the number of image links matches the number of filenames
if len(image_links) != len(filenames):
    print("Warning: The number of image links does not match the number of filenames.")
else:
    # Download the images with specified filenames
    download_images(image_links, download_folder, filenames, allow_multiprocessing=False)


# from utils import download_images
# import pandas as pd
# import os

# # Load the CSV file
# df = pd.read_csv('/Users/akshaypramodmalu/Downloads/student_resource 3/dataset/test.csv')

# # print(df.columns)
# print(df['index'].tolist())

# # df.columns = df.columns.str.strip()
# # Define the download folder
# download_folder = '/Users/akshaypramodmalu/Downloads/student_resource 3/src/Download_Images'

# # Extract image links and filter out invalid URLs
# image_links = df['image_link'].tolist()
# image_links = [link for link in image_links if isinstance(link, str) and link.strip()]

# # Extract filenames from the 'index' column and ensure they are valid
# filenames = df['index'].tolist()

# filenames = [f"{str(name)}.jpg" for name in filenames if isinstance(name, str) and name.strip()]

# # Print the number of valid links and filenames found
# print(f"Found {len(image_links)} valid image links.")
# print(f"Found {len(filenames)} valid filenames.")

# # Ensure that the number of image links matches the number of filenames
# if len(image_links) != len(filenames):
#     print("Warning: The number of image links does not match the number of filenames.")
# else:
#     # Download the images with specified filenames
#     download_images(image_links, download_folder, filenames, allow_multiprocessing=False)