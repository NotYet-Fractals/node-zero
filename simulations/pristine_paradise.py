import numpy as np
import matplotlib.pyplot as plt

class PristineParadiseEngine:
    def __init__(self, macro_scale=3.0, base_resonance=1.0, field_tension=3.14159):
        self.R = macro_scale
        self.r_base = base_resonance
        self.tau = field_tension
        
        # Linear phase velocity ratio for predictable clockwork loops
        self.phase_matrix = np.array([0.1, 0.1])
        self.phase_velocity = np.array([0.06, 0.03])
        
        self.inner_collapse = self.r_base * 0.4
        self.outer_explosion = self.r_base * 1.6

    def compute_field_pressure(self, state):
        interference_density = np.sin(self.tau * state) * np.cos(self.tau * state)
        return self.r_base + (0.2 * interference_density)

    def calculate_pristine_gradients(self, pressure):
        gradient_forces = np.array([0.0, 0.0])
        if pressure < self.inner_collapse + 0.15:
            severity = (self.inner_collapse + 0.15) - pressure
            gradient_forces += 12.0 * severity * np.array([1.0, 1.0])
        elif pressure > self.outer_explosion - 0.15:
            severity = pressure - (self.outer_explosion - 0.15)
            gradient_forces -= 12.0 * severity * np.array([1.0, 1.0])
        return gradient_forces

    def execute_pristine_cycles(self, total_steps=800):
        coordinates = []
        pressures = []
        for _ in range(total_steps):
            current_p = self.compute_field_pressure(self.phase_matrix)
            field_gradients = self.calculate_pristine_gradients(current_p)
            
            # NEAR-ZERO NOISE: Sterile, frictionless baseline environment
            stochastic_noise = np.random.uniform(-0.02, 0.02, 2)
            
            self.phase_velocity = 0.85 * self.phase_velocity + field_gradients + (stochastic_noise * 0.1)
            self.phase_matrix = (self.phase_matrix + self.phase_velocity) % (2 * np.pi)
            
            final_p = self.compute_field_pressure(self.phase_matrix)
            pressures.append(final_p)
            
            x = (self.R + final_p * np.cos(self.phase_matrix)) * np.cos(self.phase_matrix)
            y = (self.R + final_p * np.cos(self.phase_matrix)) * np.sin(self.phase_matrix)
            z = final_p * np.sin(self.phase_matrix)
            coordinates.append([x, y, z])
        return np.array(coordinates), pressures

engine = PristineParadiseEngine()
trajectory_matrix, field_pressures = engine.execute_pristine_cycles()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter_plot = ax.scatter(trajectory_matrix[:, 0], trajectory_matrix[:, 1], trajectory_matrix[:, 2], c=field_pressures, cmap='coolwarm', s=8, alpha=0.8)
ax.set_title("Node Zero Simulation: Pristine Paradise (Minimum Noise)", fontsize=12)
ax.set_xlabel("X-Axis (Material Space Matrix)")
ax.set_ylabel("Y-Axis (Awareness Core Matrix)")
ax.set_zlabel("Z-Axis (Emergent Phase Dimension)")
fig.colorbar(scatter_plot, ax=ax, pad=0.1).set_label("Internal Field Pressure Density Matrix")
plt.show()
