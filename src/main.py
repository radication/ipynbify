from parser import Ipynb

file_path = input()
file = Ipynb(file_path)
file.open()

language = file.get_language()
global_content = "# ipynb to markdown result\n\n"
cell_counter = 0

for cell in file.get_all_cells():
    cell_counter += 1
    global_content += f"\n\n## Cell **{cell_counter}**\n\n"
    cell_type = cell["cell_type"]
    cell_content = []
    if cell_type == 'code':
        cell_content = [f"```{language}\n"] + cell["source"] + ["\n```"]

    else:
        cell_content = cell["source"]

    for row in cell_content:
        global_content += row

with open(f"{file_path.replace('.ipynb', '.md')}", "w", encoding="utf-8") as f:
    f.write(global_content)