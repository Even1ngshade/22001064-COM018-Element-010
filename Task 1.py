import math

class CalculatorPrototype:
    def __init__(self):
        # Dictionary to store operations: symbol -> function mapping
        self.Operations = {}  # Format: {'symbol': function}

    def clone(self):
        # Creates a new instance of the CalculatorPrototype
        new_instance = CalculatorPrototype()
        # Copies the operations from the current instance
        new_instance.Operations = self.Operations.copy()
        return new_instance

    def addOperation(self, symbol, function):
        # Adds a new operation to the calculator
        self.Operations[symbol] = function

    def getOperation(self, symbol):
        # Retrieves the function associated with a given symbol
        return self.Operations.get(symbol)

class CalculatorSubject:
    def __init__(self):
        # Lists to hold observer objects
        self.Observers = []

    def addObserver(self, observer):
        # Adds a new observer to the list
        self.Observers.append(observer)

    def removeObserver(self, observer):
        # Removes an observer from the list
        self.Observers.remove(observer)

    def notifyObservers(self, result):
        # Notifies all registered observers with the calculation result
        for observer in self.Observers:
            observer.update(result)

class Calculator(CalculatorPrototype, CalculatorSubject):
    def __init__(self):
        # Initialises CalculatorPrototype and CalculatorSubject
        CalculatorPrototype.__init__(self)
        CalculatorSubject.__init__(self)
        # Adds default mathematical operations to the calculator
        self.addDefaultOperations()

    def addDefaultOperations(self):
        # Adds default mathematical operations supported by the calculator
        self.addOperation('+', self.add)
        self.addOperation('-', self.subtract)
        self.addOperation('*', self.multiply)
        self.addOperation('/', self.divide)
        self.addOperation('**', self.power)
        self.addOperation('%', self.modulo)
        self.addOperation('sq', self.squareRoot)
        self.addOperation('!', self.factorial)
        self.addOperation('per', self.percentage)
        self.addOperation('sin', self.sin)
        self.addOperation('cos', self.cos)
        self.addOperation('tan', self.tan)
        self.addOperation('sinM', self.sinMinus)
        self.addOperation('cosM', self.cosMinus)
        self.addOperation('tanM', self.tanMinus)
        self.addOperation('rad', self.radius)
        self.addOperation('dia', self.diameter)
        self.addOperation('cir', self.circumference)
        self.addOperation('nCr', self.numberChooseRow)
        self.addOperation('bD', self.binominalDistribution)
        self.addOperation('pD', self.poissonDistribution)
        self.addOperation('logDeB', self.logDefaultBase)
        self.addOperation('logWB', self.logWithBase)
        self.addOperation('deg-rad', self.degreeToRadians)
        self.addOperation('rad-deg', self.radiansToDegrees)
        self.addOperation('mag', self.magnitude)
        self.addOperation('dis', self.discriminant)
        self.addOperation('quadP', self.quadraticPlus)
        self.addOperation('quadM', self.quadraticMinus)
        self.addOperation('volCo', self.volumeCone)
        self.addOperation('volCu', self.volumeCuboid)
        self.addOperation('volS', self.volumeSphere)
        self.addOperation('volCy', self.volumeCylinder)

    def getNumbers(self, numPrompt):
        try:
            numbers = []
            while True:
                # Prompts the user to input numbers for calculations
                number = float(input(numPrompt))
                numbers.append(number)
                # Checks if the user wants to input another number
                if input("Do you want to enter another number? (Y/N): ").upper() != 'Y':
                    break
            return numbers
        except ValueError:
            # Handles invalid input errors
            print("Invalid input! Please enter a valid number.")
            # Recursively calls getNumbers until valid input is provided
            return Calculator.getNumbers(numPrompt)

    # Defines mathematical operation methods here
    def add(self, numbers):
        return sum(numbers)

    def subtract(self, numbers):
        result = numbers[0] - sum(numbers[1:])
        return result

    def multiply(self, numbers):
        result = 1
        for num in numbers:
            result *= num
        return result

    def divide(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            if num != 0:
                result /= num
            else:
                raise ValueError("Error! Division by zero is not allowed.")
        return result

    def power(self, numbers):
        return numbers[0] ** numbers[1]

    def modulo(self, numbers):
        result = numbers[0]
        for num in numbers[1:]:
            result %= num
        return result

    def squareRoot(self, numbers):
        return math.sqrt(numbers[0])

    def factorial(self, numbers):
        return math.factorial(int(numbers[0]))

    def percentage(self, numbers):
        return (numbers[0] * numbers[1]) / 100

    def sin(self, numbers):
        return math.sin(numbers[0])

    def cos(self, numbers):
        return math.cos(numbers[0])

    def tan(self, numbers):
        return math.tan(numbers[0])

    def sinMinus(self, numbers):
        return math.asin(numbers[0])

    def cosMinus(self, numbers):
        return math.acos(numbers[0])

    def tanMinus(self, numbers):
        return math.atan(numbers[0])

    def radius(self, numbers):
        return numbers[0] / (2 * math.pi)

    def diameter(self, numbers):
        return numbers[0] / 2

    def circumference(self, numbers):
        return 2 * math.pi * numbers[0]

    def numberChooseRow(self, numbers):
        return math.factorial(int(numbers[0])) / (math.factorial(int(numbers[1])) * math.factorial(int(numbers[0] - numbers[1])))
#                                      n                                  r                                n            r

    def binominalDistribution(self, numbers):
        return numbers[0] * (numbers[1] ** numbers[2]) * ((1 - numbers[1]) ** (numbers[3] - numbers[2]))
#               (nx)            p               x               q(1-p)          n               x

    def poissonDistribution(self, numbers):
        return ((numbers[0] ** numbers[1]) * (math.e ** (-numbers[0]))) / math.factorial(int(numbers[1]))
#                 lambda           x        e constant      lambda                               x

    def logDefaultBase(self, numbers):
        return math.log(numbers[0])
#                           x

    def logWithBase(self, numbers):
        return math.log(numbers[0], numbers[1])
#                           x         base
    
    def degreeToRadians(self, numbers):
        return numbers[0] * (math.pi / 180)
    
    def radiansToDegrees(self, numbers):
        return numbers[0] / (math.pi / 180)
    
    def magnitude(self, numbers):
        return math.sqrt((numbers[0] ** 2) + (numbers[1] ** 2))
#                            x squared           y squared
    
    def discriminant(self, numbers):
        return (numbers[0] ** 2) - (4 * numbers[1] * numbers[2])
#                  b squared                    4ac
    
    def quadraticPlus(self, numbers):
        return (-numbers[0] + math.sqrt((numbers[0] ** 2) - (4 * numbers[1] * numbers[2]))) / (2 * numbers[1])
#                  -b                        b squared                    4ac                         2a

    def quadraticMinus(self, numbers):
        return (-numbers[0] - math.sqrt((numbers[0] ** 2) - (4 * numbers[1] * numbers[2]))) / (2 * numbers[1])
#                  -b                        b squared                    4ac                         2a

    def volumeCone(self, numbers):
        return (1 / 3) * math.pi * (numbers[0] ** 2) * numbers[1]

    def volumeCuboid(self, numbers):
        return numbers[0] * numbers[1] * numbers[2]

    def volumeSphere(self, numbers):
        return (4 / 3) * math.pi * (numbers[0] ** 3)

    def volumeCylinder(self, numbers):
        return math.pi * (numbers[0] ** 2) * numbers[1]

    def calculate(self, operation, numbers):
        # Gets the corresponding function for the operation symbol
        operationFunc = self.getOperation(operation)
        if operationFunc:
            # Performs the calculation and notifies observers with the result
            result = operationFunc(numbers)
            self.notifyObservers(result)
            return result
        else:
            # Raises an error for invalid operations
            raise ValueError("Invalid operation")

class CalculatorObserver:
    def update(self, result):
        # Updates the method called by the Calculator to notify observers with the result
        print('Result:', result)

def main():
    # Initialises calculator and observer
    calculator = Calculator()
    observer = CalculatorObserver()
    calculator.addObserver(observer)

    # Main loop to perform calculations
    while True:
        try:
            # Prompts the user for operation selection
            operation = input('''Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power of
% for modulo
sq for square root
! for factorial
per for percentage of
sin for sine (in radians)
cos for cosine (in radians)
tan for tangent (in radians)
sinM for sine (in radians)
cosM for cosine (in radians)
tanM for tangent (in radians)
rad for radius
dia for diameter
cir for circumference
nCr for number Choose row
bD for binomial distribution
pD for poisson distribution
logDeB for logarithm with default base
logWB for logarithm with a user set base
deg-rad for degrees to radians
rad-deg for radians to degrees
mag for magnitude of vectors
dis for discriminant
quadP for quadratic Plus
quadM for quadratic Minus
volCo for volume of a Cone
volCu for volume of a Cuboid
volS for volume of a Sphere
volCy for volume of a Cylinder
Type your operation here (scroll up to see all the available operations): ''')

            # Prompts the user for numbers based on the selected operation
            if operation in ['+', '-', '*', '/', '**', '%', 'per', 'nCr', 'bD', 'pD', 'logWB', 'mag', 'dis', 'quadP', 'quadM', 'volCo', 'volCu', 'volS', 'volCy']:
                numbers = calculator.getNumbers('Please enter a number: ')
            elif operation in ['sq', '!', 'sin', 'cos', 'tan', 'sinM', 'cosM', 'tanM', 'rad', 'dia', 'cir', 'logDeB', 'deg-rad', 'rad-deg']:
                numbers = [float(input('Please enter a number: '))]
            else:
                print('You have not typed a valid operator, please run the program again.')
                continue

            # Performs the calculation and the result is displayed using the class CalculatorObserver (as if it was also here, it would show the result twice, and so that the code
            # follows the Observer Pattern)
            result = calculator.calculate(operation, numbers)

            # Asks the user if they want to perform another calculation
            calcAgain = input('Do you want to calculate again? (Y/N): ')
            if calcAgain.upper() != 'Y':
                print('See you later.')
                break

        except ValueError as e:
            # Handles errors and continues the loop
            print(e)
            continue

if __name__ == "__main__":
    main()

# TASK 1
# Follows Singleton Pattern, Prototype Pattern and Observer Pattern
# It should address a real-world problem or scenario (Calculator (solves mathmatical problems)), emphasising the following aspects:
# Correctness: The application must achieve its intended purpose.
# Design Quality: Proper application of chosen design patterns for improved structure and maintainability.
# Scalability: The design should facilitate easy integration of additional features.
# Flexibility: Demonstrate how changes in requirements can be accommodated without major code modifications.