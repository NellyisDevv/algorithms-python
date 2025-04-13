import os
from pathlib import Path
import time


def check_html(file_path):


    if not os.path.isfile(file_path):
        print("could not locate the file!")
        return

    html_file_content = Path(file_path).read_text()
    print(html_file_content)

    stack = []
    length_of_html = 0

    while length_of_html < len(html_file_content):
        if html_file_content[length_of_html] == "<":
            if html_file_content[length_of_html : length_of_html + 4] == "<!--":
                end_comment = html_file_content.find("-->", length_of_html)
                if end_comment == -1:
                    print("comment never closed?")
                    return
                length_of_html = end_comment + 3
                continue

            ending_tag_position = html_file_content.find(">", length_of_html)
            if ending_tag_position == -1:
                print("no closing bracket found for tag.")
                return

            tag = html_file_content[length_of_html + 1 : ending_tag_position].strip()

            if tag.endswith("/"):
                length_of_html = ending_tag_position + 1
                continue

            if tag.startswith("/"):
                tag_name = tag[1:].split()[0]
                if not stack:
                    print(f"extra closing tag </{tag_name}>?")
                    return
                open_tag = stack.pop()
                if open_tag != tag_name:
                    print(
                        f"mismatch: opened with <{open_tag}> but closed with </{tag_name}>"
                    )
                    return
            else:
                tag_name = tag.split()[0]
                if tag_name.lower():
                    stack.append(tag_name)

            length_of_html = ending_tag_position + 1
        else:
            length_of_html += 1

    if stack:
        print("tags not fully matched")
    else:
        print("tags matched correctly!")


def main():
    path = input("HTML file path? ").strip()
    start_time = time.time() 
    check_html(path)
    end_time = time.time() 
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
    
"""
execution_time = timeit.timeit('greatestcomdom(a, b)', globals=globals(), number=1000)
print(f'Execution time: {execution_time} seconds')
"""