# Rudin Translation

This project will be to translate the mother of all analysis books to a more
user friendly version that is more approachable. In particular the goals of
this project are to use Walter Rudin's treasured classic _Principles of
Mathematical Analysis_ to create a more motivated, and sound introduction to
analysis for those who do not have the mathematical maturity that Rudin expects.

Pre-requisites are lame, but if we **had** to say, we would say having taken
multi-variable calculues, and some linear algebra would be helpful, but by no
means absolutely necessary. Familiarity with basic proof methods---such as
proof by contradiction/contrapositive/induction and direct proofs--- will be
helpful, but again we will do our best to provide necessary information along
the way.

We would love help with this project from anyone, especially from those who have
once struggled through Rudin themselves. Also pointing us towards your favorite
analysis book or even favorite math book would be super handy.

## Build

To build the full pdf of the book, run the following command in the root of the
project.
```
latexmk -pdf main
```
The project is also set up with the
[`subfiles`](https://ctan.org/pkg/subfiles?lang=en) package so that each
section, or each chapter can be compiled on its own so as the project grows,
your compiles dont have to. To compile a single chapter or section you can run
`latexmk` or just `pdflatex` on the main file or the section file respectively.
That said `latexmk` seems to be giving a few errors which would be great to
work out, but I haven't seem to find whats going wrong yet (and besides, it's
compiling as of now).
