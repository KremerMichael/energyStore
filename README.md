# energyStore
### Proposal 
With the growing popularity of ‘Time of Use’ energy plans at the consumer level, a new opportunity is rising for average consumers to optimize their energy usage. We propose that creating an embedded system to store energy into a home backup system, (Think Tesla Powerwall) when energy is “cheap” during non-peak hours.Then using that energy when energy costs rise during peak hours would be beneficial for both consumers and suppliers of energy.

### Technical Problems
Through the energy storage embedded system we will be tackling the issues concerning high energy cost for customers and curtailment issues of renewable energy. During peak hours there is always an increase in the price of power due to the increase in demand and when demand is lower the prices are also lower. The embedded system will determine the best time to buy and store energy based on different parameters set into the system. The stored energy would be used as demand increases, the home would switch from grid energy to its own stored energy. Therefore, cost would be cut for the user since energy would be bought and stored for the home during low demand and used by the user when normal grid power is more costly. This brings an economical advantage for the user and also helps utility companies maintain a more steady rate of energy production during peak hours. That being said conventional power systems are unable to fully utilize renewable energy resulting in over generation and curtailment of renewables, which increases the cost and reduces the environmental benefits of renewables. If the embedded system is used in a place of high renewable energy it could potentially help conventional power systems produce energy at a constant rate and allow for heavier usage of renewables. 

## Deliverables
### Application:
Mobile and Desktop application that shows the user their battery usage, when energy is bought, when it is planned to be bought, and other statistics to optimize energy consumption. The user can switch between ‘Eco-Friendly Mode’, where the energy is bought automatically according to the ML model, and they can use ‘Manual Mode’ where they choose when to buy energy manually. The user interface will offer graphs of parameters over time to show the user trends compared with normal energy consumption (Cost * Energy trends). 

### Embedded System:
The embedded system will measure the relevant values for the ML Model, run the ML Model, be the mechanism for storing and releasing energy from the battery, and push all this data to the application. To accurately calculate the efficiency of storing and releasing energy from any given battery, the embedded system must have a way of measuring the temperature of the battery, voltage of the battery (to determine charge), and current in/out of the battery. The embedded system must have a method of measuring these values with sufficient resolution to train the ML Model (See ML Model section for more information relating to software). The hardware will involve a microcontroller/processor. Currently our primary reference is the Jetson Nano X. A solution would leverage this device and add a module on the GPI/O pins for our functionality or use other processors such FPGAS, Zynq processors, or SoC solutions. Battery control will depend on what battery we can reasonably work with for testing. Some home batteries may support wireless interfacing, a wired interface, or no interface. We will have to evaluate this once we source a battery. In order to conveniently provide data and control to the user, this system must have a method for receiving remote commands and sharing data. This may take the form of either a wired network connection or a wireless network connection. Power consumption of the system will not create a noticeable difference in the energy stores. The US household average is 1.2 kWh per hour, whereas a Jetson Nano runs Linux and provides 472 GFLOPS of FP16 compute performance with 5-10W of power consumption. At this current moment there is no need to add any greatly discernable energy draw.

### ML Model:
The model will predict optimal values within a 5% confidence interval for each of the parameters that dictate when energy is bought. The idea is to minimize Cost ($) for the user and minimize energy loss in the battery so the system can buy energy at the optimal time. These parameters are battery charge and battery temperature (measured using sensors), price of energy and outside temperature (API calls). For the battery specific parameters, they will be measured and stored in the database upon change, whereas the API calls will be done hourly. The model will also include a database that stores the measured values from the battery, as well as the other parameters for at least a year to account for seasonal changes. 

References:
https://www.weforum.org/agenda/2018/05/visualizing-u-s-energy-consumption-in-one-chart
https://www.nrel.gov/docs/fy16osti/65023.pdf
https://hourlypricing.comed.com/live-prices/
https://elinux.org/Jetson_Nano
https://www.nrel.gov/docs/fy16osti/65023.pdf
