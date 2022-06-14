FROM ubuntu

RUN apt-get update --fix-missing && \
  apt-get -y install python3.6 python3-pip && \
  apt-get clean && \
  pip3 install grpcio protobuf==3.19.4 wget typing-extensions>=3.6.2.1

# For regression service.
RUN export DEBIAN_FRONTEND=noninteractive && export CMAKE_ARGS="-DONNX_USE_PROTOBUF_SHARED_LIBS=ON" && \
  apt-get update --fix-missing && \
  apt-get -y install cmake protobuf-compiler libprotoc-dev && \
  pip3 install sklearn numpy>=1.16.6 scikit-learn onnx skl2onnx

COPY src /regresioncnf