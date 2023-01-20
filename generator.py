import json

# Open the file
with open('form.json', 'r') as file:
    # Load the JSON data from the file
    form = json.load(file)

# Open the file for reading
with open('template.html', 'r') as file:
    # Read the contents of the file
    data = file.read()
    # Replace the string
    data = data.replace('{{ header }}', form['header'])
    data = data.replace('{{ headerDescription }}', form['headerDescription'])
    data = data.replace('{{ logoLink }}', form['logoLink'])
    data = data.replace('{{ dashboardImageLink }}', form['dashboardImageLink'])
    data = data.replace('{{ featureWords }}', form['featureWords'])
    data = data.replace('{{ featureWordsDescription }}', form['featureWordsDescription'])
    data = data.replace('{{ stepOneActionImageLink }}', form['stepOneActionImageLink'])
    data = data.replace('{{ stepOneAction }}', form['stepOneAction'])
    data = data.replace('{{ stepOneActionDescription }}', form['stepOneActionDescription'])
    data = data.replace('{{ stepTwoActionImageLink }}', form['stepTwoActionImageLink'])
    data = data.replace('{{ stepTwoAction }}', form['stepTwoAction'])
    data = data.replace('{{ stepTwoActionDescription }}', form['stepTwoActionDescription'])
    data = data.replace('{{ stepThreeActionImageLink }}', form['stepThreeActionImageLink'])
    data = data.replace('{{ stepThreeAction }}', form['stepThreeAction'])
    data = data.replace('{{ stepThreeActionDescription }}', form['stepThreeActionDescription'])
    data = data.replace('{{ stepFourActionImageLink }}', form['stepFourActionImageLink'])
    data = data.replace('{{ stepFourAction }}', form['stepFourAction'])
    data = data.replace('{{ stepFourActionDescription }}', form['stepFourActionDescription'])


# Open the file for writing
with open('output.html', 'w') as file:
    # Write the new data to the file
    file.write(data)
