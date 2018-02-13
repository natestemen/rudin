import os
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

input_template = '''
\\section{{{section}}}\\label{{{label}}}
\\input{{{filename}}}'''

for i, (chapter, secs) in enumerate(zip(chapter_dir_names, section_file_names)):
    names = sections[i]
    macros = '''\\newcommand{{\\pathtoroot}}{{{root}}}
\\let\\oldinput\\input
\\renewcommand{{\\input}}[1]{{\\oldinput{{\\pathtoroot/#1}}}}\n'''.format(
        root=os.path.join('content', chapter)
    )
    inputs = ''
    for number, section, name in zip(section_numbers[:len(secs)], secs, names):
        path = os.path.join('content', chapter, number + '-' + section)
        with open('../' + path + '.tex', 'w+') as f:
            f.write('filler content...')

        inputs += input_template.format(
            section=name,
            label=':'.join(['sec', section]),
            dir=chapter,
            filename='-'.join([number, section])
        )
        inputs += '\n'
    
    main = os.path.join('../content', chapter, 'main.tex')
    with open(main, 'w+') as f:
        f.truncate()
        f.write(inputs)    

chap_template = '''
\\chapter{{{chapname}}}\\label{{{label}}}
\\subimport{{{dir}}}{{{filename}}}\n'''

content = ''

for name, dirname in zip(chapter_names, chapter_dir_names):
    content += chap_template.format(
        chapname=name,
        label=':'.join(['chap', dirname]),
        dir=dirname + os.sep,
        filename='main'
    )

with open('../content/content.tex', 'w+') as f:
    f.truncate()
    f.write(content)

