# Introduction

#### Well hello there! :wave:

It looks like you are interested in contributing to this project and that's
awesome because the more people we get involved, the more varied perspectives
on analysis we get. With more perspectives and ideas, the better a book we can
write that will be a pedagogical and hopefully reach more of those struggling
through (potentially) dry and boring analysis classes.

# Ground Rules

We appreciate contributions to this project, but if we don't adhere to some
rules it makes for a bad time.

#### Responsibilities
 * Create issues for any major changes and enhancements that you wish to make.
 Discuss things transparently and get community feedback.
 * Don't add any packages to the codebase unless absolutely needed.
 * Be welcoming to newcomers and encourage diverse new contributors from all
 backgrounds.


# Your First Contribution

There are two major ways to contribute:

 1. Writing parts of the book
 2. Writing some LaTeX

If there are any issues tagged with [good first issue](https://github.com/natestemen/rudin/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22
that's also a great way get started.

If you are new to git, [here](http://makeapullrequest.com/) and
[here](http://www.firsttimersonly.com/) are two websites to visit to learn more
about contributing to OSS projects. Keep in mind these are geared towards more
feature based open source projects so not _everything_ is applicable.

# Getting started

In contributing changes there are a few things to keep in mind. First and
foremost, please make sure your changes do not introduce any errors in the
LaTeX source. Please compile locally to make sure this all works correctly. If
you've added some content and are getting some confusing LaTeX errors, but
don't know how to fix them feel free to push your changes up, open a PR and ask
for some help.

As a general workflow it would be good to follow:

 1. Create your own fork of the code
 2. Make some changes in your fork in a feature branch
    - We are currently using one branch for each section of the book so that
      pull requests don't get massive. The convention is `0n-keyword` where `n`
      is the chapter number and `keyword` should be used to indicate which
      section you are working on. Take a look at existing branch names to get
      some ideas (or just use an existing one if you're planning on changing
      around some content that's already been worked on).
 3. Compile the pdf and make sure thare are no errors
 4. Make a pull request explaining the changes you have made and why they
    should be merged into master.

# How to report a bug

See the [issue template](ISSUE_TEMPLATE.md).

# How to suggest an enhancement

This is a bit tricky as the content of a book is rather subjective. That said
if you think there are major pedagogical improvements to be had, please open an
issue detailing how the particular path we are taking is possibly misguided and
could be corrected. Please try and provide helpful guidance, but if all you see
is an issue with no possible correction, I guess it can't hurt to just post it
and start a discussion.

# Code review process
This needs to be discussed as ultimately we don't currently have a way to vote
on what changes are good and what aren't as helpful. This makes me, or Kevin
play the dictator which chooses what's good and what's not which is FAR from
ideal. Ideas here are much appreciated.