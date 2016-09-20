# SCubed
My code for [CVGS Senior Science Senario](http://www.cvgs.k12.va.us/academics/senior-science-scenario-s-cubed)



## Carbon Cycle

The Carbon Cycle folder contains three iterations of a program which calculates the flow of carbon through its cycle (Atmosphere, Mixed Upper Ocean Layer, Deep Ocean Layer, Short-lived Terrestrial Biota, Long-lived Biota, Detritus, and Soil).

#### Evolution of CarbonCycle.py

The original `CarbonCycle.py` file separates out all of the multiplications into separate functions which increases readability, however it also leads to a lot of repetitive code.

The `CarbonCycle2.py` file condenses the `Fij()` functions into just one `F()` function. The new `F()` function also handles two special cases: Mixed Upper Ocean Layer to Atmosphere and Atmosphere to Short-lived Terrestrial Biota. The `k` values have been moved into a two dimensional array because the `kij` form mapped perfectly. Not entirely sure if this is more efficient, although it should be noted that `CarbonCycle.py` does not work and `CarbonCycle2.py` does work. `CarbonCycle2.py` also moves the `N` and `originalN` values into lists primarily so they can be accessed by `F()`.

The `CarbonCycle3.py` file does away with the `deltaN` functions in favor of using a dictionary with lambda functions corresponding to the various containers (Atmosphere, etc.). Again I'm not particularly sure that this is more efficient, however it is a neat capability of the language which for a program that doesn't need to be fast is something fun to play with. Using the dictionary also makes it easy to have just one function to apply Euler's method which calls up the appropriate lambda from the dictionary, as opposed to repeatedly typing the same function for each container.  This significantly cleans up the `for` loop and makes it easier to understand.

All three `CarbonCycle` files produce different outputs, with the final one (and the one that was turned in) being most correct. So I got that goin' for me, which is nice.

## Malaria

Malaria and its interactions with an increasingly vaccinated population was the primary focus of this project. Unfortunately, I no longer have access to the research our team collected nor the final paper we produced.  I can, however, state that the population is loosely modelled after Nigeria. The Primary difference between `Malaria.py` and `Malaria(Broken).py` is that the latter uses constants pulled directly from one of the papers our team found which uses a rate of infection which, while accurate, does not reflect the fact that in the calculations (both theirs and ours) every infected individual has a chance to infect every member of the population rather than just the small percentage that they would realistically encounter.

`Malaria.py` behaves in a very similar way to  the `CarbonCycle` files, using Euler's method to graph curves based on the interaction between several different groups.

`WritingScript.py` and `EfficientTkinter.py` were used to test if it was more time efficient to type out all the elements used in the GUI or if using a loop to produce the repetitive elements would be alright. The result from some time trials was that the speed difference is almost non-existent, with the loop sometimes being faster and the typed out version sometimes being faster.

## Prelim

These files serve primarily to demonstrate how Euler's method works in code. `PopulationGrowthWithEulersMethod.py` uses a simple equation to calculate the growth of a population.

`PreditorPreyEuler.py` demonstrates using Euler's method to predict the fluctuations in population of an ecosystem with foxes and rabbits in it.