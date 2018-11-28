"""This module implements the algorithm *'Top Trading Cycles'*.
This implementation is based on Abdulkadiroglu and Sonmez (2003).

.. Note::
   This algorithm is considerably slower than the others. 
"""

from graph_tool.all import Graph, graph_draw, all_circuits, arf_layout

from py_school_match.algorithms.abstract_matching_algorithm import AbstractMatchingAlgorithm
from py_school_match.entities.student_queue import StudentQueue
from py_school_match.util.file_util import gen_filepath


class TTC(AbstractMatchingAlgorithm):
    """This class searches for cycles where each student gets his best option.

    This takes a list of students, a list of schools and a ruleset
    (which is used to calculate priorities).
    This works by generating a directed graph, where each student points
    at at his best option, and each school points at the student (or students)
    with the highest priority.
    """

    EDGE_WIDTH_SIZE_FACTOR = 700
    """Size factor (in the image) of each edge that is not part of the main cycle."""
    EDGE_WIDTH_CYCLE_SIZE = 10
    """Size factor (in the image) of each edge that takes part of the main cycle."""

    def __init__(self, generate_images=False, images_folder="TTC_images", use_longest_cycle=True):
        """Initializes the algorithm.

        :param generate_images: If the process generates images or not.
        :type generate_images: bool
        :param images_folder: Where images are saved.
        :type images_folder: str
        :param use_longest_cycle: If the algorithm applies the longest cycle available, or the first one encountered.
        :type use_longest_cycle: bool
        """
        self.generate_images = generate_images
        self.images_folder = images_folder
        self.use_longest_cycle = use_longest_cycle

        self.__graph = None
        self.__vertices_by_school_id = None
        self.__vertices_by_student_id = None
        self.__students_by_id = None
        self.__schools_by_id = None

        self.__entity_id = None
        self.__entity_type = None

    def reset_variables(self):
        """Resets all variables."""
        self.__graph = Graph()
        self.__vertices_by_school_id = {}
        self.__vertices_by_student_id = {}
        self.__students_by_id = {}
        self.__schools_by_id = {}

        self.__entity_id = self.__graph.new_vertex_property("int")
        self.__graph.vertex_properties["entity_id"] = self.__entity_id

        self.__entity_type = self.__graph.new_vertex_property("string")
        self.__graph.vertex_properties["entity_type"] = self.__entity_type

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

            cycles = [c for c in all_circuits(self.__graph, unique=True)]
            # print("CYCLES", cycles, "iteration", iteration_counter)

            cycle_edges = []

            if cycles:
                for cycle in cycles: # ToDo: Possible optimisation: apply all disjoint cycles at once
                    for current_v_index in range(len(cycle)):
                        next_v_index = (current_v_index + 1) % len(cycle)

                        from_v = self.__graph.vertex(cycle[current_v_index])
                        target_v = self.__graph.vertex(cycle[next_v_index])
                        edge = self.__graph.edge(from_v, target_v)
                        cycle_edges.append(edge)

                        if self.__entity_type[from_v] == "st":
                            sel_student = self.__students_by_id[self.__entity_id[from_v]]
                            sel_school = self.__schools_by_id[self.__entity_id[target_v]]
                            sel_student.assigned_school = sel_school
                            sel_school.assignation.append(sel_student)

                        # vertex_school_target_id = self.__entity_id[target_v]
                        # vertex_school_target = self.__schools_by_id[vertex_school_target_id]

                        # print("CYCLE: Student", sel_student.id, "School", sel_school.id)

                        # print("VVV: School {} -> School {}    (Student {}) ".format(self.__entity_id[from_v], self.__entity_id[target_v], self.__entity_id[self.__graph.edge(from_v, target_v)]))

                    if self.generate_images:
                        self.generate_image(cycle_edges, iteration_n=iteration_counter)
            else:
                can_improve = False

            self.__graph.clear()
            iteration_counter += 1

    def structure_graph(self, students, schools):
        """Creates a graph where students points to schools, and schools points to students.

        In the graph, each student points at at his best option, and each school points
        at the student (or students) with the highest priority.

        :param students: List of students.
        :type students: list
        :param schools: 
        :type schools: list
        """
        if not self.__students_by_id and not self.__schools_by_id:
            for student in students:
                self.__students_by_id[student.id] = student
            for school in schools:
                self.__schools_by_id[school.id] = school

        for school in schools:
            setattr(school, 'preferences', StudentQueue(school, preference_mode=True))

        remaining_students = [student for student in students if not student.assigned_school]

        for student in remaining_students:
            for pref_school in student.preferences:
                pref_school.preferences.append(student)

        for student in remaining_students:
            v_source_student = self.create_vertex_student(student)

            pref_school = next((school for school in student.preferences if len(school.assignation.get_all_students()) < school.capacity), None)

            if pref_school:
                v_target_school = self.create_vertex_school(pref_school)
                self.create_edge(v_source_student, v_target_school)

        for school in schools:
            if len(school.assignation.get_all_students()) < school.capacity:
                v_source_school = self.create_vertex_school(school)

                pref_student = next(iter(school.preferences.get_all_students()), None)

                if pref_student:
                    v_target_student = self.create_vertex_student(pref_student)
                    self.create_edge(v_source_school, v_target_student)

        # graph_draw(self.__graph,
        #            vertex_text=self.__entity_id, vertex_shape="circle",
        #            output_size=(1000, 1000), bg_color=[1., 1., 1., 1], output="graph.png")

    def create_vertex_student(self, student):
        """Defines a new student as a vertex in the graph (if it did not existed before)."""
        if student.id in self.__vertices_by_student_id:
            vertex = self.__vertices_by_student_id[student.id]
        else:
            vertex = self.__graph.add_vertex()
            self.__vertices_by_student_id[student.id] = vertex
            self.__entity_id[vertex] = student.id
            self.__entity_type[vertex] = "st" # ToDo: There may be other ways to do this.
        return vertex

    def create_vertex_school(self, school):
        """Defines a new school as a vertex in the graph (if it did not existed before)."""
        if school.id in self.__vertices_by_school_id:
            vertex = self.__vertices_by_school_id[school.id]
        else:
            vertex = self.__graph.add_vertex()
            self.__vertices_by_school_id[school.id] = vertex
            self.__entity_id[vertex] = school.id
            self.__entity_type[vertex] = "sc"
        return vertex

    def create_edge(self, source_v, target_v):
        """Creates a directed edge between two vertices."""
        self.__graph.add_edge(source_v, target_v)

    def generate_image(self, cycle_edges, iteration_n=0):
        """Generates an image of a graph.

        :param cycle_edges: Edges which are part of the main cycle (they will be highlighted in red).
        :type cycle_edges: list
        :param iteration_n: Number of iteration of the algorithm (this is added in the filename of the image).
        :type iteration_n: int

        .. DANGER::
        This is an experimental feature.
        """
        edge_color = self.__graph.new_edge_property("vector<float>")
        edge_width = self.__graph.new_edge_property("int")

        for edge in self.__graph.edges():
            if edge in cycle_edges:
                edge_color[edge] = [1., 0.2, 0.2, 0.999]
                edge_width[edge] = 7
            else:
                edge_color[edge] = [0., 0., 0., 0.3]
                edge_width[edge] = 4

        vertex_shape = self.__graph.new_vertex_property("string")
        vertex_size = self.__graph.new_vertex_property("int")

        for vertex in self.__graph.vertices():
            if self.__entity_type[vertex] == "st":
                vertex_shape[vertex] = "circle"
                vertex_size[vertex] = 1
            else:
                vertex_shape[vertex] = "double_circle"
                vertex_size[vertex] = 100

        # pos = sfdp_layout(self.__graph, C=10, p=5, theta=2, gamma=1)
        pos = arf_layout(self.__graph, d=0.2, a=3)
        graph_draw(self.__graph, pos=pos, vertex_text=self.__entity_id, vertex_font_size=1,  # ToDo: Move image related code outside the class.
                   vertex_fill_color=[0.97, 0.97, 0.97, 1], vertex_color=[0.05, 0.05, 0.05, 0.95],
                   vertex_shape=vertex_shape, edge_color=edge_color, edge_pen_width=edge_width,
                   output_size=(1000, 1000), bg_color=[1., 1., 1., 1], output=self.generate_filename(iteration_n))

    def generate_filename(self, iteration_n):  # ToDo: Move this to utils
        """Returns a filename (which is used to generate the images)."""
        filename = "Graph (iteration {})".format(iteration_n) if iteration_n > 0 else "Graph"
        output_file = gen_filepath(self.images_folder, filename=filename, extension="png")
        return output_file
