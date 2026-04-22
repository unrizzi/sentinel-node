import psutil, time

class NetworkAnalyzer:
    def __init__(self):
        self.connection_history = {}
    
    def scan(self, rules):
        alerts = []
        current_time = time.time()
        active_now = set()
        try:
            for conn in psutil.net_connections(kind='inet'):
                if conn.status == 'ESTABLISHED' and conn.raddr:
                    addr = (conn.raddr.ip, conn.raddr.port)
                    active_now.add(addr)
                    is_bad, cat, sev, ignore_time = rules.analyze_connection(addr[0], addr[1])
                    if addr not in self.connection_history:
                        self.connection_history[addr] = current_time
                    duration = current_time - self.connection_history[addr]
                    if is_bad:
                        alerts.append((addr, cat, sev))
                    elif not ignore_time and duration > 600:
                        alerts.append((addr, "Suspicious Persistence", "Medium"))
            self.connection_history = {k: v for k, v in self.connection_history.items() if k in active_now}
            return alerts
        except Exception as e:
            print(f"[ERROR]: Analysis failed: {e}")
            return []