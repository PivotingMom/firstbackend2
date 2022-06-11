from tkinter import INSERT
from flask import Flask, request, jsonify
import db_helpers 
import sys 

app = Flask(__name__)

@app.post('/api/animals')

def animals_post():
  #special object that allows me to access data 
  data = request.json
  #since i'm expecting 2 variable 
  animal_name=data.get('animalName')
  image_url=data.get('imageURL')
  #helps to get info from a dictionary
  #if animal-name == None
  if not animal_name: 
        return jsonify("missing required argument 'animalName'"), 422
  if not image_url: 
        return jsonify("missing required argument 'imageURL'"), 422
  #todo: error checking the actual values for the arguement 
  #next create a helper folder and reuse the DB folder - done
  #todo: DB write -done below
  db_helpers.run_query("INSERT iNTO animal (name, image_url) VALUES(?,?)", [animal_name, image_url])
  return jsonify("Animal added", 200) 
  
@app.get('/api/animals') #path is the same just different function
  
def animals_get():
  #todo: DB select
  animal_list = db_helpers.run_query("SELECT * FROM animal")
  resp = []
  for animal in animal_list:
      an_obj ={}
      an_obj['animalId'] = animal[0]
      an_obj['animalName'] = animal[1]
      an_obj['imageURL'] = animal[2]
      resp.append(an_obj)
      return jsonify(animal_list), 200 

#to test if our code is correct sys argv , import sys, placeit at the very end 
if len(sys.argv) > 1: 
    mode = sys.argv[1]
else:
  print("Missing required mode arguement")
  exit()
  
if mode == 'testing':
  from flask_cors import CORS
  CORS(app)
  app.run(debug=True)
elif mode == 'production':
    import bjoern
    bjoern.run(app, "0.0.0.0", 5005)  
else: 
    print("mode must be in testing |production")
    exit()
  
  #next create a helper folder and reuse the DB folder - done
    