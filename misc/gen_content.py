import os

chapter_names = []
chapter_dir_names = []
chapter_numbers = []

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

for chapter, sections in zip(chapter_dir_names, section_file_names):
    for number, section in zip(section_numbers[:len(sections)], sections):
        path = os.path.join('../content', chapter, number + '-' + section + '.tex')
        with open(path, 'w+') as f:
            f.write('filler content...')
    


import pprint

