---
title: 'Py-school-match: Matching algorithms to assign students to schools'
tags:
  - Python
  - Matching
  - Algorithm
  - School
  - Students
authors:
  - name: Iacopo Garizio
    orcid: 0000-0002-8431-516X
    affiliation: 1
affiliations:
 - name: Pontificia Universidad Católica de Chile
   index: 1
date: 25 november 2018
bibliography: paper.bib
---

# Summary

In many countries where schools cannot discriminate among student applicants
(no entrance exams, no interviews, no previous grades examination, etc.),
there is always one question that cannot be answered directly: How to assign students
fairly and efficiently?

Over the years, there have been many proposed solutions to this problem. These
vary from simple ``lotteries'' (random priority assignment) to more complex graph algorithms.
Because each option has its own strengths and weaknesses, and given that in the
real world there is an extra layer of requirements (quotas, special conditions, ranks 
of preference, etc.) it is vital to analyze and simulate every available option.
The correct selection of the algorithm can have serious effects on efficiency and fairness,
as it has been exemplified by studies conducted in school systems from Boston [@boston_match]
and New York [@new_york_match; @strategy_vs_efficiency]).

``py-school-match`` is a Python library that implements multiple matching algorithms and
aims to ease the process of choosing the best alternative for each school system.
It allows researchers to simply specify the country's requirements or conditions,
and then run interchangeably the different algorithms to compare their results.
What makes ``py-school-match`` different from other libraries is that it is specifically
created to be used in the the student-to-school assignment problem. 
Another distinctive characteristic is that it allows the use of quotas, priorities, capacities,
among others, without much effort.

``py-school-match`` implements the following algorithms:

- Top Trading Cycles (TTC) [@school_mechanism_design]
- Deferred acceptance with multiple tie-breaking (DAMTB) [@GS_1962]
- Deferred acceptance with single tie-breaking (DASTB) [@school_mechanism_design]
- Stable improvement cycles (SIC) [@whats_the_matter_tie_breaking]
- Deferred Acceptance with multiple tie-breaking, plus stable cycles (MSIC)
- Deferred Acceptance with single tie-breaking, plus non-stable cycles (NSIC)

# Acknowledgement:
I would like to thank my advisor, Nicolás Figueroa, for his valuable feedback.

# References