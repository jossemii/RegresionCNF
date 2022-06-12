FROM ubuntu
RUN apt-get update --fix-missing && \
  apt-get -y install python3.6 python3-pip && \
  apt-get clean && \
  pip3 install grpcio protobuf==3.19.4

# For regression service.
RUN export DEBIAN_FRONTEND=noninteractive && \
  apt-get update --fix-missing && \
  apt-get -y install cmake protobuf-compiler libprotoc-dev && \
  pip3 install sklearn numpy scikit-learn skl2onnx

COPY src /regresioncnf/