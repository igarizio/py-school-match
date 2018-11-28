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

The problem of assigning students to schools in a fair way is a long-lasting problem
with many proposed solutions. These solutions go from simple ``lotteries'' to more complex
graph algorithms, all of which have strengths and weaknesses. Given the nature of the
problem and the fact that in the real world there is an extra layer of
requirements (quotas, special conditions, ranks of preference, etc.) it is vital to
analyze and simulate every available option.

``py-school-match`` is a Python library that implements multiple matching algorithms
and allows users to simply specify the country's conditions  or requirements, and then
run interchangeably the different algorithms.
What makes ``py-school-match`` different from other libraries is that it is specifically
created to be used in the student-to-school assignation problem. Another distinctive
characteristic is that it allows the use of quotas, priorities, capacities, among
others, without much effort. These characteristics allow researchers to evaluate accurately
the different algorithms, without the need of developing case-by-case solutions.

``py-school-match`` implements the following algorithms:

    - Top Trading Cycles (TTC)
    - Deferred acceptance with multiple tie-breaking (DAMTB)
    - Deferred acceptance with single tie-breaking (DASTB)
    - Stable improvement cycles (SIC)
    - Deferred Acceptance with multiple tie-breaking, plus stable cycles (MSIC)
    - Deferred Acceptance with single tie-breaking, plus non-stable cycles (NSIC)
    

# References
