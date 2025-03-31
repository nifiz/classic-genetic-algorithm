## Genetic Algorithm

A genetic algorithm uses methods based on what has been observed in nature - evolution (*hence the "genetic" part*), in order to find
optimal solutions for otherwise hard to solve problems. <br>
In this case, my team and I have created an algorithm that attempts to find a global minimum for a chosen test function.

### Tech stack
- Web UI was done with <a href="https://streamlit.io/">streamlit</a>.
- Using <a href="gowno">Docker</a>, we have contenerized the app to make development as seamless and easy as possible on different machines.
- Python
#
### So how does it work?

In essence, this kind of an algorithm does the following:

#### 1. Create a population of chromosomes. 
That's what individual members are called. In the case of this project, a chromosome is just a sequence of bits, that encodes 2 numbers - X and Y.

#### 2. Pick a number of chromosomes that will reproduce.
There are MANY possible selection methods, such as random selection, roulette, tournament etc.

#### 3. Create offspring - crossover of chromosomes.
Parent-chromosomes are used to create offspring-chromosomes. Again, there's a lot of ways to do this, you can slice chromosomes at an index and concatenate (one point crossover), at 2 or 3 indices,
you could also pick bits randomly or with a given chance to inherit from one or the other parent (granular or uniform crossover).

#### 4. Introduce a mutation (sometimes)
Just like in the real world, random things happen. Genes sometimes mutate, and introducing this random element to an algorithm helps in getting better results.
It's done in a similar manner to producing offspring.

#### 5. Rinse & Repeat
A genetic algorithm, similarly to evolution, should run a little more than once. After all, it wasn't your grandma who has lived in primordial soup.
In case of our project where we only were tasked with finding a global minimum for a 2 dimensional test function, around 60 epochs proved enough to give satisfactory results.
