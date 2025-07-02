from faker import Faker
from PIL import Image, ImageDraw
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from flask import Flask, jsonify
import random

faker = Faker()

def create_damaged_image(filename):
    img = Image.new('RGB', (200,200), color='grey')
    draw = ImageDraw(img)
    for _ in range(random.randint(5,15)):
        draw.rectangle((random.randint(0,150), random.randint(0,150), random.randint(50,200), random.randint(50,200)), fill='black')
    img.save(f'dbfs:/FileStore/images/damaged')

def generate_incidents(n=1000):
    incidents = []
    for i in range(n):
        image_path = f'damaged_{i:03d}.jpg' if i<100 else None
        if image_path:
            create_damaged_image(image_path)
        incidents.append({
        'type' : faker.random_element(elements = ('AI', 'Infra', 'Supply_Chain')),
        'severity' : faker.random_element(elements = ('P1','P2','P3')),
        'description' : faker.sentence(nb_words=20),
        'impact' : f'{faker.random_int(100000, 1000000)} INR loss',
        'mitigation' : faker.sentence(nb_words=10),
        'anomaly': "spike" if i%50==0 else 'normal',
        'image_path' : image_path
        })
    return pd.DataFrame(incidents)

app = Flask(__name__)

@app.route('/run_ingestion', methods=['GET'])
def run_ingestion():
    try:
        df = generate_incidents()
        db_url = 'postgresql://postgres:<pwd>@<supabase_host>:5432/postgres'
        engine = create_engine(db_url)

        with engine.begin() as connection : #ensuring auto-cleanup
            df.to_sql('incidents', conn, if_exists='replace', index=False)
        
        return jsonify({'status':'success', 'table':'incidents'})
    except Exception as e :
        return jsonify({'status':'error', 'message':str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)