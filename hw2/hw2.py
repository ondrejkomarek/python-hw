
import requests
import csv
import plotly.express as px

url = "https://api.open-meteo.com/v1/forecast?latitude=50.6607&longitude=14.0323&hourly=temperature_2m"
file_csv = "./hw2//data_csv.csv"

def get_temperature():
  try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
      json_data = response.json()
      return json_data["hourly"]
    else:
      print(f"Error")
      return None
  except Exception as e:
    print(f"Request failed: {e}")
    return False

def convert_data(row_data):
  data = []
  while sum([1 for item in row_data["time"]]) > 0:
    data.append({"time": row_data["time"].pop(0), "temp": row_data["temperature_2m"].pop(0)})
  return data

def save_to_csv(data):
  with open(file_csv, "w") as file:
    writer = csv.writer(file)
    writer.writerow(["time", "temperature"])
    for item in data:
      writer.writerow([item["time"], item["temp"]])


def create_graph(data):
  fig = px.scatter(
    data,
    x="time",
    y="temp",
    title="Temp in Usti",
  )
  fig.show()

data_temperature = get_temperature()
data_converted =convert_data(data_temperature)
save_to_csv(data_converted)
create_graph(data_converted)
