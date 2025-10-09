# backend/agents/dependency_graph_agent.py
from services.graph_services import GraphService

class DependencyGraphAgent:
    """
    Agent for visualizing tasks and owners in a dependency graph.
    """
    def __init__(self):
        self.graph_service = GraphService()

    def create_graph(self, action_items: list, output_path: str = "dependency_graph.html"):
        """
        Creates and saves an interactive graph.

        Args:
            action_items (list): The list of action items.
            output_path (str): The path to save the HTML file for the graph.
        """
        if not action_items:
            print("Dependency Graph Agent: No action items to visualize.")
            return None
            
        print("Dependency Graph Agent: Creating graph...")
        graph = self.graph_service.create_task_graph(action_items)
        graph.save_graph(output_path)
        print(f"Dependency Graph Agent: Graph saved to {output_path}")
        return output_path