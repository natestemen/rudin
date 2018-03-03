import os
import copy
import pprint

chapter_names = []
chapter_dir_names = []

with open('chapters.txt') as f:
    for i, chapter in enumerate(f):
        chapter_names.append(chapter.strip())
        name = chapter.strip().replace(' ', '-').lower()
        if i < 10:
            chapter_dir_names.append('0' + str(i) + '-' + name)
        else:
            chapter_dir_names.append(str(i) + '-' + name)

for name in chapter_dir_names:
    directory = os.path.join('../content', name)
    if not os.path.exists(directory):
        os.mkdir(directory)

sections = []
previous = False

with open('sections.txt') as f:
    for section in f:
        section = section.strip()
        if section == '-----':
            previous = True
        elif previous or len(sections) == 0:
            sections.append([section])
            previous = False
        else:
            sections[-1].append(section)
sections.insert(0, [])

convert = lambda li: [
    el.replace(' ', '-').replace(',', '').replace("'",'').lower()
    for el in li
]

section_file_names = list(map(convert, sections))
section_numbers = []
longest = max(section_file_names, key=len)

for i in range(len(longest)):
    if i < 10:
        section_numbers.append('0' + str(i))
    else:
        section_numbers.append(str(i))

input_template = '''\\subfile{{\\relative {filename}}}'''

chapter_head = '''\\chapter{{{chap}}}\\label{{chap:{label}}}'''

chapter_template = [
    '''\\documentclass[../../templates/chapter]{subfiles}''',
    '''\\begin{document}'''
]

section_template = '''\\documentclass[../../templates/section]{{subfiles}}

\\begin{{document}}

\\section{{{section}}}\\label{{sec:{label}}}

filler content...

\\end{{document}}
'''

for i, (chapter, secs) in enumerate(zip(chapter_dir_names, section_file_names)):
    names = sections[i]
    chapter_name = chapter_names[i]
    inputs = copy.deepcopy(chapter_template)
    inputs.append(chapter_head.format(
        chap=chapter_name,
        label=chapter
        )
    )
    for number, section, name in zip(section_numbers, secs, names):
        numbered = '-'.join([number, section])
        path = os.path.join('content', chapter, numbered)
        contents = section_template.format(section=name, label=section)
        with open('../' + path + '.tex', 'w+') as f:
            f.write(contents)

        inputs.append(input_template.format(filename=numbered))
    inputs.append('''\\end{document}''')

    main = os.path.join('../content', chapter, 'main.tex')
    with open(main, 'w+') as f:
        f.truncate()
        f.write('\n\n'.join(inputs))

content = ''

for name, dirname in zip(chapter_names, chapter_dir_names):
    from_root = os.path.join('content', dirname)
    content += '\\renewcommand{{\\relative}}{{{}}}\n'.format(from_root + os.sep)
    content += '\\subfile{{{}}}'.format(os.path.join(from_root, 'main'))
    content += '\n\n'

with open('../content/content.tex', 'w+') as f:
    f.truncate()
    f.write(content)

