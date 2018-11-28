.. _intro-getting_started:

===============
Getting started
===============

Py-school-match's basic structure
=================================

Py-school-match tries to expose flexible and easy-to-understand structures and functions.

In order to use the library, you should create at least one element of each category:

* :class:`.Student`: Represents one student.
* :class:`.School`: Represent one school. A school can have many seats.
* :class:`.SocialPlanner`: This entity runs the selected algorithm.

You should also select one algorithm:

* :class:`.TTC`: Top trading cycles.
* :class:`.DAMTB`: Deferred acceptance with multiple tie-breaking.
* :class:`.DASTB`: Deferred acceptance with single tie-breaking.
* :class:`.SIC`: Stable improvement cycles.
* :class:`.MSIC`: Deferred Acceptance with multiple tie-breaking, and then searches for stable cycles.
* :class:`.NSIC`: Deferred Acceptance with single tie-breaking, and then searches for non-stable cycles.

Finally, you can also define:

* :class:`.Criteria`: Associates an adjective and a value type.
* :class:`.Characteristic`: Associates a criteria with a value.
* :class:`.Rule`: Is used to determine the priority of a student.
* :class:`.Ruleset`: Aggregates a set of rules in a prioritized manner.
