FROM ubuntu
RUN apt-get update --fix-missing && \
  apt-get -y install python3.6 python3-pip && \
  apt-get clean && \
  pip3 install grpcio protobuf

# For regression service.
RUN export DEBIAN_FRONTEND=noninteractive && \
  apt-get update --fix-missing && \
  apt-get -y install cmake protobuf-compiler libprotoc-dev && \
  pip3 install sklearn numpy scikit-learn skl2onnx

RUN mkdir /regresioncnf && cd /regresioncnf && \
  apt-get update && apt-get -y install git && \
  git clone --branch main https://github.com/jossemii/RegresionCNF.git && mv RegresionCNF/* . && \
  mv RegresionCNF/.service/ . && rm -rf RegresionCNF  && rm -rf .git
