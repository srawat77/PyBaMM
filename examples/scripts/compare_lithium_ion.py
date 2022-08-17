#
# Compare lithium-ion battery models
#
import pybamm

pybamm.set_logging_level("INFO")

# load models
models = [
    pybamm.lithium_ion.SPM(),
    pybamm.lithium_ion.SPMe(),
    pybamm.lithium_ion.DFN(),
    pybamm.lithium_ion.NewmanTobias(),
]
parameter_values = pybamm.ParameterValues("Chen2020")

# create and run simulations
sims = []
for model in models:
    sim = pybamm.Simulation(model, parameter_values=parameter_values)
    sim.solve([0, 3600])
    sims.append(sim)

# plot
pybamm.dynamic_plot(
    sims,
    [
        "Terminal voltage [V]",
        "X-averaged negative electrode active material volume fraction",
        "Average negative particle concentration",
        "X-averaged negative electrode interfacial current density",
        "Current [A]",
    ],
)
