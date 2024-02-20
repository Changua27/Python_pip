import utils
import Leer_csv
import graficas

def run():
  data = Leer_csv.read_csv('data.csv')
  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  graficas.generate_pie_chart(countries, percentages)
  
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    graficas.generate_bar_chart(country["Country"], labels, values)
  

if __name__ == '__main__':
  run()