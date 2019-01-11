.. _intro-examples:

========
Examples
========

Basic example
==============

The following example simulates three students (with one marked as ``vulnerable``) and three schools (who prioritize
``vulnerable`` students).
The code runs :class:`.SIC` (Stable Improvements Cycles) as an example, but it can be replaced with any of the stated algorithms.

.. code-block:: python

    # Importing py-school-match
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
        if student.assigned_school is not None:
            print("Student {} was assigned to School {}".format(student.id, student.assigned_school.id))
        else:
            print("Student {} was not assigned to any school".format(student.id))


Example using quotas
====================

The following example simulates three students (with one marked as ``vulnerable``) and three schools (who prioritize
``vulnerable`` students). This time, a minimum quota of 50% of vulnerable students is required.
The code runs :class:`.SIC` (Stable Improvements Cycles) as an example, but it can be replaces with any of the stated algorithms.

.. code-block:: python

    # Importing py-school-match
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
    # This time, a flexible quota is imposed.
    # This means that each school should have at least 50% percent
    # vulnerable students. The "flexible" part means that if there are
    # no vulnerable students left, even if the quota is not met, the
    # school can now accept non-vulnerable students.
    rule_vulnerable = psm.Rule(vulnerable, quota=0.5)

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
        if student.assigned_school is not None:
            print("Student {} was assigned to School {}".format(student.id, student.assigned_school.id))
        else:
            print("Student {} was not assigned to any school".format(student.id))


Visualizing algorithms
======================

.. WARNING::
   Experimental code.

In iterative algorithms you can visualize each iteration.

In order to generate images, simply add ``generate_images=True`` to the algorithm definition. See the following example:

.. code-block:: python

    algorithm = psm.SIC(generate_images=True)
    planner.run_matching(algorithm)

Note that if an algorithm does not find any cycle or cannot make any iteration, no image will be created.
