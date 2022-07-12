FROM pytorch/pytorch:latest

RUN apt-get update
RUN apt-get install git

RUN pip install jupyterlab ipywidgets

CMD ["jupyter", "lab", "--allow-root"]