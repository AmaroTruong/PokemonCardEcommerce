FROM python:3
WORKDIR /Users/amarotruong/PokemonCardEcommerce-3
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . . 
EXPOSE 5000
CMD python ./app.py