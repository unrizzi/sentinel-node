import psutil

class NetworkAnalyzer:
    def __init__(self):
        self.active_connections = set()
    
    def get_current_connections(self):
        connections_found = []
        try:
            for conn in psutil.net_connections(kind='inet'):
                if conn.status == 'ESTABLISHED' and conn.raddr:
                    ip = conn.raddr.ip
                    port = conn.raddr.port
                    connections_found.append((ip, port))
            return connections_found
        except (psutil.AccessDenied, psutil.NoSuchProcess) as e:
            print(f"[ERROR]: Permission denied or process missing while scanning: {e}")
            return []
        except Exception as e:
            print(f"[ERROR]: Unexpected error during network analysis: {e}")
            return []