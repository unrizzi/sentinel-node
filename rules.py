class SecurityRules:
    SUSPICIOUS_PORTS = {3333, 4444, 6666, 8888, 14444, 6667, 9001}
    TRUSTED_PORTS = {80, 443, 53}

    @classmethod
    def analyze_connection(cls, ip, port):
        if port in cls.SUSPICIOUS_PORTS:
            return True, "Malicious Signature", "High", False
        if port in cls.TRUSTED_PORTS:
            return False, "Trusted Service", "None", True
        return False, "Unknown/Generic", "Low", False