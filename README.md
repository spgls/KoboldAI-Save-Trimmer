# KoboldAI-Save-Trimmer
 A simple console program to trim excess data from KoboldAI Lite save files. There is also a sample of web interface
## Why was this program created?
The idea for this program came when on a low-performance android smartphone I reached 400k characters in KoboldAI Lite, and the performance of the site was terrible, it could no longer handle such volumes of text. So I came up with the idea to make a program to clean up excess context, and other unnecessary data
## Installation
 - - Install [Python](https://www.python.org/downloads/release/python-3106/) (3.10.6 Exactly works, but you can try using a different one)
 - - Install dependencies for the web interface (Optional if you won't be using it)
```shell
 pip install flask
   ```
 - - Clone the repository via git clone, or just download it as code and extract it to the desired location
## Usage
Before using it, you need to check "Export Settings" in KoboldAI Lite in the settings and download the save file via Save button, and then trim it using one of the methods below
#### 1. Run from the command line
```shell
python c:\example\path\trimmer.py -i c:\example\patch2\saved_story.json -o c:\example\patch2\saved_story-trim.json -a 10000
```
-a optional argument, if it is not specified, 10000 characters of context shall be retained
##### Context length
About 8k-10k context characters are needed for neural networks with a context window of 2048 tokens. (Most neural networks)
About 20k characters are needed for neural networks with a context window of 4096 tokens. (Example Llama 2)
About 35k-40k needed for SuperHOT-8K patched neural networks with context window of 8192 tokens
#### 2. Start using the start.bat script
Just place the .json file next to the start.bat script and then run it, the output of the program will create a trimmed.json file in the same folder
#### 3. Web Interface
Just run the `app.py` file in the flask-web folder and follow the link http://localhost:5002
 - For security reasons, it is best not to use it outside the local network