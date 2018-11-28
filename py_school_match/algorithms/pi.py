"""This module searches for cycles of *'Pareto improvements'*.
It stops when there are no cycles left.

.. DANGER::
   Be careful when running this algorithm. If the number of possible
   improvements is large, this my consume all RAM available.
   If this happens, set:

    .. code-block:: python
       
       USE_STACK_LIMIT = True
       STACK_SAFE_LIMIT = A_CONSTANT
    
    Where :code:`A_CONSTANT` should be a number between 0 and 1.
    
    .. NOTE::
       This may generate a non-optimal solution.
"""

import random
from collections import defaultdict

import graph_tool.all

from graph_tool.all import Graph, graph_draw, all_circuits, sfdp_layout

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm
from py_school_match.entities.student_queue import StudentQueue
from py_school_match.util.file_util import gen_filepath

USE_STACK_LIMIT = True
STACK_SAFE_LIMIT = 0.3


class PI(AbstractMatchingAlgorithm):
    """This class searches for cycles of *'Pareto Improvement'*.

    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate priorities).
    This works by generating a directed graph (with students as edges, 
    and schools as vertices), and then searches for possible cycles;
    if it finds one, it is applied; if not, the algorithm ends.
    """

    EDGE_WIDTH_SIZE_FACTOR = 700
    """Size factor (in the image) of each edge that is not part of the main cycle."""
    EDGE_WIDTH_CYCLE_SIZE = 10
    """Size factor (in the image) of each edge that takes part of the main cycle."""

    def __init__(self, stable_improvements=True, generate_images=False, images_folder="PI_images", use_longest_cycle=True):
        """Runs the algorithm.

        :param stable_improvements: If the algorithm will search for stable improvements or not.
        :type stable_improvements: bool
        :param generate_images: If the process generates images or not.
        :type generate_images: bool
        :param images_folder: Where images are saved.
        :type images_folder: str
        :param use_longest_cycle: If the algorithm applies the longest cycle available, or the first one encountered.
        :type use_longest_cycle: bool
        """
        self.stable_improvements = stable_improvements
        self.generate_images = generate_images
        self.images_folder = images_folder
        self.use_longest_cycle = use_longest_cycle

        self.__graph = None
        self.__vertices_by_id = None
        self.__students_by_id = None
        self.__schools_by_id = None

        self.__school_id = None
        self.__student_id = None

    def reset_variables(self):
        """Resets all variables."""
        self.__graph = Graph()
        self.__vertices_by_id = {}
        self.__students_by_id = {}
        self.__schools_by_id = {}

        self.__school_id = self.__graph.new_vertex_property("int")
        self.__graph.vertex_properties["school_id"] = self.__school_id

        self.__student_id = self.__graph.new_edge_property("int")
        self.__graph.edge_properties["student_id"] = self.__student_id

    def run(self, students, schools, ruleset):
        """Runs the algorithm.
        First it creates the graph, then it lists all the cycles available,
        after that it selects one cycle, and applies it. Finally, it starts
        the process again.

        :param students: List of students.
        :type students: list
        :param schools: List of school.
        :type schools: list
        :param ruleset: Set of rules used.
        :type ruleset: Ruleset
        """

        self.reset_variables()

        can_improve = True
        iteration_counter = 1

        while can_improve:
            self.structure_graph(students, schools)

            cycles = [c for c in all_circuits(self.__graph, unique=True) if len(c) > 1]

            if cycles:
                selected_cycle = max(cycles, key=lambda cycle: len(cycle)) if self.use_longest_cycle else cycles[0]
                cycle_edges = []

                for current_v_index in range(len(selected_cycle)):
                    next_v_index = (current_v_index + 1) % len(selected_cycle)

                    from_v = self.__graph.vertex(selected_cycle[current_v_index])
                    target_v = self.__graph.vertex(selected_cycle[next_v_index])
                    edge = self.__graph.edge(from_v, target_v)
                    cycle_edges.append(edge)

                    edge_student_id = self.__student_id[edge]
                    edge_student = self.__students_by_id[edge_student_id]

                    vertex_school_target_id = self.__school_id[target_v]
                    vertex_school_target = self.__schools_by_id[vertex_school_target_id]

                    if vertex_school_target in edge_student.preferences:
                        edge_student.assigned_school = vertex_school_target

                if self.generate_images:
                    self.generate_image(cycle_edges, iteration_n=iteration_counter)

            else:
                can_improve = False

            self.__graph.clear()
            iteration_counter += 1

    def structure_graph(self, students, schools):
        """Creates a graph where students are edges, and schools vertices.
        
        A vertex is created between two edges, if there is at least one student who
        was assigned to one of the edges and prefers the other. Also, if 
        :code:`stable_cycles` is selected, the student needs to be in the group of
        highest priority of the edge which he prefers.
        
        :param students: List of students.
        :type students: list
        :param schools: 
        :type schools: list
        """
        if not self.__students_by_id and not self.__schools_by_id:  # Maybe this could be moved to Student and School.
            for student in students:
                self.__students_by_id[student.id] = student
            for school in schools:
                self.__schools_by_id[school.id] = school

        for school in schools:
            setattr(school, 'preferences', StudentQueue(school, preference_mode=True))

        for student in students:
            for pref_school in student.preferences:
                if student.assigned_school:
                    try:
                        if student.preferences.index(pref_school) < student.preferences.index(student.assigned_school):
                            pref_school.preferences.append(student)
                    except Exception:
                        print("EXCEPTION", student.id, "---", pref_school.id, student.assigned_school.id, [s.id for s in student.preferences])
                else:
                    pref_school.preferences.append(student)

        for target_school in schools:
            target_school_indiference_groups = target_school.preferences.gen_indifference_groups()
            selected_groups = target_school_indiference_groups[:1] if self.stable_improvements else target_school_indiference_groups

            for group in selected_groups:
                for student in group:
                    stack_safe_limit = True if not USE_STACK_LIMIT else random.random() < STACK_SAFE_LIMIT
                    if student.assigned_school and stack_safe_limit:
                        if student.preferences.index(target_school) < student.preferences.index(student.assigned_school):
                            v_source_school = self.create_vertex(student.assigned_school)
                            v_target_school = self.create_vertex(target_school)
                            self.create_edge(student, v_source_school, v_target_school)

    def create_vertex(self, school):
        """Creates a new vertex in the graph (if it did not existed before)."""
        if school.id in self.__vertices_by_id:
            vertex = self.__vertices_by_id[school.id]
        else:
            vertex = self.__graph.add_vertex()
            self.__vertices_by_id[school.id] = vertex
            self.__school_id[vertex] = school.id
        return vertex

    def create_edge(self, student, v_source_school, target_v):
        """Creates a directed edge between two vertices."""
        e_student = self.__graph.add_edge(v_source_school, target_v)
        self.__student_id[e_student] = student.id

    def generate_image(self, cycle_edges, iteration_n=0):
        """Generates an image of a graph.
        
        :param cycle_edges: Edges which are part of the main cycle (they will be highlighted in red).
        :type cycle_edges: list
        :param iteration_n: Number of iteration of the algorithm (this is added in the filename of the image).
        :type iteration_n: int

        .. DANGER::
        This is an experimental feature.
        """
        edge_width = self.__graph.new_edge_property("int")
        self.__graph.edge_properties["edge_width"] = edge_width

        edge_color = self.__graph.new_edge_property("vector<float>")
        self.__graph.edge_properties["edge_color"] = edge_color

        edge_count = defaultdict(int)

        for edge in self.__graph.edges():
            corresponding_edge = next((e for e in edge_count if self.compare_edges(e, edge)), edge)
            edge_count[corresponding_edge] += 1

        for edge in self.__graph.edges():
            if edge in cycle_edges:
                edge_width[edge] = PI.EDGE_WIDTH_CYCLE_SIZE
                edge_color[edge] = [1., 0.2, 0.2, 0.999]
            else:
                edge_width[edge] = 0.9 + PI.EDGE_WIDTH_SIZE_FACTOR * edge_count[edge] / self.__graph.num_edges()
                edge_color[edge] = [0., 0., 0., 0.3]

        pos = sfdp_layout(self.__graph, K=500, C=20, p=10, theta=20, gamma=0.1)
        graph_draw(self.__graph, pos=pos, vertex_text=self.__school_id, vertex_font_size=30,
                   vertex_fill_color=[0.97, 0.97, 0.97, 1], vertex_color=[0.05, 0.05, 0.05, 0.95],
                   edge_pen_width=edge_width, edge_color=edge_color,
                   output_size=(1000, 1000), bg_color=[1., 1., 1., 1], output=self.generate_filename(iteration_n))

    def generate_filename(self, iteration_n): # ToDo: Move this to utils
        """Returns a filename (which is used to generate the images)."""
        filename = "Graph (iteration {})".format(iteration_n) if iteration_n > 0 else "Graph"
        output_file = gen_filepath(self.images_folder, filename=filename, extension="png")
        return output_file

    def compare_edges(self, e1, e2):
        """Compares two edges."""
        return (self.__school_id[e1.source()] == self.__school_id[e2.source()]) and (self.__school_id[e1.target()] == self.__school_id[e2.target()])

