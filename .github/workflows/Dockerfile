FROM pytorch/pytorch:latest

RUN apt install update
RUN apt-get install git

RUN pip install jupyterlab ipywidgets

CMD ["jupyter", "lab", "--allow-root"]