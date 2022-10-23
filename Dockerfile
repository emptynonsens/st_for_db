FROM python:3.10.8

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /app

# ENTRYPOINT ["streamlit run main.py --server.port 8505"] 

ENTRYPOINT ["streamlit", "run"] 

CMD ["main.py"]

# CMD streamlit run main.py --server.port 8501

