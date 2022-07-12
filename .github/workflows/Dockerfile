FROM pytorch/pytorch:latest

RUN apt-get -y update
RUN apt-get -y install git

RUN pip install jupyterlab ipywidgets

CMD ["jupyter", "lab", "--allow-root"]