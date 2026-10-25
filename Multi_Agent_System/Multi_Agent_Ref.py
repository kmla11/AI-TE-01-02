# Simulasi Sederhana Multi-Agent System (MAS)
class Environment:
    def __init__(self):
        self.data_status = "Belum Diperiksa"

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def work(self, env):
        if self.role == "Pengumpul":
            env.data_status = "Data Telah Dikumpulkan"
            print(f"[{self.name}] ({self.role}): Berhasil mengumpulkan data lingkungan.")
        elif self.role == "Analis":
            print(f"[{self.name}] ({self.role}): Menganalisis status -> {env.data_status}")

# Menjalankan simulasi
if __name__ == "__main__":
    print("=== MEMULAI SIMULASI MULTI-AGENT ===")
    env = Environment()
    
    agent1 = Agent("Agen-Alpha", "Pengumpul")
    agent2 = Agent("Agen-Beta", "Analis")
    
    agent1.work(env)
    agent2.work(env)
    print("=== SIMULASI SELESAI ===")