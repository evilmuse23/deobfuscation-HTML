This Python script is designed to read .txt files within the same directory and modify their content. It specifically looks for the characters > and < and makes sure that they are surrounded by newlines. The script overwrites the existing .txt files with the modified content.

For example, if the text file contains:

php
Copy code
<div>SomeText</div><div>MoreText<d>
The script will change it to:

php
Copy code
<div>
SomeText
</div>
<div>
MoreText
</div>
Requirements
Python 3.x
Text files in the same directory as the script
How to Use
Place the script in the directory where your .txt files are located.
Run the script using the command python script_name.py, replacing script_name.py with the name you've given to the script.
The script will automatically parse all .txt files in the directory, modifying them according to the specified conditions.
