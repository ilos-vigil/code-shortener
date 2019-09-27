import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.argument('category', type=click.Choice(['Semicolon', 'Markup'], case_sensitive=False), default='semicolon')
def main(path, category):
    """Simple program that save your money"""
    # 1. Input & Output file
    input_file_path = path
    input_file_extension = input_file_path[input_file_path.rfind('.') + 1:]
    input_file_path_without_extenstion = path[0:path.rfind('.')]
    output_file_path = input_file_path_without_extenstion + \
        "_output." + input_file_extension
    output = open(output_file_path, 'w')
    input = open(path, 'r').readlines()

    # 2. Variable to store new line
    new_lines = []
    continuous_line = ""

    for line in input:
        # 3. Strip space and EOL
        line = line.lstrip(' ')
        line = line.rstrip('\n')
        line = line.rstrip(' ')

        # 4. Remove empty line
        if line == "":
            continue

        # 5. Check if multi line is possible
        if category.lower() == 'semicolon':
            if line[-1] != ';' and line[-1] != '}':  # is multi line
                continuous_line += line.rstrip('\n') + ' '
                continue
            elif continuous_line != '' and line != '}':
                continuous_line += line
                line = continuous_line
        elif category.lower() == 'markup':
            if line[-2:] != '/>' and line[-1] != ">":
                continuous_line += line.rstrip('\n') + ' '
                continue
            else:
                continuous_line += line
                line = continuous_line

        # 6. Add if all condition satisfy
        if line == '}':
            new_lines[len(new_lines) - 1] = new_lines[len(new_lines) -
                                                      1].rstrip('\n') + ' }\n'
        else:
            new_lines.append(line + '\n')

        # 7. Reset `continuous_line`
        continuous_line = ''

    # 8. Check if last continuous_line is ''
    if continuous_line != '':
        new_lines.append(continuous_line)

    # 9. Write to a file
    output.writelines(new_lines)
    output.close()
    click.echo(f"Your shortened code location is {output_file_path}")


if __name__ == '__main__':
    main()
