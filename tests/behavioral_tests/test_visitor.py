from unittest import TestCase
from pypattyrn.behavioral.visitor import Visitor, Visitee


class VisitorTestCase(TestCase):
    """
    Unit testing class for the Visitor class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """
        class Node(object):
            pass

        class A(Node):
            pass

        class B(Node):
            pass

        class C(A, B):
            pass

        class NodeVisitor(Visitor):

            def generic_visit(self, node, *args, **kwargs):
                return 'generic_visit ' + node.__class__.__name__

            def visit_b(self, node, *args, **kwargs):
                return 'visit_b ' + node.__class__.__name__

        self.a = A()
        self.b = B()
        self.c = C()
        self.node_visitor = NodeVisitor()

    def test_generic_visit(self):
        """
        Test that the generic_visit method is called.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals('generic_visit A', self.node_visitor.visit(self.a))

    def test_non_generic_visit(self):
        """
        Test that a non_generic visit method is called.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals('visit_b B', self.node_visitor.visit(self.b))

    def test_inheritance_visit(self):
        """
        Test that a parent visit method is called if a child does not have one.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals('visit_b C', self.node_visitor.visit(self.c))


class VisiteeTestCase(TestCase):
    """
    Unit testing class for the Visitee class.
    """
    def setUp(self):
        """
        Initialize testing data.
        """

        class Node(object):
            pass

        class A(Node, Visitee):
            pass

        class B(A, Visitee):
            pass

        class C(B, Visitee):
            pass

        class NodeVisitor(Visitor):
            def generic_visit(self, node, *args, **kwargs):
                return 'generic_visit ' + node.__class__.__name__

            def visit_b(self, node, *args, **kwargs):
                return 'visit_b ' + node.__class__.__name__

        self.a = A()
        self.b = B()
        self.c = C()
        self.visitor = NodeVisitor()

    def test_accept(self):
        """
        Test the accept method.

        @raise AssertionError: If the test fails.
        """
        self.assertEquals('generic_visit A', self.a.accept(self.visitor))
        self.assertEquals('visit_b B', self.b.accept(self.visitor))
        self.assertEquals('visit_b C', self.c.accept(self.visitor))
