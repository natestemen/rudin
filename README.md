# Rudin: Translated

Walter Rudin's [_Principles of Mathematical
Analysis_](https://www.mheducation.com/highered/product/principles-mathematical-analysis-rudin/M007054235X.html)
is a tried and true textbook for learning analysis, but as anyone has ever read
it can say, it is very terse. This leaves many readers struggling through
clever arguments and stumbling through manipulations. With this project we aim
to take Rudin's great organization of the subjects material, but present it in
a way that more can appreciate. With more intuitive explanations, graphics, and
anything else we can that aids in learning a notoriously hard subject like
analysis.

## Getting Started

To get the project you must first have [`git`](https://git-scm.com/). You can
then clone the project via
```
git clone git@github.com:natestemen/rudin.git
```

To build the full pdf, run
```
latexmk -pdf main.tex
```
in the root directory of the project. See [below](#prerequisites) if you do
not have the `latexmk` command or a LaTeX distribution.

### Prerequisites

First and foremost, you will need a LaTeX distribution which can be found for
your OS [here](https://www.latex-project.org/get/#tex-distributions). With that
installed you _should_ have the `latexmk` command (which is similar to
`pdflatex`, but smarter) which I would recommend using to compile the pdf's.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/natestemen/rudin/blob/master/CONTRIBUTING.md)
for details on our code of conduct, and the process for submitting pull
requests.

## Authors

* **Nate Stemen** - *Initial work* 
* **Kevin Yeh** - *Initial work*

See also the list of
[contributors](https://github.com/natestemen/rudin/blob/master/AUTHORS) who
participated in this project.  

## License

This project is licensed under the GPL License - see the
[LICENSE.md](https://github.com/natestemen/rudin/blob/master/LICENSE) file for details

## Acknowledgments

* Walter Rudin
* Mom and Dad
* epsilon
