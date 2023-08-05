import tools



class c_code_2_mermaid:

    def __init__(self, text_file_path, output_path) -> None:
        self.TEXT_HEADER = r"```mermaid"
        self.GRAPH_TYPE = r"flowchart LR"
        self.TEXT_END = f"\n```"

        self.text_file_path = text_file_path
        self.output_path = output_path
        self.raw_text_list = []
        self.final_text_list = []
        self.md_output_string = ""
        self.do_pipeline()

    def do_pipeline(self):
        self.open_text_file()
        self.pre_process_text()
        self.write_md_file()

    def open_text_file(self):
        with open(self.text_file_path, 'r',  encoding='utf-8') as file:
            content = file.readlines()
            content = [line.strip() for line in content]
            self.raw_text_list = content
            print(content)

    def pre_process_text(self):
        for index, line in enumerate(self.raw_text_list):
            # print(f"{index}) {line=}")
            line = line.replace("{", "").replace("}", "")
            line = line.replace("}", "").replace("}", "")
            if line:
                self.final_text_list.append(line)
            # print(f"{index}) {line=}")

        tools.print_text_list(self.final_text_list)

    def create_mermaid_block(self, line_code, line_id):
        line_block = f"\n\t{line_id}(\"{line_code}\")"
        return line_block

    def write_md_file(self):

        self.md_output_string += self.TEXT_HEADER + "\n"
        self.md_output_string += self.GRAPH_TYPE + "\n"

        for index, line in enumerate(self.final_text_list):
            self.md_output_string += self.create_mermaid_block(
                line, tools.number_to_letter(index+1))

        self.md_output_string += self.TEXT_END

        print(self.md_output_string)

        with open(self.output_path, "w") as file:
            file.write(self.md_output_string)


if __name__ == "__main__":
    c_file = r"Examples/main.c"
    md_output = r"Output/Mermaid_cfg.md"
    teste = c_code_2_mermaid(text_file_path=c_file, output_path=md_output)
