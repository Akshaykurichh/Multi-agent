import socket
from agents.research_agent import ResearchAgent
from agents.memory_agent import MemoryAgent
from agents.synthesis_agent import SynthesisAgent

def handle_client(conn, addr):
    data = conn.recv(4096)
    request = json.loads(data.decode())
    agent_type = request["agent_type"]
    if agent_type == "research":
        response = ResearchAgent().handle_request(request)
    elif agent_type == "memory":
        response = MemoryAgent().handle_request(request)
    elif agent_type == "synthesis":
        response = SynthesisAgent().compose_report(request['data'], request['context'])
    conn.sendall(json.dumps(response).encode())

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 5000))
    s.listen()
    while True:
        conn, addr = s.accept()
        handle_client(conn, addr)

if __name__ == "__main__":
    start_server()
