# backend/services/graph_service.py
from pyvis.network import Network
import networkx as nx

class GraphService:
    """
    A service for creating and visualizing task dependency graphs.
    """
    def create_task_graph(self, action_items: list) -> Network:
        """
        Generates an interactive graph from a list of action items.

        Args:
            action_items (list): A list of dictionaries, each with 'task' and 'owner'.

        Returns:
            pyvis.network.Network: An interactive graph object.
        """
        net = Network(height="500px", width="100%", bgcolor="#222222", font_color="white", notebook=True)
        
        owners = list(set([item['owner'] for item in action_items]))
        
        for owner in owners:
            net.add_node(owner, label=owner, color="#00ff00", size=25, shape='ellipse')
            
        for item in action_items:
            task = item['task']
            owner = item['owner']
            net.add_node(task, label=task, color="#cceeff", size=15, shape='box')
            net.add_edge(owner, task)
            
        return net