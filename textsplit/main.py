import textwrap 

def split_text_file(file_path, line_length):

  with open(file_path, 'r') as f:
    lines = f.read().split('\n')

  output = []
  for line in lines:
    if len(line) > line_length:
      line_wrapped = textwrap.wrap(line, width=line_length)
      output.extend(line_wrapped)
    else:
      output.append(line)

  with open(file_path, 'w') as f:
    f.write("\n".join(output))

file_path = input("Enter file path: ")
line_length = int(input("Enter line length: "))

split_text_file(file_path, line_length)

print("File converted successfully!")