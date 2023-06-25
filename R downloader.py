import os, subprocess, urllib, atexit, os, requests, sys
from bs4 import BeautifulSoup

# Send a GET request to the URL
url = "https://cran.r-project.org/bin/windows/base/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the div element with class "download"
download_div = soup.find('div', class_='download')
# Find the link within the div element
link = download_div.find('a')['href']
# Download the file
filename = link.split('/')[-1]
print("R Downloader by Alex Ilchenko, 2023")
if not os.path.isfile(filename):
    # Print the extracted link
    print("Downloading R from:\n" +
          url + link + "\n" +
          "Please wait...")
    urllib.request.urlretrieve(url+link, filename)

# Launch the downloaded file
subprocess.Popen(filename)
'''
def delete_file():
    file_path = filename  # Specify the path to the executable file

    if os.path.exists(file_path):
        os.chmod(file_path, 0o777)
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted.")

# Register the delete_file function to be called on exit
atexit.register(delete_file)

# Launch the executable
subprocess.Popen(filename)  # Replace "example.exe" with the actual executable file name

def generate_bash_script(filename):
    script_content = f"""\
@echo off

set EXE_FILE='{filename}'

start "" '{filename}'

:WAIT_LOOP
timeout /t 1 /nobreak >nul
tasklist | find /i '{filename}' >nul
if errorlevel 1 (
    echo File '{filename}' is closed.
    del "%EXE_FILE%"
    echo File '{filename}' has been removed.
    exit /b
)
goto WAIT_LOOP

"""

    script_filename = "remove_R_installer.sh"

    with open(script_filename, 'w') as file:
        file.write(script_content)

    print(f"Bash script '{script_filename}' generated.")
    return script_filename

# Generate the bash script file
bash_script_file = generate_bash_script(filename)

# Run the bash script
subprocess.run(["bash", bash_script_file])

# Remove the bash script file
subprocess.run(["rm", bash_script_file])
print(f"Bash script '{bash_script_file}' removed.")

'''








