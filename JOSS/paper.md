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
fairly and efficiently.

Along the years, there have been many proposed solutions to this problem. These
vary from simple ``lotteries'' (random priority assignation) to more complex graph algorithms.
Because each option has its own strengths and weaknesses, and given that in the
real world there is an extra layer of requirements (quotas, special conditions, ranks 
of preference, etc.) it is vital to analyze and simulate every available option.
The correct selection and implementation of the algorithm can have serious 
effects on efficiency and fairness.

``py-school-match`` is a Python library that implements multiple matching algorithms
and allows users to simply specify the country's conditions  or requirements, and then
run interchangeably the different algorithms.
What makes ``py-school-match`` different from other libraries is that it is specifically
created to be used in the student-to-school assignation problem. Another distinctive
characteristic is that it allows the use of quotas, priorities, capacities, among
others, without much effort. These characteristics allow researchers to evaluate accurately
the different algorithms without the need of developing case-by-case solutions.

``py-school-match`` implements the following algorithms:

- Top Trading Cycles (TTC) [@school_mechanism_design]
- Deferred acceptance with multiple tie-breaking (DAMTB) [@GS_1962]
- Deferred acceptance with single tie-breaking (DASTB) [@school_mechanism_design]
- Stable improvement cycles (SIC) [@whats_the_matter_tie_breaking]
- Deferred Acceptance with multiple tie-breaking, plus stable cycles (MSIC)
- Deferred Acceptance with single tie-breaking, plus non-stable cycles (NSIC)

# Related literature:

- The Boston Public School Match [@boston_match]
- The New York City High School Match [@new_york_match]
- Strategy-proofness versus Efficiency in Matching with
Indifferences: Redesigning the NYC High School Match [@strategy_vs_efficiency]

# Acknowledgement:
I would like to thank my advisor, Nicolás Figueroa for all of his valuable feedback.

# References