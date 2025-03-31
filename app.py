import streamlit as st
from src.genetic_algorithm import GeneticAlgorithm
from src.util.plotter import Plotter3D
from src.util.bin_to_decim import binary_to_decimal
from datetime import datetime
from src.util.runtime_format import runtime_format
from src.util.result_storage import results_to_json

st.title("Classic Genetic Algorithm Visualization")

population_size = st.slider("Population size", min_value=50, max_value=1000, value=500)
precision = st.slider("Precision", min_value=5, max_value=50, value=20)
epochs = st.slider("Epochs", min_value=10, max_value=200, value=60)
offspring_percentage = st.slider("Percent of the population to produce offspring", 
                                            min_value = 1, 
                                            max_value=100, 
                                            value=50)
lower_bound = st.slider("Lower Boundary", min_value=-10.0, max_value=0.0, value=-5.0)
upper_bound = st.slider("Upper Boundary", min_value=0.0, max_value=10.0, value=5.0)
selection_method = st.selectbox("Selection Method", ['best', 'roulette', 'tournament'])
crossover_method = st.selectbox("Crossover Method", ['one_point', 'two_point' , 'uniform', 'granular'])
mutation_method = st.selectbox("Mutation Method", ['one_point', 'two_point', 'boundary'])
fitness_function = st.selectbox("Fitness Function", ['hypersphere', 'michalewicz'])
mutation_rate = st.slider("Mutation Rate", min_value=0.01, max_value=0.1, value=0.05)
elitar_percentage = st.slider("Percentage of elite individuals", min_value=0, max_value=50, value=5)
#elitar_strategy = st.checkbox("Elitar strategy?", value=True)
inversion_enabled = st.checkbox("Enable inversion operator?", value=False)

plot = Plotter3D([], [], [], 'x', 'Y', 'Fitness Values')

fitness_chart = st.empty() #line live chart
fitness_data = [] #fitness values for line live chart

ga = GeneticAlgorithm(
    population_size,
    precision,
    epochs,
    offspring_percentage,
    lower_bound,
    upper_bound,
    selection_method,
    crossover_method,
    mutation_method,
    fitness_function,
    mutation_rate,
    #elitar_strategy,
    plot=plot,
    fitness_chart=fitness_chart, #line live chart
    fitness_data=fitness_data, #line live chart
    inversion_enabled=inversion_enabled,
    elitar_percentage=elitar_percentage
)

# if no calculations have been executed so far
if 'calculated' not in st.session_state:
    st.session_state.calculated = False

def calculate():
    start = datetime.now()

    best_solution, fitness = ga.run()

    calculation_time = runtime_format(datetime.now() - start)

    best_solution_decimal = binary_to_decimal(best_solution, upper_bound, lower_bound, precision)

    fig = plot.build()

    # clear live graph
    fitness_chart.empty()

    # cache results
    st.session_state.best_solution = best_solution
    st.session_state.fitness = fitness
    st.session_state.best_solution_decimal = best_solution_decimal
    st.session_state.fig = fig
    st.session_state.calculation_time = calculation_time
    st.session_state.fitness_data = fitness_data
    st.session_state.calculated = True

if st.button("Calculate"):
    calculate()

# display cached calculations results, if they exist 
if st.session_state.calculated:
    st.line_chart(st.session_state.fitness_data)

    st.pyplot(st.session_state.fig)

    st.write(f"Best result: {st.session_state.best_solution}")
    st.write(f"Global extremum found at (x = {st.session_state.best_solution_decimal[0]:.6f}, y = {st.session_state.best_solution_decimal[1]:.6f}).")
    st.write(f"Fitness value: {st.session_state.fitness}")

    st.download_button(
        label="Download results",
        file_name="results.json",
        data=results_to_json(ga, st.session_state.best_solution, st.session_state.fitness),
        mime="application/json",
        icon="⬇️",
        type="primary"
    )

    st.write(f"Calculation time: {st.session_state.calculation_time}")
