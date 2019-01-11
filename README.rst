===============
Py-school-match
===============

.. raw:: html

   <a href="http://joss.theoj.org/papers/460a2eeea7e19a32c8a4f9040dc1ea4a"><img  src="http://joss.theoj.org/papers/460a2eeea7e19a32c8a4f9040dc1ea4a/status.svg"></a>

.. image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
   :target: https://github.com/igarizio/py-school-match/blob/master/LICENSE
   :alt: Licence

.. image:: https://readthedocs.org/projects/py-school-match/badge/?version=latest
   :target: https://py-school-match.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/py-school-match.svg
   :target: https://pypi.org/project/py-school-match/
   :alt: PyPI


Overview
========

**Py-school-match** is an open-source Python package that implements multiple matching algorithms in order to assign
students to schools.

It provides multiple algorithms ready to use:

- Top Trading Cycles (TTC)
- Deferred acceptance with multiple tie-breaking (DAMTB)
- Deferred acceptance with single tie-breaking (DASTB)
- Stable improvement cycles (SIC)
- Deferred Acceptance with multiple tie-breaking, plus stable cycles (MSIC)
- Deferred Acceptance with single tie-breaking, plus non-stable cycles (NSIC)

**Py-school-match** is designed specifically for the student-to-school assignation problem. Because of this,
you can focus on evaluating different settings and algorithms, without the need to adapt or develop a
complete solution.

Sample code
===========

.. code-block:: python

    import py_school_match as psm

    # Creating three students.
    st0 = psm.Student()
    st1 = psm.Student()
    st2 = psm.Student()

    # Creating a criteria. This means 'vulnerable' is now a boolean.
    vulnerable = psm.Criteria('vulnerable', bool)

    # Assigning st1 as vulnerable
    student_vulnerable = psm.Characteristic(vulnerable, True)
    st1.add_characteristic(student_vulnerable)

    # Creating three schools, each with one seat available.
    sc0 = psm.School(1)
    sc1 = psm.School(1)
    sc2 = psm.School(1)

    # Defining preferences (from most desired to least desired)
    st0.preferences = [sc0, sc1, sc2]
    st1.preferences = [sc0, sc2, sc1]
    st2.preferences = [sc2, sc1, sc0]

    # Creating a lists with the students and schools defined above.
    schools = [sc0, sc1, sc2]
    students = [st0, st1, st2]

    # Defining a ruleset
    ruleset = psm.RuleSet()

    # Defining a new rule from the criteria above.
    rule_vulnerable = psm.Rule(vulnerable)

    # Adding the rule to the ruleset. This means that a 'vulnerable' student has a higher priority.
    # Note that rules are added in order (from higher priority to lower priority)
    ruleset.add_rule(rule_vulnerable)

    # Creating a social planner using the objects above.
    planner = psm.SocialPlanner(students, schools, ruleset)

    # Selecting an algorithm
    algorithm = psm.SIC()

    # Running the algorithm.
    planner.run_matching(algorithm)

    # inspecting the obtained assignation
    for student in students:
        print("Student {} was assigned to School {}".format(student.id, student.assigned_school.id))



Installation
============

Dependencies
------------

* graph-tool (>= 2.27)

User installation
-----------------

.. code-block:: shell

  pip install py-school-match

Or you can clone the repo and install it:

.. code-block:: shell

  git clone https://github.com/igarizio/py-school-match
  cd py-school-match
  python setup.py install

Remember to first install `graph-tool <https://graph-tool.skewed.de>`_ (`install instructions <https://git.skewed.de/count0/graph-tool/wikis/installation-instructions>`_).

Development
-----------

| Contributions are more than welcome. Feel free to open an issue or contact me!
| Remember that this package does not provide ANY WARRANTY OF ANY KIND.


Documentation
=============

Documentation is available at https://py-school-match.readthedocs.io/en/latest/
and in the ``docs`` directory.

