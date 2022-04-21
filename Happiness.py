# Program Name: Happiness
# Date:         21st of April 2022
# Developer:    Albert Banoy
# Purpose:      To solve Bloomsberg Programming Competition 
#               2022's first coding challenge

# Test Cases
#   Case 0 -
#       [Input]
#           Enter net worth for Alice, Bob, and Charlie: no
#       [Output]
#           Value error
#       [Input]
#           Enter net worth for Alice, Bob, and Charlie: 1 3 6
#       [Output]
#           Billions more needed for happiness: 4 1 0
#   Case 1 -
#       [Input]
#           Enter net worth for Alice, Bob, and Charlie: 3 2 5
#       [Output]
#           Billions more needed for happiness: 1 3 0
#   Case 2 -
#       [Input]
#           Enter net worth for Alice, Bob, and Charlie: 8 6 8
#       [Output]
#           Billions more needed for happiness: 0 3 0
#   Case 3 -
#       [Input]
#           Enter net worth for Alice, Bob, and Charlie: 6 3 3
#       [Output]
#           Billions more needed for happiness: 0 2 2

def calculation(inputs):
    # Variable initaiation
    output = []
    average = sum(inputs) / len(inputs)
    newer_average = average

    # For each element in inputs
    for index in range(0, len(inputs)):

        # If this element is less then the inital average
        if inputs[index] <= average:

            # Temporarily hold the element's value
            tempValue = inputs[index]
            
            # While the element's value is less then the newer average
            while inputs[index] <= newer_average:
                
                # Add a value
                inputs[index] += 1

                # Calculate a newer average
                newer_average = sum(inputs) / len(inputs)

            # Append the result and ungarbage the input 
            output.append(inputs[index])
            inputs[index] = tempValue
        else:
            output.append(0)

    # For each element in inputs
    for index in range(0, len(inputs)):

        # If an element's output is greater than zero
        if output[index] > 0:

            # Find the incremental value
            output[index] -= inputs[index]
        
    return output

def main():
    parameter_value = list(map(int, input("Enter net worth for Alice, Bob, and Charlie: ").split()))
    print("Billions more needed for happiness: ", end="")
    print(*calculation(parameter_value))
    input("Press enter to continue.")

if __name__ == "__main__":
    try:
        main()
    except ValueError:
        print("Value Error")
        main()