import os

def parse_txt_file(filepath):
    with open(filepath, 'r') as infile:
        content = infile.read()

    output_content = ""
    i = 0
    length = len(content)

    while i < length:
        if i < length - 1 and content[i] == '>' and content[i + 1] == '<':
            output_content += ">\n<"
            i += 2
        else:
            if content[i] == '>' and i < length - 1 and content[i + 1] != '\n':
                output_content += ">\n"
            elif content[i] == '<' and i > 0 and content[i - 1] != '\n':
                output_content += "\n<"
            else:
                output_content += content[i]
            i += 1

    with open(filepath, 'w') as outfile:
        outfile.write(output_content)

if __name__ == "__main__":
    directory = os.path.dirname(os.path.realpath(__file__))
    
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            parse_txt_file(filepath)
