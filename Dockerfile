FROM python:3
WORKDIR /Users/amarotruong/PokemonCardEcommerce-3
ADD . /Users/amarotruong/PokemonCardEcommerce-3
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python ./app.py