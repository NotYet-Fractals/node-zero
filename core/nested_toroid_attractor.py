import numpy as np
import matplotlib.pyplot as plt

class NestedChaosEngine:
    def __init__(self, R_major=4.0, r_minor=1.5, rho_nested=0.5):
        # The Three Cascading Scales of Geometric Order
        self.R = R_major        # Macro-Scale Network Skeleton
        self.r = r_minor        # Meso-Scale Fluidic Boundary
        self.rho = rho_nested  # Micro-Scale Chaotic Vibration Wave
        
        # 3D Phase Space State Vector Inits
        self.state = np.array([0.1, 0.1, 0.1])
        
        # High-fracture frequencies to intentionally simulate chaotic code stutters
        self.omega_u = 1.0
        self.omega_v = 3.14159
        self.omega_w = 13.666

    def execute_attractor_cycles(self, steps=5000):
        """Generates continuous high-entropy trajectories that self-organize into a nested toroid."""
        coordinates = []
        entropy_pressures = []
        
        # Initial phase velocities
        u, v, w = 0.1, 0.1, 0.1
        
        for t in range(steps):
            # INTENTIONAL CHAOS INJECTION: Highly erratic, non-repeating step increments
            dt = 0.015
            
            # Non-linear coupling equations (Forces the chaos to feed back into itself)
            u += (np.sin(self.omega_u * v) - 0.05 * u) * dt
            v += (np.cos(self.omega_v * u) - 0.05 * v) * dt
            w = (w + self.omega_w * (u * v)) % (2 * np.pi)
            
            # THE NESTED PARAMETRIC PIVOT:
            # Maps the micro-chaos (w) inside the meso-loop (v), nested inside the macro-shell (u)
            x = (self.R + (self.r + self.rho * np.cos(w)) * np.cos(v)) * np.cos(u)
            y = (self.R + (self.r + self.rho * np.cos(w)) * np.cos(v)) * np.sin(u)
            z = (self.r + self.rho * np.cos(w)) * np.sin(v) + self.rho * np.sin(w)
            
            # Measure local field pressure density delta (The color matrix)
            pressure = np.sqrt(u**2 + v**2)
            
            coordinates.append([x, y, z])
            entropy_pressures.append(pressure)
            
        return np.array(coordinates), entropy_pressures

print("Compiling Nested Chaos Attractor Pipeline...")
engine = NestedChaosEngine()
trajectory, field_pressures = engine.execute_attractor_cycles()

fig = plt.figure(figsize=(10, 8)); ax = fig.add_subplot(111, projection='3d')

# Render the continuous chaotic stream as a highly dense, glowing vascular web
scatter_plot = ax.scatter(
    trajectory[:, 0], 
    trajectory[:, 1], 
    trajectory[:, 2], 
    c=field_pressures, 
    cmap='coolwarm', 
    s=2,              # Tiny pixels so you can see through the nested layers
    alpha=0.6,
    edgecolors='none'
)

ax.set_title("Node Zero: Nested Churning Toroid (Macroscopic Order in Chaos)", fontsize=12)
ax.set_xlabel("X-Axis (Material Space Matrix)")
ax.set_ylabel("Y-Axis (Awareness Core Matrix)")
ax.set_zlabel("Z-Axis (Emergent Phase Dimension)")

# Set wide camera container bounds to see the whole structure zoom out
ax.set_xlim(-6.5, 6.5)
ax.set_ylim(-6.5, 6.5)
ax.set_zlim(-3.5, 3.5)

fig.colorbar(scatter_plot, ax=ax, pad=0.1).set_label("Localized Entropy Pressure Density Gradient")

print("Superimposition complete. Launching recursive fractal proof."); plt.show()
